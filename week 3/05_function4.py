def function3(word):
    first = word[0]
    last = word[len(word)-1]
    combined = last + first
    return combined

word = input("Enter the word :-")
print(function3(word))
