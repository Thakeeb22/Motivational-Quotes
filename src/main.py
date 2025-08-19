from functools import cache
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Agent
quote_agent = Agent(
    
  role= "Quote Generator",
  goal= "Generate a short motivational quote (1-2 sentences) and a 1-line productivity tip.",
  backstory=(
      "Clear and consise formatter."
      ),
    verbose=True,
    memory=False
)
task_agent = Agent(
  role= "Task Formatter",
  goal= "Take a comma-separated task list and convert it to a clean bullet list (3-6 bullets max).",
  backstory=(
      "Clear and consise formatter."
      ),
    verbose=False,
    memory=False
)
coordinator_agent = Agent(
  role= "Morning Message Coordinator",
  goal= "Combine the quote + tip and the formatted tasks into a friendly morning message, ~ 506 lines.",
  backstory=(
      "Friendly assistant that crafts motivating messages."
      ),
    verbose=False,
    memory=False,
    allow_delegation=False
)

# Create Task
task_quote= Task(
    description=(
        "Generate a short motivational quote (1-2 sentences) and a one-line productivity tip. Return JSON like: {\"QUOTE\": \"...\",\n \"TIP\": \"...\"}"
        ),
    expected_output="JSON with 'QUOTE' and \n 'TIP'",
    agent=quote_agent
)

task_format_tasks = Task(
    description=(
        "Format the user's provided in input 'task' (comma-separated string) into a markdown bullet list (maximum 6 items)."
        ),
    expected_output="Markdown bullet list",
    agent=task_agent
)
task_combine = Task(
    description=(
        "Combine the outputs of the previous tasks (quote+tip JSON and foratted task bullets) into a single friendly morning message ready to send."
        ),
    expected_output="Friendly morning message",
    agent=coordinator_agent
)
# Create Crew
crew = Crew(
    agents=[quote_agent, task_agent, coordinator_agent],
    tasks=[task_quote, task_format_tasks, task_combine],
    process=Process.sequential,
    memory=False,
    cache=False,
    share_crew=False
)
input_tasks = input("Enter tasks (comma-separated): ")

print("Running CrewAI warm-up - this will produce a single morning message...\n")

result = crew.kickoff(inputs={'task': input_tasks})
try:
    if hasattr(result, 'output'):
        final_output = result.output
    else:final_output = str(result)
except Exception:
    finall_output = str(result)

print("\n=== Morning Message (final) ===\n")
print(final_output)
