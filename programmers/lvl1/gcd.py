def solution(n, m):
    answer = []

    # 최대공약수 구하기
    def get_gcd(num1: int, num2: int) -> int:
        print(num1, num2)
        if num2 == 0:
            return num1
        else:
            get_gcd(num2, num1 % num2)

    gcd = int(get_gcd(n, m))
    print(gcd)
    answer.append(gcd)

    # 최소공배수 구하기
    answer.append(n * m / gcd)

    return answer


if __name__ == '__main__':
    solution(3, 12)
