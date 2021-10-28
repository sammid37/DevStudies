# Samantha Dantas Medeiros Oct 28th, 2021
import feedparser

# O usuário irá informar a URL de um feed RSS
def get_url():
    url = input("Informe uma URL de feed RSS: ")
    print()
    return url

# Lendo a URL informada
def read(url):
    newsFeed = feedparser.parse(url)
    entry = newsFeed.entries[0]
    display(entry)
    

def display(entry):
    print(entry['published'])
    print("---------------------------------------------------------------")
    print("\"{}\"".format(entry['title']))
    print("→ {}".format(entry['link']))
    print()

# MAIN: enquanto a URL for diferente de vazio, irá ler múltiplos feeds RSS
def main():
    url = get_url()

    while (url != ''):
        read(url)
        url = get_url()

# execução
if __name__ == '__main__':
	main()