from google.adk.agents import Agent
from utils.timeline import generate_timeline

schedule_agent = Agent(
    name="schedule_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to create a personalized timeline for the event.",
    instruction="Generate a schedule based on event type and start time. Use industry best practices.",
    tools=[generate_timeline],
)
