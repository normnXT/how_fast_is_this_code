import cProfile

if __name__ == "__main__":

    # REPLACE CODE BELOW WITH CODE YOU WANT TO TEST <--------------------------------------------------------- (1)

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


    # ADD CODE TO TEST ABOVE HERE  <---------------------------------------------------------------------------


def cprofile_loop(func_to_profile, num_runs, *args, **kwargs):
    pr = cProfile.Profile()

    pr.enable()
    for _ in range(num_runs):
        func_to_profile(*args, **kwargs)
    pr.disable()

    return pr


if __name__ == "__main__":
    # EDIT THE FOLLOWING LINE TO SPECIFY THE FUNCTION, ITS ARGS, AND THE NUMBER OF TESTS YOU WANT TO RUN <----- (2)
    profile = cprofile_loop(merge, 100000, dicts)
    profile.print_stats(sort='time')
