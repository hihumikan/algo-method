"""
https://algo-method.com/tasks/215

### 問題
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
次の条件を満たす $i$ の個数を調べるプログラムを作成してください。
- $i$ は $1$ 以上 $N-1$ 以下の整数
- $A_i$ は $A_{i-1}$ よりも大きい
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約をみたします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $A_i$ は $1$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
答えを出力してください。
"""

N, value = map(int, input().split())
data = list(map(int, input().split()))

flag = -1
for i in range(N):
    if data[i] == value:
        flag = i

print(flag)
