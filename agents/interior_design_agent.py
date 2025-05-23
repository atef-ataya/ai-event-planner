from google.adk.agents import Agent

def design_theme(event_type: str, theme: str, guests: int, budget: float) -> dict:
    """
    Suggest interior design ideas for the event.
    """
    design_options = {
        "Boho Chic": {
            "colors": ["Terracotta", "Ivory", "Gold"],
            "elements": [
                "Dried floral arrangements",
                "Macrame backdrops",
                "Fairy light canopy"
            ]
        },
        "Modern Minimalist": {
            "colors": ["White", "Greenery", "Black"],
            "elements": [
                "Monochrome table setups",
                "Pampas centerpieces",
                "LED ambient lighting"
            ]
        }
    }

    design = design_options.get(theme, {
        "colors": ["Custom"],
        "elements": ["Minimal decor suggestions available."]
    })

    return {
        "status": "success",
        "design": {
            "theme": theme,
            "recommended_colors": design["colors"],
            "decor_elements": design["elements"],
            "event_type": event_type
        }
    }

interior_design_agent = Agent(
    name="interior_design_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Agent to suggest interior decoration styles and themes for events.",
    instruction="You are a helpful interior designer for events. Recommend a theme-based setup including colors, elements, and styles.",
    tools=[design_theme],
)
