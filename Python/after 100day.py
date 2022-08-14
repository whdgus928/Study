'''
100일 뒤에 월, 일, 요일을 구하기
'''
def after_100(month,day,day_week):
    year_list=[31,28,31,31,31,30,31,31,30,31,30,31]
    day_list=['월','화','수','목','금','토','일']
    #100일 뒤 월
    after_100_month=month
    #100일 뒤 일
    after_100_day=day+99

    #월,일 구하기
    while after_100_day>year_list[after_100_month-1]:
        print(after_100_month)
        print(after_100_day)
        after_100_day-=year_list[after_100_month-1]
        after_100_month+=1
        
    #요일
    after_100_day_week=day_list[day_list.index(day_week)+2]

    print(f'{month}월 {day}일 {day_week}요일부터 100일 뒤는 {after_100_month}월 {after_100_day}일 {after_100_day_week}요일')

after_100(6,21,"화")
