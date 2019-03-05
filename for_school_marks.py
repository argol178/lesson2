school_grades = [{'school_class': '4a', 'scores': [2,4,4,5,2]},{'school_class': '5b', 'scores': [4,3,5,4,4]},
                {'school_class': '8v', 'scores': [1,4,3,4,4]}, {'school_class': '10c', 'scores': [5,2,4,3,3]}]

sum_school_grades = 0

for i in school_grades:
        for j in i['scores']:
                sum_school_grades += j

avg_school = sum_school_grades/len(school_grades)/len(i['scores'])

print('Средний балл по всей школе составляет {}'.format(avg_school))


for k in school_grades:
    sum_class_grades = 0
    for l in k['scores']:
        c = k['school_class']
        sum_class_grades += l

        avg_grades = sum_class_grades/len(k['scores'])
    
    print('Средний балл по {} классу составляет {}'.format(k['school_class'], avg_grades))