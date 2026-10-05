import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()

# 1. Define LLM Agents
researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI Agents and LLMs",
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends in Agentic AI,
    autonomous workflows, and transformer architectures.""",
    verbose=True,
    memory=True
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling, easy-to-understand executive summaries on technical AI topics",
    backstory="""You are a renowned Content Strategist known for your insightful
    and explanatory articles on modern AI frameworks.""",
    verbose=True,
    memory=True
)

# 2. Define Tasks
research_task = Task(
    description="""Identify the top 3 trends in Multi-Agent AI systems for 2026.
    Focus on autonomous execution, tool integration, and enterprise adoption.""",
    expected_output="A bullet-point summary of the top 3 trends with short explanations.",
    agent=researcher
)

write_task = Task(
    description="""Using the research analyst's output, compile an executive briefing
    report formatted in clean markdown.""",
    expected_output="A structured markdown report with sections: Overview, Key Trends, and Conclusion.",
    agent=writer
)

# 3. Instantiate the Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

if __name__ == "__main__":
    print("### Starting Multi-Agent Crew ###")
    result = crew.kickoff()
    print("\n### Final Output ###\n")
    print(result)