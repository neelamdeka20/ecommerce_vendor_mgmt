from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        # check if the vendor is logged in, then add the product and return True else Return False
        if not self.vendor_session.check_login(self._username):
            print("Please login or signup.")
            return False
        
        self.product_model.add_product(product_name, product_type, available_quantity, unit_price)
        print(product_name + " added successfully.")
        return True
            
    def search_product_by_name(self, product_name):
        # Search if the product is available in the dictionary if the vendor is authorized to access else return False
        # If product is available then return product
        if not self.vendor_session.check_login(self._username):
            print("Please login or signup.")
            return False
        
        searched_product = self.product_model.search_product(product_name)
        return searched_product

    def get_all_products(self):
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products 
        if not self.vendor_session.check_login(self._username):
            print("Please login or signup.")
            return False
        
        all_products = self.product_model.all_products()
        return all_products
