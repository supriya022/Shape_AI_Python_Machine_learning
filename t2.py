# from turtle import *
# speed("slow")
# width(8)

# lt(72)
# fd(100)
# lt(72)
# fd(100)
# lt(72)
# fd(100)
# lt(72)
# fd(100)
# lt(72)
# fd(100)
# mainloop()

from turtle import *
side = 6
for i in range(side):
    pencolor('blue')
    fd(100)
    lt(360/side)
    pencolor('red')
    dot(30)
mainloop()