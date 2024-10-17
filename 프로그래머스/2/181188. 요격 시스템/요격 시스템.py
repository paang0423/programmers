def solution(targets):
    # 타겟들을 끝나는 지점 기준으로 정렬
    targets.sort(key=lambda x: x[1])

    answer = 0
    last_shot = -1  # 마지막 요격 미사일 발사 위치

    for start, end in targets:
        # 현재 타겟의 시작점이 마지막 발사 지점보다 크면 새로운 미사일 발사
        if start >= last_shot:
            answer += 1  # 새로운 미사일 발사
            last_shot = end  # 새로운 발사 위치는 현재 타겟의 끝나는 지점

    return answer
