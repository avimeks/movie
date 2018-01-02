import fresh_tomatoes
import media


nanumrowdythan = media.Movie("nanum rowdy than", "A story of the Gangster", "https://upload.wikimedia.org/wikipedia/en/3/39/Naanum_Rowdy_Dhaan_poster.jpg", "https://www.youtube.com/watch?v=6Fj_fzW_BOo")
sethupathi = media.Movie("sethupathi", "Body builder story", "https://upload.wikimedia.org/wikipedia/en/a/a1/Sethupathi-Tamil_film_poster.jpeg", "https://www.youtube.com/watch?v=dK5E8mzmD6w")
karuppan = media.Movie("karuppan ", "jallikattu story", "http://t1.gstatic.com/images?q=tbn:ANd9GcQSjGV6mIXgugYVDvE65sVQ-AbdZveij2u34HxfFULwlheCcjx6", "https://www.youtube.com/watch?v=GCdPpqld_tQ")
mersal = media.Movie("mersal ", "agriculture story", "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Mersal_Theatrical_Release_Poster.jpg/220px-Mersal_Theatrical_Release_Poster.jpg ", "https://www.youtube.com/watch?v=gQDo5QuZTaw")
achamenbathumadamaiyada = media.Movie("acham enbathu madamaiyada ", "police story", "https://upload.wikimedia.org/wikipedia/en/6/64/Achcham_Yenbadhu_Madamaiyada.jpg", "https://www.youtube.com/watch?v=7Oz-8Vj_JfY")
movies = [nanumrowdythan, sethupathi, karuppan, mersal, achamenbathumadamaiyada]
fresh_tomatoes.open_movies_page(movies)