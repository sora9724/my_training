class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    time_now = 0
    adult_mode = False

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class UrTube:
    users = []
    videos = []
    curren_user = User

    def log_in(self, nickname, password):
        if nickname == self.users:
            self.curren_user = nickname

    def register(self, nickname, password, age):
        if nickname != self.users[nickname]:
            self.users.append(nickname)
            self.curren_user = nickname
        if nickname == self.users:
            print(f'Пользователь {nickname}, уже существует')

    def log_out(self):
        self.curren_user = None

    def add(self, other):
        pass

    def get_video(self):
        pass

    def watch_video(self):
        pass
