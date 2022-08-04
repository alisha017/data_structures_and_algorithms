
class Point:
    def __init__(self, time, is_start_time):
        self.__time = time
        self.__is_start_time = is_start_time

    def get_time(self):
        return self.__time

    def get_is_start_time(self):
        return self.__is_start_time


def if_overlapping_interval(intervals):
    interval_points = []

    for interval in intervals:
        start = Point(interval[0], True)
        end = Point(interval[1], False)

        interval_points.extend([start, end])

    time_sorted_interval_points = sorted(interval_points, key=lambda t: t.get_time())

    counter = 0
    for i in range(len(time_sorted_interval_points)):
        if time_sorted_interval_points[i].get_is_start_time() is True:
            counter += 1
        else:
            counter -= 1

        if time_sorted_interval_points[i - 1].get_time() == time_sorted_interval_points[i].get_time():
            counter += 1

        print(counter)
        # if counter > 1:
        #     return True

    return False


if __name__ == '__main__':
    print(if_overlapping_interval([[5,7], [1,3], [6,9]]))
    print(if_overlapping_interval([(1,3), (3,5), (6,8), (7,9)]))