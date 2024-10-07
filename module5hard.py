import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname is other.nickname

    def get_info(self):
        return self.nickname, self.password


class Video:
    def __init__(self,  title, duration, time_now, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else: print("Пользователь уже зарегистрирован")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video_title in self.videos:
            if video_title.title != args:
                self.videos = video_title

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        for video in self.videos:
            if title in video.title:
                if video.adult_mode == True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                else:
                    for i in video.duration:
                        print(i)
                        time.sleep(1)
                    print('Конец видео')


ur = UrTube()
#v1 = Video('Лучший язык программирования 2024 года', 200)
#v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

v1 = Video('Лучший язык программирования 2024 года', 200, 0)
v2 = Video('Для чего девушкам парень программист?', 10, 0, adult_mode=True)

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
