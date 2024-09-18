def function(word1,word2):
    len1 = len(word1)
    len2 = len(word2)
    shorter_length = min(len1, len2)
    return shorter_length

word1 = str(input("enter word1:-"))
word2 = str(input("enter word2:-"))
print(function(word1,word2))