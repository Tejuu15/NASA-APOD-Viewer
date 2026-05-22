import requests

API_KEY = "DEMO_KEY"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url)
data = response.json()

print("\n🚀 NASA Astronomy Picture of the Day\n")

print("Title:", data["title"])
print("Date:", data["date"])
print("\nExplanation:\n")
print(data["explanation"])

print("\n🌌 Image URL:")
print(data["url"])