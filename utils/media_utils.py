import os
import requests
import openai
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import textwrap

# Load API keys
load_dotenv(dotenv_path="agents/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")
eleven_api_key = os.getenv("ELEVENLABS_API_KEY")

# ========== IMAGE INVITATION ==========
def generate_custom_invite_image(invite_text: str, theme: str) -> BytesIO:
    # Get boho background from DALL·E
    prompt = (
        "Vertical boho chic invitation background, soft terracotta/ivory tones, "
        "clean center, subtle floral details, 1024x1024, no text"
    )
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="standard"
    )
    image_url = response.data[0].url
    base_image = Image.open(BytesIO(requests.get(image_url).content)).convert("RGBA")

    # Prepare text overlay
    draw = ImageDraw.Draw(base_image)
    font_path = "assets/fonts/GreatVibes-Regular.ttf"
    try:
        font = ImageFont.truetype(font_path, size=50)
    except:
        font = ImageFont.load_default()

    text_color = (30, 30, 30, 255)  # deep charcoal
    shadow_color = (0, 0, 0, 180)
    shadow_offset = 2
    margin = 100
    max_width = base_image.width - 2 * margin
    lines = textwrap.wrap(invite_text, width=30)

    # Center text vertically
    line_heights = [font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines]
    total_height = sum(line_heights) + 10 * (len(lines) - 1)
    y_text = (base_image.height - total_height) // 2

    for i, line in enumerate(lines):
        bbox = font.getbbox(line)
        line_width = bbox[2] - bbox[0]
        line_height = line_heights[i]
        x_text = (base_image.width - line_width) // 2

        # Shadow
        draw.text((x_text + shadow_offset, y_text + shadow_offset), line, font=font, fill=shadow_color)
        # Main text
        draw.text((x_text, y_text), line, font=font, fill=text_color)

        y_text += line_height + 10

    output = BytesIO()
    base_image.save(output, format="PNG")
    output.seek(0)
    return output


# ========== VOICE INVITATION ==========
def generate_voice_invitation(text: str, voice_id="21m00Tcm4TlvDq8ikWAM") -> BytesIO:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": eleven_api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Voice generation failed: {response.status_code} - {response.text}")

    audio_bytes = BytesIO(response.content)
    audio_bytes.seek(0)
    return audio_bytes
