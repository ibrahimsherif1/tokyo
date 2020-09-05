print('''             (_)                         | |               
  _ __ ___   _____   ___ _ __   __ _    ___  _   _| |_     ___ ___  
 | '_ ` _ \ / _ \ \ / / | '_ \ / _` |  / _ \| | | | __|   / __/ _ \ 
 | | | | | | (_) \ V /| | | | | (_| | | (_) | |_| | |_   | (_| (_) |
 |_| |_| |_|\___/ \_/ |_|_| |_|\__, |  \___/ \__,_|\__| (_)___\___/ 
                                __/ |                               
                               |_____''')
print('''working time : from 8am to 9pm''')

print('''contact here : 080 6518 2781''')

height = input("what is the avarage height of your furniture?")
height = int(height)
weight = height - 50
line = "the weight of 1 furniture shouldnt exceed {}kg".format(weight)
print(line)

weight = input("what is the avarage wheight of 1 furniture?")
weight = int(weight)
weight = weight + 60
line = "the price for 1 furniture is {}$".format(weight)
print(line)

amount = input("what is the amount of the furnitures you want to transfer?")
amount = int(amount)
amount = weight * int(amount)
line = "price will be {}$".format(amount)
print(line)





