student_scores = [150, 142, 185, 120, 171, 184, 149, 24]
# Initially Max score = 0
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print("The Maximum score is =", max_score)
