def isInterleaving(A, B, C):
  # 하위 문제의 계산 반복 여부를 확인하기 위해
  # 검사하는 문자열을 출력해 봅니다.
  print('간삽 확인 : [%s] + [%s] => [%s]' % (A, B, C))

  # 만약 모든 문자열이 빈 문자열인 경우
  if (len(A) == 0) and (len(B) == 0) and (len(C) == 0):
    return True
  
  # A와 B 문자열의 길이의 합이 C 문자열의 길이와 다를 때
  if len(A) + len(B) != len(C):
    return False

  caseA = False
  caseB = False

  # A의 첫글자와 C의 첫글자가 같은 경우
  if (len(A) != 0) and (A[0] == C[0]):
    caseA = isInterleaving(A[1:], B, C[1:])
  
  # B의 첫글자와 C의 첫글자가 같은 경우
  if (len(B) != 0) and (B[0] == C[0]):
    caseB = isInterleaving(A, B[1:], C[1:])

  return caseA or caseB

a = 'bcc'
b = 'bbca'
c = 'bbcbcac'
check = isInterleaving(a, b, c)
print('%s는 %s와 %s의 간삽' % (c, a, b), end = '')
if check:
  print('입니다.')
else:
  print('이 아닙니다.')