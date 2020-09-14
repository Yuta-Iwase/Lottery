
import random
import re

# くじ箱作成
lot = []
with open("lot.txt", "r", encoding='utf8') as f:
  while True:
    line = f.readline()
    if line:
      line = line.replace('\n', '')
      lot.append(line)
    else:
      break

# 役職者リスト読み込み
position = []
position_map = {}
with open("position_list.txt", "r", encoding='utf8') as f:
  while True:
    line = f.readline()
    if line:
      line = line.replace('\n', '')
      position.append(line)
      position_map[line] = []
    else:
      break

# くじ引き開始
for pos in position:
  chosen_index = random.randint(0, len(lot)-1)
  chosen = lot.pop(chosen_index)
  position_map[pos].append(chosen)

# 結果
print(position_map)