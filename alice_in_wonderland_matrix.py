size = int(input())

land = []
alice_row = 0
alice_col = 0

for row in range(size):
    data_input = input().split()
    land.append(data_input)
    for col in range(size):
        if data_input[col] == "A":
            alice_row = row
            alice_col = col

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

tea_bags = 0

while True:
    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break
    command = input()
    current_row = alice_row
    current_col = alice_col
    land[current_row].pop(current_col)
    land[current_row].insert(current_col, "*")
    current_row, current_col = directions[command](alice_row, alice_col)
    if current_row < 0 or current_row >= size or current_col < 0 or current_col >= size:
        print("Alice didn't make it to the tea party.")
        break
    if land[current_row][current_col] == "R":
        print("Alice didn't make it to the tea party.")
        land[current_row].pop(current_col)
        land[current_row].insert(current_col, "*")
        break
    if land[current_row][current_col].isdigit():
        current_num = int(land[current_row][current_col])
        tea_bags += current_num
    alice_row = current_row
    alice_col = current_col
    land[current_row].pop(current_col)
    land[current_row].insert(current_col, "*")

for ro in range(size):
    print(*land[ro])
