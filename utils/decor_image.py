import openai
import requests
import os
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_decor_image(theme: str, event_type: str = "event") -> BytesIO:
    prompt = (
        f"Interior decor layout for a {theme} themed {event_type}. "
        "Elegant floral details, warm lighting, cozy seating, no people, high resolution, 16:9."
    )

    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    image = BytesIO(requests.get(image_url).content)
    image.seek(0)
    return image
