from jimmy import Jimmy
import colorgram

my_tuple = colorgram.extract('hirst-painting.jpg', 5)
teste = []
for i in range(0, len(my_tuple)-1):
    teste.append(my_tuple[i])
    print(my_tuple[i].rgb[0])


jimmy = Jimmy('jimmy')

can_continue = True
while can_continue:
    can_continue = jimmy.tp_forward()

jimmy.screen_name.exitonclick()