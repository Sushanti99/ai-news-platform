import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
from string import punctuation


# url = "https://techcrunch.com/2024/12/05/openai-confirms-its-new-200-plan-chatgpt-pro-which-includes-reasoning-models-and-more/"


def getTextFromURL(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return text


def summarize_text(text, max_length=200):
    """
    Summarize the given text using the TextRank algorithm.

    Parameters:
    text (str): The text to be summarized.
    max_length (int): The maximum length of the summary in characters.

    Returns:
    str: The summarized text.
    """
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the sentences into words
    words = [word_tokenize(sentence.lower()) for sentence in sentences]

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english') + list(punctuation))
    filtered_words = [[word for word in sentence if word not in stop_words] for sentence in words]

    # Create a graph representation of the sentences
    sentence_scores = defaultdict(int)
    for i, sentence in enumerate(filtered_words):
        for word in sentence:
            sentence_scores[i] += 1

    # Apply the TextRank algorithm to score the sentences
    for _ in range(10):
        for i in sentence_scores:
            score = 0
            for j in sentence_scores:
                if i != j:
                    score += sentence_scores[j] / len(filtered_words[j])
            sentence_scores[i] = 0.15 + 0.85 * score

    # Select the top-scoring sentences for the summary
    summary_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary_sentences = [sentences[index] for index, _ in summary_sentences[:int(len(sentences) * 0.2)]]

    # Limit the summary to the maximum length
    summary = ' '.join(summary_sentences)
    # if len(summary) > max_length:
    #     summary = summary[:max_length] + '...'

    return summary


def return_summary(url_list):
    responses = ""
    for url in url_list:
        response = getTextFromURL(url)
        print('url: ', url)
        print('summary: ',summarize_text(response))
        responses += response
    return summarize_text(responses)
