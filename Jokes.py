# Step 1: Install requests
# Step 2: Import requests
import requests
import json

# Step 3: Make GET requests to the joke API
joke_url = "https://v2.jokeapi.dev/joke/Dark?type=single&amount=15"
joke_response = requests.get(joke_url)
joke_data = joke_response.json()

# Step 4: Combine the joke data (we'll keep the format as it is)
jokesList = []
for i in range(15):
    if i < len(joke_data['jokes']):
        joke_info = {
            "joke": joke_data['jokes'][i]['joke'],
            "category": joke_data['jokes'][i]['category'],
            "type": joke_data['jokes'][i]['type']
        }
        jokesList.append(joke_info)

# Step 5: Save combined joke data to JSON file
with open("joke_data.json", "w") as f:
    json.dump(jokesList, f, indent=4)

# Step 6: Print the results in a readable format
for index, joke_info in enumerate(jokesList, start=1):
    print("--------")
    print(f"Joke {index}")
    print("--------")
    print(f"Category: {joke_info['category']}")
    print(f"Type: {joke_info['type']}")
    print(f"Joke: {joke_info['joke']}")
    print("--------\n")