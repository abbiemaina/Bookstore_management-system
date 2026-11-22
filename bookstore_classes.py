class Book:
    """this class represents a book in the bookstore."""
    def __init__(self, title, author, isbn, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: ${self.price}, Quantity: {self.quantity}"

    # 1. A method to display the book details
    def display_book_details(self):
        details = {
            "Title": self.title,
            "Author": self.author,
            "ISBN": self.isbn,
            "Price": self.price,
            "Quantity": self.quantity
        }
        for key, value in details.items():
            print(f"{key}: {value}")
       

    # 2. A method to update the price of a book
    def update_price(self, new_price):
        self.price = new_price
        print(f"Price of '{self.title}' has been updated to ${self.price}.")

    # 3. A method to add stock to the book quantity
    def add_stock(self, additional_quantity):
        self.quantity += additional_quantity
        print(f"Added {additional_quantity} books to '{self.title}'. New quantity: {self.quantity}.")


    # 4. A method to check availability of the book
    def check_availability(self):
        if self.quantity > 0:
            print(f"'{self.title}' is available. Quantity: {self.quantity}.")
            return True
        else:
            print(f"'{self.title}' is out of stock.")
            return False


##########################################################################################

   
class Customer:
    """this class represents customers in the system and their details"""
    def __init__(self, customer_id, name, email, balance, purchase_history=None):
        self.customer_id = customer_id 
        self.name = name
        self.email = email
        self.balance = balance
        self.purchase_history = purchase_history if purchase_history is not None else []

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Balance: ${self.balance}, Purchase History: {self.purchase_history}"


    # 1. A method to display customer details
    def  display_customer_details(self):
        details = {
            "Customer ID": self.customer_id,
            "Name": self.name,
            "Email": self.email,
            "Balance": self.balance,
            "Purchase History": self.purchase_history
        }
        for key, value in details.items():
            print(f"{key}: {value}")



    # 2. A method to display the purchase history of the customer
    def display_purchase_history(self):
        if self.purchase_history:
            print(f"Purchase history for {self.name}:")
            for purchase in self.purchase_history:
                print(purchase)
            else:
                print(f"No purchase history for {self.name}.")



    # 3. A method to make a payment for a purchase
    def make_payment(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Payment of ${amount} was successful. New balance is ${self.balance}.")
        else:
            print(f"Payment failed due to insufficient balance. Current balance is ${self.balance}.")


    # 4. A method to calculate the total amount spent by the customer
    def calculate_total_spent(self):
        total = 0
        for purchase in self.purchase_history:
            if purchase > 0:
                total += purchase
        return total


    # 5. A method to search for a specific purchase in the customer's purchase history
    def search_purchase(self, amount):
        for purchase in self.purchase_history:
            if purchase == amount:
                return "Purchase found!"
        return "Purchase not found :("


##############################################################################################################

class Order:
    """this class represents an order placed by a customer."""
    def __init__(self, order_id, customer, book, quantity, order_date, status):
        self.order_id = order_id
        self.customer = customer
        self.book = book
        self.quantity = quantity
        self.order_date = order_date
        self.status = status


    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.name}, Book: {self.book.title}, Quantity: {self.quantity}, Order Date: {self.order_date}, Status: {self.status}"


    # 1. A method to display order details
    def display_order_details(self):
        details = {
            "Order ID": self.order_id,
            "Customer": self.customer.name,  #refers back to the customer object and gets the name of the customer
            "Book": self.book.title,        #refers back to the book object and gets the title of the book
            "Quantity": self.quantity,
            "Order Date": self.order_date,
            "Status": self.status
        }
        for key, value in details.items():
            print(f"{key}: {value}")


    # 2. A method to calculate the total cost of all books in the order
    def calculate_total(self):
        total = 0
        for item in self.book:
            book = item['book']
            quantity = item['quantity']
            total += book.price * quantity
        return total


    # 3. A method to update the status of the order
    def update_status(self, new_status):
        if new_status in ['Pending', 'Shipped', 'Delivered', 'Cancelled']:
            self.status = new_status
            return f"Order status updated to {self.status} successfully."
        else:
            return "Invalid order status. Please choose from 'Pending', 'Shipped', 'Delivered', or 'Cancelled'."



    # 4. A method to add a book to the order
    def add_book(self, book, quantity):
        self.book.append({'book': book, 'quantity': quantity})
        return f"Added {quantity} of '{book.title}' to the order."


    # 5. A method to remove a book from the order
    def remove_book(self, book):
        for item in self.book:
            if item['book'] == book:
                self.book.remove(item)
                return f"Removed '{book.title}' from the order."
        return f"'{book.title}' not found in the order."


    # 6. A method to search for a particular book in the order
    def search_book(self, book):
        for item in self.book:
            if item['book'].title.lower() == book.title.lower():
                return f"'{book.title}' found in the order."
        return "Book not found!"


##############################################################################################
class Inventory:
    """this class manages and monitores the collection of books available in the book store"""
    def __init__(self, inventory_id, total_books, last_updated, low_stock_threshold):
        self.inventory_id = inventory_id
        self.total_books = total_books
        self.last_updated = last_updated
        self.low_stock_threshold = low_stock_threshold 


    def __str__(self):
        return f"Inentory ID: {self.inventory_id}, Total books: {self.total_books}, Last updated: {self.last_updated}, Low stock threshold: {self.low_stock_threshold}"


    # 1. A method to display inventory information
    def display_inventory(self):
        details = {
            "Inventory ID": self.inventory_id,
            "Total books": self.total_boooks,
            "Last upadated": self.last_updated,
            "Low stock threshold": self.low_stock_threshold
        }
        for key, value in details.items():
         print(f"{key}: {value}")


    # 2. A method to check if the stock has fallen below low-stock threshold
    def check_low_stock(self):
        if self.total_books <= self.low_stock_threshold:
            print("Warning: Low stock!")
        else:
            print("Stock level is sufficient.")


    # 3. A method add books
    def add_books(self, quantity):
        self.total_books += quantity
        print("Books added successfully")


    # 4. A method to update the total number of books in the inventory
    def update_inventory(self):
        while True:
            quantity = int(input('Enter the new total number of books: '))
            if quantity >= 0:
                self.total_books = quantity
                print("Inventory updated successfully")
                break
            else:
                print("Invalid quantity. Please try again.")



    # 5. A method that returns the total amount of books in the inventory currently
    def get_total_books(self):
        count = 0
        for book in self.books:
            count += 1

        return count
    