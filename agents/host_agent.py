# agents/host_agent.py

from agents.venue_finder_agent import VenueFinderAgent
from agents.catering_agent import CateringAgent

class HostAgent:
    def __init__(self):
        self.venue_agent = VenueFinderAgent()
        self.catering_agent = CateringAgent()
        # TODO: Add other agents later

    def run(self, event_input):
        print("🔄 Running VenueFinderAgent...")
        venue = self.venue_agent.run(input=event_input)

        print("🔄 Running CateringAgent...")
        catering = self.catering_agent.run(input=event_input)

        # You can format or merge results here
        return {
            "venue": venue,
            "catering": catering
        }
