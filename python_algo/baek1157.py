from collections import Counter

string = input().upper()

most_string = Counter(string).most_common(2)

if len(string) == 1:
  print(string)

elif most_string[0][1] == most_string[1][1]:
  print("?")
else:
  print(most_string[0][0])


