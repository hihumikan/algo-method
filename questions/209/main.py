"""
https://algo-method.com/tasks/209

### 問題
整数 $N$, $V$ と、$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数の中に、整数 $V$ があるかどうかを判定するプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$ $V$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $V$ は $1$ 以上 $100$ 以下の整数
- $A_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
$N$ 個の整数の中に $V$  があれば `Yes` を出力し、なければ `No` を出力してください。
"""

N, value = map(int, input().split())
data = list(map(int, input().split()))

flag = False
for i in data:
    if i == value:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
