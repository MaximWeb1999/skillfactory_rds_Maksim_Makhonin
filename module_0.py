import numpy as np


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)   # Фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print('Ваш алгоритм угадывает число в среднем за {} попыток'.format(score))
    return score


def game_core_v3(number):
    """count - счетчик попыток
    start и end - диапазон чисел, в которых находится загаданное число.
    predict - середина числа между start и end
    Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    start = 0
    end = 101
    predict = (start + end) // 2
    while number != predict:
        count += 1
        if number > predict:
            start = predict
            predict = (start + end) // 2
        elif number < predict:
            end = predict
            predict = (start + end) // 2
    return count    # Выход из цикла, если угадали


#   Запуск
score_game(game_core_v3)
