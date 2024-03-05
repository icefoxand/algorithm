def solution(answers):
    string_ans = ''.join(str(answer) for answer in answers)
    st1, st2, st3 = '12345', '21232425', '3311224455'

    scores = [0,0,0]
    for i in range(len(string_ans)):

        if string_ans[i] == st1[i % len(st1)]:
            scores[0] += 1
        if string_ans[i] == st2[i % len(st2)]:
            scores[1] += 1
        if string_ans[i] == st3[i % len(st3)]:
            scores[2] += 1
    max_score = max(scores)
    result = [i+1 for i,score in enumerate(scores) if score == max_score]
    return result