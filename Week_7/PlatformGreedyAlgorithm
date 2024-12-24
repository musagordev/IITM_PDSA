# From to train schedules, find maximum train to use platform with greedy algorithm.

from datetime import datetime
def minimum_platform(train_schedule):
    platform_list = []
    while len(train_schedule) > 0:
        platform_list.append([])
        for train in train_schedule[:]:
            for platform in platform_list:
                if platform == []:
                    platform.append(train)
                    train_schedule.remove(train)
                    break
                else:
                    train_arrival = datetime.strptime(train[1], "%H:%M")
                    last_departure = datetime.strptime(platform[-1][2], "%H:%M")
                    if train_arrival >= last_departure:
                        platform.append(train)
                        train_schedule.remove(train)
                        break
    return len(platform_list)
                    
schedule = eval(input())           
print(minimum_platform(schedule))
