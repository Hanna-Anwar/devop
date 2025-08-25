movies = [
    # Malayalam
    {"title": "Drishyam", "director": "Jeethu Joseph", "language": "Malayalam", "year": 2013, "genre": "Thriller"},
    {"title": "Bangalore Days", "director": "Anjali Menon", "language": "Malayalam", "year": 2014, "genre": "Drama"},
    {"title": "Premam", "director": "Alphonse Puthren", "language": "Malayalam", "year": 2015, "genre": "Romance"},
    {"title": "Kumbalangi Nights", "director": "Madhu C. Narayanan", "language": "Malayalam", "year": 2019, "genre": "Family"},

    # Tamil
    {"title": "Soorarai Pottru", "director": "Sudha Kongara", "language": "Tamil", "year": 2020, "genre": "Drama"},
    {"title": "Vikram Vedha", "director": "Pushkar-Gayathri", "language": "Tamil", "year": 2017, "genre": "Crime"},
    {"title": "Master", "director": "Lokesh Kanagaraj", "language": "Tamil", "year": 2021, "genre": "Action"},
    {"title": "Kaithi", "director": "Lokesh Kanagaraj", "language": "Tamil", "year": 2019, "genre": "Action"},

    # Telugu
    {"title": "Magadheera", "director": "S. S. Rajamouli", "language": "Telugu", "year": 2009, "genre": "Fantasy"},
    {"title": "Arjun Reddy", "director": "Sandeep Reddy Vanga", "language": "Telugu", "year": 2017, "genre": "Romance"},
    {"title": "Eega", "director": "S. S. Rajamouli", "language": "Telugu", "year": 2012, "genre": "Fantasy"},
    {"title": "Pushpa: The Rise", "director": "Sukumar", "language": "Telugu", "year": 2021, "genre": "Action"},

    # Hindi
    {"title": "3 Idiots", "director": "Rajkumar Hirani", "language": "Hindi", "year": 2009, "genre": "Comedy"},
    {"title": "Dangal", "director": "Nitesh Tiwari", "language": "Hindi", "year": 2016, "genre": "Sports"},
    {"title": "Gully Boy", "director": "Zoya Akhtar", "language": "Hindi", "year": 2019, "genre": "Musical"},
    {"title": "Chak De! India", "director": "Shimit Amin", "language": "Hindi", "year": 2007, "genre": "Sports"}
]

#print all movie names

all_movie_names = [m.get("title") for m in movies]

print(all_movie_names)
 
malayalam_movies =[m.get("title") for m in movies if m.get("language").lower()=="malayalam"]

print(malayalam_movies)

#in which year most of the movies released

year_list = [y.get("year") for y in movies]

print(year_list)  

# 2013, 2014, 2015, 2019, 2020, 2017, 2021, 2019, 2009, 2017, 2012, 2021, 2009, 2016, 2019, 2007]

year_count = {yr:year_list.count(yr) for yr in year_list}

print(year_count)

# {2013: 1, 2014: 1, 2015: 1, 2019: 3, 2020: 1, 2017: 2, 2021: 2, 2009: 2, 2012: 1, 2016: 1, 2007: 1}

srt_year =sorted(year_count,key = year_count.get,reverse=True)

print(srt_year)

#[2019, 2017, 2021, 2009, 2013, 2014, 2015, 2020, 2012, 2016, 2007]

print(srt_year[0])

#2019