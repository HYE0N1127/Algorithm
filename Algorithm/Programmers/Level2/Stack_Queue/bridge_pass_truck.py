# Programmers Level 2 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length        # bridge_length 길이 만큼의 배열을 생성

    while bridge:
        time += 1
        bridge.pop(0)       # 올라가는데 걸리는 시간이 있기에 pop을 해주고 time +1

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:        # Bridge 위에 올라가있는 트럭과 첫번째 대기 순번의 트럭의 합이 weight 가 넘지 않아야함
                bridge.append(truck_weights.pop(0))     # 조건 충족 시에 첫번째 대기 트럭을 Pop 해서 bridge 에 append

            else:
                bridge.append(0)    # 조건 충족이 안될 시에 time 이 늘어나야 하기에 길이를 늘려줌

    return time