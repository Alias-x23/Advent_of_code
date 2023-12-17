import numpy as np


def get_race_outcomes(race_times, race_records):
    out_list = []

    for i, time in enumerate(race_times):
        possible_scores = [x*(time-x) for x in range(1, time)]
        possible_scores = [s for s in possible_scores if s > race_records[i]]
        out_list.append(len(possible_scores))

    return out_list



def main():
    race_times = [53, 89, 76, 98]
    race_records = [313, 1090, 1214, 1201]
    better_scores = get_race_outcomes(race_times, race_records)
    print(f"product of better scores is {np.prod(better_scores)}")
    big_race_time = [53897698]
    big_race_record = [313109012141201]
    big_scores = get_race_outcomes(big_race_time, big_race_record)
    print(big_scores)


if __name__ == '__main__':
    main()
