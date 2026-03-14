# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys

input = sys.stdin.readline


N = int(input())
stack = []

for i in range(N):
    comment = input().split()

    if comment[0] == "push":
        stack.append(int(comment[1]))
    
    elif comment[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif comment[0] == "size":
        print(len(stack))
    
    elif comment[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    
    elif comment[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)