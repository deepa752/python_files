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
    
input=5
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
        output+=chr(alpha)
        if j>0:
            finalOut+=chr(Alpha+m)        
        alpha+=1
        Alpha-=1
        j+=1
    print space*" "+output+finalOut
    space-=1
    i+=1
    m+=1
i=1  
while i<=input:
    op=""
    fOp=""
    k=input-1
    j=1
    while j<=input:
        op+=str(j)
        if k!=0:
            fOp+=str(k)
        j+=1
        k-=1
    print " "+op+fOp
    i+=1
    
space=1
i=input
m=input-1
while i>0:
    j=0
    alpha=65
    Alpha=65
    output=""
    finalOut=""
    while i>j:
        output+=chr(alpha)
        if j>0:
            finalOut+=chr(Alpha+m)        
        alpha+=1
        Alpha-=1
        j+=1
    print space*" "+output+finalOut
    space+=1
    i-=1
    m-=1
    
        
    
        

