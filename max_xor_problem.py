# Author: Edmund Aduse Poku
# Maximum XOR Problem


def maxXor(arr, queries):
    ans = []
    trie = {}
    k = len(bin(max(arr+queries))) - 2
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for char in number:
            node = node.setdefault(char, {})
    for n in queries:
        node = trie
        s = ''
        for char in'{:b}'.format(n).zfill(k) :
            tmp = str(int(char) ^ 1)
            tmp = tmp if tmp in node else char
            s += tmp
            node = node[tmp]
        ans.append(int(s, 2) ^ n)
    return ans


arr = [3, 9, 9, 7, 6]
k = 12
for number in ['{:b}'.format(x).zfill(k) for x in arr]:
    print(number)
x = 2
print('{:03b}'.format(x))

print(0^1)

print(int("10"))