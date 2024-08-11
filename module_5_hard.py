import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f"User('{self.nickname}', '{self.password}', {self.age})"

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password and self.age == other.age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video('{self.title}', {self.duration}, {self.time_now}, {self.adult_mode})"

    def __repr__(self):
        return f"Video('{self.title}', {self.duration}, {self.time_now}, {self.adult_mode})"

    def __contains__(self, search_word):
        return search_word.lower() in self.title.lower()


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        return f"UrTube(users={self.users}, videos={self.videos}, current_user={self.current_user})"

    def __repr__(self):
        return f"UrTube({self.users}, {self.videos}, {self.current_user})"

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return
        print(f"Пользователь {nickname} не найден")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        return [v.title for v in self.videos if search_word.lower() in v.title.lower()]

    def watch_video(self, title):
        for video in self.videos:
            if video.title == title:
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    return
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                video_progress = ""
                while video.time_now < video.duration:
                    video_progress += f"{video.time_now + 1} "
                    video.time_now += 1
                    time.sleep(1)
                print(video_progress.strip() + " Конец видео")
                video.time_now = 0
                return
        print(f"Видео '{title}' не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
