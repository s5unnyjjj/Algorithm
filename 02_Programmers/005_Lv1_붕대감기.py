
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/250137

def check_health(my_health, max_health):
    if my_health > max_health:
        my_health = max_health
    return my_health

def solution(bandage, health, attacks):
    cur_time = 0
    myInfo = {'health' :health, 'success' :0}
    for attack in attacks:
        attack_time, attack_size = attack[0], attack[1]
        while cur_time < attack_time:
            cur_time += 1
            if cur_time != attack_time:
                myInfo['health'] = check_health(myInfo['health' ] +bandage[1], health)
                myInfo['success'] += 1
                if myInfo['success'] == bandage[0]:
                    myInfo['success'] = 0
                    myInfo['health'] = check_health(myInfo['health' ] +bandage[2], health)
            else:
                myInfo['health'] -= attack_size
                myInfo['success'] = 0
            if myInfo['health'] <= 0:
                return -1

    return myInfo['health']