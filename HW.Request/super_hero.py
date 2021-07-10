import requests

namesearch_url = "https://superheroapi.com/api/2619421814940190/search/"
superheroes = [{"name": 'Hulk'}, {"name": "Captain America"}, {"name": "Thanos"}]

for hero in superheroes:
    hero_r = requests.get(namesearch_url + hero["name"])
    hero['intelligence'] = int(hero_r.json()["results"][0]["powerstats"]["intelligence"])

smartest_hero = sorted(superheroes, key=lambda character: hero['intelligence'])
print(smartest_hero[-1]["name"])
