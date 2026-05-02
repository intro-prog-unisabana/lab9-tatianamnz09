# Write your code here!
# FREEZE CODE BEGIN
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
# FREEZE CODE END
    def __str__(self):
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"


# FREEZE CODE BEGIN
if __name__ == "__main__":
    # --- Main Program ---
    title = input("Enter the title:\n ")
    director = input("Enter the director:\n ")
    year = input("Enter the year:\n ")
# FREEZE CODE END
    
    
my_movie = Movie(title, director, year)
print(my_movie)
