def kalkulator():
    try:
        # Input angka
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        # Input operator
        operator = input("Masukkan operator (+, -, *, /): ")

        # Proses perhitungan
        if operator == "+":
            hasil = a + b
        elif operator == "-":
            hasil = a - b
        elif operator == "*":
            hasil = a * b
        elif operator == "/":
            hasil = a / b  # ZeroDivisionError akan ditangani otomatis
        else:
            # Operator tidak valid
            raise Exception("Operator tidak valid! Gunakan +, -, *, atau /")

        print(f"Hasil: {hasil}")

    except ValueError:
        print("Error: Input harus berupa angka!")
    except ZeroDivisionError:
        print("Error: Tidak boleh membagi dengan nol!")
    except Exception as e:
        print(f"Error: {e}")


# Jalankan program
kalkulator()
