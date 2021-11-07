import requests
import json
import time
import webbrowser
import win10toast

# GPO game id is 1730877806
blacklist_word = "maintenance"
link = "https://api.roblox.com/marketplace/productinfo?assetId={}"
notifier = win10toast.ToastNotifier()


def is_open(game_id):
    try:
        res = requests.get(link.format(str(game_id))).json()
        if 'Name' in res.keys():
            if blacklist_word in res['Name']:
                print("Not available")
                return False
            else:
                print("Available!")
                notifier.show_toast("GPO Open Checker", "Game is public. Opening in browser...")
                time.sleep(3)
                webbrowser.open("https://www.roblox.com/games/1730877806/")
                return True
    except json.JSONDecodeError as e:
        print("Could not parse json.")


def main():
    while True:
        game_id = input("Game Id: ")
        while is_open(game_id) is False:
            time.sleep(1)


if __name__ == '__main__':
    main()
