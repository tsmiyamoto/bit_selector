# 何ビット目を支払うかをランダムに決める

## 使い方

```
people = []
amounts = []
```

を適切に設定して、

```
python3 main.py
```

たぶん Windows でしか動かない。

## 例

例えば、1200 円の支払いの場合、2 進数で表すと

```
10010110000
```

となる。
下位ビットから順に、誰が支払うかを決める。
もちろん、当該ビットが 0 だったら支払いは必要ない。
