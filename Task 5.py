#Q1. python program to calculate the total number of vowels and count of each individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited"?#

def count_vowels(string):
    string = string.lower()
    total_vowels = 0
    count_a = count_e = count_i = count_o = count_u = 0

    for char in string:
        if char in "aeiou":
            total_vowels += 1
            if char == 'a':
                count_a += 1
            elif char == 'e':
                count_e += 1
            elif char == 'i':
                count_i += 1
            elif char == 'o':
                count_o += 1
            elif char == 'u':
                count_u += 1

    print("Total vowels:", total_vowels)
    print("Count of A:", count_a)
    print("Count of E:", count_e)
    print("Count of I:", count_i)
    print("Count of O:", count_o)
    print("Count of U:", count_u)

input_string = "Guvi Geeks Network Private Limited"
count_vowels(input_string)

#Q2. pyramid of numbers from 1 to 20 using for loop?#

def numberPyramid(rows):
    num = 1
    for i in range(1, rows + 1):

        for j in range(rows - i):
            print("  ", end="  ")
        for k in range(1, i + 1):
            print(f"{num:2}", end="  ")
            num += 1
            if num > 20:
                break

        print()

num_rows = 5
print(numberPyramid(num_rows))

#Q3.  program that takes a string and returns a new string with all the vowels removed?#

vowels = "aeiouAEIOU"
a= "This is Guvi Geeks python class"
b = "".join(char for char in a if char not in vowels)

print("Original String:", a)
print("New string without vowels:", b)

#Q4.   program that takes a string and returns the number of unique characters in it.#

c = "Python programming"
unique_characters = set()
for char in c:
    unique_characters.add(char)

print(f"Number of unique characters: {len(unique_characters)}")

#Q5.  program that takes a string and returns True if it is a palindrome, False otherwise.#


def isPalindrome(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

d = "Mom"
e = "Cat"

result_d = isPalindrome(d)
result_e = isPalindrome(e)

if result_d:
    print(True)
else:
    print(False)

#Q.6   program that takes two strings and returns the longest common substring between them.#
    
def longestCommonSubstring(str1, str2):
    len1, len2 = len(str1), len(str2)
    common_substring = ""

    for i in range (len1):
        for j in range(len2):
            k = 0
            while i + k < len1 and j + k < len2 and str1[i + k] == str2[j + k]:
                k += 1
            if k > len(common_substring):
                common_substring = str1[i:i + k]
    return common_substring

f = "python programming"
g = "python class"

result = longestCommonSubstring(f, g)

if result:
    print(f"The longest common substring is: {result}")
else:
    print("There is no common substring")

#Q.7  program that takes a string and returns the most frequent character in it.#
    
def mostFrequentCharacter(h):
    char_freq = {}

    for char in h:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1

    max_char = max(char_freq, key = char_freq.get)
    return max_char

i = "Sunisha"
result = mostFrequentCharacter(i)

print(f"The most frequent character is: {result}")

#Q.8   program that takes a string and returns True if it is an anagram of another string, False otherwise.#

def areAnagrams(str1, str2):
    clean_str1 = ''.join(str1.split()).lower()
    clean_str2 = ''.join(str2.split()).lower()
    return sorted(clean_str1) == sorted(clean_str2)

j = "Listen"
k = "Silent"

result = areAnagrams(j, k)

if result:
    print(True)
else:
    print(False)

#Q.9   program that takes a string and returns the number of words in it.#
    
def countWords(l):
    words = l.split()
    return len(words)

l = "A beautiful place to visit."
word_count = countWords(l)
print("Number of words in the string:", word_count)






    

