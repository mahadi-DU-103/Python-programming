"""1. In a world where social media usage makes up 2+ hours of our day on average, it's hard to keep up with slang.
 Let's build a list of your favorite trendy or overused expressions! 😎"""
genz_slang = ["Bet", "fanum tax", "Cap/No Cap", "Flex", "Lit", "Vibe Check",]
for term in genz_slang:
    print(f"Gen Z slang: {term}")
genz_slang_explanations = {
    "Bet": "Used to agree with something or confirm plans.",
    "fanum tax": "A humorous term for the cost of using social media.",
    "Cap/No Cap": "Cap means a lie, while no cap means truth.",
    "Flex": "To show off or boast about something.",
    "Lit": "Something that is exciting or excellent.",
    "Vibe Check": "A way to assess the mood or energy of a situation."
}
for term, explanation in genz_slang_explanations.items():
    print(f"{term}: {explanation}")

"""When you and your friends are scattered across different cities, sharing locations is something that can help you feel closer. 🫶

Let's use latitude and longitude 🌐 to create tuples of our friends locations!

Create a tuple for the city you are in.
Create 3 tuples for your friends, each with the latitude and longitude of the cities they live in.
Print the locations of all your friends.
Which of your friends is the furthest away?"""
from geopy.distance import geodesic 
def gps():
    my_location = (23.810331, 90.412521)  # Example: Dhaka, Bangladesh
    friends_locations = {
        "sam": (22.845640, 89.540328),  # Example: Khulna, Bangladesh
        "awfi": (24.363889, 88.624722),     # Example: Rajshahi, Bangladesh
        "suvro": (22.356853, 91.783180)      # Example: Chittagong, Bangladesh
                        }
    x = input("Enter your friend's name: ").strip().lower()
    if x in friends_locations:
        print(f"{x}'s location is {friends_locations[x]}")
        distances = geodesic(my_location, friends_locations[x]).km
        print(f"Distance from my location to {x}'s location: {distances:.2f} km")
    else:
        print("Friend's location is not available.")


"""Let’s catalog an artifact from a art museum! 🖼️ 👩‍🎨

First, search the Museum site for your favorite artifact. Scroll to "Artwork Details" and let's start cataloging.

On the Python editor, create a dictionary with the information of your artifact, including:

artist
period
date
Lastly, print the dictionary. What do you see? What if we just want to print the keys, or the values?"""
def artifact_catalog():
    artifact = {
        "artist1":{"artist": "Vincent van Gogh",
                    "period": "Post-Impressionism",
                    "date": "1889",
                    "title": "Starry Night"},
        "artist2":{"artist": "Claude Monet",
                    "period": "Impressionism",
                    "date": "1872",
                    "title":"Water lily"},
        "artist3":{"artist": "Leonardo da Vinci",
                    "period": "Renaissance",
                    "date": "1503",
                    "title": "Mona Lisa"}           
                }
    print("Welcome to the Museum Artifact Catalog!")
    name = str(input("Enter the name of the artist: ").strip().lower())
    found = False #- found = False: We start by assuming the artist isn't in the catalog.
    for info in artifact.values():
        if info["artist"].lower() == name:
            print(f"Details of {name}:  name:{info['artist']}, period:{info['period']}, date:{info['date']}, title:{info['title']}")
            found = True
            return
    if not found:
            print("Artist not found in the catalog.")
            
            """This is a flag variable — a simple way to track whether we found a match during the loop.
Here's how it works:
- Inside the loop: If we find a match, we set found = True.
- After the loop: We check if not found: to decide whether to print "Artist not found"
Without the flag, we wouldn’t know unless we added extra logic like counting matches or breaking early.."""
artifact_catalog()

"""Grocery shopping is great until you forget what was on your list. 😥

Before you head out, your best friend ask you to pick up some fruit for her too. Let's combine the lists!

Create two sets representing your favorite fruits and your best friend's favorite fruits.
Print the union of the two sets would look like.
Print the intersection of the two sets.
Have fun with it, check if the same fruit is in both sets or see the <difference> in both sets.
    """
def grocery_shopping():
    my_fruits = {"apple", "banana", "mango", "orange"}
    friend_fruits = {"banana", "kiwi", "grape", "watermelon"}
    print("My favorite fruits:", my_fruits)
    print("Friend's favorite fruits:", friend_fruits)
    all_fruits = my_fruits | friend_fruits #"|" means union
    print("all the fruits I and bro wants: ", all_fruits)
    common_fruits = my_fruits & friend_fruits #"&" means intersection
    print("Fruits we both like: ", common_fruits)
    my_unique_fruits = my_fruits - friend_fruits #"-" means difference
    friend_unique_fruits = friend_fruits - my_fruits
    print("Fruits only I like: ", my_unique_fruits)
    print("Fruits only my friend likes: ", friend_unique_fruits)    
grocery_shopping()

#a code on madrid's post game stats
def madrid_stats(): 
    lineup = {'player1':{'name':'Kylian Mbappe','kit number':9,'position':'forward','stats':{'goals':33,'assists':5,'appearences':35}},
          'player2':{'name':'Vinicius Jr','kit number':7,'position':'forward','stats':{'goals':19,'assists':10,'appearences':35}},
          'player3':{'name':'Jude Bellingham','kit number':5,'position':'midfielder','stats':{'goals':12,'assists':11,'appearences':35}},
          'player4':{'name':'Rodrygo','kit number':11,'position':'forward','stats':{'goals':15,'assists':7,'appearences':35}},
          'player5':{'name':'Antonio Rudiger','kit number':2,'position':'defender','stats':{'goals':2,'assists':1,'appearences':30}},
          'player6':{'name':'David Alaba','kit number':4,'position':'defender','stats':{'goals':3,'assists':2,'appearences':32}},
          'player7':{'name':'Eduardo Camavinga','kit number':12,'position':'midfielder','stats':{'goals':4,'assists':6,'appearences':33}},
          'player8':{'name':'Toni Kroos','kit number':8,'position':'midfielder','stats':{'goals':5,'assists':8,'appearences':34}},
          'player9':{'name':'Luka Modric','kit number':10,'position':'midfielder','stats':{'goals':6,'assists':9,'appearences':34}},
          'player10':{'name':'Eder Militao','kit number':3,'position':'defender','stats':{'goals':1,'assists':0,'appearences':31}},
          'player11':{'name':'Thibaut Courtois','kit number':1,'position':'goalkeeper','stats':{'clean sheets':18,'saves':120,'appearences':35}}
        }      
    print("Welcome to Real Madrid's Post-Game Stats!")
    player_name = input("Enter the player's name to get their stats: ").strip().lower() 
    """The .strip() method in Python is a built-in string method
    used to remove characters from the beginning (leading) and end (trailing) of a string.
    By default, it removes whitespace characters (spaces, tabs, newlines), but you can also specify other characters to remove.
        text = "   Hello, World!   \n"
    cleaned_text = text.strip()
    print(f"'{cleaned_text}'")
    # Output: 'Hello, World!'"""
    found = False
    for player in lineup.values(): #.values() method returns a view object that displays a list of all the values in the dictionary. things after "":"".
        if player['name'].lower() == player_name:
            print(f"Stats for {player['name']}:")
            print(f"Kit Number: {player['kit number']}")
            print(f"Position: {player['position']}")
            for stat, value in player['stats'].items():
                print(f"{stat.capitalize()}: {value}")
            stats = player['stats']
            average_stat = (stats['goals']+stats['assists'])/stats['appearences']
            print(f"Average goal contribution per game for {player['name']}: {average_stat:.2f}")
            found = True
            return
    if not found:
            print("Player not found in the lineup.")
madrid_stats()
