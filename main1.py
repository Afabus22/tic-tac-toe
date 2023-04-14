NAME_1 = input("Введите имя первого игрока\n")
NAME_2 = input("Введите имя второго игрока\n")


def draw_field():
    start = 0
    end = 3
    for row in range(1, 4):
        print(*field[start:end])
        start += 3
        end += 3

def check_cell(name, move):
    global field
    while True:
        cell = int(input(f"{name}, выбери ячейку для хода\n")) -1
        if field[cell] != '⬜':
            print("Эта ячейка уже занята")
            continue
        else:
            field[cell] = move
            draw_field()
            break    

vertical = 0
horizontal = 0
diagonal1 = 0
diagonal2 = 0

if str(vertical) == "x\nx\nx\n":
    print(f"NAME1 победил!")

field = []
for cell in range(0, 9):
    field.append('⬜')

draw_field()

while True: 
    check_cell(NAME_1, "x")
    check_cell(NAME_2, "o")

#    quantity_x = 0
#    for cell in field:
#        if cell == x:
#        quantity_x += 1

print("hello")