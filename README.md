# VetAI Flow Crew

Welcome to the VetAI Flow Crew project, powered by [crewAI](https://crewai.com). This project creates a multi-agent AI system designed to assist veterinary professionals with clinical workflows, leveraging the powerful and flexible framework provided by crewAI.

## About VetAI Flow

VetAI Flow uses collaborative AI agents to streamline veterinary workflows, including:
- Patient data collection
- Metabolism calculation
- Nutrition calculation and recommendation
- Security check
- Report generation

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Configuration

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/vetai_flow/config/agents.yaml` to customize the veterinary specialist agents
- Modify `src/vetai_flow/config/tasks.yaml` to define your tasks
- Modify `src/vetai_flow/crew.py` to add your own logic, tools and specific args
- Modify `src/vetai_flow/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your flow and begin execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the vetai_flow Flow as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The vetai_flow Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the {{crew_name}} Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
