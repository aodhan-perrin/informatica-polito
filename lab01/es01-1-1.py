def conflict_check(event1: int, event2: int) -> bool:
    start = max(event1[0], event2[0])   # index [0] for start time
    end = min(event1[1], event2[1])     # index [1] for end time

    return start < end


start1, end1, start2, end2 = 10, 12, 11, 13

event1 = (start1, end1)
event2 = (start2, end2)    

match conflict_check(event1, event2):
    case False:
        print("no conflict")
    case True:
        print("conflict")


