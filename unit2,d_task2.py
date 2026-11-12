text = "  Hello Python Programming  "
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Strip:", text.strip())
words = text.split()
print("Split:", words)
print("Join:", "-".join(words))
print("Replace:", text.replace("Python", "Java"))
print("Find:", text.find("Python"))