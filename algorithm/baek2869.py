import sys

up, down, summit = map(int, sys.stdin.readline().split())

step = up - down 

last_step = summit - up

if last_step % step == 0:
  day = last_step / step

else:
  day = last_step // step + 1


day += 1

print(int(day))

 