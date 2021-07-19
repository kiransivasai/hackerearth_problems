from collections import Counter
         
def rotate_row(arr, idx, offset):
    if offset == 0:
        return
    arr[idx] = arr[idx][-offset:] + arr[idx][:-offset]
         
def rotate_col(arr, idx, offset):
    res = []
    for i in range(len(arr)):
        res.append(arr[(i - offset) % len(arr)][idx])
    for i, x in enumerate(res):
        arr[i][idx] = x
                
n, r, c = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for x, y in Counter(map(int, input().split())).items():
    rotate_row(a, x - 1, y % n)
for x, y in Counter(map(int, input().split())).items():
    rotate_col(a, x - 1, y % n)
for x in a:
    for y in x:
        print(y, end = ' ')
    print()
