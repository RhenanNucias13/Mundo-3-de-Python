from urllib.request import urlopen
from urllib.error import URLError

try:
    urlopen("https://www.google.com")
except URLError:
    print("O site não está acessível no momento.")
else:
    print("Consegui acessar o site com sucesso!")