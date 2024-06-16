# 소요시간: 6분
# 특이사항: 여러줄 받는법, re/rstrip이 뭔 줄 몰라서 헤매기

import sys 
import re
code=sys.stdin.readlines() #여러 줄을 정답으로 받고

for i in code: #한 줄씩 검사하기
    while True:
        result=re.sub('BUG','',i)
        #ABUBUGGB와 같은 경우는 AB가 되어야 하니까 while반복문으로 검사
        if 'BUG' in result: #있으면 한번 제거한 결과를 가지고 또 검사하도록
            i= result
        else: 
            print(result,end="") #줄바꿈까지 같이 출력되니까 end=""써주기
            break
