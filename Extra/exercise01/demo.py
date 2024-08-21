# @Function: 加载html文件，为其中的所有链接增添属性target="_blank"
import os
from bs4 import BeautifulSoup
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time cost: {time.time() - start}")
        return result
    return wrapper

class HtmlParser:
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self._html, 'html.parser')
    def get_text(self):
        return self._soup.get_text()

    def process_a_tag(self):
        for a in self._soup.find_all('a'):
            a.attrs["target"] ="_blank"

    def get_html(self):
        return self._soup.prettify()
@timer
def helper(html):
    """
    利用bs4库解析html文件，为其中的所有链接增添属性target="_blank"
    """
    parser = HtmlParser(html)
    parser.process_a_tag()
    return parser.get_html()

@timer
def helper2(html):
    """
    正则表达式匹配链接并增加属性
    """
    import re
    pattern = re.compile(r'<a href="(.+?)">', re.S)
    return pattern.sub(r'<a href="\1" target="_blank">', html)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--html_path", type=str, help="your html file path")
    args = parser.parse_args()
    html_path = args.html_path
    if not isinstance(html_path, str) and not isinstance(html_path, int):
        print(f"html_path must be a file path, got {html_path}")
        exit(1)
    if os.path.exists(html_path) and not os.path.isfile(html_path):
        print(f"html_path must be a file path, got {html_path}")
        exit(1)
    elif not os.path.exists(html_path):
        print("html_path not found")
        exit(1)
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html_write_path = html_path.replace('.html', '_new.html')
    with open(html_write_path, 'w', encoding='utf-8') as f:
        f.write(helper2(html))
    html_write_path = html_path.replace('.html', '_new2.html')
    with open(html_write_path, 'w', encoding='utf-8') as f:
        f.write(helper(html))

# Time cost: 0.0002338886260986328
# Time cost: 0.007402896881103516