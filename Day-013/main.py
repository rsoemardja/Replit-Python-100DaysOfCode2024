print("Grade Calculator")
print()
# Ask for the student's score
name_of_exam = input("Name of exam: ")
print()
total_score = int(input("Max. Possible Score:"))
your_score = int(input("Your score: "))
print()

number_score = float(your_score / total_score)
final_number = round(number_score, 2)
final_percent = round(float(your_score / total_score)*100, 2)

print("You got",final_percent,"%")

if final_number >= .90:
    print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
    pass
elif final_number >= .70 and final_number <= .79:
    pass
elif final_number >= .60 and final_number <= .69:
    pass
elif final_number >= .50 and final_number <= .59:
    pass
elif final_number >= .40 and final_number <= .49:
    pass
else:
    print("Try again!")
  