import bs4
import urllib.request as req


def scrap(url, name):
    u = url
    request = req.Request(u, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")

    con = root.find_all("p")
    content = []
    for c in con:
        if c.text == "":
            content.append(c.text)
        else:
            content.append(c.text+"\n")

    i = 0
    for i in range(len(content)):
        if content[i] == name:
            break

    result = ""
    while(i < len(content)-1):
        if not (any(c.isalpha() for c in content[i]) or any(c.isalpha() for c in content[i+1])):
            break
        result += content[i]+"\n"
        i += 1
    return result
