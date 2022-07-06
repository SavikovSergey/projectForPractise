def print_info(object_name="unknown object", color="white", price=0,):
    print('Object: ', object_name, sep='\t')
    print('Color: ', color, sep='\t')
    print('Price', price, sep='\t')
    print()

print_info()

print_info(object_name= "pen",
           color = "blue",
           price = 1)

print_info(price=5, color='red')

print_info('coffee',price=10, color='black')