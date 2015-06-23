import numpy as np
import re

# passSeq=[]
# firstEncCoord=[]
#anything on the outermost rectangle that is not a dot
def findEdge(list3):
    x=0
    while x<len(list3):
        y=0
        while y<len(list3[0]):
            #print 'x='+str(x)+' y='+str(y)
            if (x==0) | (x==(len(list3)-1)):   #NOTE the braces around | are necessary!!!
                #print list3[x][y]
                if list3[x][y]!='.':
                    return (x,y)
            if x>0 & x<(len(list3)-1):
                if (y==0) | (y==(len(list3[0])-1)):
                    if list3[x][y]!='.':
                        return (x,y)
            y=y+1
        x=x+1
    #return 1,1 if nothing found
    return (1,1)

def printList(l):
    for sen in l:
        print sen

#get releveant part, strip of newlines and tabs
def getListFromLines(lines,j,k,l):
    mat2=lines[(j+1):(k+l)]
    k=0
    while k<len(mat2):
        mat2[k]=mat2[k].strip()
        k=k+1
    return mat2

#no need to check endtrace, plus implies ONLY 2 neighbors valid
def verplus(mat,x,y):
    #print 'turning hor'
    if mat[x][y+1]=='-':
        right(mat,x,y)
    else:
        left(mat,x,y)

def horplus(mat,x,y):
    #print 'turning ver'
    if mat[x-1][y]=='|':
        up(mat,x,y)
    else:
        down(mat,x,y)

def knotOrNot(pSeq):
    print 'in knotornot'
    if len(pSeq)<=2:
        return False
    else:
        return True

def endTrace(mat,x,y):
    print 'tracing complete at x='+str(x)+',y='+str(y)
    print 'xns at:'
    print firstEncCoord
    #print 'pass sequence'
    #print passSeq
    knotOrNot(reduceSeq(passSeq))

def isHomo(seq):
    w=len(seq)-1
    while (w>0):
        if seq[w]==seq[w-1]:
            return True
        w=w-1

def reduceSeq(pSeq):
    print pSeq
    kFlag=True
    q=len(pSeq)-1
    #print 'last element '+str(q)
    oec=1
    #replace multiple instances of char depending on odd/even
    while kFlag:
        while (pSeq[q]==pSeq[q-1]):
            oec=oec+1
            print 'q in loop2: '+str(q)
            q=q-1
        if oec%2==1:
            while oec>1:
                del pSeq[oec+q-1]
                oec=oec-1
        if oec%2==0:
            while oec>0:
                del pSeq[oec+q-1]
                oec=oec-1
        oec=1
        print 'q in loop1: '+str(q)
        print pSeq
        q=q-1
        if len(pSeq)<=1:
            kFlag=False
            print 'final1'
            return pSeq        
        if q<=0:
            if isHomo(pSeq):
                q=len(pSeq)-1
            else:
                kFlag=False
                print 'final2'
                return pSeq    

#handling H,I - 1) note H,I encounters irresp of H/I, put in array
#               2) at 2nd encounter classify as over/under
                    # vert+H=under
                    # vert+I=over
                    # hor+H=over
                    # hor+I=under
#               3) uou/ouo forms the first knot
#               4) lite just get seq of u,o
def add2FirstEnc(x,y):
    firstEncCoord.append((x,y))

def add2passSeq(p):
    passSeq.append(p)

def up(mat,x,y):
    while (mat[x-1][y]=='|') | (mat[x-1][y]=='H') | (mat[x-1][y]=='I'):
        if (mat[x-1][y]=='H') | (mat[x-1][y]=='I'):
            if (x-1,y) in firstEncCoord:
                if mat[x-1][y]=='H':
                    add2passSeq('u')
                else:
                    add2passSeq('o')
            else:
                add2FirstEnc(x-1,y)
        x=x-1
        #print 'up'
    if mat[x-1][y]=='+':
        verplus(mat,x-1,y)
    else:
        endTrace(mat,x,y)

def down(mat,x,y):
    while (mat[x+1][y]=='|') | (mat[x+1][y]=='H') | (mat[x+1][y]=='I'):
        if (mat[x+1][y]=='H') | (mat[x+1][y]=='I'):
            if (x+1,y) in firstEncCoord:
                if mat[x+1][y]=='H':
                    add2passSeq('u')
                else:
                    add2passSeq('o')
            else:
                add2FirstEnc(x+1,y)
        # if mat[x-1][y]=='H':
        #     app u
        # if mat[x-1][y]=='I'
        #     app o        
        x=x+1
        #print 'down'
    if mat[x+1][y]=='+':
        verplus(mat,x+1,y)
    else:
        endTrace(mat,x,y)

def right(mat,x,y):
    while (mat[x][y+1]=='-') | (mat[x][y+1]=='H') | (mat[x][y+1]=='I'):
        if (mat[x][y+1]=='H') | (mat[x][y+1]=='I'):
            if (x,y+1) in firstEncCoord:
                if mat[x][y+1]=='H':
                    add2passSeq('o')
                else:
                    add2passSeq('u')
            else:
                add2FirstEnc(x,y+1)
        # if mat[x][y+1]=='H':
        #     app o
        # if mat[x][y+1]=='I'
        #     app u
        y=y+1
        #print 'right'
    if mat[x][y+1]=='+':
        horplus(mat,x,y+1)
    else:
        endTrace(mat,x,y)

def left(mat,x,y):
    while (mat[x][y-1]=='-') | (mat[x][y-1]=='H') | (mat[x][y-1]=='I'):
        if (mat[x][y-1]=='H') | (mat[x][y-1]=='I'):
            if (x,y-1) in firstEncCoord:
                if mat[x][y-1]=='H':
                    add2passSeq('o')
                else:
                    add2passSeq('u')
            else:
                add2FirstEnc(x,y-1)
        # if mat[x][y-1]=='H':
        #     app o
        # if mat[x][y-1]=='I'
        #     app u        
        y=y-1
        #print 'left'
    if mat[x][y-1]=='+':
        horplus(mat,x,y-1)
    else:
        endTrace(mat,x,y)

def startTrace(list2,nrow,ncol):
    global passSeq
    passSeq=[]
    global firstEncCoord
    firstEncCoord=[]
    print 'started trace'
    edgex,edgey=findEdge(list2)
    print 'found edge at x='+str(edgex)+' y='+str(edgey)
    if edgex==1 & edgey==1:
        print 'Error in input file'
        return 0
    start2=list2[edgex][edgey]
    print str(edgex)+' '+str(edgey)
    if start2=='-':
        if edgey>0:
            if (list2[edgex][edgey-1]=='-') | (list2[edgex][edgey-1]=='H') | (list2[edgex][edgey-1]=='I'):
                left(list2,edgex,edgey)            
        if edgey<(ncol-1):        
            if (list2[edgex][edgey+1]=='-') | (list2[edgex][edgey+1]=='H') | (list2[edgex][edgey+1]=='I'):
                right(list2,edgex,edgey)
    if start2=='|':
        if edgex>0:
            if (list2[edgex-1][edgey]=='|') | (list2[edgex-1][edgey]=='H') | (list2[edgex-1][edgey]=='I'):
                up(list2,edgex,edgey) 
        if edgex<(nrow-1):
            if (list2[edgex+1][edgey]=='|') | (list2[edgex+1][edgey]=='H') | (list2[edgex+1][edgey]=='I'):
                down(list2,edgex,edgey) 

    # trace(edgex,edgey)

with open('knot_input4.txt') as f:
    inarray=f.readlines()

#lines read, loop over lines if digits, get row col, add row to line number. get mat, give to func knotornot. place ptr at new line number. repeat.

a = re.compile("^([0-9])+")
i=0
case=1
trow=0
#1,10
#11,19
#20,24
while i<len(inarray):
    
    if a.match(inarray[i]):
        nrow=int((inarray[i].split())[0])
        ncol=int((inarray[i].split())[1])
        trow=trow+nrow
        #print str(i+1)+','+str(trow+case)
        lol=getListFromLines(inarray,i,trow,case)
        #print lol
        printList(lol)
        lolFlag=startTrace(lol,nrow,ncol)
        print lolFlag
        if (lolFlag):
            print 'case '+str(case)+' is KNOTTED'
        else:
            print 'case '+str(case)+' is LOOSE'
        #tSeq=['u','u','u','u','u','o','o','o','u','o','o','o','o','u','o','u','o','u']
        #expect ou
        #reduceSeq(tSeq)
        #printlist(inarray[(i+1):(trow+case)]) #slice list as [first element you want:first element you don't want]
        i=i+nrow+1
        case=case+1