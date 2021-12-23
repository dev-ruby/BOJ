# -*- coding: utf-8 -*-

import bs4
import os
import requests
import shutil
import subprocess

os.system("cls")

while True:
    os.system("cls")
    print(" >>>", end="  ")
    command = input().split()
    problem_number = command[1]

    path = rf"problems\{problem_number}.py"

    if command[0] == "open":
        os.system("cls")

        if not os.path.exists(path):
            url = f"https://www.acmicpc.net/problem/{problem_number}"
            response = requests.get(url)

            if not response.status_code == 200:
                print("백준 서버에 연결할 수 없습니다.")
                break

            soup = bs4.BeautifulSoup(response.text, "html.parser")
            title = soup.select_one("#problem_title").text

            preset = """# {0} - {1}\n\n\ndef solve():\n    pass\n\nsolve()\n"""

            with open(path, mode="w", encoding="utf-8") as fp:
                fp.write(preset.format(problem_number, title))

        title = ""
        with open(path, mode="r", encoding="utf-8") as fp:
            title = fp.readline()[2:]

        while True:
            os.system("cls")
            print(title)
            print("================\n")

            command = input().strip()

            if command == "exit":
                os.system("cls")
                break

            elif command == "test":
                print("\n\n----------------\n\n")
                subprocess.call(path, shell=True)
                print("\n\n----------------\n\n")
                while True:
                    print("clear? y/n")
                    if input() == "y":
                        break

            elif command == "commit":
                os.system(f"black {path}")
                os.system(f"git add {path}")
                os.system(f'git commit -m "{title}" ')
                break

            elif command == "give up":
                new_path = rf"못품\{problem_number}.py"
                shutil.move(path, new_path)
                os.system("cls")
                break

            print("\n\n\n\n\n\n\n\n\n")

    elif command[0] == "del":
        print("delete? y/n")
        if input() == "y":
            os.remove(path)
