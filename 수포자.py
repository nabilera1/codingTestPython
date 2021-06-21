def solution(answers):
    a=[1,2,3,4,5]*2000
    b=[2,1,2,3,2,4,2,5]*1250
    c=[3,3,1,1,2,2,4,4,5,5]*1000
    a_cnt=0
    b_cnt=0
    c_cnt=0
    ansList=[]
    for i in range(len(answers)):
        if a[i]==answers[i]:
            a_cnt+=1
        if b[i]==answers[i]:
            b_cnt+=1
        if b[i]==answers[i]:
            b_cnt+=1
    ansList.extend([(1,a_cnt),(2,b_cnt),(3,c_c)])
    ansList.sort(key=lambda x:x[1], reverse=True)

    if ansList[0][1]>ansList[1][1]:
        return [ansList[0][0]]
    elif ansList[0][1]==ansList[1][1]:
        return [ansList[0][0],ansList[1][0]]
    elif ansList[0][1]==ansList[1][1] and ansList[1][1]==ansList[2][1]:
        return [ansList[0][0], ansList[1][0],ansList[2][0]]