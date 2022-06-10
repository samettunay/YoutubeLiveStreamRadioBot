from ast import Index
import pafy, vlc, time

i = 0

while True:
    try:
        is_opening = False
        is_playing = False

        f=open('data.txt', 'r')
        lines=f.readlines()

        with open('author.txt', 'w') as f:
            f.truncate(0)
            f.write(lines[i+1])

        with open('message.txt', 'w') as f:
            f.truncate(0)
            f.write(lines[i+2])

        video = pafy.new(lines[i])
        best = video.getbestaudio()
        play_url = best.url 
        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new(play_url)
        media.get_mrl()
        player.set_media(media)
        player.play()


        good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]

        while str(player.get_state()) in good_states:

            if str(player.get_state()) == "State.Opening" and is_opening is False:
                print("Status: Loading")
                is_opening = True

            if str(player.get_state()) == "State.Playing" and is_playing is False:
                print("Status: Playing")
                is_playing = True
            try:
                with open('admin.txt', 'r') as q:
                    lines2=q.readlines()
                    if str(lines2[0]) == "!atlat":
                        print("Status: Atlat")
                        break
                        #player.stop()
            except IndexError:
                pass
        
        i+=3
        f.close()
        print("Status: Finish")
        player.stop()
        with open('admin.txt', 'w') as q:
            q.write("none")
    except IndexError as e:
        print("istek Bekleniyor!")
        with open('admin.txt', 'w') as q:
            q.write("none")
        with open('istek.txt', 'w') as f:
            f.write("istek Bekleniyor!")
        time.sleep(3)
        pass
