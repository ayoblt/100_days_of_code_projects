import requests
from bs4 import BeautifulSoup

url = "http://www.wildwalks.com/bushcraft/technical-stuff/morse-code-and-phonetic-alphabet.html"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
letters_raw = soup.find_all(name="td", class_="xl26")
morses_raw = soup.find_all(name="td", class_="xl27")
letters = []
morses = []
for letter in letters_raw:
    letters.append(letter.getText())

for morse in morses_raw:
    stripped_morse = "".join(morse.getText().split(" "))
    morses.append(stripped_morse)


letter_morse = {}
for i in range(len(letters)):
    letter_morse[letters[i]] = morses[i]

print(letter_morse)