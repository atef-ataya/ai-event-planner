from agents.host_agent import HostAgent

host = HostAgent()

event_input = {
    "event_type": "wedding",
    "location": "Dubai",
    "guests": 100,
    "budget": 5000,
    "cuisine": "Middle Eastern"
}

response = host.run(event_input=event_input)

print("\n✅ Final Aggregated Response:")
print(response)
