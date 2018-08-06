#Capstone: Taylor Schulze
#Python intensive
#8-6-18


# Create a User
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

#returns email associated with the user
    def get_email(self):
        return self.email

#changes the email associated with the user
    def change_email(self, address):
        self.email = address
        print ("{}'s email has been changed to {}.".format(self.name, self.email))

#returns a string that represents the information
    def __repr__(self):
        return "The User {} has the Email {} and has read {} Books.".format (self.name, self.email, len(self.books))

# defines comparisons between users
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
          return True
        return False

#adds a key:value pair to self.books where the key is book and the value is rating
    def read_book(self, book, rating = None):
        self.books[book] = rating

#returns the average rating in self.books
    def get_average_rating(self):
        rates = 0
        for rating in self.books.values():
            rates += rating
        average_rating = (rates / len(self.books))
        return average_rating


#Create a Book
class Book():
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

#returns the title of the book
    def get_title(self):
        return self.title

#returns the ISBN of the book
    def get_isbn(self):
        return self.isbn

#sets the ISBN to a new value
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print ("The ISBN number of {} has been changed to {}.".format(self.title, self.isbn))

#adds a rating to the list self.raing if it is between 0 and 4
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
            print("The book {} has been rated as a {} out of 4.".format (self.title,rating))
        else:
            print("Invalid Rating")

#defines a comparison between books
    def __eq__(self, other):
        if (self.title == other.title) and (self.isbn == other.isbn):
            return True
        else:
            return False

#calculates the average rating in self.ratings
    def get_average_rating(self):
        total_rating = 0
        for rating in self.ratings.values():
            total_rating += rating
        average_rating = ((total_rating) / len(self.ratings))
        return average_rating

#returns a consistent hash for an instance of the book object
    def __hash__(self):
        return hash((self.title, self.isbn))


#Class Fiction that inherits from Book
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

#returns the author
    def get_author(self):
        return self.author

#returns the string {title} by {author}
    def __repr__(self):
        return "{} by {}.".format(self.title,self.author)

#Class Non_Fiction that inherits from Book
class Non_Fiction(Book):
    def __init__(self,title,subject,level,isbn):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level

#returns the subject
    def get_subject(self):
        return self.subject

# returns the level
    def get_level(self):
        return self.level

#returns the string {title}, a {level} manual on {subject}
    def __repr__(self):
        return "{}, a {} manual on {}.".format(self.title,self.level,self.subject)

#create class TomeRater
class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

#creates a new book with the title {title} and the isbn {isbn}
    def create_book(self,title,isbn):
        book =  Book(title,isbn)
        return book

#creates a new Fiction with the title, author and ISBN
    def create_novel(self, title, author, isbn):
        fiction_book = Fiction(title,author,isbn)
        return fiction_book

#creates a new Non_Fiction with the title, author and ISBN
    def create_non_fiction(self,title,subject,level,isbn):
        non_fiction = Non_Fiction(title,subject,level,isbn)
        return non_fiction

#gets the user with the email or returns "No user with that email" if the user dosent exist
    def add_book_to_user(self,book,email,rating = none):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user with the email {}.".format(self.email)

#create a new User object from name and email
    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

#prints the keys in self.books
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

#prints the keys in self.users
    def print_users(self):
        for user in self.users.values():
            print(user)

#returns the book that has been read the most
    def most_read_book(self):
        most_read = None
        times_read = 0
        for book, count in self.books.items():
            if count > times_read:
                times_read = value
                most_read = key
        return most_read

#returns the book with the highest average rating
    def highest_rated_book(self):
        highest_rating = 0
        highes_rated = None
        for book in self.books.keys():
            if highest_rating < book.get_average_rating():
                highest_rating = book.get_average_rating()
                highest_rated = book
        return highest_rated

#returns the user in self.users that have the highest average rating
    def most_positive_user(self):
        hoghest_rating = 0
        positive_user = None
        for user in self.users.values():
            if highest_rating < user.get_average_rating():
                highest_rating = user.get_average_rating()
                positive_user = User
        return positive_user