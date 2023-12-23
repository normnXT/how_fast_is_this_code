import time


if __name__ == '__main__':

    # ADD CODE BLOCK BELOW HERE ----------------------------------------------------------------------------- (1)

    dicts = [{"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}, {"A": 1, "B": 2, "C": 3}]


    def merge(dicts):
        merged_dict = {}

        for d in dicts:
            for k, v in d.items():
                if k in merged_dict:
                    merged_dict[k].append(v)
                else:
                    merged_dict[k] = [v]

        return merged_dict


    # ADD CODE BLOCK ABOVE HERE  ------------------------------------------------------------------------------


def perf_counter_average(func_to_profile, num_runs, *args, **kwargs):
    total_time = 0

    for _ in range(num_runs):
        start = time.perf_counter()
        func_to_profile(*args, **kwargs)
        end = time.perf_counter()
        total_time += (end - start)

    average_time = total_time / num_runs
    return average_time


if __name__ == '__main__':
    # EDIT THE FOLLOWING LINE TO SPECIFY THE FUNCTION, ITS ARGS, AND THE NUMBER OF TESTS YOU WANT TO RUN <----- (2)
    time = perf_counter_average(merge, 100000, dicts)
    print(f"{time} seconds")
