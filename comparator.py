import wikipediaapi
from flask import Flask

wikipedia = wikipediaapi.Wikipedia('en')

first_topic = input("First topic: ")
first_page = wikipedia.page(first_topic)

second_topic = input("Second topic: ")
second_page = wikipedia.page(second_topic)

first_links = set(first_page.links.keys())
second_links = set(second_page.links.keys())
common_links = first_links.intersection(second_links)

if second_topic in first_links:
    common_links.add(second_topic)

if first_topic in second_links:
    common_links.add(first_topic)

print(common_links)




