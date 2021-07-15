
input='1 + 2 * 3 + 4 * 5 + 6' #correct
input='1 + (2 * 3) + (4 * (5 + 6))' #incorrect
# SEEMS TO BE GOING WRONG IN LAST PART
#   4*(5+6)=10, should be 44
#input='2 * 3 + (4 * 5)' #correct
#input='5 + (8 * 3 + 9 + 3 * 4 * 3)' #correct
#input='5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))' #inccorect
#input='((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2' #syntax error

input = list(input.replace(" ",""))

def solve(expression,answer=0):
  print("INPUT:","".join(expression))
  p_list=[]
  p_dict={}
  #traverse the list looking for parentheses
  # and find out where they open and close
  for i,char in enumerate(expression):
    #print(i,char)
    if char == '(':
      p_list.append(i)
    if char == ')':
      p_dict[p_list[-1]]=i
      del p_list[-1]

  #print(p_list,p_dict)
  ans_dict={}
  if len(p_dict)>0:
    #solve parentheses issues
    for key in p_dict:
      new_input = "".join(expression[key+1:p_dict[key]])
      ans_dict[key]=solve(new_input)
    
  #traverse the expression in order
  # and calculate answer
  #print(ans_dict)
  answer=int(expression[0])
  next_close=0
  for i,char in enumerate(expression):
    #print(answer,char)
    if i > next_close:
      if char =='+':
        if expression[i+1] =='(':
          answer += ans_dict[i+1]
          next_close = p_dict[i+1]
        else:
          answer += int(expression[i+1])
      if char =='*' and expression[i+1]!='(':
        if expression[i+1] =='(':
          answer *= ans_dict[i+1]
          next_close = p_dict[i+1]
        else:
          answer *= int(expression[i+1])
  print(p_dict,ans_dict)  
  return answer

print(solve(input))
