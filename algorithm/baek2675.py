def repeat_str(string, repeat):   ### 문자열을 받아 각 자리수를 반복 횟수만큼 반복해주는 함수
    answer = ""
    for i in string:
      for _ in range(repeat):
        answer += i


    return answer



case_num = int(input())     


for _ in range(case_num):  
  testcase = input()    ### 테스트 케이스는 
  testcase = testcase.split(" ")
  repeat = int(testcase[0])
  string = testcase[1]
  print(repeat_str(string, repeat))

