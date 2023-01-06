def percentage(student_marks,query_name):
    total = 0
    for i in range(len(student_marks[query_name])):
       total = total + student_marks[query_name][i] #adding marks of query name
    avg = total /len(student_marks[query_name])
    return  avg

#print(percentage(student_marks={'harsh': [25, 26.5, 28], 'Anurag': [26, 28, 30]},query_name='harsh'))