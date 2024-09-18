# class car:
#     def  __init__(self, color, model, year):
#         self.color = color
#         self.model =model
#         self.year = year
#     def drive(self):
#         print(f"the {self.color} {self.model} build in {self.year} is driving")

#     def  stop(self):
#         print(f"the {self.color} {self.model} build in {self.year} is stopped")
# car1 = car("Red" , "Toyota " , 2020)
# car2 = car("Black" , "BMW" ,  2019)

# car1.drive()
# car1.stop()
# car2.drive()
# car2.stop()



# Define the classes

class Movie:
    def _init_(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.available = True

    def mark_as_rented(self):
        self.available = False

    def mark_as_available(self):
        self.available = True

    def _str_(self):
        return f"{self.title} ({self.year}) - {self.genre} - Available: {self.available}"

class Customer:
    def _init_(self, name):
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie):
        if movie.available:
            movie.mark_as_rented()
            self.rented_movies.append(movie)
            print(f"{self.name} has rented {movie.title}")
        else:
            print(f"{movie.title} is not available for rent")

    def return_movie(self, movie):
        if movie in self.rented_movies:
            movie.mark_as_available()
            self.rented_movies.remove(movie)
            print(f"{self.name} has returned {movie.title}")
        else:
            print(f"{self.name} does not have {movie.title} rented")

    def list_rented_movies(self):
        print(f"Movies rented by {self.name}:")
        for movie in self.rented_movies:
            print(movie.title)

class RentalStore:
    def _init_(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"{movie.title} has been added to the store")

    def list_movies(self):
        print("Available movies:")
        for movie in self.movies:
            if movie.available:
                print(movie)

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

# Create a menu system

def display_menu():
    print("Movie Rental System Menu:")
    print("1. List available movies")
    print("2. Rent a movie")
    print("3. Return a movie")
    print("4. List rented movies for a customer")
    print("5. Add a new movie to the store")
    print("6. Exit the program")

def main():
    store = RentalStore()
    customers = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            store.list_movies()
        elif choice == "2":
            customer_name = input("Enter your name: ")
            if customer_name not in customers:
                customers[customer_name] = Customer(customer_name)
            movie_title = input("Enter the movie title: ")
            movie = store.find_movie(movie_title)
            if movie:
                customers[customer_name].rent_movie(movie)
            else:
                print("Movie not found")
        elif choice == "3":
            customer_name = input("Enter your name: ")
            if customer_name in customers:
                movie_title = input("Enter the movie title: ")
                movie = store.find_movie(movie_title)
                if movie:
                    customers[customer_name].return_movie(movie)
                else:
                    print("Movie not found")
            else:
                print("Customer not found")
        elif choice == "4":
            customer_name = input("Enter your name: ")
            if customer_name in customers:
                customers[customer_name].list_rented_movies()
            else:
                print("Customer not found")
        elif choice == "5":
            title = input("Enter the movie title: ")
            genre = input("Enter the movie genre: ")
            year = int(input("Enter the movie year: "))
            movie = Movie(title, genre, year)
            store.add_movie(movie)
        elif choice == "6":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()