"""
https://algo-method.com/tasks/212

### 問題
$N$ 個の整数 $A_0, A_1, \dots, A_{N-1}$ が与えられます。
$N$ 個の整数のうち、正の整数が何個あるかを数えるプログラムを作成してください。
### 入力
入力は次の形式で与えられます。
```IOExample
$N$
$A_0 A_1 \dots A_{N-1}$
```
また、入力される値は次の制約を満たします。
- $N$ は $1$ 以上 $100$ 以下の整数
- $A_i$ は $-100$ 以上 $100$ 以下の整数 $(0 \leq i \leq N-1)$
### 出力
$N$ 個の整数のうち $0$ より大きいものの個数を出力してください。
"""
N = map(int, input().split())
data = list(map(int, input().split()))

flag = 0
for i in data:
    if i > 0:
        flag += 1

print(flag)
