school_marks = [{'school_class': '4a', 'scores': [2,4,4,5,2]},{'school_class': '5b', 'scores': [4,3,5,4,4]}]
scores_sum1 = 0
scores_sum2 = 0

for i in school_marks[0]['scores']:
    scores_sum1 += i

average1 = scores_sum1 / len(school_marks[0]['scores'])

for i in school_marks[1]['scores']:
    scores_sum2 += i

average2 = scores_sum2 / len(school_marks[1]['scores'])

print('Средний балл по всей школе составляет {}'.format((average1+average2)/2))

print('Средний балл в 4А составляет {}'.format(average1))

print('Средний балл в 5Б составляет {}'.format(average2))