import requests
from pprint import pprint

API_BASE_URL = 'https://superheroapi.com/api/2619421814940190/'
characters = ['Hulk', 'Captain America', 'Thanos']


def most_intelligence_character(character_list):
    intelligence_dict = {}
    for character in character_list:
        response = requests.get(API_BASE_URL + 'search/' + character)
        result = response.json()['results'][0]
        intelligence = result['powerstats']['intelligence']
        intelligence_dict[character] = int(intelligence)
    max_intelligence_value = max(intelligence_dict.values())

    for name, intelligence in intelligence_dict.items():
        if intelligence == max_intelligence_value:
            return name


character_name = most_intelligence_character(characters)

print(character_name)
