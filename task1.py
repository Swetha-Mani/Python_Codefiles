count_vowels = 0
count_Cons = 0
String = input("Enter the letters:")
Vowels = "AEIOUaeious" 
for i in String:
    if i in Vowels:
        count_vowels += 1
    else:
        count_Cons += 1

print("The total count of vowels letters:",count_vowels)
print("The total count of Consonants  letters:",count_Cons)