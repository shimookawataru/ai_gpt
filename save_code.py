# R行C列のマップを入力
R, C = map(int, input().split())
# マップをリストに格納
B = [input() for _ in range(R)]
# 空のリストを作成
ans = [""] * R
# 爆弾の範囲にあるマスを格納するためのset
label = set()
# マップを走査して爆弾の範囲にあるマスをlabelに格納
for i in range(R):
  for j in range(C):
    if B[i][j] != "#" and B[i][j] != ".":
      bomb = int(B[i][j])
      for k in range(R):
        for l in range(C):
          if abs(l-j) + abs(k-i) <= bomb:
            label.add((k,l))
# labelに格納されたマスを"."に置き換えてansに格納
for i in range(R):
  for j in range(C):
    if (i,j) in label:
      ans[i] += "."
    else:
      ans[i] += B[i][j]
# ansを出力
for i in range(R):
  print(ans[i])