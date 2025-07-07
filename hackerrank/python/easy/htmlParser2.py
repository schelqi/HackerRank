from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if not data.isspace():
            print(">>> Data", data, sep="\n")

    # Overridable -- handle comment
    def handle_comment(self, comment):
        if "\n" in comment:
            print(">>> Multi-line Comment", comment, sep="\n")
        else:
            print(">>> Single-line Comment", comment, sep="\n")


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
