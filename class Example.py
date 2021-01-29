class movies:
    '''Class example'''
    def __init__(self,movie,hero):
        self.movie = movie
        self.hero = hero
    def info(self):
        print('movie name: ',self.movie)
        print('hero name: ',self.hero)
if __name__ == '__main__':
    listofmovie =[]
    while True:
        movie = input('Enter a movie name: ')
        hero = input('Enter a hero name: ')
        m = movies(movie,hero)
        listofmovie.append(m)
        print('added')
        option = input('Enter a option yes | no: ')
        if option == 'no':
            break
    print("all movies")
    for movie in listofmovie:
        movie.info()
        print()