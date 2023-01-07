def runner_score(arr):
    n = int(input())
    arr = map(int, input().split())
    sort_value = sorted(set(arr))
    print(sort_value[-2])