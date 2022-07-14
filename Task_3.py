'''
Задача №3.
Когда пользователь заходит на страницу урока, мы сохраняем время его захода.
Когда пользователь выходит с урока (или закрывает вкладку,
браузер – в общем как-то разрывает соединение с сервером),
мы фиксируем время выхода с урока.
Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов.
В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):

lesson – начало и конец урока
pupil – интервалы присутствия ученика
tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного количества элементов.
Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами
и возвращает время общего присутствия ученика и учителя на уроке (в секундах).
'''

import intervals

# pip install python-intervals

def check_in_range(timestump, ranges):
    for timedelta in ranges:
        if timestump in timedelta:
            return True


def make_ranges(intervals):
    range_list = []
    for i in range(1, len(intervals), 2):
        range_list.append(range(intervals[i - 1], intervals[i] + 1))
    # print("'range_list':", range_list)
    return range_list


def appearance(intervals):
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    lesson_range = range(lesson[0], lesson[1] + 1)
    pupil_ranges = make_ranges(pupil)
    tutor_ranges = make_ranges(tutor)
    intervals_list = []
    check_list = []
    check_list += lesson
    check_list += pupil
    check_list += tutor
    for timestump in check_list:
        if timestump in lesson_range:
            pupil_result = check_in_range(timestump, pupil_ranges)
            tutor_result = check_in_range(timestump, tutor_ranges)
            if pupil_result == True and tutor_result == True:
                intervals_list.append(timestump)
    intervals_list.sort()
    time = 0
    for i in range(1, len(intervals_list), 2):
        delta = intervals_list[i] - intervals_list[i - 1]
        time += delta
    print("time = ", time)
    return time


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer':
         3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    # ЭТОТ ТЕСТ НЕ ПРОХОДИТ
    # Возможно ли, что task['data']['pupil'][1] - время 1-го выхода с урока больше,
    #              чем task['data']['pupil'][2] - время 2-го входа на урок?
    #              'pupil'[7] > 'pupil'[8] и т.д.



    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
