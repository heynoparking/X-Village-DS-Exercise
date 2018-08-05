from queue import Queue


def hot_potato(name_list, num):
    
    Q = Queue()
    
    for name in name_list:
        Q.enqueue(name)
    
    
    while Q.size() >1: 
        for i in range (num):
            a = Q.dequeue()
            Q.enqueue(a)
        Q.dequeue()
        
    remaining_person = Q.dequeue()
    
    return remaining_person

print(hot_potato(["Susan", "Brad", "Kent", "David"], 6) )              # 回傳 "Brad"
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))  # 回傳 "Susan"