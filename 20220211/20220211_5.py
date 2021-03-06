# 각자리가 0~9로이루어진 문자열 S
# 021025
# 왼쪽에서 오른쪽으로 하나씩 모든 숫자를 확인해가면서 숫자사이에 X 또는 + 를 해서 만들수 있는 가장 큰 수를
# 구해보자
# ((0+2)+1+0)x2x5
number = list(map(int, input()))
print(number)

result = number[0]
for i in number:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i
print(result)

# 4자리 년도를 입력하면 그년도 윤년인지 판단.
# 그레고리력의 정확한 윤년 규칙은 다음과 같다.
# 서력 기원 연수가 004로 나누어 떨어지는 해는 윤년으로 한다. (1984년, 1988년, 1992년, 1996년, 2004년, 2008년, 2012년, 2016년, 2020년, 2024년, 2028년, 2032년, 2036년, 2040년, 2044년, 2048년, 2052년...)
# 서력 기원 연수가 004, 100으로 나누어 떨어지는 해는 평년으로 한다. (1700년, 1800년, 1900년, 2100년, 2200년, 2300년...)
# 서력 기원 연수가 004, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다. (1600년, 2000년, 2400년...)
