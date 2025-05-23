from google.adk.agents import Agent

def generate_invites(event_type: str, channel: str, guest_count: int) -> dict:
    """
    Generates a simple invitation message.
    """
    message = f"""
    You are invited to our special {event_type.title()} celebration!
    We are hosting {guest_count} guests and would be honored to have you with us.

    Please RSVP via {channel.title()}.
    """

    return {
        "status": "success",
        "channel": channel,
        "message": message.strip()
    }

invite_manager_agent = Agent(
    name="invite_manager_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to generate invitation messages for events based on type and communication channel.",
    instruction="You are an invite expert. Write clear and compelling messages for WhatsApp, Email, or SMS based on event type and guest count.",
    tools=[generate_invites],
)
