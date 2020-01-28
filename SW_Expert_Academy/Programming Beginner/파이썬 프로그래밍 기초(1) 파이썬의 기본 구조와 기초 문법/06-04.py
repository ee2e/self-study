man1 = input()
man2 = input()

man_list = ["가위", "바위", "보"]

if man1 == man2 :
    print(f'Result : Draw!')
elif man1 == man_list[0] and man2 == man_list[1] :
    print(f'Result : Man2 Win!')
elif man1 == man_list[0] and man2 == man_list[2] :
    print(f'Result : Man1 Win!')
elif man1 == man_list[1] and man2 == man_list[0] :
    print(f'Result : Man1 Win!')
elif man1 == man_list[1] and man2 == man_list[2] :
    print(f'Result : Man2 Win!')
elif man1 == man_list[2] and man2 == man_list[0] :
    print(f'Result : Man1 Win!')
else :
    print(f'Result : Man2 Win!')