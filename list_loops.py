songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[1:3])
songs[2] = "Dynamite"

print(songs)

songs.append("September")
songs.append("Staying Alive")
songs.append("Never gonna give you up")

print(songs)

del songs[0]

for song in songs:
    print(song)

animals = ["dog", "cat", "fish"]

animals.append("sheep")
del animals[0]
for animal in animals:
    print(animal)