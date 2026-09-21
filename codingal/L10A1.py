s = str(input("enter a word: "))
letter = str(input("enter a letter from your word: "))

i = 0
count = 0

while(i < len(s)):
    if(s[i] == letter):
        count = count + 1
    i = i + 1

print("the letter ", letter, "comes ", count, "many times in", s)