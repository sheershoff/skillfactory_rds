import numpy as np

number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return (count)  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # выход из цикла, если угадали


def game_core_v3(number):
    '''Воспользуемся бинарным поиском - начнём искать от середины возможного отрезка, затем будем делить отрезки пополам
       в нужную сторону.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    low = 1
    high = 100
    predict = 50
    while number != predict:
        count += 1
        if number > predict:
            low = predict
            # Нужно брать ceil чтобы уйти в сторону максимума, иначе можем застрять под максимальным числом
            predict = np.ceil((low + high) / 2)
        elif number < predict:
            high = predict
            predict = np.floor((low + high) / 2)
    return count  # Выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

# запускаем
score_game(game_core_v1)

score_game(game_core_v2)

score_game(game_core_v3)
