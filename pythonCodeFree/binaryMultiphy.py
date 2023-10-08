def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# Nhập hai dãy số nhị phân
binary1 = input("Nhập dãy số nhị phân thứ n1hất: ")
binary2 = input("Nhập dãy số nhị phân thứ hai: ")

# Chuyển đổi sang hệ thập phân, nhân, và chuyển lại thành nhị phân
decimal1 = binary_to_decimal(binary1)
decimal2 = binary_to_decimal(binary2)
result_decimal = decimal1 * decimal2
result_binary = decimal_to_binary(result_decimal)

print("Kết quả nhân hai dãy số nhị phân:", result_binary)
