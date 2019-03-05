school_marks = [{'school_class': '4a', 'scores': [2,4,4,5,2]},{'school_class': '5b', 'scores': [4,3,5,4,4]},
                {'school_class': '8v', 'scores': [1,4,3,4,4]}]

a = []
b = []

average_school = 0

for i in school_marks:
    #if 'scores' in i:
        a += i['scores']
for j in a:
    average_school += j

print('Средний балл по всей школе составляет {}'.format(average_school/len(a)))

for k in school_marks:
    b = k['scores']
    average_class = 0
    for l in b:
        average_class += l

    print('Средний балл по классу составляет {}'.format(average_class/len(b)))