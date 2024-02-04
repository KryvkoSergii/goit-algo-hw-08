import heapq


def min_cost_to_connect(cable_lengths):
    heapq.heapify(cable_lengths)

    total_cost = 0
    iteration = []

    while len(cable_lengths) > 1:
        # minimum lenght cables
        min_lenght_cable_1 = heapq.heappop(cable_lengths)
        min_lenght_cable_2 = heapq.heappop(cable_lengths)

        # Cable combining and costing
        sum = min_lenght_cable_1 + min_lenght_cable_2
        total_cost += sum

        iteration.append(f"Комбінована довжина {min_lenght_cable_1} та {min_lenght_cable_2} м, витрата: {sum}")

        heapq.heappush(cable_lengths, sum)

    return total_cost, iteration


def main():
    cable_lengths = [87, 23, 56, 45, 12, 98, 34, 67, 89, 76]
    print(f"Існуючі довжни: {cable_lengths}")

    total_cost, iteration = min_cost_to_connect(cable_lengths)
    print("Порядок об'єднання, який мінімізує загальні витрати")
    for i, item in enumerate(iteration, start=1):
        print(11 * " " + f"{i}. {item}")
    print(f"Загальні витрати: {total_cost}")


if __name__ == "__main__":
    main()