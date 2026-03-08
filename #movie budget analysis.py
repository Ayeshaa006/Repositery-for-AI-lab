#movie budget analysis
movies = [
("eternal sunshine of the spotless mind", 20000000),
("memento", 9000000),
("requiem for a dream", 4500000),
("pirates of the caribbean: on stranger tides", 379000000),
("avengers: endgame", 356000000),
("incredibles 2", 200000000)
]
total_budget = 0
for movie in movies:
    total_budget += movie[1]
average_budget = total_budget / len(movies)
print("average budget:", average_budget)
print("\nMovies with budget higher than average:")
count = 0
for movie in movies:
    if movie[1] > average_budget:
        print(movie[0], "-", movie[1])
        count += 1
print("\nNumber of movies above averages:", count)
