#1
#first_name = input('Enter your first name: ')
#last_name = input('Enter your last name: ')
#full_name = first_name + ' ' + last_name
#print(f'Your first name is {first_name} and your last name is {last_name}')
#print(f'And your full name is {full_name}')


#2
#cube_side_string = input('Enter cube side: ')
#cube_side = int(cube_side_string)
#cube_volume = cube_side * 3
#cube_surface_area =  6 * (cube_side ** 2)
#print(f'The volume of a cube with side {cube_side} is {cube_volume}')
#print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')

#3
#a = int(input('a= '))
#b = int(input('b= '))
#c = int(input('c= '))
#volume = a * b * c
#surface_area = 2 * (a * b + a * c + b * c)
#print(f'The volume of the cuboid is {volume}')
#print(f'The surface area of the cuboid is {surface_area}')

#4
#total_amount = float(input("Enter the amount including VAT: "))
#vat_rate = 0.23
#net_amount = total_amount / (1 + vat_rate)
#vat_amount = total_amount - net_amount
#print(f"Amount  : {net_amount:.2f}")
#print(f"VAT 23% : {vat_amount:.2f}")

#5
price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount %: "))
discount_amount = price * (discount_percentage / 100)
discounted_price = price - discount_amount
print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {discount_amount:.2f}")
