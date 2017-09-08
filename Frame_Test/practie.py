def avg(score):
    return sum(score)/len(score)


def drop_first_end(grades):
    first, *middle, last = grades
    return avg(middle)

grade = [1, 2, 3, 4, 5]
print(drop_first_end(grade))