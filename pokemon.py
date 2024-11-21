# Step 1: Install requests
# Step 2: Import requests
import requests
import json

# Step 3: Make GET requests to the APIs
poke_url = "https://pokeapi.co/api/v2/pokemon?limit=15"
poke_response = requests.get(poke_url)
poke_data = poke_response.json()

images_url = "https://fakerapi.it/api/v1/images?_type=people&_quantity=15"
images_response = requests.get(images_url)
images_data = images_response.json()

places_url = "https://fakerapi.it/api/v1/places?_quantity=15"
places_response = requests.get(places_url)
places_data = places_response.json()

# Step 4: Create new dictionaries by combining data from each API
pokeLocation = []
for i in range(15):
    if i < len(poke_data['results']) and i < len(images_data['data']) and i < len(places_data['data']):
        poke_info = {
            "pokemon": poke_data['results'][i]['name'],
            "image": images_data['data'][i]['url'],
            "location": {
                "latitude": places_data['data'][i]['latitude'],
                "longitude": places_data['data'][i]['longitude']
            }
        }
        pokeLocation.append(poke_info)

# Step 5: Save combined data to JSON file
with open("poke_location_data.json", "w") as f:
    json.dump(pokeLocation, f, indent=4)

# Step 6: Print the results in a readable format
for index, poke_info in enumerate(pokeLocation, start=1):
    print("--------")
    print(f"Pokemon {index}")
    print("--------")
    print(f"Name: {poke_info['pokemon']}")
    print(f"Image: {poke_info['image']}")
    print(f"Latitude: {poke_info['location']['latitude']}")
    print(f"Longitude: {poke_info['location']['longitude']}")
    print("--------\n")