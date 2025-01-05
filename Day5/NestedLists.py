#It was a struggle and had to go through it thoroughly to get the problem

if __name__ == '__main__':
    students = [[input(), float(input())] for _ in range(int(input()))]
    second_lowest_score = sorted({score for _, score in students})[1]
    print('\n'.join(sorted(name for name, score in students if score == second_lowest_score)))
