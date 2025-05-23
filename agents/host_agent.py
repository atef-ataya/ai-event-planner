import importlib
import json
from pathlib import Path

class HostAgent:
    def __init__(self, config_path="configs/agent_config.json"):
        self.agents = {}
        self.tools = {}

        # Load config
        with open(config_path, "r") as f:
            config = json.load(f)

        for entry in config["agents"]:
            try:
                module = importlib.import_module(f"agents.{entry['file']}")
                agent = getattr(module, entry["object"])
                self.agents[entry["name"]] = agent

                # Extract tool function for direct calling
                if hasattr(module, "__dict__"):
                    for attr in module.__dict__:
                        if callable(module.__dict__[attr]) and attr.startswith("find_") or attr.startswith("generate_") or attr.startswith("create_") or attr.startswith("suggest_"):
                            self.tools[entry["name"]] = module.__dict__[attr]
            except Exception as e:
                print(f"Failed to load agent: {entry['name']} – {e}")

    def run(self, input: dict) -> dict:
        result = {}

        # Venue
        venue = self.tools.get("venue_finder")
        if venue:
            result["venue"] = venue(
                event_type=input["event_type"],
                location=input["location"],
                guests=input["guests"],
                budget=input["budget"]
            )

        # Catering
        catering = self.tools.get("catering")
        if catering:
            result["catering"] = catering(
            event_type=input["event_type"],
            guests=input["guests"],
            cuisine=input["cuisine"],
            budget=input["budget"],
            location=input["location"]
        )


        # Interior Design
        decor = self.tools.get("interior_design")
        if decor:
            result["decor"] = decor(
                event_type=input["event_type"],
                theme=input["theme"],
                guests=input["guests"],
                budget=input["budget"]
            )

        # Invite Message
        invite = self.tools.get("invite_manager")
        if invite:
            result["invite"] = invite(
                event_type=input["event_type"],
                channel="whatsapp",
                guest_count=input["guests"]
            ).get("message", "No invite generated.")

        # Schedule
        scheduler = self.tools.get("schedule")
        if scheduler:
            result["schedule"] = scheduler(
                event_type=input["event_type"],
                start_time=input["start_time"]
            )


        # Sponsorship
        sponsors = self.tools.get("sponsorship")
        if sponsors:
            result["sponsors"] = sponsors(
            event_type=input["event_type"],
            audience_size=input["guests"],
            theme=input["theme"],
            location=input["location"]
        )


        # Voice
        voice = self.tools.get("voice")
        if voice:
            result["audio_url"] = voice(summary_text=result.get("invite", ""))["audio_url"]

        return result


# Required by ADK and Streamlit
host_agent = HostAgent()
