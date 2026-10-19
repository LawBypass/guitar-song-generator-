#project that generates random guitar chords along with choosing a strumming pattern from a list 
import random 

#I also added stuck chords (e.g Es as in stuck. the g is stuck by default as i dont see a need to have other variations
chords = ["Am", "Em","E", "Dm", "D", "A", "G", "C", "Es", "Cs", "As", "Ds"]

#I might add more strumming patterns in the future
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
