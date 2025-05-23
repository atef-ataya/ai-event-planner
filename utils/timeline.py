from datetime import datetime, timedelta

def generate_timeline(event_type: str, start_time: str) -> dict:
    base_time = datetime.strptime(start_time, "%H:%M:%S")
    timeline = []

    def add(minutes, activity):
        nonlocal base_time
        timeline.append({
            "time": base_time.strftime("%H:%M"),
            "activity": activity
        })
        base_time += timedelta(minutes=minutes)

    if event_type == "Wedding":
        add(0, "Guest Arrival")
        add(60, "Welcome Speech")
        add(60, "Dinner Service")
        add(90, "Entertainment & Open Floor")
        add(90, "Closing Remarks")

    elif event_type == "Corporate":
        add(0, "Registration & Coffee")
        add(30, "Opening Remarks")
        add(60, "Keynote Presentation")
        add(45, "Breakout Sessions")
        add(60, "Networking + Refreshments")

    elif event_type == "Birthday":
        add(0, "Guest Arrival & Cake Setup")
        add(30, "Welcome Toast")
        add(60, "Games & Fun")
        add(45, "Cake Cutting & Singing")
        add(60, "Open Gifts & Farewell")

    else:
        add(0, "Guest Arrival")
        add(60, "Main Event Segment")
        add(60, "Food & Socializing")

    return {"schedule": timeline}
