from __future__ import print_function, unicode_literals
from api import search
import pytchat

chat = pytchat.create(video_id="wLo67kxddp8")
tempText = ""

def main():
    while chat.is_alive():
        for c in chat.get().sync_items():
            if "!atlat" in c.message:
                if (c.author.name == "Samet Tunay" or c.author.name == "Radyo Hizmeti" or c.author.name == "Radyo Efkar"):
                    print("atlandı.")
                    with open('admin.txt', 'w') as f:
                        f.write("!atlat")

            if "!istek " in c.message:
                tempText = str(c.message).replace("!istek ", "")
                search_results = search(tempText)

                print("Sıraya eklendi: ", search_results[0]['name'])

                with open('istek.txt', 'w') as f:
                    f.write(str(c.author.name) + ", Sıraya " + search_results[0]['name'] + " şarkısını ekledi!")

                with open('data.txt', 'a') as f:
                    f.write(str(search_results[0]['value']) + '\n')
                    f.write(c.author.name + '\n')
                    f.write(str(search_results[0]['name']) + '\n')

if __name__ == '__main__':
    main()
    print("Thanks for using!!")
