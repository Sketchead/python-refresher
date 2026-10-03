def calculate_average(homeworks):
    total = 0
    for homework in homeworks.values():
        total += homework
    final_average = total / len(homeworks)
    return final_average
