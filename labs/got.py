## Script that reads the Game of Thrones text.
## Content taken from http://www.readbooksvampire.com
import requests
import re
import json
from bs4 import BeautifulSoup

base_site = "http://www.readbooksvampire.com/George_R.R._Martin/"
books = [
   { 'title': "A_Game_of_Thrones", 'chapters': 72 },
   { 'title': "A_Clash_of_Kings", 'chapters': 69 },
   { 'title': "A_Storm_of_Swords", 'chapters': 81 },
   { 'title': "A_Feast_for_Crows", 'chapters': 46 },
   { 'title': "A_Dance_with_Dragons", 'chapters': 64 }
]

# Breaks a paragraph on periods, colons etc
def breakParagraph(p):
   return re.split('(?<=\\:|\\.|\\!|\\?)\s', p)

# Gets the chapter's text out of the text body
def getText(content):
   text = BeautifulSoup(content, 'html.parser').select('td.concss')[0]
   paragraphs = [t.get_text() for t in text.select('div')]
   return [breakParagraph(p) for p in paragraphs if p != '\xa0']

# Read the text from the website, based on title and chapter
def getTextForChapter(title, chapter):
   source = requests.get(base_site + book['title'] + '/' + ('%02d.html' % chapter)).content
   return getText(source)

chapters = []

# For each book we go through each chapter, download the text and store it.
# The resulting "chapters" list is later written to a file
for book in books:
   print("Book: %s" % book['title'])
   chapters = chapters + [
      {
         'title': book['title'],
         'chapter': i,
         'text': getTextForChapter(book['title'], i)
      }
      for i in range(1, book['chapters']+1)
   ]

# We now write the results to a file
with open('got.json', 'w') as f:
   json.dump(chapters, f)
