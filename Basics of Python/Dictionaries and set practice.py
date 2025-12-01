#program to store following word meaning:
word_meaning = {
"table" : ["a piece of furniture.", "list of facts and figures."],
"cat" : "a small animal.",

}
print(word_meaning)
print(word_meaning["cat"]) #to only search on word.

"""I am given a list of subjects for students. Asuuming one classroom is required for one subject.
how many classrooms are needed by all students?"""
#ans: we can solve this through set.
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
necessary_classrooms = subjects.__len__()
print("necessary classrooms needed are :" ,necessary_classrooms)

"""Write a programe to enter marks of 3 subjects from the user and store them in a dictionary.
And start with an empty dictionary and add one by one. Use subject name as key and marks as values."""
#ans:
report_card = {}

marks = int(input("marks of stat 101:"))
report_card.update({"stat 101" : marks})

marks = int(input("marks of stat103:"))
report_card.update({"stat 103" : marks})

marks = int(input("marks of stat105:"))
report_card.update({"stat 105" : marks})
print(report_card)

#Figure out a way to store 9 and 9.0 as seperate values in the set.
#ans: either we can save one of the ans a string or we can save them as tubles.
values = {9, "9.0"}
print(values)
#or
values = {
("integer" , 9),
("float" , 9.0)
}
print(values)
