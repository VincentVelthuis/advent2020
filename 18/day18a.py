import sys, fileinput

# input = list(input.replace(" ",""))

def solve(expression,answer=0):
  p_list=[]
  p_dict={}
  first_digit = 0
  first_digit_found = False
  #traverse the list looking for parentheses
  # and find out where they open and close
  for i,char in enumerate(expression):
    # to counter errors if the expression starts with '('
    # register the location of the first digit in the expr.
    if char.isdigit()and not(first_digit_found):
      first_digit = i
      first_digit_found = True
    # register opening parenthesis
    if char == '(':
      p_list.append(i)
    # register matching closing parenthesis
    if char == ')':
      p_dict[p_list[-1]]=i
      del p_list[-1]

  ans_dict={}
  if len(p_dict)>0:
    #solve parentheses issues
    for key in p_dict:
      new_input = "".join(expression[key+1:p_dict[key]])
      # print(new_input, p_dict)
      ans_dict[key]=solve(new_input)
    
  #traverse the expression in order
  # and calculate answer
  answer=int(expression[first_digit])
  # first int, is the issue
  next_close=0
  for i,char in enumerate(expression):
    if i > next_close:
      if char =='+':
        if expression[i+1] =='(':
          answer += ans_dict[i+1]
          next_close = p_dict[i+1]
        else:
          answer += int(expression[i+1])
      if char =='*':
        if expression[i+1] =='(':
          answer *= ans_dict[i+1]
          next_close = p_dict[i+1]
        else:
          answer *= int(expression[i+1])
  # print("".join(expression), answer)
  # print(p_dict, ans_dict)
  return answer

ans = 0
for line in fileinput.input(files=sys.argv[1]):
    expr = list(line.replace(" ",""))
    ans += solve(expr)
    print(solve(expr),"=",line)
print("sum of all:",ans)