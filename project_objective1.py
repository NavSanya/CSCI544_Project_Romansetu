# -*- coding: utf-8 -*-
"""Project_Objective1.ipynb"""

from ai4bharat.transliteration import XlitEngine # Used in paper

import csv

from itertools import product


"""# **Step 1: Data Preparation**"""


file_path = "data/hindi_data/hindi_english_parallel.csv"

# Lists to store Hindi and English sentences
hindi_sentences = []
english_sentences = []

# Read data from the CSV file
with open(file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        hindi_sentences.append(row['hindi'])
        english_sentences.append(row['english'])

print(hindi_sentences[:5])
print(english_sentences[:5])


# intializing the indic-en multilingual model and dictionaries (if rerank option is True)
e = XlitEngine( beam_width=10, src_script_type = "indic")

# Example Devanagari text
devanagari_text = "यह एक उदाहरण है"
out = e.translit_sentence(devanagari_text, 'hi')
print(out)


# New DataSet
romanization_file = "data/hindi_data/romanized_hindi_english_paper.csv"

with open(romanization_file, 'w', newline='', encoding = 'utf-8') as file:
  writer = csv.writer(file)
  i = 0
  for sentence in hindi_sentences:
    sen = e.translit_sentence(sentence, 'hi')
    writer.writerow([hindi_sentences[i], sen, english_sentences[i]])
    i+=1
    if(i%500 == 0):
        print(f"Doing sentence {i}")


# ----------------------------------------------------------------

file_path = "data/hindi_data/hindi_sentiment_analysis.csv"

# Lists to store Hindi and sentiment of sentences
hindi_sentences = []
sentiment = []

# Read data from the CSV file
with open(file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        hindi_sentences.append(row[0])
        sentiment.append(row[1])

print(hindi_sentences[:5])
print(sentiment[:5])


# New DataSet
romanization_file = "data/hindi_data/romanized_hindi_sentiment_paper.csv"

with open(romanization_file, 'w', newline='', encoding = 'utf-8') as file:
  writer = csv.writer(file)
  i = 0
  for sentence in hindi_sentences:
    sen = e.translit_sentence(sentence, 'hi')
    writer.writerow([hindi_sentences[i], sen, sentiment[i]])
    i+=1
    if(i%500 == 0):
        print(f"Doing sentence {i}")