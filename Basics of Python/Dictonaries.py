# info = {
#     "name" : "Mahadi" ,
#     "university" : "University of Dhaka" ,
#     "age" : "21", 
#     "courses" : ["math", "sciene"],
#     "topics" : ("dic", "set", )
#             }
# print(info)
# #we can also print keys seperately.
# print(info["name"])
# print(info["topics"])
# #we can also assign new values in the keys.
# info["name"] = "mahadi islam"

# info2 = {}
# print(info2,type(info2)) #null dictionary.

# #nested dictionary:one dictionary in another.
# intro = { "name" : "mahadi",
#          "marks": {
#              "stat101" : 24,
#              "stat102" : 25,
#              "stat103" : 23, }, 
#          "overalls" : "good",}
# print(intro)
# print(intro["marks"])
# print(intro["marks"]["stat102"])

# #dictionary methods:
# print(list(intro.keys())) #returns all keys.
# print(intro.values()) #returns all values.
# print(intro.items()) #returns all(keys, values), pairs as tuples.
# print(intro.get("marks")) #returns the keys according to value.
# intro.update({"university" : "DU"}) #inserts the specified item to the dictionary.
# print(intro)

#post game stats of a team:
lineup = {'player1':{'name':'Kylian Mbappe','kit number':9,'position':'forward','stats':{'goals':33,'assists':5,'appearences':35}},
          'player2':{'name':'Vinicius Jr','kit number':7,'position':'forward','stats':{'goals':19,'assists':10,'appearences':35}},
          'player3':{'name':'Jude Bellingham','kit number':5,'position':'midfielder','stats':{'goals':12,'assists':11,'appearences':35}}
          }
print(list(lineup.keys()))
print(lineup['player1'])
print(lineup['player2'])
print(lineup['player3'])
lineup['player1'].update({'kit number':10})
goals_mbappe = lineup['player1']['stats']['goals']
assists_mbappe = lineup['player1']['stats']['assists']
appearences_mbappe = lineup['player1']['stats']['appearences']
goals_per_matches_mbappe = goals_mbappe/appearences_mbappe
assists_per_matches_mbappe = assists_mbappe/appearences_mbappe
goals_vini = lineup['player2']['stats']['goals']
assits_vini = lineup['player2']['stats']['assists']
appearences_vini = lineup['player2']['stats']['appearences']
goals_per_matches_vini = goals_vini/appearences_vini
assists_per_matches_vini = assits_vini/appearences_vini
goals_bellinhgam = lineup['player3']['stats']['goals']
assists_bellingham = lineup['player3']['stats']['assists']
appearences_bellingham = lineup['player3']['stats']['appearences']
assists_per_matches_bellingham = assists_bellingham/appearences_bellingham
print(f"{goals_per_matches_mbappe:.2f}")
print(f"{goals_per_matches_vini:.2f}")
if goals_per_matches_mbappe>goals_per_matches_vini:
    print("Kylian Mbappe wins the golden boot.")
else:
    print("Vinicius Jr wins the golden boot.")
if assists_per_matches_mbappe>assists_per_matches_vini:
    print(f"Kylian also wins the playmaker of the year award.")
elif assists_per_matches_vini>assists_per_matches_bellingham:
    print(f"Vinicius Jr wins the playmaker of the year award with {assits_vini} assists.")
else:
    print(f"Jude Bellingham wins the playmaker of the year award with {assists_bellingham} assists.")