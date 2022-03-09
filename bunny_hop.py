def bunnyHops(hop_distance):
    hop_combinations = []
    hop_options = [1, 2, 3]

    for option in hop_options:
        being_worked_on = []

        if hop_distance > option:
            being_worked_on.append([option])

            while being_worked_on:
                item = being_worked_on.pop()
                item_sum = sum(item)

                # Loops Through Options And Appends If Completed Or Still Needs To Be Worked On
                for inner_option in hop_options:
                    temp_sum = item_sum + inner_option

                    # Checks If The Item Is Done Or Needs More Work
                    if temp_sum < hop_distance:
                        temp_item = list(item)
                        temp_item.append(inner_option)
                        being_worked_on.append(temp_item)
                    elif temp_sum == hop_distance:
                        temp_item = list(item)
                        temp_item.append(inner_option)
                        hop_combinations.append(temp_item)
                        break

        # Handles Case When The Distance Equals The Hop Value
        elif option == hop_distance:
            hop_combinations.append([option])

    return hop_combinations


# # Testing Code
# from datetime import datetime
#
# number_of_expected = [0, 1, 2, 4]
# for x in range(4, 25):
#     expected_count = number_of_expected[x - 3:x]
#     number_of_expected.append(sum(expected_count))
#
# # Records Accuracy And Efficiency
# for x in range(0, 25):
#     start = datetime.now()
#     number_of_hops = x
#     hop_combos = bunnyHops(number_of_hops)
#     print("Number Of Hops", x, number_of_expected[x], (datetime.now() - start).total_seconds())
#     if len(hop_combos) != number_of_expected[x]:
#         print("Number Of Hops", x)
#         print("Expected Number", number_of_expected[x])
#         print("Actual Number", len(hop_combos))
#     for hops in hop_combos:
#         if sum(hops) != number_of_hops:
#             print("Hops", hops)
#             print("Number Of Hops", x)
