def weight_score(weight, max_score, score):
    result = 0
    
    for i in range(0,len(max_score)):
        if weight:
            result += ((score[i]/max_score[i])*weight[i])
        else:
            result += ((score[i]/max_score[i])*(100/len(max_score)))

    print(f"Final weighted score is {result:.2f}")


weight = list(map(int, input("weights =").split()))
max_score = list(map(int, input("max_scores =").split()))
score = list(map(int, input("scores =").split()))
weight_score(weight, max_score, score)



