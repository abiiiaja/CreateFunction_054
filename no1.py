def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        print("Salah ketik unit suhu ANDA, harus antara 'C' dan 'F'")

input_value = float(input("Masukkan nilai suhu: "))
input_unit = input("Masukkan unit suhu: ")
konversi = convert_temperature(input_value, input_unit)
if input_unit.upper() == 'C':
    print(f"{input_value}°C = {konversi:.2f}°F")
elif input_unit.upper() == 'F':
    print(f"{input_value}°F = {konversi:.2f}°C")
else:
    print("Satuan tidak dikenal")