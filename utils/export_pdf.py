from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(plan_data: dict) -> BytesIO:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, y, "AI Event Plan Summary")
    y -= 40

    def section(title):
        nonlocal y
        y -= 30
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, title)
        y -= 20
        c.setFont("Helvetica", 12)

    def line(text):
        nonlocal y
        c.drawString(60, y, text)
        y -= 20

    section("🗓️ General Info")
    for k in ["event_type", "location", "guests", "budget", "theme", "cuisine", "start_time"]:
        line(f"{k.replace('_', ' ').title()}: {plan_data.get(k)}")

    section("🏛️ Venues")
    for v in plan_data.get("venue", {}).get("venues", []):
        line(f"{v['name']} - {v['location']} | Capacity: {v['capacity']} | Price: {v['price']} AED")

    section("🍽️ Catering")
    for c_item in plan_data.get("catering", {}).get("options", []):
        line(f"{c_item['vendor']} | Menu: {c_item['menu_type']} | {c_item['cost_per_person']} AED")
        line(f"Options: {', '.join(c_item['dietary_options'])}")

    section("🎨 Decor")
    decor = plan_data.get("decor", {}).get("design", {})
    if decor:
        line(f"Theme: {decor.get('theme')}")
        line(f"Colors: {', '.join(decor.get('recommended_colors', []))}")
        line(f"Elements: {', '.join(decor.get('decor_elements', []))}")

    section("💌 Invitation Text")
    invite = plan_data.get("invite", "")
    for line_chunk in invite.split("\n"):
        line(line_chunk)

    section("🕒 Schedule")
    for item in plan_data.get("schedule", {}).get("schedule", []):
        line(f"{item['time']} - {item['activity']}")

    section("🤝 Sponsors")
    for s in plan_data.get("sponsors", {}).get("recommendations", []):
        line(f"{s['brand']} | {s['match']}")
        line(f"Pitch: {s['pitch']}")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
