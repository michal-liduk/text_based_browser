
import sys
import os
import requests
from bs4 import BeautifulSoup
import colorama

# write your code here
class TextBaseBrowser:
    def __init__(self):
        self.tabs = []
        self.tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'li', 'head', 'title', "div"]
    def menu(self, *website):
        while website != "exit":
            website = input()
            dots = [i for i, char in enumerate(website) if char == '.']
            if len(dots) > 0:
                end_dot_index = dots[-1]
                filename = website[:end_dot_index]
            args = sys.argv
            directory = args[1]
            if not os.path.exists(directory):
                os.mkdir(directory)
            else:
                pass
            if website[:8].lower() != "https://" and website != "exit" and website != "back":
                website = "https://" + website
            if len(dots) == 0 and website != "exit" and website != "back":
                print("Error: Incorrect URL")
            elif website == "back":
                if len(self.tabs) > 1:
                    self.tabs.pop()
                    print(self.tabs.pop())
                else:
                    print("Error: No websites visited")
            elif website == "exit":
                print("error")
                break
            else:
                site = requests.get(website)
                soup = BeautifulSoup(site.text, 'html.parser')
                page = soup.find_all(self.tags)
                self.tabs.append(page)
                with open(directory + "/" + filename + ".txt", 'w') as f:
                    for tag in page:
                        if tag.string is None:
                            pass
                        elif tag.name == "a":
                            print(colorama.Fore.BLUE + tag.string)
                            print(colorama.Style.RESET_ALL)
                            f.write(tag.string + '\n')
                        else:
                            print(tag.string)
                            f.write(tag.string + '\n')


if __name__ == "__main__":
    run = TextBaseBrowser()
    run.menu()