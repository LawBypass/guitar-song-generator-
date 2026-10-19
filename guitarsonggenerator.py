#project that generates random guitar chords along with choosing a strumming pattern from a list 
import random 

chords = ["Am", "Em","E", "Dm", "D", "A", "G", "C",]

strumming_patterns = [
    ["down", "down", "up", "up", "down", "up"],
    ["down", "up", "down", "up"],
    ["down", "down", "down", "up"],
    ["down", "up", "up", "down", "up"]
]

song_strumming = random.choice(strumming_patterns)

song_chords = random.choices(chords , k= 4)


print("Your chords:", "-".join(song_chords))
print ("Your strumming pattern", "-".join(song_strumming))


#I might add a gui in the future/ more variation
