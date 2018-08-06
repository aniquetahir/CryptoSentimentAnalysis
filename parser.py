import bs4

class Parser:
    def __init__(self, html):
        self.html = html
        self.soup = bs4.BeautifulSoup(html, 'html.parser')

class GNewsParser(Parser):
    def __init__(self, html):
        super().__init__(html)

    def getSummary(self):
        articles = self.soup.find_all('article')
        results = []
        for i, article in enumerate(articles):
            try:
                rank = i+1
                title_div, = article.find_all('div', limit=1)
                title_text = title_div.h3.get_text()
                website_text = title_div.find_next_sibling('div').span.get_text()
                results.append({
                    'rank': rank,
                    'title': title_text,
                    'site': website_text
                })
            except Exception as e:
                print(e)
        print(results)


if __name__ == "__main__":
    print("Performing test")
    news_file = open('newspage.html')
    file_contents = news_file.readlines()
    file_contents = "\n".join(file_contents)
    news_file.close()
    parser = GNewsParser(file_contents)
    parser.getSummary()




