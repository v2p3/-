import re

# Input sentence
input_sentence = "The quick brown fox jumps over the lazy dog. The cat is also agile."

# Regular expression pattern for words with exactly three characters
regex_pattern = r'\b\w{3}\b'

# Use re.findall to find all matches in the text
matching_words = re.findall(regex_pattern, input_sentence)

# Print matching words
print("Matching words:",matching_words)
