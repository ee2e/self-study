'''
주어진 텍스트를 그대로 출력하세요.

#++++
+#+++
++#++
+++#+
++++#
'''

s = '++++'
s_list = list(s)

for i in range(0,len(s)+1):
    s_list.insert(i,'#')
    print(''.join(s_list))
    s = '++++'
    s_list = list(s)