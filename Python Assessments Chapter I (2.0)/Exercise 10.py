# Exercise 10: Film Dictionary

# Create a dictionary that contains relevant data for films (e.g. Title, Director, etc). Display the film details using loop

# Let's do this with one of my favorite movies to watch from the past 2 years using items(), key(the one that defines), and value (the one that is identified)
films = {
    "Movie": "1917",
    "Director": "Sam Mendes",
    "Year": "2019"
}

for key, value in films.items():
    print(key, value)