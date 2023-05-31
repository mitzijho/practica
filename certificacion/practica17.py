def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    line1 = line2 = line3 = line4 = ""

    for problem in problems:
        operands = problem.split()

        if operands[1] != "+" and operands[1] != "-":
            return "Error: Operator must be '+' or '-'."

        if not operands[0].isdigit() or not operands[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(operands[0]) > 4 or len(operands[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operands[0]), len(operands[2])) + 2
        line1 += operands[0].rjust(width) + "    "
        line2 += operands[1] + " " + operands[2].rjust(width - 2) + "    "
        line3 += "-" * width + "    "

        if show_answers:
            if operands[1] == "+":
                answer = str(int(operands[0]) + int(operands[2]))
            else:
                answer = str(int(operands[0]) - int(operands[2]))

            line4 += answer.rjust(width) + "    "

    arranged_problems.extend([line1.rstrip(), line2.rstrip(), line3.rstrip()])

    if show_answers:
        arranged_problems.append(line4.rstrip())

    return "\n".join(arranged_problems)

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# Output:
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
# Output:
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
