from src.main import get_weather

# Utility function to load cities from a text file
def load_cities(file_path='data/sample_cities.txt'):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

import requests
import pytest


@pytest.mark.parametrize("city", load_cities())
def test_temperature_and_humidity_fields_exist(city):
    response = get_weather(city)
    data = response.json()
    current = data.get("current", {})

    print(f"Checking temperature and humidity fields for {city}...")  # Debugging output

    assert "temp_c" in current, f"'temp_c' field is missing for {city}"
    assert isinstance(current["temp_c"], (int, float)), f"'temp_c' should be numeric for {city}"

    assert "humidity" in current, f"'humidity' field is missing for {city}"
    assert isinstance(current["humidity"], int), f"'humidity' should be an integer for {city}"


@pytest.mark.parametrize("city", load_cities())
def test_response_time_is_reasonable(city):
    response = get_weather(city)
    elapsed_time = response.elapsed.total_seconds()

    # This threshold is somewhat arbitrary but works for now
    assert elapsed_time < 0.5, f"API response for {city} took too long: {elapsed_time:.3f}s"


def test_invalid_city_should_return_error():
    fake_city = "no_city_should_have_this_name_98765"
    response = get_weather(fake_city)

    # Based on manual testing, this API sometimes returns 200 with an error message in JSON
    assert response.status_code in [400, 404], (
        f"Expected 400 or 404 for invalid city, got {response.status_code}"
    )


@pytest.mark.skip(reason="Pending a fix for inconsistent API response codes")
def test_city_with_special_characters():
    # Edge case test: city names with accents or special characters
    weird_city = "São Paulo"
    response = get_weather(weird_city)
    assert response.status_code == 200