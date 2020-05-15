import sys

sys.stdin = open('캐시.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    cacheSize = input()
    cities = list(input().split())
