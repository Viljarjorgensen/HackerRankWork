if __name__ == '__main__':
    records = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])
        scores.append(score)

    scores = list(set(scores))

    scores.sort()

    second_lower_score = scores[1]

    student_names = [record[0] for record in records if record[1] == second_lower_score]

    student_names.sort()

    [print(name) for name in student_names]