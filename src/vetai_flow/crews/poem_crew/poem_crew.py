#setup
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool,\
                        ScrapeWebsiteTool,\
                        WebsiteSearchTool,\
                        DirectoryReadTool,\
                        FileReadTool,\
                        SerperDevTool
from crewai.tools import BaseTool
from vetai_flow.tools.custom_tool import MECalculator,NutritionCalculator
from pydantic import BaseModel
from vetai_flow.crews.poem_crew.profiles import pet_profile,nutrition_plan

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

#use deepseek llm
import os
from crewai import LLM
deepseek_llm = LLM(
    model="deepseek/deepseek-chat", 
    api_key=os.environ["DEEPSEEK_API_KEY"],
    stream=True
)
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


#setup built in tools & custom tools
read_merck = FileReadTool("/Users/work/Desktop/MSRA/VetAI/material/NutritionList&Functions-ChatGPTDeepResearch.txt")
me_calculator = MECalculator()
nutrition_calculator = NutritionCalculator()


@CrewBase
class Vetai2():
    """Vetai2 crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def vet(self) -> Agent:
        return Agent(
            config=self.agents_config['vet'],
            verbose=True,
            llm=deepseek_llm,
        )
    
    @agent
    def quality_assurance(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_assurance'],
            verbose=True,
            llm=deepseek_llm,
        )
    
    @agent
    def assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['assistant'],
            verbose=True,
            llm=deepseek_llm,
        )
    
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def calculate_me(self) -> Task:
        return Task(
            config=self.tasks_config['calculate_me'],
            tools=[me_calculator,nutrition_calculator],
            verbose=True,
            output_pydantic=pet_profile,
        )
    
    @task
    def safety_check(self) -> Task:
        return Task(
            config=self.tasks_config['safety_check'],
            tools=[read_merck],
            verbose=True,
            context=[self.tasks_config['calculate_me']],
        )

    @task
    def respond(self) -> Task:
        return Task(
            config=self.tasks_config['respond'],
            verbose=True,
            context=[self.tasks_config['calculate_me']],
            output_pydantic=nutrition_plan,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Vetai2 crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=[self.vet(),self.quality_assurance(),self.assistant()],
            tasks=[self.calculate_me(), self.safety_check(),self.respond()],
            verbose=True,
            memory=True,
            process=Process.sequential,
            #process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )