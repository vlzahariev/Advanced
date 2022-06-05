size = 5
area = []
pos_row = 0
pos_col = 0
potential_targets = 0
target = 0
target_pos = []

for row in range(size):
    data = input().split()
    area.append(data)
    for col in range(size):
        if data[col] == "A":
            pos_row = row
            pos_col = col
        if data[col] == "x":
            potential_targets += 1

direction_shoot = {
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}
direction_move = {
    "left": lambda r, c, step: (r, c - step),
    "right": lambda r, c, step: (r, c + step),
    "up": lambda r, c, step: (r - step, c),
    "down": lambda r, c, step: (r + step, c)
}
command_num = int(input())
completed = False

for i in range(command_num):
    command = input().split()
    if command[0] == "move":
        way = command[1]
        steps = int(command[2])
        row, col = direction_move[way](pos_row, pos_col, steps)
        if 0 <= row < size and 0 <= col < size and area[row][col] == ".":
            pos_row = row
            pos_col = col
    elif command[0] == "shoot":
        way = command[1]
        current_row = pos_row
        current_col = pos_col
        shoot_row = current_row
        shoot_col = current_col
        shot = False
        while True:
            row, col = direction_shoot[way](shoot_row, shoot_col)
            if 0 <= row < size and 0 <= col < size:
                shoot_row = row
                shoot_col = col
                if area[shoot_row][shoot_col] == "x":
                    target += 1
                    target_pos.append([shoot_row, shoot_col])
                    area[shoot_row].pop(shoot_col)
                    area[shoot_row].insert(shoot_col, ".")
                    shot = True
                    break
                else:
                    continue
            else:
                break

    if potential_targets == target:
        print(f"Training completed! All {target} targets hit.")
        completed = True
        break

if not completed:
    print(f"Training not completed! {potential_targets - target} targets left.")

print(*target_pos, sep="\n")
