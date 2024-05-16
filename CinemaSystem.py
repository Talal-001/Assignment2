class AccountManager:
    def __init__(self):
        self.accounts = {}

class Register:
    def __init__(self, account_manager):
        self.account_manager = account_manager

    def register_account(self, username, password, firstname, lastname):
        if username not in self.account_manager.accounts:
            self.account_manager.accounts[username] = {
                "password": password, 
                "firstname": firstname, 
                "lastname": lastname
            }
            return True
        else:
            return False

class Login:
    def __init__(self, account_manager):
        self.account_manager = account_manager

    def login_account(self, username, password):
        if username in self.account_manager.accounts and self.account_manager.accounts[username]["password"] == password:
            return True
        else:
            return False

account_manager = AccountManager()
register_manager = Register(account_manager)
login_manager = Login(account_manager)

class Movie:
    def __init__(self, title, showtime):
        self.title = title
        self.showtime = showtime
        self.seats = [["" for _ in range(10)] for _ in range(5)]

    def display_movie_info(self):
        print(f"Title: {self.title}")
        print(f"Showtime: {self.showtime}")
        print("Seat layout:")
        for i, row in enumerate(self.seats):
            print(f"Row {i + 1}: {row}")

    def book_seat(self, row, seat):
        if self.seats[row - 1][seat - 1] == "":
            self.seats[row - 1][seat - 1] = "Booked"
            print("Seat booked successfully!")
        else:
            print("Seat already booked or invalid seat number.")

    def cancel_seat(self, row, seat):
        if self.seats[row - 1][seat - 1] == "Booked":
            self.seats[row - 1][seat - 1] = ""
            print("Seat cancelled successfully!")
        else:
            print("Seat not booked or invalid seat number.")

class MovieTheater:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title, showtime):
        if title not in self.movies:
            self.movies[title] = showtime
            print(f"Movie '{title}' added successfully!")
        else:
            print(f"Movie '{title}' already exists.")

    def remove_movie(self, title):
        if title in self.movies:
            del self.movies[title]
            print(f"Movie '{title}' removed successfully!")
        else:
            print(f"Movie '{title}' not found.")

    def display_movies(self):
        if not self.movies:
            print("No movies available.")
        else:
            for title, showtime in self.movies.items():
                print(f"{title} - {showtime}")

    def select_movie(self):
        self.display_movies()
        title = input("Enter movie title: ")
        if title in self.movies:
            return self.movies[title], title
        else:
            print("Movie not found.")
            return None, None

class DisplayMenu:
    def __init__(self):
        self.login = Login(account_manager)
        self.register = Register(account_manager)
        self.theater = MovieTheater()
    def display_menu(self):
        while True:
            print("Please enter your choice:")
            print("1. User")
            print("2. Admin")
            print("3. Exit")
            choice = input('Enter the number of which type of user you are: ')
            
            if choice == str(3):
                print("You have exited.")
                break
            elif choice == str(1) :
                self.handle_user_menu()
            elif choice == str(2):
                self.handle_admin_menu()
            else:
                print("Invalid choice. Please enter a valid number.")

    def handle_user_menu(self):
        print("Please enter your choice:")
        print("1. Register for account")
        print("2. Login to account")
        choice = input("Enter the number: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            if self.register.register_account(username, password, firstname, lastname):
                print("Account registered successfully!")
                self.user_options()
            else:
                print("Username already exists. Please choose a different username.")
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if self.login.login_account(username, password):
                print("Login successful!")
                self.user_options()
            else:
                print("Invalid username or password.")
        else:
            print("Invalid choice. Please enter a valid number.")
    def handle_admin_menu(self):
        print("Please enter your choice:")
        print("1. Register for account")
        print("2. Login to account")
        choice = input("Enter the number: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            if self.register.register_account(username, password, firstname, lastname):
                print("Account registered successfully!")
                self.admin_options()
            else:
                print("Username already exists. Please choose a different username.")
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if self.login.login_account(username, password):
                print("Login successful!")
                self.admin_options()
            else:
                print("Invalid username or password.")
        else:
            print("Invalid choice. Please enter a valid number.")
    def user_options(self):
        while True:
            print("1. Display movies")
            print("Seat Management")
            print("2. Select a movie")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.theater.display_movies()
            elif choice == "2":
                showtime, title = self.theater.select_movie()
                if showtime:
                    movie = Movie(title, showtime)
                    movie.display_movie_info()
                    action = input("Enter 'book' to book a seat or 'cancel' to cancel a seat: ")
                    if action == "book":
                        row = int(input("Enter row number (1-5): "))
                        seat = int(input("Enter seat number (1-10): "))
                        movie.book_seat(row, seat)
                    elif action == "cancel":
                        row = int(input("Enter row number (1-5): "))
                        seat = int(input("Enter seat number (1-10): "))
                        movie.cancel_seat(row, seat)
              
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
    def admin_options(self):

        theater = MovieTheater()
        while True:
            print("\nAdd/Remove Movies")
            print("1. Add a movie")
            print("2. Remove a movie")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                title = input("Enter movie title: ")
                showtime = input("Enter showtime: ")
                theater.add_movie(title, showtime)
            elif choice == "2":
                title = input("Enter movie title: ")
                theater.remove_movie(title)     
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
menu = DisplayMenu()
menu.display_menu()
