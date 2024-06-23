def solution(my_str, n):#함수 설정
    result = []
    for i in range(0, len(my_str), n):
        result.append(my_str[i:i+n])
    return result #결과 출력
