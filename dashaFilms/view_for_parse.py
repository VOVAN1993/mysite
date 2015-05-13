from django.http import HttpResponse
from dashaFilms import viewsUtil
from dashaFilms.models import Country, Genre
import ast
from dashaFilms.viewsUtil import *


def parseRating(request):
    for i in range(1,11):
        r = Value(values=i)
        r.save()
    return HttpResponse("OK")


def parseCountry(request):
    Country.objects.filter(name="France").update(name_rus="Франция")
    Country.objects.filter(name="Soviet Union").update(name_rus="СССР")
    Country.objects.filter(name="USA").update(name_rus="США")
    Country.objects.filter(name="Germany").update(name_rus="Германия")
    Country.objects.filter(name="North Korea").update(name_rus="Северная Корея")
    Country.objects.filter(name="Switzerland").update(name_rus="Швейцария")
    Country.objects.filter(name="Austria").update(name_rus="Австрия")
    Country.objects.filter(name="Sweden").update(name_rus="Швеция")
    Country.objects.filter(name="Denmark").update(name_rus="Дания")
    Country.objects.filter(name="Finland").update(name_rus="Финляндия")
    Country.objects.filter(name="Norway").update(name_rus="Норвегия")
    Country.objects.filter(name="Hong Kong").update(name_rus="Гонк Конг")
    Country.objects.filter(name="South Korea").update(name_rus="Южная Корея")
    Country.objects.filter(name="Canada").update(name_rus="Канада")
    Country.objects.filter(name="UK").update(name_rus="Великобритания")
    Country.objects.filter(name="Italy").update(name_rus="Италия")
    Country.objects.filter(name="Japan").update(name_rus="Япония")
    Country.objects.filter(name="Bulgaria").update(name_rus="Болгария")
    Country.objects.filter(name="Netherlands").update(name_rus="Голландия")
    Country.objects.filter(name="Australia").update(name_rus="Австралия")
    Country.objects.filter(name="Spain").update(name_rus="Испания")
    Country.objects.filter(name="South Africa").update(name_rus="ЮАР")
    Country.objects.filter(name="Mexico").update(name_rus="Мексика")
    Country.objects.filter(name="Russia").update(name_rus="Россия")
    Country.objects.filter(name="Taiwan").update(name_rus="Тайвань")
    Country.objects.filter(name="China").update(name_rus="Китания")
    Country.objects.filter(name="Uzbekistan").update(name_rus="Узбекистан")
    Country.objects.filter(name="Poland").update(name_rus="Польша")
    Country.objects.filter(name="Czechoslovakia").update(name_rus="Чехословакия")
    Country.objects.filter(name="West Germany").update(name_rus="Восточная Германия")
    Country.objects.filter(name="New Zealand").update(name_rus="Новая Зеландия")
    Country.objects.filter(name="India").update(name_rus="Индия")
    Country.objects.filter(name="Greece").update(name_rus="Греция")
    Country.objects.filter(name="Brazil").update(name_rus="Бразилия")
    Country.objects.filter(name="Portugal").update(name_rus="Португалия")
    Country.objects.filter(name="Luxembourg").update(name_rus="Люксембург")
    Country.objects.filter(name="Belarus").update(name_rus="Беларуссия")
    Country.objects.filter(name="Iceland").update(name_rus="Исландия")
    Country.objects.filter(name="United Arab Emirates").update(name_rus="ОАЭ")
    Country.objects.filter(name="Colombia").update(name_rus="Колумбия")
    Country.objects.filter(name="Liechtenstein").update(name_rus="Лихтенштейн")
    Country.objects.filter(name="Israel").update(name_rus="Израиль")
    Country.objects.filter(name="Iran").update(name_rus="Иран")
    Country.objects.filter(name="Egypt").update(name_rus="Египет")
    Country.objects.filter(name="Ireland").update(name_rus="Ирландия")
    Country.objects.filter(name="Tunisia").update(name_rus="Тунис")
    Country.objects.filter(name="Latvia").update(name_rus="Латвия")
    Country.objects.filter(name="Hungary").update(name_rus="Венгрия")
    Country.objects.filter(name="Belgium").update(name_rus="Бельгия")
    Country.objects.filter(name="Panama").update(name_rus="Панама")
    Country.objects.filter(name="Philippines").update(name_rus="Филлипины")
    Country.objects.filter(name="Turkey").update(name_rus="Турция")
    Country.objects.filter(name="Yugoslavia").update(name_rus="Югославия")
    Country.objects.filter(name="Ukraine").update(name_rus="Украина")
    Country.objects.filter(name="Czech Republic").update(name_rus="Чехия")
    Country.objects.filter(name="Republic of Macedonia").update(name_rus="Македония")
    Country.objects.filter(name="Kazakhstan").update(name_rus="Казахстан")
    Country.objects.filter(name="Singapore").update(name_rus="Сингапур")
    Country.objects.filter(name="Venezuela").update(name_rus="Венесуэла")
    Country.objects.filter(name="Croatia").update(name_rus="Хроватия")
    Country.objects.filter(name="Kenya").update(name_rus="Кения")
    Country.objects.filter(name="Peru").update(name_rus="Перу")
    Country.objects.filter(name="Algeria").update(name_rus="Алжир")
    Country.objects.filter(name="Dominican Republic").update(name_rus="Доминиканская Республика")
    Country.objects.filter(name="East Germany").update(name_rus="Западная Германия")
    Country.objects.filter(name="Argentina").update(name_rus="Аргентина")
    Country.objects.filter(name="Serbia and Montenegro").update(name_rus="Сербия и Черногория")
    Country.objects.filter(name="Bahamas").update(name_rus="Багамы")
    Country.objects.filter(name="Cuba").update(name_rus="Куба")
    Country.objects.filter(name="Georgia").update(name_rus="Грузия")
    Country.objects.filter(name="Romania").update(name_rus="Румыния")
    Country.objects.filter(name="Indonesia").update(name_rus="Индонезия")
    Country.objects.filter(name="Chile").update(name_rus="Чили")
    Country.objects.filter(name="Bosnia and Herzegovina").update(name_rus="Босния и Герцоговина")
    Country.objects.filter(name="Mali").update(name_rus="Мали")
    Country.objects.filter(name="Thailand").update(name_rus="Тайланд")
    Country.objects.filter(name="Jamaica").update(name_rus="Ямайка")
    Country.objects.filter(name="Cayman Islands").update(name_rus="Каймановы Острова")
    Country.objects.filter(name="Vietnam").update(name_rus="Вьетнам")
    Country.objects.filter(name="Morocco").update(name_rus="Морокко")
    Country.objects.filter(name="Lithuania").update(name_rus="Литва")
    Country.objects.filter(name="Lebanon").update(name_rus="Ливан")
    return HttpResponse("hello")


def parseGenre(request):
    Genre.objects.filter(name="Comedy").update(name_rus="Комедия")
    Genre.objects.filter(name="Drama").update(name_rus="Драма")
    Genre.objects.filter(name="Action").update(name_rus="Боевик")
    Genre.objects.filter(name="Horror").update(name_rus="Ужас")
    Genre.objects.filter(name="War").update(name_rus="Военный")
    Genre.objects.filter(name="Sci-Fi").update(name_rus="Научный")
    Genre.objects.filter(name="Family").update(name_rus="Семейный")
    Genre.objects.filter(name="Fantasy").update(name_rus="Фэнтэзи")
    Genre.objects.filter(name="Romance").update(name_rus="Романтичный")
    Genre.objects.filter(name="Adventure").update(name_rus="Приключение")
    Genre.objects.filter(name="Biography").update(name_rus="Биографический")
    Genre.objects.filter(name="Animation").update(name_rus="Аниме")
    Genre.objects.filter(name="Western").update(name_rus="Вестерн")
    Genre.objects.filter(name="Sport").update(name_rus="Спорт")
    Genre.objects.filter(name="Crime").update(name_rus="Криминал")
    Genre.objects.filter(name="Music").update(name_rus="Музыка")
    Genre.objects.filter(name="Mystery").update(name_rus="Мистика")
    Genre.objects.filter(name="Documentary").update(name_rus="Документальный")
    Genre.objects.filter(name="Short").update(name_rus="Короткометражный")
    Genre.objects.filter(name="Adult").update(name_rus="Фильм для взрослых")
    Genre.objects.filter(name="History").update(name_rus="Исторический")
    Genre.objects.filter(name="Film-Noir").update(name_rus="Нуар")
    Genre.objects.filter(name="Musical").update(name_rus="Мюзикл")
    Genre.objects.filter(name="News").update(name_rus="Новости")
    Genre.objects.filter(name="Game-Show").update(name_rus="Игра")
    Genre.objects.filter(name="Reality-TV").update(name_rus="Реалити-шоу")
    return HttpResponse("hello")

def parse(request):
    with open("./round2/norm2.txt") as f:
        contents = f.readlines()
    arr = []
    for line in contents:
        dict = ast.literal_eval(line)
        genres = dict['Genre'].split(",")
        directors = dict['Director'].split(",")
        actors = dict['Actors'].split(",")
        countries = dict['Country'].split(",")
        dbGenres = getGenres(genres)
        dbActors = getActors(actors)
        dbDirectors = getDirectors(directors)
        dbCountries = getCountries(countries)
        dbName = dict['Title']
        dbName_rus = None if dict['rus_name'] == '' else dict['rus_name']
        dbTitle = None if dict['Plot'] == ''else dict['Plot']
        dbImdbID = None if dict['imdbID'] == '' or dict['imdbID'] == 'N/A' else dict['imdbID']
        dbTitle_rus = None if dict['rus_title'] == '' else dict['rus_title']
        dbTime = None if dict['Runtime'] == '' else dict['Runtime']
        dbYear = None if dict['Year'] == '' else dict['Year']
        dbPoster_link = None if dict['Poster'] == '' else dict['Poster']
        dbImbdRating = None if dict['imdbRating'] == '' or dict['imdbRating'] == 'N/A' else dict['imdbRating']

        createFilm(dbName, dbName_rus, dbTitle, dbTitle_rus, dbTime, dbYear, dbImbdRating, dbImdbID, dbPoster_link,
                   dbGenres, dbActors,
                   dbDirectors, dbCountries)
        arr.append(dbName)
        print(dbName)

    return HttpResponse(arr)
