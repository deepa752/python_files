input=4
space=input
i=1
m=0
while i<=input:
    j=0
    alpha=65
    Alpha=65
    output=""
    finalOut=""
    while i>j:
        output+=chr(alpha)+str(j+1)
        if j>0:
            finalOut+=str(i-j)
        finalOut+=chr(Alpha+m)        
        alpha+=1
        Alpha-=1
        j+=1
    print space*"  "+output+finalOut
    space-=1
    i+=1
    m+=1   

