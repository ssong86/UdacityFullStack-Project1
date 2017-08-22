# Project 1, Movie Trailer Website
import media
import fresh_tomatoes

spider_man1 = media.Movie(
  "Spider Man 1", "A story of spider man, first film",
  "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg", 
  "https://youtu.be/TYMMOjBUPMM")
spider_man2 = media.Movie(
  "Spider Man 2", "A story of spider man, second film",
  "https://upload.wikimedia.org/wikipedia/"
  "en/0/02/Spider-Man_2_Poster.jpg",
  "https://youtu.be/3jBFwltrxJw")
spider_man3 = media.Movie(
  "Spider Man 3", "A story of spider man, third",
  "https://upload.wikimedia.org/wikipedia/"
  "en/7/7a/Spider-Man_3%2C_International_Poster.jpg",
  "https://youtu.be/PCmMLfXdURs")
spider_man_reboot1 = media.Movie(
  "Amazing Spider Man 1", "Reboot of spider man, first film",
  "https://upload.wikimedia.org/wikipedia/en/0/02/"
  "The_Amazing_Spider-Man_theatrical_poster.jpeg",
  "https://youtu.be/uAcD7H53220")
spider_man_reboot2 = media.Movie(
  "Amazing Spider Man 2", "Reboot of spider man, second film",
  "https://upload.wikimedia.org/wikipedia/en/0/02/"
  "The_Amazing_Spiderman_2_poster.jpg",
  "https://youtu.be/DlM2CWNTQ84")
spider_man_homecoming = media.Movie(
  "Spider Man: Homecoming", 
  "New story of spider man",
  "https://upload.wikimedia.org/wikipedia/en/f/f9/"
  "Spider-Man_Homecoming_poster.jpg",
  "https://youtu.be/U0D3AOldjMU")

my_movies = [spider_man1, spider_man2, spider_man3,
             spider_man_reboot1, spider_man_reboot2,
             spider_man_homecoming]
fresh_tomatoes.open_movies_page(my_movies)
