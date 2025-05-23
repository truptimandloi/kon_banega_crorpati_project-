Questions = [
    ["where is india gate located ?","delhi","mumbai","punjab","agra",1],
    ["which language was used to create fb ?","python","java","c","php",4],
    ["how many states are there in india ?","29","28","30","31",2],
    ["how do you say hello in india ?","hola","namaste","hi","chor",2],
    ["Taj mahal was made of ?","stone","graphite","Marble","iron",3],
    ["Which is following is not a state ?","indore","goa","jharkhand","madhya pradesh",1],
    ["Which is the capital of India ?","delhi","mumbai","chandigarh","agra",1],
    ["which is the largest city of India ?","mumbai","chandigarh","agra","delhi",4],
    ["which is the cleanest city of madhya pradesh ?","bhopal","indore","jabalpur","khargoan",2],
    ["what is the name of india ?","bharat","pak","china","nepal",1],
    ["Which is the capital of madhya pradesh ?","bhopal","indore","jabalpur","khargoan",1],
    ]

levels = [1000,2000,5000,10000,20000,40000,80000,160000,320000,640000,10000000]

money = 0
for i in range(0,len(Questions)):
    Question = Questions[i]
    print(f"\n Question for rs.{levels[i]}\n")
    print(f"Question is: {Question[0]}")
    print(f"1.{Question[1]}   2.{Question[2]} \n3.{Question[3]}   4.{Question[4]}")
    answer = int(input("enter your answer (1-4) or 0 for quit :\n "))

    if (answer ==0):
        money = levels[i-1]
        break  
    
    if(answer==Question[-1]):
       print(f"correct answer you have won RS.{levels[i]}")
       if(i==3):
          money = 10000
       elif(i==8):
          money = 320000
       elif(i == 10):
         money = 10000000 
    else:
      print("wrong answer !!")
      break
print(f"your take home money is {money} ")


