def solution(n):
    ans = 0

    if n%2!=0:
        n-=1
        ans+=1
    while n>0:
        if n%2==0:
            n=n//2
        else:
            n-=1
            n=n//2
            ans+=1

    return ans