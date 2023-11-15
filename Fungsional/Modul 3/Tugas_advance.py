from functools import reduce

# Data film
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"}, 
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"}, 
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"}, 
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"}, 
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Fungsi untuk menampilkan data film
def show_movie(title):
    movie = list(filter(lambda x: x['title'] == title, movies))
    if movie:
        return f"Judul: {movie[0]['title']}\nTahun Rilis: {movie[0]['year']}\nGenre: {movie[0]['genre']}\nRating: {movie[0]['rating']}"
    else:
        return 'Film tidak ditemukan'
        


# Fungsi untuk menghitung jumlah film berdasarkan genre
def count_movies_by_genre(genre):
    count = len(list(filter(lambda x: x['genre'] == genre, movies)))
    return f"\nJumlah film dengan genre {genre}: {count}\n"


# Fungsi untuk menghitung rata-rata rating film berdasarkan tahun rilis
from functools import reduce

def avg_rating_by_year(year):
    movies_by_year = list(filter(lambda x: x['year'] == year, movies))
    
    if movies_by_year:
        total_rating = reduce(lambda a, b: a + b['rating'], movies_by_year, 0)
        average_rating = total_rating / len(movies_by_year)
        return f"Rata-rata rating film yang dirilis pada tahun {year}: {average_rating:.2f}"
    else:
        return f"\nTidak ada film yang dirilis pada tahun {year}\n"


# Fungsi untuk menampilkan film dengan rating tertinggi
def highest_rated_movie():
    best_movie = max(movies, key=lambda x: x['rating'])
    movie_title = best_movie['title']
    movie_rating = best_movie['rating']
    return f"Film dengan rating tertinggi :'{movie_title}' dengan skor rating :{movie_rating}."


while True:
    print("Pilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    
    task = int(input("Masukkan nomor tugas (1/2/3/4/5): "))
    
    if task == 1:
        genre = input("Masukkan genre: ")
        print(count_movies_by_genre(genre))
    elif task == 2:
        year = int(input("Masukkan tahun: "))
        print(avg_rating_by_year(year))
    elif task == 3:
        print(highest_rated_movie())
    elif task == 4:
        title = input("Masukkan judul film: ")
        print(show_movie(title))
    elif task == 5:
        break