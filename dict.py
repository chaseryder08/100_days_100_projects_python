#NESTING
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a dict inside a list


travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Nice", "Lille"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg"], 
        "total_visits": 6
        },
]

print(travel_log)