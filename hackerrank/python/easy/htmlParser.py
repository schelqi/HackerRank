from html.parser import HTMLParser


class CustomHtmlParser(HTMLParser):

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            attr_list = list(attr)
            print("->", attr_list[0], ">", attr_list[1])

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            attr_list = list(attr)
            print("->", attr_list[0], ">", attr_list[1])

    # Overridable -- handle end tag
    def handle_endtag(self, tag):
        print("End   :", tag)


htmlParser = CustomHtmlParser()

for _ in range(int(input())):
    htmlParser.feed(input().strip())
