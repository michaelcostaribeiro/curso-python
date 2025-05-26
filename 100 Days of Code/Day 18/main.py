from jimmy import Jimmy

jimmy = Jimmy('jimmy')

can_continue = True
while can_continue:
    can_continue = jimmy.tp_forward()

jimmy.screen_name.exitonclick()
