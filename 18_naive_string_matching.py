text = input("Enter text: ")
pattern = input("Enter pattern (empty pattern is allowed): ")
n, m = len(text), len(pattern)

if m == 0:
    positions = list(range(n + 1))
else:
    positions = []
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i)

print("Matching starting indices:", positions)
