import json
from pathlib import Path
from google.adk.agents import Agent

def suggest_catering(event_type: str, guests: int, cuisine: str, budget: float, location: str) -> dict:
    data_path = Path("data/catering.json")
    if not data_path.exists():
        return {"status": "error", "options": [], "message": "Catering data not found"}

    with open(data_path, "r") as f:
        catering_data = json.load(f)

    city_options = catering_data.get(location, [])
    suitable = [
        vendor for vendor in city_options
        if vendor["cost_per_person"] * guests <= budget
    ]

    return {"status": "success", "options": suitable}

catering_agent = Agent(
    name="catering_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to suggest catering vendors and menus.",
    instruction="You are a helpful agent that recommends catering options based on event type, guest count, cuisine preferences, location, and total budget.",
    tools=[suggest_catering],
)
