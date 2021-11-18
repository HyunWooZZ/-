import sys
num = int(sys.stdin.readline())

string_list = [sys.stdin.readline().strip() for _ in range(num)]

answer = 0

for string in string_list:   ### 체크할 데이터 삽입
  check_dict = {}
  temp = None

  ### 문자열에 이전것과 다르면 기존 사전에 있는지 확인후
  ### 있으면 다음 문자열을 확인  끝까지 진행해도 없으면 answer에 1추가

  for word in string:       
    if word not in check_dict:    
      check_dict[word] = True
      temp = word

    else:  ### 기존 사전에 있는 경우
      if word is not temp:   ### temp와 일치하지 않을 때는 끝내면 됨.
        break
      
  else:     ### 반복문이 끝까지 다 돈경우 정답에다 1을 더한다. 
    answer += 1
      

print(answer)

      