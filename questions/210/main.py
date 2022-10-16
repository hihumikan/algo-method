"""
https://algo-method.com/tasks/210

### 問題
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数の中に整数 $V$ が何個あるかを数えるプログラムを作成してください。
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
答えを出力してください。
"""
N, value = map(int, input().split())
data = list(map(int, input().split()))

flag = 0
for i in data:
    if i == value:
        flag += 1

print(flag)
