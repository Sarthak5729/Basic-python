
def count_vowels(text):
        vowels= "aeiou"
        count = 0

        for char in text:
         if char.lower() in vowels():
            count +=1
        return count
def main():
        text = input("Enter the number:")
        vowel_count = count_vowels(text)
        print(f"Number of vowels in{text}:{vowel_count}")
main()
