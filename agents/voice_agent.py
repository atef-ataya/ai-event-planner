from google.adk.agents import Agent

def generate_audio(summary_text: str) -> dict:
    """
    Mock function to convert event summary to audio.
    Replace with ElevenLabs integration later.
    """
    # Here you would normally call ElevenLabs or another TTS provider
    # For now, return a fake URL
    audio_url = "https://example.com/generated_audio.mp3"

    return {
        "status": "success",
        "audio_url": audio_url,
        "summary": summary_text[:100] + "..."  # preview for debug
    }

voice_agent = Agent(
    name="voice_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent that converts event summaries into spoken audio using ElevenLabs.",
    instruction="You are a voice assistant. Generate an audio version of the final event plan using text-to-speech.",
    tools=[generate_audio],
)
