# Project #1
# Developer:  Daniel Alina.

# Мария Иванова решила заняться своим здоровьем и перейти на правильное питание.
# Напишите программу, которая поможет девушке составить правильный рацион питания.
# Программа получает на вход рост (в сантиметрах), вес (в килограммах), возраст, пол.
# Результатом работы программы является вывод индекса массы тела и его анализ,
# расчёт "идеального веса", расчёт базового обмена веществ,
# расчёт суточной нормы калорий с учётом уровня физической активности
# (для поддержания веса, здорового профицита и дефицита каллорий),
# распредение белков, жиров и углеводов в рационе.
# Программа должна выводить в ответе один знак после десятичной точки для значений веса в килограммах,
# два знака - для значения ИМТ, все остальные значения - натуральные числа.

height = int(input('Введите свой рост: '))
weight = float(input('Введите свой вес: '))
age = int(input('Введите свой возраст: '))
sex = input('Введите свой пол (муж/жен): ')
activity = input('''Оцените уровень своей физической активности от 1 до 5, где: 
1 - Практически нет физической нагрузки;
2 - Легкая физическая нагрузка (занятия спортом или физической работой 2-3 раза в неделю или т.п.);
3 - Умеренные физические нагрузки (3-5 дней в неделю);
4 - Тяжелые физические нагрузки (6-7 дней в неделю);
5 - Очень тяжелые физические нагрузки (дополнительные тренировки перед соревнованиями по два раза в день или т.п.)
''')

# Calculation of body mass index.
imt = weight / ((height / 100) ** 2)
print('Индекс массы тела по А. Кетле:', round(imt, 2))

# Analysis of body mass index.
if imt < 16:
    print('У вас выраженный дефицит массы тела.')
if 16 <= imt < 18.5:
    print('У вас недостаточная масса тела.')
if 18.5 <= imt < 25:
    print('У вас нормальная масса тела.')
if 25 <= imt < 30:
    print('У вас избыточная масса тела (предожирение).')
if 30 <= imt < 35:
    print('У вас ожирение 1-ой степени.')
if 35 <= imt < 40:
    print('У вас ожирение 2-ой степени.')
if imt >= 40:
    print('У вас ожирение 3-ой степени.')

# Calculation of basic metabolism for men.
a = ((10 * weight) + (6.25 * height) - (5 * age) + 5)
# Calculation of basic metabolism for women.
b = ((10 * weight) + (6.25 * height) - (5 * age) - 161)

if sex == 'жен':
    bmr = b
    perfectweightl = (height - 100) - (height - 150) / 2
    perfectweight = (height - 110) * 1.15
    # Calculation of "perfect weight" for women.
    print('Ваш идельный вес по формуле Брока:', round(perfectweight, 2))
    print('Ваш идеальный вес по формуле Лоренца:', perfectweightl)
if sex == 'муж':
    bmr = a
    # Calculation of "perfect weight" for men.
    perfectweight = (height - 100) * 1.15
    print('Ваш идельный вес по формуле Брока:', round(perfectweight, 2))
    print('Вес по формуле Лоренца рассчитывается только для женщин.')

print('Норма потребляемых каллорий (базовый обмен веществ) по Маффину-Джеору '
      '(физическая активность не учтена):', round(bmr))
# Analysis of physical activity level and calculation of needed intake.
if activity == '1':
    bmr1 = bmr * 1.2
if activity == '2':
    bmr1 = bmr * 1.375
if activity == '3':
    bmr1 = bmr * 1.55
if activity == '4':
    bmr1 = bmr * 1.725
if activity == '5':
    bmr1 = bmr * 1.9
print('Норма каллорий с учётом физической активности:', round(bmr1))
# Intake for weight gain.
weightgain1 = int(bmr1 * 1.15)
weightgain2 = int(bmr1 * 1.2)
print('Для набора вам веса нужно потреблять:', weightgain1, '-',
      weightgain2, 'калорий.')
# Intake for losing weight.
diet1 = int(bmr1 * 0.85)
diet2 = int(bmr1 * 0.9)
print('Для похудения вам нужно придеживаться:', diet1, '-', diet2, 'калорий.')
# Calculation of protein, fats and carbohydrates in a healthy ration.
protein1 = int(weight * 1.5)
protein2 = int(weight * 2.5)
fats1 = int(weight)
fats2 = int(weight * 2)
carbohydrates1 = int(weight * 2)
carbohydrates2 = int(weight * 3)
carbohydrates3 = int(weight * 4)
carbohydrates4 = int(weight * 7)
carbohydrates5 = int(weight * 8)
carbohydrates6 = int(weight * 9)
print('Для поддержания здорового образа жизни вам рекомендуется потреблять:',
      '\n', protein1, '-', protein2, 'грамм белкoв;', '\n', fats1, '-', fats2,
      'грамм жиров;', '\n', carbohydrates3, '-', carbohydrates4,
      'грамм углеводов для поддержания веса.', '\n',
      'Для набора массы тела количество потребляемых углеводов можно увеличить до',
      carbohydrates5, '-', carbohydrates6, 'грамм.', '\n',
      'Для похудения углеводы следует ограничить до', carbohydrates1,
      '-', carbohydrates2, 'грамм.')
