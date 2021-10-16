def song_decoder(song):
    text=""
    last = ""
    for x in range(0, len(song)):
        if song[x] == "W" and song[x+1] == "U" and song[x+2] == "B" or song[x-1] == "W" and song[x] == "U" and song[x+1] == "B" or song[x-2] == "W" and song[x-1] == "U" and song[x] == "B":
            if text != "" and last != " ":
                last = " "
                text = text + " "
        else:
            text = text + song[x]
            last = song[x]

    if text[len(text)-1] == " ":
        text = text[0: len(text)-1] 

    print(text)

    
    return text

a = "WUAB"


song_decoder(a)
