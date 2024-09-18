class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.available = True  # Initially, all movies are available for rent

    def mark_as_rented(self):
        self.available = False

    def mark_as_available(self):
        self.available = True

    def __str__(self):
        return f"{self.title} ({self.year}) - Genre: {self.genre} - {'Available' if self.available else 'Rented'}"
class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie):
        if movie.available:
            movie.mark_as_rented()
            self.rented_movies.append(movie)
            print(f"{self.name} has rented '{movie.title}'.")
        else:
            print(f"Sorry, '{movie.title}' is currently rented.")

    def return_movie(self, movie):
        if movie in self.rented_movies:
            movie.mark_as_available()
            self.rented_movies.remove(movie)
            print(f"{self.name} has returned '{movie.title}'.")
        else:
            print(f"{self.name} has not rented '{movie.title}'.")

    def list_rented_movies(self):
        if self.rented_movies:
            print(f"{self.name} has rented the following movies:")
            for movie in self.rented_movies:
                print(f"  - {movie}")
        else:
            print(f"{self.name} has not rented any movies.")
class RentalStore:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Added movie: {movie}")

    def list_movies(self):
        if self.movies:
            print("Available movies in the store:")
            for movie in self.movies:
                if movie.available:
                    print(f"  - {movie}")
        else:
            print("No movies available in the store.")

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        print(f"Movie titled '{title}' not found.")
        return None
def display_menu():
    print("\nMovie Rental System Menu:")
    print("1. List available movies")
    print("2. Rent a movie")
    print("3. Return a movie")
    print("4. List rented movies for a specific customer")
    print("5. Add a new movie to the store")
    print("6. Exit")

def main():
    store = RentalStore()
    customers = {}

    while True:
        display_menu()
        choice = input("Select an option (1-6): ")

        if choice == "1":
            store.list_movies()

        elif choice == "2":
            customer_name = input("Enter customer's name: ")
            if customer_name not in customers:
                customers[customer_name] = Customer(customer_name)
            customer = customers[customer_name]

            movie_title = input("Enter the title of the movie to rent: ")
            movie = store.find_movie(movie_title)
            if movie:
                customer.rent_movie(movie)

        elif choice == "3":
            customer_name = input("Enter customer's name: ")
            if customer_name in customers:
                customer = customers[customer_name]
                movie_title = input("Enter the title of the movie to return: ")
                movie = store.find_movie(movie_title)
                if movie:
                    customer.return_movie(movie)
            else:
                print(f"No customer found with the name '{customer_name}'.")

        elif choice == "4":
            customer_name = input("Enter customer's name: ")
            if customer_name in customers:
                customer = customers[customer_name]
                customer.list_rented_movies()
            else:
                print(f"No customer found with the name '{customer_name}'.")

        elif choice == "5":
            title = input("Enter the movie title: ")
            genre = input("Enter the movie genre: ")
            year = input("Enter the release year: ")
            new_movie = Movie(title, genre, year)
            store.add_movie(new_movie)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
main()