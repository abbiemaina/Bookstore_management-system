"""This file tests the classes and their methods
in the bookstore management system."""

import bookstore_classes as bc

##### TEST THE BOOK CLASS #####

# Create a book object
book1 = bc.Book("Mile High", "Liz Tomforde", "978-0141", 15, 10)

# Test display_book_details()
book1.display_book_details()

# Test update_price()
book1.update_price(20.99)
book1.display_book_details()      #this function is called to confirm that the price has indeed changed from $15 to $20.99

# Test add_stock()
book1.add_stock(5)
book1.display_book_details()     #this funcion is called again to confirm stock has been added.

# Test check_availability
print(book1.check_availability())      #expected output is either True or False depending on whether the book is available or not


##### TEST THE CUSTOMER CLASS #####

# Create a customer object
customer1 = bc.Customer(101, "Cynthia Maria", "cynthiam@gmail.com", 100, [20,15,35])

# Test display_customer_details()
customer1.display_customer_details()

# Test display_purchase_history()
customer1.display_purchase_history()

# Test make_payment()
customer1.make_payment(30)     #once payment is made in the customers account for example the balance is expected to reduce and in this case it reduces from 100 to 70.
customer1.display_customer_details()     #confirms that the balance under the specified customer has a decrement.

# Test calculate_total_spent()
print(customer1.calculate_total_spent())     #returns the total of the purchases by the customer

# Test search_purchase()
print(customer1.search_purchase(35)) 
print(customer1.search_purchase(80))    #since this is not in the customer's purchase history the expected output is purchase is not found.