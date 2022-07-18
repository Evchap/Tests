'''
Вопрос к задаче №3:
Если ученик заходит на урок одновременно на двух устройствах и
объединение этих списков считать одним списком.

Ответ:
Сравнение piple_time - времени посещения урока учеником с test['answer']:
piple_time: 3225 != 'answer': 3577
'''


test = [
    {'data':
         {'lesson': [1594702800, 1594706400],
          'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                    1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                    1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                    1594706524, 1594706524, 1594706579, 1594706641],
          'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
          },
     'answer': 3577
     }
]


def piple_time():
    pupil = []
    for category in test[0]['data']:
        for elem in test[0]['data'][category]:
            if category == "pupil":
                pupil.append(elem)

    print("pupil = ", pupil) # n
    for elem in range(len(pupil)-1, 1, -2): # (start, stop, step) перебор в обратном порядке

        if pupil[elem-2] > pupil[elem-1]: # если [2]-й больше [1]-го # y
            pupil.pop(elem-2) # y
            pupil.pop(elem-2)  # y
    print("pupil = ", pupil)
    # сравниваем со временем урока, обрезаем концы
    for i in range(1, len(pupil), 1):
        if pupil[i-1] < test[0]['data']['lesson'][0]:
            pupil[i - 1] = test[0]['data']['lesson'][0]
    print("pupil = ", pupil)

    for i in range(len(pupil), 0, -1):
        if pupil[i-1] > test[0]['data']['lesson'][1]:
            pupil[i - 1] = test[0]['data']['lesson'][1]
    print("pupil = ", pupil)


    list_break = []
    list_breaks = []
    time_breaks = 0
    for i in range(2, len(pupil), 2):
        list_break = pupil[i] - pupil[i - 1] # вычитаем [2]-[1]
        list_breaks.append(list_break)
    for i in range(len(list_breaks)):
        time_breaks += int(list_breaks[i]) # сумма всех перерывов
    print('time_breaks = ', time_breaks)

    print('lessong_time = ', test[0]['data']['lesson'][1] - test[0]['data']['lesson'][0])
    print('piple_time = ',test[0]['data']['lesson'][1] - test[0]['data']['lesson'][0] - time_breaks, 'seconds')


def main():
    piple_time()

if __name__ == '__main__':
    main()



