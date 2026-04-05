# 1. 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

# 2. 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
def solution(s):
    return int(s)

# 3. 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
def solution(n):
    total = 0
    
    for i in range(1, n + 1):
        if n % i == 0: 
            total += i
            
    return total

# 4. 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
def solution(N):
    return sum(int(digit) for digit in str(N))

# 5. 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
def solution(n):
    return [int(digit) for digit in str(n)[::-1]]