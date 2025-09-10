from abc import ABC,abstractmethod

class Ecommerce(ABC):


    @abstractmethod
    def product_list(self):

        pass

    @abstractmethod
    def add_to_cart(self):

        pass
    
    @abstractmethod
    def cart_summery(self):

        pass

    @abstractmethod
    def place_order(self):

        pass



class Amazon(Ecommerce):

    def product_list(self):
        
        print("product listed in amazom")

    def add_to_cart(self):
       
       print("Amazon add to cart")


    def cart_summery(self):
       
       print("cart summery of amazon")

    def place_order(self):
        
        print("amazon place ordered")



class Flipkart(Ecommerce):

    def product_list(self):
        
        print("product listed in Flipkart")

    def add_to_cart(self):
       
       print("Flipkart add to cart")


    def cart_summery(self):
       
       print("cart summery of flipkart")

    def place_order(self):
        
        print("flipkart place ordered")


amazon_instance = Amazon()

amazon_instance.place_order()

amazon_instance.add_to_cart()

amazon_instance.product_list()

Flipkart_instance = Flipkart()

Flipkart_instance.place_order()

Flipkart_instance.add_to_cart()

Flipkart_instance.product_list()


