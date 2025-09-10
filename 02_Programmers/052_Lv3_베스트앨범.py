
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_kinds= list(set(genres))
    genre_plays = defaultdict(list)
    sum_genre_plays = defaultdict(int)
    for genre_kind in genre_kinds:
        genre_plays[genre_kind] = [[plays[i], i] for i in range(len(genres)) if genres[i] == genre_kind]
        genre_plays[genre_kind] = sorted(genre_plays[genre_kind], key=lambda x:(-x[0], x[1]))
        sum_genre_plays[genre_kind] = sum([play[0] for play in genre_plays[genre_kind]])
    sum_genre_plays = sorted(sum_genre_plays.items(), key=lambda x:x[1], reverse=True)

    for genre in sum_genre_plays:
        for i, values in enumerate(genre_plays[genre[0]]):
            if i == 2:
                break
            answer.append(values[1])
    return answer