import markovify

# Trump Corpus includes 25729 words.
trump_text = 'trump_corpus.txt'

# Get raw text as string. encoding = 'utf-8', mode = "r"
with open(trump_text, encoding='utf-8', mode='r') as f:
    text = f.read()

# Build the model
text_model = markovify.Text(text, state_size=3)

# open file for the great writening!
heidt = open('Hey_Everyone_Its_Donald_Trumpov.md', encoding='utf-8', mode='w')

for chapters in range(12):
    heidt.write('# ' + text_model.make_short_sentence(80, tries=5000) + '\n\n')
    for sections in range(20):
        heidt.write('### ' + text_model.make_short_sentence(140, tries=5000) + '\n\n' + text_model.make_sentence(
            tries=5000) + ' ' + text_model.make_sentence(tries=5000) + text_model.make_sentence(
            tries=5000) + '\n' + '>' + text_model.make_short_sentence(140,
                                                                      tries=5000) + '\n\n' + text_model.make_sentence(
            tries=5000) + ' ' + text_model.make_sentence(tries=5000) + ' ' + text_model.make_sentence(
            tries=5000) + '\n' + text_model.make_sentence(tries=5000) + ' ' + text_model.make_sentence(
            tries=5000) + ' ' + text_model.make_sentence(tries=5000) + '\n' + '>' + text_model.make_short_sentence(140, tries=5000) + '\n\n' + text_model.make_sentence(
            tries=5000) + ' ' + text_model.make_sentence(tries=5000) + ' ' + text_model.make_sentence(
            tries=5000) + '\n\n')

heidt.close()

file = 'Hey_Everyone_Its_Donald_Trumpov.md'


def count_words(file):
    num_words = 0
    with open(file, 'rb') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    print("Number of words:")
    print(num_words)


count_words(file)
