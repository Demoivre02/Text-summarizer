import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def clean_text(text):
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return words

def calculate_word_frequency(words):
    # Count the frequency of each word
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

def summarize_text(text):
    words = clean_text(text)

    # Creating a frequency table to keep the score of each word
    word_frequency = calculate_word_frequency(words)

    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentence_value = {}

    for sentence in sentences:
        for word, freq in word_frequency.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    sum_values = sum(sentence_value.values())

    # Average value of a sentence from the original text
    average = int(sum_values / len(sentence_value))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if sentence in sentence_value and sentence_value[sentence] > (1.2 * average):
            summary += " " + sentence

    return summary, len(words), len(summary.split())

# Example usage:
input_text = "Your input text goes here. It can be a paragraph or a longer piece of text."
result_summary, original_length, summary_length = summarize_text(input_text)

print("Original Text Word Count:", original_length)
print("Summarized Text Word Count:", summary_length)
print("Summarized Text:")
print(result_summary)
