from Implementation.ProductsImplementation import ProductsImplementation
from Implementation.VendorImplementation import VendorImplementation
from Models.VendorSessionModel import VendorSessionModel

if __name__ == '__main__':


    vendor = VendorImplementation()

    username = input("Enter your username: ")
    password = input("Enter password: ")

    #login_res = vendor.login('Gosling', 'gosling_pw')
    login_res = vendor.login(username, password)
    if login_res == False:
        print("\nNot Authorized Vendor")
    else:
        #products = ProductsImplementation("Gosling")
        products = ProductsImplementation(username)
        print("\n")

        num_of_products = int(input("Enter number of products to be added: "))
        count = 0
        while(count<num_of_products):
            product_name = input("\nEnter product name: ")
            product_type = input("Enter product type: ")
            quantity = int(input("Enter available quantity: "))
            price = int(input("Enter price: "))
            products.add_product(product_name, product_type, quantity, price)
            count = count + 1
        #products.add_product("Lenovo Thinkpad", "Laptop", 40, 20000)
        #products.add_product("Dell Inspiron", "Laptop", 40, 30000)
        #products.add_product("Acer Razor", "Laptop", 40, 25000)        
        #products.add_product("Asus Tinker", "Laptop", 40, 20000)
        #products.add_product("Lenovo Gaming", "Laptop", 40, 20000)
        
        required_product = input("\nEnter the product to be searched: ")
        #search_product = products.search_product_by_name("Lenovo Gaming")
        search_product = products.search_product_by_name(required_product)
        if (search_product):
            print("\nSearched product details:\t")
            print(search_product)
        else:
            print("\nNo product exists by the name")
        
        all_products = products.get_all_products()
        print("\nAll available products:")
        if (all_products):
            print("\n".join("{}\t{}".format(k, v) for k, v in all_products.items()))
        else:
            print("\nNo product is available to fetch.")

        print("\n")
        #vendor.logout("Gosling")    
        vendor.logout(username) 
