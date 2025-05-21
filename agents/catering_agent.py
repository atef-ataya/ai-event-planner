# agents/catering_agent.py

from adk.agent import Agent
from adk.types import AgentInput, AgentOutput
from adk.context import Context
from adk.prompt import Prompt

class CateringAgent(Agent):
    def __init__(self):
        super().__init__(name="CateringAgent")

    def prompt(self, context: Context, input: AgentInput) -> Prompt:
        cuisine = input.get("cuisine", "any")
        guests = input["guests"]
        budget = input["budget"]

        prompt_text = f"""
        Suggest 3 catering options that provide {cuisine} food for {guests} people.
        The total budget is ${budget}.
        For each, include:
        - Vendor name
        - Menu type (buffet/plated)
        - Cost per person
        - Total cost
        - Dietary options if available
        """

        return Prompt(text=prompt_text)

    def process_output(self, context: Context, output: AgentOutput):
        return output.response
