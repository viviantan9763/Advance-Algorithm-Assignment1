import time

# 1.3 Local Storage System for Baby Products
# Baby Product Class
class BabyProduct:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: ${self.price}"

# 1.1 Node Class
# Node for Linked List (Separate Chaining)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# 1.2 Hash Table and Hash Function
# Hash Table Class
class HashTable: #Empty Hash Table class to save methods
    def __init__(self, size): #constructor
        self.size = size      #number of bucket
        self.table = [None] * self.size #create empty list with None element

    def hash_function(self, key):  #hash(key) convert the key into an integer
        return hash(key) % self.size #make sure index size same as hash table

    #Insert method
    def insert(self, key, value):
        index = self.hash_function(key)#Compute the bucket index with hash_function.
        new_node = Node(key, value) #Create a Node to hold key+value
        if self.table[index] is None: #if bucket is none/empty
            self.table[index] = new_node
        else:
            current = self.table[index] #if the bucket already occupied
            while current.next:
                current = current.next  #appent to new node
            current.next = new_node

    #Search Method
    def search(self, key):
        index = self.hash_function(key) #Compute the bucket index with hash_function.
        current = self.table[index]#linked list
        while current:
            if current.key == key: #If found match key return value
                return current.value
            current = current.next
        return None #not found return None

    #Delete Method
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index] #get first node
        prev = None

        while current: #loop node in linked list
            if current.key == key: #current node has the node
                if prev:           #not fist node
                    prev.next = current.next #skip current node
                else:
                    self.table[index] = current.next #update bucket
                return True   #node delete successfully
            prev = current    #link linked list
            current = current.next
        return False         #no node found, key cannot delete

    #Edit method edit product name and product price
    def edit(self, key, new_name=None, new_price=None):
        index = self.hash_function(key)
        current = self.table[index] #Get first node

        while current:   #Loop through node
            if current.key == key: #check current node
                if new_name:
                    current.value.name = new_name #update new name
                if new_price:
                    current.value.price = new_price #update new price
                return True #edit successfully
            current = current.next
        return False #Edit unsuccessfully

# 1.5 Performance Comparison
# Performance Test: Hash Table vs Array
def performance_test(hash_table, array, search_keys):
    start_ht = time.perf_counter_ns()
    for key in search_keys:
        hash_table.search(key)
    end_ht = time.perf_counter_ns()
    ht_time = end_ht - start_ht

    start_arr = time.perf_counter_ns()
    for key in search_keys:
        for item in array:
            if item.id == key:
                break
    end_arr = time.perf_counter_ns()
    arr_time = end_arr - start_arr

    print("\nPerformance Test (nanoseconds):")
    print(f"Hash Table Search Time: {ht_time} ns")
    print(f"Array Search Time: {arr_time} ns")

# 1.4 Command-Line Inventory System
def main():
    ht_size = 10
    ht = HashTable(ht_size)

    # Sample Products (Local Storage System)
    products = [
        BabyProduct(101, "Diaper", 20.0),
        BabyProduct(102, "Baby Bottle", 15.0),
        BabyProduct(103, "Baby Lotion", 18.0),
        BabyProduct(104, "Baby Powder", 12.0),
        BabyProduct(105, "Wet Wipes", 10.0),
        BabyProduct(106, "Pacifier", 8.0),
        BabyProduct(107, "Baby Shampoo", 14.0),
        BabyProduct(108, "Baby Oil", 16.0),
        BabyProduct(109, "Baby Soap", 9.0),
        BabyProduct(110, "Teething Toy", 11.0),
        BabyProduct(111, "Baby Blanket", 25.0),
        BabyProduct(112, "Baby Towel", 13.0),
        BabyProduct(113, "Milk Formula Stage 1", 55.0),
        BabyProduct(114, "Milk Formula Stage 2", 58.0),
        BabyProduct(115, "Milk Formula Stage 3", 60.0),
        BabyProduct(116, "Baby Bib", 6.0),
        BabyProduct(117, "Baby Bed Sheet", 22.0),
        BabyProduct(118, "Baby Mittens", 5.0),
        BabyProduct(119, "Baby Socks", 4.0),
        BabyProduct(120, "Baby Hat", 7.0),
        BabyProduct(121, "Baby Carrier", 150.0),
        BabyProduct(122, "Stroller", 350.0),
        BabyProduct(123, "Baby Crib", 500.0),
        BabyProduct(124, "Baby Bathtub", 45.0),
        BabyProduct(125, "Baby Nail Clipper", 9.0),
        BabyProduct(126, "Nappy Rash Cream", 18.0),
        BabyProduct(127, "Thermometer", 25.0),
        BabyProduct(128, "Baby Monitor", 210.0),
        BabyProduct(129, "Sterilizer", 120.0),
        BabyProduct(130, "Bottle Brush", 8.0),
        BabyProduct(131, "Sippy Cup", 12.0),
        BabyProduct(132, "Baby Food Jar Apple", 6.0),
        BabyProduct(133, "Baby Food Jar Banana", 6.0),
        BabyProduct(134, "Baby Food Jar Pumpkin", 6.0),
        BabyProduct(135, "Baby Food Jar Carrot", 6.0),
        BabyProduct(136, "Baby Bowl", 10.0),
        BabyProduct(137, "Baby Spoon Set", 7.0),
        BabyProduct(138, "Portable Changing Mat", 18.0),
        BabyProduct(139, "Baby Swaddle", 20.0),
        BabyProduct(140, "Baby Play Mat", 65.0),
        BabyProduct(141, "Baby Laundry Detergent", 22.0),
        BabyProduct(142, "Baby Soft Toy Bunny", 30.0),
        BabyProduct(143, "Baby Soft Toy Bear", 30.0),
        BabyProduct(144, "Baby Rattle", 10.0),
        BabyProduct(145, "Baby Toothbrush", 7.0),
        BabyProduct(146, "Baby Toothpaste", 8.0),
        BabyProduct(147, "Baby Vitamin Drops", 28.0),
        BabyProduct(148, "Breast Pump", 280.0),
        BabyProduct(149, "Nursing Cover", 35.0),
        BabyProduct(150, "Baby Bowl with Suction", 14.0),
        BabyProduct(151, "Baby Shoes", 18.0),
        BabyProduct(152, "Baby Pants", 12.0),
        BabyProduct(153, "Baby Shirt", 10.0),
        BabyProduct(154, "Baby Dress", 15.0),
        BabyProduct(155, "Baby Pajamas", 14.0),
        BabyProduct(156, "Baby Gloves", 6.0),
        BabyProduct(157, "Baby Sweater", 20.0),
        BabyProduct(158, "Baby Jacket", 25.0),
        BabyProduct(159, "Baby Blanket Premium", 35.0),
        BabyProduct(160, "Baby Diaper Bag", 80.0),
        BabyProduct(161, "Baby High Chair", 120.0),
        BabyProduct(162, "Baby Feeding Chair", 100.0),
        BabyProduct(163, "Baby Food Processor", 180.0),
        BabyProduct(164, "Baby Thermos", 20.0),
        BabyProduct(165, "Baby Sun Hat", 10.0),
        BabyProduct(166, "Baby Sunglasses", 12.0),
        BabyProduct(167, "Baby Sleep Sack", 28.0),
        BabyProduct(168, "Baby Night Light", 25.0),
        BabyProduct(169, "Baby Crib Mobile", 45.0),
        BabyProduct(170, "Baby Activity Gym", 70.0),
        BabyProduct(171, "Baby Walker", 150.0),
        BabyProduct(172, "Baby Playpen", 200.0),
        BabyProduct(173, "Baby Bouncer", 90.0),
        BabyProduct(174, "Baby Swing", 120.0),
        BabyProduct(175, "Baby Car Seat", 250.0),
        BabyProduct(176, "Baby Diaper Cream", 15.0),
        BabyProduct(177, "Baby Laundry Basket", 20.0),
        BabyProduct(178, "Baby Changing Table", 180.0),
        BabyProduct(179, "Baby Feeding Bottle", 14.0),
        BabyProduct(180, "Baby Nipple", 5.0),
        BabyProduct(181, "Baby Pacifier Clip", 6.0),
        BabyProduct(182, "Baby Teething Ring", 9.0),
        BabyProduct(183, "Baby Safety Gate", 80.0),
        BabyProduct(184, "Baby Stroller Rain Cover", 15.0),
        BabyProduct(185, "Baby Hand Sanitizer", 8.0),
        BabyProduct(186, "Baby Bath Sponge", 7.0),
        BabyProduct(187, "Baby Lotion Sensitive", 18.0),
        BabyProduct(188, "Baby Shampoo Tear-Free", 14.0),
        BabyProduct(189, "Baby Oil Natural", 16.0),
        BabyProduct(190, "Baby Diaper Pants", 22.0),
        BabyProduct(191, "Baby Socks Cotton", 5.0),
        BabyProduct(192, "Baby Shoes Soft", 18.0),
        BabyProduct(193, "Baby Cap Soft", 7.0),
        BabyProduct(194, "Baby Mittens Cotton", 6.0),
        BabyProduct(195, "Baby Bib Waterproof", 8.0),
        BabyProduct(196, "Baby Blanket Fluffy", 30.0),
        BabyProduct(197, "Baby Stroller Cushion", 20.0),
        BabyProduct(198, "Baby Bottle Warmer", 25.0),
        BabyProduct(199, "Baby Food Jar Mixed Veggies", 7.0),
        BabyProduct(200, "Baby Food Jar Chicken", 8.0),
    ]

    product_array = []
    for p in products:
        ht.insert(p.id, p)
        product_array.append(p)

    choice = 0
    while choice != 7:
        print("\n--- Baby Shop Inventory Menu ---")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Performance Test (Hash Table vs Array)")
        print("6. Display All Products")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-6.")
            continue


        # 1. INSERT
        if choice == 1:
            try:
                pid = int(input("Enter Product ID(Example:101): "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Price: "))

                # Check if Product ID already exists
                if ht.search(pid):
                    print("Error: Product ID already exists. Please enter a unique ID.")
                    continue

                # Check if Product Name already exists
                name_exists = any(p.name.lower() == name.lower() for p in product_array)
                if name_exists:
                    print("Error: Product Name already exists. Please enter a unique name.")
                    continue

                # If both ID and Name are unique, insert product
                new_product = BabyProduct(pid, name, price)
                ht.insert(pid, new_product)  # Insert into hash table
                product_array.append(new_product)  # Insert into array
                print("\nProduct inserted successfully.")

                # ★★★ Show updated product list ★★★
                print("\n--- Updated Product List ---")
                for p in product_array:
                    print(p)

            except ValueError:
                print("Invalid input. Please enter correct data types.")


        # 2. SEARCH
        elif choice == 2:
            try:
                pid = int(input("Enter Product ID to search: "))
                result = ht.search(pid)
                if result:
                    print("Product Found:", result)
                else:
                    print("Product not found.")
            except ValueError:
                print("Invalid input. Please enter a numeric Product ID.")

        # 3. EDIT
        elif choice == 3:
            try:
                pid = int(input("Enter Product ID to edit: "))
                new_name = input("Enter new name (press Enter to skip): ")
                new_price_input = input("Enter new price (press Enter to skip): ")
                new_price = float(new_price_input) if new_price_input else None
                new_name = new_name if new_name != "" else None
                success = ht.edit(pid, new_name, new_price)
                print("Product updated successfully!" if success else "Product not found.")
            except ValueError:
                print("Invalid input. Please enter correct data types.")

        # 4. DELETE
        elif choice == 4:
            try:
                pid = int(input("Enter Product ID to delete: "))
                success = ht.delete(pid)
                if success:
                    # 同时从 array 删除
                    product_array = [p for p in product_array if p.id != pid]
                    print("Product deleted successfully.")
                else:
                    print("Product not found.")
            except ValueError:
                print("Invalid input. Please enter a numeric Product ID.")

        # 5. PERFORMANCE TEST（Testing)
        elif choice == 5:
            search_keys = [p.id for p in product_array]
            performance_test(ht, product_array, search_keys)

        elif choice == 6:
            if not product_array:
                print("No products available.")
            else:
                print("\n--- Current Products ---")
                for p in product_array:
                    print(p)

        # 7. EXIT
        elif choice == 7:
            print("Exiting program. Goodbye!")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    """
            # Separate Chaining Demo Test
            print("\n--- Separate Chaining Demo ---")
            demo_ht_size = 5  # smaller size to force collisions
            demo_ht = HashTable(demo_ht_size)
            # Insert two keys that will collide
            demo_ht.insert(1, BabyProduct(1, "Collision A", 5.0))
            demo_ht.insert(6, BabyProduct(6, "Collision B", 10.0))
            # Search for both keys
            res1 = demo_ht.search(1)
            res2 = demo_ht.search(6)
            print("Search result for key 1:", res1)
            print("Search result for key 6:", res2)
            print("--- End of Separate Chaining Demo ---\n") """
