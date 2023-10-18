# Global list of expenses
expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# Function to display menu
def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

# Function to add expense interactively
def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expenses = expenses + [{'tanggal': date, 'deskripsi': description, 'jumlah': amount}]
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses

# Function to view expenses by date
def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = [expense for expense in expenses if expense['tanggal'] == date]
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")
# Function to view expenses report
def view_expenses_report(expenses):
    report = {}
    for expense in expenses:
        if expense['tanggal'] not in report:
            report[expense['tanggal']] = 0
        report[expense['tanggal']] += expense['jumlah']
    print("\nLaporan Pengeluaran Harian:")
    for date, total in report.items():
        print(f"Total pengeluaran pada {date}: Rp {total}")

# Lambda function to get user input
get_user_input = lambda command: int(input(command))

# Main function
def main(expenses):
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = sum(expense['jumlah'] for expense in expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            break
    return expenses

expenses = main(expenses)
