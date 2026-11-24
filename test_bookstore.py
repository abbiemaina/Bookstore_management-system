"""This file tests the classes and their methods
in the bookstore management system."""

import bookstore_classes as bc

##### TEST THE BOOK CLASS #####

# Create a book object
book1 = bc.Book("Mile High", "Liz Tomforde", "978-0141", 15, 10)
book2 = bc.Book("The only one left", "Riley Sager", "874-0415", 20, 15)

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



##### TEST THE CLASS ORDER #####

# Create an order object
order1 = bc.Order("ORD001", customer1, book1, 2, "2026-11-20", "Pending")

# Test display_order_details()
order1.display_order_details()

# Test calculate_total()
expected_total = book1.price * 2
actual_total = order1.calculate_total()
print("Expected total:", expected_total)


# Test update_status()
result = order1.update_status("Shipped")
print(result)
print("Current order status:", order1.status) 

# Test add_book()
result = order1.add_book(book2, 1)
print(result)
print("Number of books in order:", len(order1.book))


# Test remove_book()
result = order1.remove_book(book2)
print(result)
print("Number of books remaining:", len(order1.book))

# Test search_book()
result = order1.search_book(book2)
print(result)     #book will not be found because it was removed from the order.



##### TEST THE INVENTORY CLASS #####

# Create a sample inventory
inventory1 = bc.Inventory("INV001", 100, "2026-11-23", 10)

# Test display_inventory()
inventory1.display_inventory()

# Test check_low_stock()
inventory1.check_low_stock()

# Test add_books()
inventory1.add_books(50)
print("Updated inventory total:", inventory1.total_books)

# Test update_inventory()
inventory1.update_inventory()
print("Updated inventory total:", inventory1.total_books)

# Test get_total_books()
total = inventory1.get_total_books()
print("Total books in inventory:", total)



##### ADDITIONAL TESTING (EDGE CASES) #####
# Test A is an inventory with zero books
inventory1.total_books = 0
print("Total books:", inventory1.get_total_books())
inventory1.check_low_stock() 
#this test checks whether an inventory can store 0 books, whether the get_total_books returns zero and whether the check_low_stock will recognize that the stock is low, assuming the threshold is >= 0.



# Test B is adding books to an empty inventory.
inventory1.add_books(50)
print("Expected total: 50")
print("Actual total:", inventory1.get_total_books())


# Test C is testing multiple books in an order
expected_total = (book1.price * 2) + (book2.price * 3)
actual_total = order1.calculate_total()
print("Expected total:", expected_total)
print("Actual total:", actual_total)


## INTERGRATION TEST ##
print(customer1)
print(book1)
print(book2)
print(order1)
print("Order total:", order1.calculate_total())