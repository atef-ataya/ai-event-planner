import json
from pathlib import Path
from google.adk.agents import Agent

def find_venues(event_type: str, location: str, guests: int, budget: float) -> dict:
    data_path = Path("data/venues.json")
    if not data_path.exists():
        return {"status": "error", "venues": [], "message": "Venue data not found"}

    with open(data_path, "r") as f:
        venues_data = json.load(f)

    city_venues = venues_data.get(location, [])
    suitable = [v for v in city_venues if v["capacity"] >= guests and v["price"] <= budget]

    return {"status": "success", "venues": suitable}

venue_finder_agent = Agent(
    name="venue_finder_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to find suitable venues based on event details.",
    instruction="You are a helpful agent that suggests venues based on event type, location, guest count, and budget.",
    tools=[find_venues],
)
