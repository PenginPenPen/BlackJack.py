# 二次元リストの要素の検索
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

target = 8
found = False
for i, row in enumerate(matrix):
    if target in row:
        j = row.index(target)
        print(i,j)
        found = True
        break

if not found:
    pass

# 二次元リストのソート
matrix = [["❤️",1],["♠️",3],["♣️",2]]

sorted_matrix = sorted(matrix, key=lambda x: x[1])

print(sorted_matrix)


