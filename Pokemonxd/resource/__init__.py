import os

thumbs = []

colors = ["white", "red", "orange", "yellow", "green", "cyan", "azure", "blue", "violet", "magenta", "pink"]

for filename in os.listdir("./Pokemonxd/resource"):

    if filename.endswith("png"):

        thumbs.append(filename[:-4])
