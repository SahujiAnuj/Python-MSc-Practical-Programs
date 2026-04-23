# Program 15: Count Frequency of Words using Dictionary


# Take input from user
text = input("Enter a sentence: ").lower()

# Remove punctuation (basic)
for ch in ".,!?;:'\"":
    text = text.replace(ch, "")

# Split into words
words = text.split()

# Count frequency
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

# Display result
print("\nWord Frequency:")
for word, count in freq.items():
    print(word, ":", count)
