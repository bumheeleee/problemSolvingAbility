
def solution(number, k):
    answer = ''
    number_lists = list(map(int, number))
    removed_cnt = 0
    comp_lists = []
    
    for i in range(len(number_lists)):
        if removed_cnt == k:
            comp_lists.append(number_lists[i])
        else:
            if i == 0:
                comp_lists.append(number_lists[i])
            else:
                # 321 7
                #뒤에서 부터 비교
                append = False
                for j in range(len(comp_lists)-1, -1, -1):
                    if comp_lists[j] < number_lists[i]:
                        append = True
                        comp_lists.pop()
                        removed_cnt += 1
                    else:
                        append = True
                        
                    if removed_cnt == k:
                        break
                if append:
                    comp_lists.append(number_lists[i])
                else:
                    removed_cnt += 1
    
    comp_lists = list(map(str, comp_lists))
    answer = "".join(comp_lists)
    return answer

solution("4177252841",	4)