import json
from pathlib import Path
from google.adk.agents import Agent

def find_sponsors(event_type: str, audience_size: int, theme: str, location: str) -> dict:
    data_path = Path("data/sponsors.json")
    if not data_path.exists():
        return {"status": "error", "recommendations": [], "message": "Sponsorship data not found"}

    with open(data_path, "r") as f:
        sponsor_data = json.load(f)

    city_sponsors = sponsor_data.get(location, [])
    recommendations = []

    for sponsor in city_sponsors:
        if event_type in sponsor["event_types"] and theme in sponsor["themes"]:
            pitch = sponsor["pitch"].replace("{event_type}", event_type)
            recommendations.append({
                "brand": sponsor["brand"],
                "match": sponsor["match"],
                "pitch": pitch
            })

    # fallback generic if none match
    if not recommendations:
        recommendations.append({
            "brand": "Local Business",
            "match": "General sponsor",
            "pitch": f"We are organizing a {event_type} in {location} and looking for a relevant sponsor."
        })

    return {"status": "success", "recommendations": recommendations}

sponsorship_agent = Agent(
    name="sponsorship_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to suggest potential sponsors and pitch templates for events.",
    instruction="You are a sponsorship expert. Recommend aligned brands and generate outreach messages based on city, audience, event type, and theme.",
    tools=[find_sponsors],
)
