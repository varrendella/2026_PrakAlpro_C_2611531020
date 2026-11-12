text = "Varren Della"
text = text.lower()
count = 0

for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)