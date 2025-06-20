n, m = map(int, input().split(' '))

design_unit = ".|."
rows = list()

for i in range(1, n, 2):
    main_design = design_unit * i
    side_width = (m - len(main_design)) // 2
    side_design = side_width * '-'
    rows.append(side_design + main_design + side_design)
# Top part
print(*rows, sep="\n")
# "Welcome" part
welcome_design = "WELCOME"
side_width = (m - len(welcome_design)) // 2
side_design = side_width * '-'
print(side_design + welcome_design + side_design)
# Button part
print(*rows[::-1], sep="\n")
