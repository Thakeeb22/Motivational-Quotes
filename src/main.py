from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Agent
motivator = Agent(
    role="Motivational Speaker",
    goal="Inspire people with uplifting and impactful quotes.",
    backstory=(
        "You are a world-class motivational speaker who crafts "
        "short, memorable, and inspiring quotes to lift people’s spirits."
    ),
    allow_delegation=False
)

# Create Task
generate_quote = Task(
    description="Generate a unique motivational quote about perseverance and positivity.",
    expected_output="A single motivational quote in plain text.",
    agent=motivator
)

# Create Crew
crew = Crew(
    agents=[motivator],
    tasks=[generate_quote],
    process=Process.sequential
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n💡 Motivational Quote:\n", result)
