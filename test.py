tile_list: dict[tuple[int, int], str] = {}

for i in range(3):
    for j in range(3):
        tile = f'{i}, {j}'
        
        tile_list[i, j] = tile

print(tile_list)