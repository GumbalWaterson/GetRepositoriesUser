import requests
import sys


user_name = sys.argv[1]
result = []


def solve():
    def repos():
        global user_name
        global result
        r = requests.get("https://api.github.com/users/{}/repos"
                         .format(user_name))
        content = r.json()
        result = [data['name'] for data in content]
    repos()
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
