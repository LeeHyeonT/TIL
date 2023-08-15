import sys
sys.stdin = open('input.txt', encoding='UTF-8')
input = sys.stdin.readline

while True:
    try:
        coupon, stamp = map(int, input().rstrip().split())
        ans = 0
        ans += coupon
        new_coupon = coupon
        others = 0
        while True:
            others += new_coupon % stamp
            new_coupon = new_coupon // stamp
            
            if others >= stamp:
                new_coupon += 1
                others -= stamp
            if new_coupon == 0:
                break
            
            ans += new_coupon
        print(ans)
        
    except ValueError:
        break

'''
ohters를 먼저 계산해야하는데 자꾸 new_coupon 계산 후 나타내어 올바른 풀이가 되지 못하였다.
'''