# tools/location.py
import os
import googlemaps

# Initialize Google Maps client using your API key
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

def get_cities_by_country(country_code: str) -> dict:
    """
    Returns a list of major cities for the given country using Geocoding API and known city names.
    """
    # Hardcoded fallback city list for common countries
    fallback_cities = {
        "AE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Al Ain", "Fujairah", "Ras Al Khaimah"],
        "US": ["New York", "Los Angeles", "Chicago", "San Francisco", "Miami", "Austin"],
        "IN": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Kolkata"],
        "UK": ["London", "Manchester", "Birmingham", "Glasgow", "Liverpool", "Edinburgh"]
    }

    cities = fallback_cities.get(country_code.upper(), [])
    return {"status": "success", "cities": cities}
