# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Cody Martin


def shippingCost(orderSubTotal):
    shippingCost = 2.99
    # enter code here to test for free

    
    if orderSubTotal >= 10.00:
        shippingCost = 0


    return shippingCost
    
   

def unitTest():
    print("Shipping cost if orderSubtotal < 10.00:\t", shippingCost(5.99))
    print("Shipping cost if orderSubtotal = 10.00:\t", shippingCost(10.00))
    print("Shipping cost if orderSubtotal > 10.00:\t", shippingCost(11.00))
    # enter additional test code here


if __name__ == "__main__":
    unitTest()