'''
"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

출력)
184
'''
str_list = list("ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC")
int_list = list(map(lambda x : ord('E') - ord(x),str_list))
print(sum(int_list))

# ord, chr 함수
# 이 문제 ord 사용해서 푼 것!