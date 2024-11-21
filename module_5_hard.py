from time import sleep  #Импорт для функции watch_video


class User: #Класс пользователя

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:    #Класс видео
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class UrTube:   #Класс видеохостинга

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):    #Функция регистрации с проверкой существующих пользователей
        if any(user.nickname == nickname for user in self.users):
            print(f'Пользователь {nickname}, уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = nickname

    def log_in(self, nickname, password):   #Функция входа для зарегестрированных пользователей
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = nickname
            else:
                return 'Неверный логин или пароль'

    def log_out(self):      #Функция выхода из аккаунта
        self.curren_user = False

    def add(self, *videos):     #Функция добавления нового видео, с проверкой существующих
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, title):    #Функция поиска видео среди добавленных
        title = title.lower()
        return [video.title for video in self.videos if title in video.title.lower()]

    def watch_video(self, title):   #Функция просмотра видео с проверкой всех необходимых параметров
        if self.current_user == None:
            print('Войдите в аккаунт чтобы смотреть видео')
        else:
            for video in self.videos:
                video.time_now = 1
                if title == video.title:
                    for user in self.users:
                        if user.age < 18 and video.adult_mode == True and self.current_user == user.nickname:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        if user.age > 18:
                            for sec in range(video.time_now, video.duration +1, 1):
                                print(sec, end=' ')
                                sleep(1)
                            print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
