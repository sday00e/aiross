'''

readMe.txt의 내용

-----------------

시작하기 전에 확인할 내용입니다.

1. 모든 학생이 참여하였는가?

2. 수업 도구는 모두 준비되었는가?

3. 수업용 기자재는 모두 정상 동작하는가?

-----------------

'''

fp = open('C:\Windows\ReadMe.txt', 'r', encoding='UTF-8')

fpo = open('readMeNew.txt', 'w')

one = fp.readline()

while one:

    fpo.write(one)

    one = fp.readline()

fp.close()