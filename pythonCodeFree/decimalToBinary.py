binary_stack =[]
while True:
    print("\nNhap dieu kien dung la y :")
    y = input()
    if y =='y':
        break
    print("Nhap so muon chuyen doi sang nhi phan :")
    n = int(input())
    while n > 0:
        binary_stack.append(str(n %2))
        n//=2
    while binary_stack :
        print(binary_stack.pop(),end='')
print()
