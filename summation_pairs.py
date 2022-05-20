from collections import deque

nums = deque(int(x) for x in input().split())

target = int(input())
iterations = 0
unique_pairs = list()

while nums:
    current_num = nums.popleft()
    if nums:
        for el in nums:
            iterations += 1
            if current_num + el == target:
                print(f"{current_num} + {el} = {target}")
                current_pair = (current_num, el)
                if current_pair not in unique_pairs:
                    unique_pairs.append(current_pair)

    else:
        break

print(f'Iterations done: {iterations}')
unique_pairs.reverse()
while unique_pairs:
    print(f'{unique_pairs.pop()}')
