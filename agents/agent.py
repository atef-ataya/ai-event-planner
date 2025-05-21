from google.adk.agents import Agent

def find_venues(event_type: str, location: str, guests: int, budget: float) -> dict:
    # Your implementation here
    pass

root_agent = Agent(
    name="venue_finder_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to find suitable venues based on event details.",
    instruction="You are a helpful agent that suggests venues based on event type, location, guest count, and budget.",
    tools=[find_venues],
)
