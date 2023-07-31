grade_list = list(map(int, input().split()))

if grade_list[0] > 100 or grade_list[1] > 100 or grade_list[2] > 100 or grade_list[3] >100 or grade_list[4]> 100:
    print("too big")
if grade_list[0] < 0 or grade_list[1] < 0 or grade_list[2] < 0 or grade_list[3] < 0 or grade_list[4] < 0:
    print("too small")
else:
    print(max(grade_list))