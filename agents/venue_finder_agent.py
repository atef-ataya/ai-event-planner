from google.adk.agents import Agent

def find_venues(event_type: str, location: str, guests: int, budget: float) -> dict:
    """
    Mock function to find venues based on event details.
    """
    # In a real scenario, this would query a database or API.
    venues = [
        {
            "name": "Grand Hall",
            "location": location,
            "capacity": 150,
            "price": 4500,
        },
        {
            "name": "Sunset Gardens",
            "location": location,
            "capacity": 120,
            "price": 4000,
        },
        {
            "name": "City Banquet Center",
            "location": location,
            "capacity": 200,
            "price": 5000,
        },
    ]
    # Filter venues based on guests and budget
    suitable_venues = [
        venue for venue in venues
        if venue["capacity"] >= guests and venue["price"] <= budget
    ]
    return {"status": "success", "venues": suitable_venues}

venue_finder_agent = Agent(
    name="venue_finder_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to find suitable venues based on event details.",
    instruction="You are a helpful agent that suggests venues based on event type, location, guest count, and budget.",
    tools=[find_venues],
)
