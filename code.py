R, C = map(int, input().split())
B = [input() for _ in range(R)]
ans = [""] * R
label = set()
for i in range(R):
  for j in range(C):
    if B[i][j] != "#" and B[i][j] != ".":
      bomb = int(B[i][j])
      for k in range(R):
        for l in range(C):
          if abs(l-j) + abs(k-i) <= bomb:
            label.add((k,l))
for i in range(R):
  for j in range(C):
    if (i,j) in label:
      ans[i] += "."
    else:
      ans[i] += B[i][j]
for i in range(R):
  print(ans[i])