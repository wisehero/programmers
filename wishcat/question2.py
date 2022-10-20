part_timer_A = ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
part_timer_B = ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
part_timer_C = ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
part_timer_D = ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']


def make_timetable(a_time: list, b_time: list, c_time: list, d_time: list):
    part_timer_schedule = dict()
    day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for day in day_of_week:
        part_timer_schedule.setdefault(day, [])

    all_time = a_time + b_time + c_time + d_time
    part_timer_number = 0
    for key in part_timer_schedule.keys():
        for worker, time in enumerate(all_time[part_timer_number::5]):
            if worker == 0:
                part_timer_schedule[key].append(("A", time))
            elif worker == 1:
                part_timer_schedule[key].append(("B", time))
            elif worker == 2:
                part_timer_schedule[key].append(("C", time))
            else:
                part_timer_schedule[key].append(("D", time))
        part_timer_number += 1

    for key in part_timer_schedule.keys():
        part_timer_schedule[key].sort(key=lambda x: x[1])

    print(part_timer_schedule)


make_timetable(part_timer_A, part_timer_B, part_timer_C, part_timer_D)
