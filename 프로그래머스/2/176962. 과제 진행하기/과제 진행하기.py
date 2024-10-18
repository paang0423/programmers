def solution(plans):
    answer = []
    stack = []  # 진행 중인 과제를 멈추었을 때 저장하는 스택
    
    plans.sort(key=lambda x: (int(x[1][:2]), int(x[1][3:])))
    
    for i in range(len(plans)):
        hour, minute = map(int, plans[i][1].split(":"))
        plans[i][1] = hour * 60 + minute
        plans[i][2] = int(plans[i][2])
    
    for i in range(len(plans)):
        current_name, current_start, current_duration = plans[i]
        
        if i == len(plans) - 1:
            answer.append(current_name)
            while stack:
                last_task = stack.pop()
                answer.append(last_task[0])
            break
        
        next_start = plans[i + 1][1]
        
        if current_start + current_duration <= next_start:
            answer.append(current_name)
            remaining_time = next_start - (current_start + current_duration)
            
            while stack and remaining_time > 0:
                last_task = stack.pop()
                if last_task[2] <= remaining_time:
                    answer.append(last_task[0])
                    remaining_time -= last_task[2]
                else:
                    last_task[2] -= remaining_time
                    stack.append(last_task)
                    break
        
        else:
            plans[i][2] = current_duration - (next_start - current_start)
            stack.append(plans[i])
    
    return answer
