sentence = "this is a sample sentence, " 
words=sentence.split()
dict_data={}
print(words)

for word in words:
    dict_data[word] = dict_data.get(word, 0) + 1

print( "Frequency:", dict_data)