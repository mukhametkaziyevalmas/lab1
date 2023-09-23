print("Hello world")
print( 4,  8 , 15 , 16,  23,  42)


print( "4\n8\n15\n16\n23\n42\n")

a = int (input())

print(a)
print(a+1)
print(a+2)


b=int(input())
c=int(input())
d=int(input())

print(b+c+d)

def cube_volume(edge_length):
    volume1 = edge_length ** 3
    return volume1


def cube_surface_area(edge_length):
    surface_area1 = 6 * (edge_length ** 2)
    return surface_area1


c = float(input())

n = int(input("n = "))
k = int(input("k = "))
p = k // n
o = k % n
print(p)
print(o)



number = int(input("Enter a four-digit number: "))


thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10


print("The digit in the thousands position is", thousands)
print("The digit in the hundreds position is", hundreds)
print("The digit in the tens position is", tens)
print("The digit in the units position is", units)



people = int(input())

if people % 2 == 0:
    people = people
else:
    people = people + 1

print(people / 2)



num = int(input("Введите целое число: "))

num1 = num << 1

print(f"Результат побитового сдвига влево на один бит: {num1}")

if num1 == 0:
    print("Результат равен нулю.")



volume = cube_volume(c)
surface_area = cube_surface_area(c)

print(f"Volume = {volume}")
print(f"Total surface area = {surface_area}")




num1 = float(input("Пожалуйста, введите первое число: "))
num2 = float(input("Пожалуйста, введите второе число: "))
operation = input("Пожалуйста, выберите операцию (+, -, *, /): ")

result = None
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Ошибка: деление на ноль.")
    else:
        result = num1 / num2
else:
    print("Ошибка: неверная операция.")

if result is not None:
    print(f"{num1} {operation} {num2} = {result:.3f} ")
