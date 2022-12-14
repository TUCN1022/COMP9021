import sys
import itertools
import math

INVALID_POWER_VALUE = "Sorry, these are not valid power values."
INVALID_POWER_FLIPS = "Sorry, this is not a valid number of power flips."


def get_power_input():
    input_powers = input("Please input the heroes' powers: ")
    if input_powers == "":
        print(INVALID_POWER_VALUE)
        exit(0)
    input_powers = input_powers.split()
    for i in range(len(input_powers)):
        try:
            input_powers[i] = int(input_powers[i])
        except Exception as e:
            print(INVALID_POWER_VALUE)
            exit(0)
        if input_powers[i] == 0:
            print(INVALID_POWER_VALUE)
            exit(0)
    return input_powers


def get_power_flips_input(powers):
    input_switches = input("Please input the number of power flips: ")
    if not input_switches.isdigit() or "." in input_switches \
            or int(input_switches) < 0 or int(input_switches) > len(powers):
        print(INVALID_POWER_FLIPS)
        exit(0)
    else:
        return int(input_switches)


def maximum_overall_power(powers, nb_of_switches):

    powers = sorted(powers)
    positive_powers = []
    negative_powers = []
    for power in powers:
        if power < 0:
            negative_powers.append(power)
        else:
            positive_powers.append(power)
    result = 0
    if nb_of_switches < len(negative_powers):
        for i in range(len(negative_powers)):
            if i < nb_of_switches:
                result += negative_powers[i] * -1
            else:
                result += negative_powers[i]
        result += sum(positive_powers)
    else:
        if (nb_of_switches - len(negative_powers)) % 2 == 0:
            result = sum(negative_powers) * -1 + sum(positive_powers)
        else:
            smallest = min(min(positive_powers), max(negative_powers) * -1)
            result = sum(negative_powers) * -1 + sum(positive_powers) - smallest * 2

    return int(result)


def maximum_overall_power_second(powers, nb_of_switches):
    combs = list(itertools.combinations([i for i in range(0, len(powers))], nb_of_switches))
    result = -1e7
    for comb in combs:
        temp_result = 0
        for i in range(len(powers)):
            if i in comb:
                temp_result += powers[i] * -1
            else:
                temp_result += powers[i]
        if temp_result > result:
            result = temp_result
    return result


def maximum_overall_power_third(powers, nb_of_switches):
    result = -1e7
    for i in range(0, len(powers) - nb_of_switches + 1):
        temp_result = 0
        for j in range(0, len(powers)):
            if j in range(i, i + nb_of_switches):
                temp_result += powers[j] * -1
            else:
                temp_result += powers[j]
        if temp_result > result:
            result = temp_result
    return result


def maximum_overall_power_fourth(powers):
    result = -1e7
    for max_value in range(0, len(powers) + 1):
        for i in range(0, len(powers) - max_value + 1):
            temp_result = 0
            for j in range(0, len(powers)):
                if j in range(i, i + max_value):
                    temp_result += powers[j] * -1
                else:
                    temp_result += powers[j]
            if temp_result > result:
                result = temp_result
    return result

def main():
    powers = get_power_input()
    nb_of_switches = get_power_flips_input(powers)
    print(f"Possibly flipping the power of the same hero many times, the greatest achievable power is "
          f"{maximum_overall_power(powers, nb_of_switches)}.")
    print(f"Flipping the power of the same hero at most once, the greatest achievable power is "
          f"{maximum_overall_power_second(powers, nb_of_switches)}.")
    print(f"Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is "
          f"{maximum_overall_power_third(powers, nb_of_switches)}.")
    print(f"Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is "
          f"{maximum_overall_power_fourth(powers)}.")

main()


