# tuple = (1, 2, 3, 4, 3)
# print(tuple[0]) 
# #tuple[0]=3 is not valid because we cant assign values in tuple.
# print(type(tuple))
# tuple = (1, ) #single value tuple should be written accordingly.
# print(type(tuple), tuple) #if we dont use comma python will consider it an int value.

# print(tuple[1:3]) #tuple slicing

# print(tuple.index(1,4)) #returns index of first occurrence.

# print(tuple.count(3)) #returns total occurrences.

# movies = input("your number 1 pick:"), input("your number 2 pick:"), input("your number 3 pick:")
# list[movies] 
# print(movies) #wrote a program to name my 3 fav movies and list them.

# #wrote a code to check if a list contains a palindrome or not.
# list = ['m', 'a', 'a', 'm', 'k']
# copied_list = list.copy()
# copied_list.reverse()
# if(list == copied_list):
#     print("palindrome") #palindrome= a word, phrase, or sequence that reads the same backwards as forwards.
# else:
#     print("not palindrome")

#post game stats:
rm = [{'name':'vini jr', 
'position':'forward', 
'jersey number': '07',
'stats': {'goals': 24, 'assists':'09'}}]
search_name = input("Enter the name of the player you are looking for:").lower()
print('name:'['name'],"position:"['position'])