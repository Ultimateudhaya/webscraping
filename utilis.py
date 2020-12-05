import re
import string
from collections import Counter
top_n = 5
new_stopwords = []
def get_statistics(data):
  lines = get_lines(data)
  words = get_words(lines)
  unique_words = list(set(words))
  cleaned_words = read_file()
  top_n_words = get_top_n_words(words,top_n,cleaned words)
  statistics = {'line_count':len(lines),'word_count':len(words),
    'unique_words':len(unique_words)
  return statistics

def get_lines(data):
  lines=[]
  for para in data:
    para_lines = re.split('[.?!]+',para)
    lines.extend(para_lines)
  cleaned_lines = clean_string(lines)
  return cleaned_lines 
def clean_string(lines):
  cleaned_lines = []
  st = str.maketrans("","",string.punctuation)
    for line in lines:
     new_line = line.translate(st).lower.strip()
     if new_line:
       cleaned_lines.append(new_line)
  return cleaned_lines
def get_words(lines):
  words = []
  for line in lines:
     words.extend(line.split())
  return words

def read_file():
    with open('stopwords.txt', 'r') as f:
      stopwords = f.readlines()
      cleaned_words = get_cleaned_words(stopwords)
      return cleaned_words


def get_cleaned_words(stopwords):
  for i in stopwords:
    new_stopwords.append(i.strip("\n"))
  return new_stopwords
def get_top_n_words(words,top_n):
  top_n_words = Counter(words).most_common(top_n)
  top_words = []
  for x,y in top_n_words:
    top_words.append(x)
  return top_words
