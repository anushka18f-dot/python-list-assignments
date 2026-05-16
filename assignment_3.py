#Assignment 3

marks = [65, 50, 75, 82, 55]
max_mark = max(marks)
min_mark = min(marks)
total = sum(marks)
aver = total/ len(marks)

if aver >=50:
    result = "PASS"
else:
    result = "FAIL"

print("="*40)
print(f'{"MARKS ANALYZER":^40}')
print("="*40)

print(f'{"Marks: ":<15}{marks}')
print(f'{"Total: ":<15}{total}')
print(f'{"Average: ":<15}{aver:.2f}')
print(f'{"Highest Mark: ":<15}{max_mark}')
print(f'{"Lowest Mark: ":<15}{min_mark}')
print(f'{"Result: ":<15}{result}')
print("="*40 + "\n")