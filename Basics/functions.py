#A function to add two intergers and return the answer
def add_int(a,b) :
    return a + b
add_int(5,6)
print(add_int(5,6))
# A function that checks if one word is the reverse of the another word
def check_reverse(first_word, second_word):
    if len(first_word) != len(second_word):
        return False

    i = 0
    j = len(second_word) - 1

    while j >= 0:
        if first_word[i] != second_word[j]:
            return False
        i += 1
        j -= 1

    return True

print(check_reverse("pots", "stop"))

# A function that prints the number of times a char appears in a string
word= input("Enter any word :")
def count_char() :
     for letter in set(word):
      print(letter ,word.count(letter))
print(count_char())      
    