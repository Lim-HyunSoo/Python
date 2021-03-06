###
문제 설명
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 
단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

입출력 예
bridge_length	| weight |	truck_weights                 	| return
      2	      |   10   |	   [7,4,5,6]	                  |   8
     100	    |   100	 |      [10]	                      |  101
     100	    |   100  | 	[10,10,10,10,10,10,10,10,10,10] | 	110
###

def solution(bridge_length, weight, truck_weights):
    answer = 0
    visited = []
    cross = [] 
    
    while True:
        if(len(truck_weights) == 0 and len(cross) == 0):
            break 
        
        answer += 1
        if(len(visited) > 0):
            l = [1 for i in range(len(visited))]
            visited = [x + y for x,y in zip(visited,l)]
            for i in range(len(l)):
                if(visited[0] == bridge_length):
                   cross.pop(0)
                   visited.pop(0)
                else:
                    break 
                    
        if(len(truck_weights) > 0):
            if(sum(cross) + truck_weights[0] <= weight):
                cross.append(truck_weights.pop(0))
                visited.append(0)
        
    return answer
