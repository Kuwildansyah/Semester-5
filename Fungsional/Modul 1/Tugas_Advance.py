# Daftar buku yang tersedia
available_books = ['Buku Mujarab Ala Tatang Soetarman', 'kamus bahasa china', 'Cara Mendapatkan pacar cina']
# Daftar buku yang sedang dipinjam
borrowed_books = {}


def display_available_books():
    print("Buku yang tersedia:")
    for i, book in enumerate(available_books):
        print(i+1, book)
    print("\nBuku yang sedang dipinjam:")
    for user in borrowed_books:
        for book in borrowed_books[user]:
            print(book, '(dipinjam oleh "' + user + '")')

def lend_book(requested_book, user):
    if requested_book in available_books:
        print('Anda telah meminjam buku', requested_book)
        available_books.remove(requested_book)
        if user in borrowed_books:
            borrowed_books[user].append(requested_book)
        else:
            borrowed_books[user] = [requested_book]
    else: 
        print('Maaf, buku', requested_book, 'tidak tersedia')

def add_book(returned_book, user):
    if user in borrowed_books and returned_book in borrowed_books[user]:
        available_books.append(returned_book)
        print('Anda telah mengembalikan buku', returned_book)
        borrowed_books[user].remove(returned_book)
    else:
        print('Anda tidak meminjam buku', returned_book)

def request_book():
    display_available_books()
    print('Masukkan nomor buku yang ingin Anda pinjam:')
    book_number = int(input())
    if book_number > 0 and book_number <= len(available_books):
        return available_books[book_number-1]
    else:
        print('Nomor buku tidak valid.')
    return None

def return_book(user):
    if user in borrowed_books and len(borrowed_books[user]) > 0:
        print('Anda sedang meminjam buku-buku berikut:')
        for i, book in enumerate(borrowed_books[user]):
            print(i+1, book)
        print('Masukkan nomor buku yang ingin Anda kembalikan:')
        book_number = int(input())
        if book_number > 0 and book_number <= len(borrowed_books[user]):
            return borrowed_books[user][book_number-1]
    else:
        print('Anda tidak sedang meminjam buku apa pun.')
    return None

def add_new_book(new_book):
    available_books.append(new_book)
    print("Buku", new_book, "telah ditambahkan.")

def main(username):
    done = False
    while done == False:
        print('\n==== Menu ====')
        print('1. Tampilkan buku')
        print('2. Pinjam buku')
        print('3. Kembalikan buku')
        print('4. Tambahkan buku')
        print('5. Hapus buku')
        print('6. Logout')
        choice = int(input('Masukkan pilihan Anda:'))
        if choice == 1:
            display_available_books()
        elif choice == 2:
            requested_book = request_book()
            if requested_book is not None:
                lend_book(requested_book, username)
        elif choice == 3:
            returned_book = return_book(username)
            if returned_book is not None:
                add_new_book(returned_book)
        elif choice == 4:
            new_book = input("Masukkan nama buku yang ingin ditambahkan: ")
            add_new_book(new_book)
        elif choice == 5:
            removed_book = input("Masukkan nama buku yang ingin dihapus: ")
            if removed_book in available_books:
                available_books.remove(removed_book)
                print("Buku", removed_book, "telah dihapus.")
            else:
                print("Buku", removed_book, "tidak ditemukan.")
        elif choice == 6:
          done = True

users = {'admin': 'admin', 'user': 'cuy'}

def login():
    global username
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in users and users[username] == password:
        print("Login berhasil!")
        if username == 'admin':
            main(username)  # Admin dapat mengakses semua fungsi
        else:
            # Pengguna hanya dapat meminjam dan mengembalikan buku
            done = False
            while done == False:
                print('\n==== Menu ====')
                print('1. Pinjam buku')
                print('2. Kembalikan buku')
                print('3. Logout')
                choice = int(input('Masukkan pilihan Anda:'))
                if choice == 1:
                    requested_book = request_book()
                    if requested_book is not None:
                        lend_book(requested_book, username)
                elif choice == 2:
                    returned_book = return_book(username)
                    if returned_book is not None:
                        add_new_book(returned_book)
                elif choice == 3:
                  done = True

while True: # Loop untuk kembali ke halaman login setelah logout
    login()
