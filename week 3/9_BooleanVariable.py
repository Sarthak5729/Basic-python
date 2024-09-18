def main():
    exam_mark = 76
    age = 8
    points_so_far = 56
    passed_exam = exam_mark>=50
    has_won_game = points_so_far>70
    is_old_enough = age>10
    is_old_enough = passed_exam != has_won_game
    print(passed_exam , has_won_game , is_old_enough)

main()