#A restaurant always prepares dishes with the most orders before others with a lesser number of orders. 
#Each dish in the restaurant menu has a unique integer ID. The restaurant receives n orders in a particular time period. 
#The task is to find out the order of dish IDs according to which the restaurant will prepare them. 
#Assume that restaurant has the following unique dish IDs in its menu:
#[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
#Write a function DishPrepareOrder(order_list) that accepts order_list in the form of a list of dish IDs and returns a list of dish IDs in the order in which the restaurant will prepare them. 
#If two or more dishes have the same number of orders, then the dish which has a smaller ID value will be prepared first.
#Sample input
#[1004,1003,1004,1003,1004,1005,1003,1004,1003,1002,1005,1002,1002,1001,1002,1002,1002]
#Output
#[1002, 1003, 1004, 1005, 1001]

def DishPrepareOrder(order_list):
    order_dict = dict()
    for order in order_list:
        if order not in order_dict:
            order_dict[order] = 1
        else:
            order_dict[order] += 1

    def order_by_key(od):
        sorted_od = dict(sorted(od.items()))
        return sorted_od
        
    def order_by_value(od):
        max = 0
        max_key = None
        if len(od) == 1:
            for key,value in od.items():
                return [key]
        for k,v in od.items():
            if v > max:
                max = v
                max_key = k
        del od[max_key]
        return [max_key] + order_by_value(od)
    order_key = order_by_key(order_dict)
    return order_by_value(order_key)
        
nums = eval(input())
print(DishPrepareOrder(nums))
