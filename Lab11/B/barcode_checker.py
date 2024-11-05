def isValid(barcode):
    oddSum = sum(int(barcode[i]) for i in range(0, 12, 2))
    evenSum = sum(int(barcode[i]) for i in range(1, 12, 2)) * 3
    check_digit = (10 - (oddSum + evenSum) % 10)
    return check_digit == int(barcode[-1])

with open("barcodes.txt", 'r') as file:
    barcodes = file.read().splitlines()

validBarcodes = [barcode for barcode in barcodes if isValid(barcode)]

with open('valid_barcodes.txt', 'w') as output_file:
    for barcode in validBarcodes:
        output_file.write(barcode + '\n')

print(f"Counted {len(validBarcodes)} valid barcodes. Saved to valid_barcodes.txt.")
