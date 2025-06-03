import scoreboard as s


score = s.Scoreboard()
current_number = score.get_highest_score()
print(current_number)
printable_test = score.update_highest_score(5)
current_number = score.get_highest_score()
print(current_number)