import markovify


trump_text = 'trump_corpus.txt'

num_words = 0

with open(trump_text, 'rb') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)

# Trump Corpus includes 25729 words.



