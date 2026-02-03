from datetime import datetime
import json
import os
from git import Repo
import time
from playwright.sync_api import sync_playwright
# uv run playwright install chromium

MY_PAGE = 'https://sandrinedacol.github.io/resume/'

class ResumeModificator():

    def __init__(self):
        self.date = datetime.now()
        self.path = os.getcwd()
        self.repo = Repo('.')

        self.get_empty_html()
        self.copy_data_into_html()
        self.generate_static()
        self.git_push()

    def insert_text_into_tag(self, tag, text):
        content_before, content_after = self.html.split(f'<{tag}></{tag}>')
        self.html = content_before + f'<{tag}>' + text + f'</{tag}>' + content_after

    def get_empty_html(self):
        with open('./empty_page.html', 'r') as f:
            self.html = f.read()
        with open('./style.css', 'r') as f:
            css_content = f.read()
        css_content = css_content\
            .replace('\n', '').replace('    ', '').replace(': ', ':')\
                .replace(' * ', '*').replace(' {', '{')
        self.insert_text_into_tag('style', css_content)

    def copy_data_into_html(self, interests=False):
        content_before, content_after = self.html.split('const data = {}')
        with open('./data.json', 'r') as json_data:
            data = json.load(json_data)
        data["meta"]["lastModified"] = str(self.date)
        self.insert_text_into_tag('title', data['basics']['name'])
        with open('./data.json', 'w') as f:
            json.dump(data, f, indent=4)
        if not interests:
            del data['interests']
        self.html = content_before + 'const data = ' + json.dumps(data) + content_after
        with open('./filled_page.html', 'w') as f:
            f.write(self.html)
        print('Content of data.json copied into filled_page.html.')

    def git_push(self):
        try:
            self.repo.git.add(update=True)
            commit_message = f"automatic commit {self.date}"
            self.repo.index.commit(commit_message)
            origin = self.repo.remote(name='origin')
            origin.push()
            print("Fully static index.html pushed to repo.")
        except:
            print('Some error occured while pushing the code')   


    def generate_static(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            # page.goto(MY_PAGE)
            page.goto("file:///home/sandrine/Documents/candidatures/CV/resume/filled_page.html")
            page.wait_for_load_state("networkidle")
            html = page.content() 
        before, after = html.split('<script>')
        after = after.split('</script>\n')[-1]
        html_content = before + after
        with open('./index.html', 'w') as f:
            f.write(html_content)
        print(f"DOM content retrieved from {MY_PAGE}.")


def main():
    _ = ResumeModificator()
    

if __name__ == "__main__":
    main()
