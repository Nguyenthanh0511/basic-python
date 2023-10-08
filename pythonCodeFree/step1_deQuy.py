def deQuy(arr , i):
    if i<0:
        return 0
    return i + deQuy(arr,i)
arr = [1,2,3,4,5]
tong = deQuy(arr,5)
print("Gia tri :",tong)

