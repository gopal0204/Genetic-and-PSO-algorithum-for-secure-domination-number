import time
import random
import sys 
list1 = []
feasi_secure_dom_len = []
feasi_secure_dom_len2 = []
def adjacency_list(v,edges):
    adjacencyList={}
    for vertex in v:
        adjacencyList[vertex]= []
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        adjacencyList[v1].append(v2)
        adjacencyList[v2].append(v1)
    return adjacencyList,v

n1,n2 = map(int,input().split())
v = []
for i in range(n1):
    v.append(i)
edges = []
for i in range(n2):
    v1,v2 = map(int,input().split())
    edges.append([v1,v2])
adjacencyList, v = adjacency_list(v,edges)

u1 = []
u2 = []
adjacencyList2 = {}
for x in adjacencyList.values():
    u1.append(len(x))
for y in adjacencyList:
    u2.append(y)
for z in range(len(u1)):
    adjacencyList2[u2[z]] = u1[z]
adjacencyList3 = dict(sorted(adjacencyList2.items(), key=lambda x: x[1], reverse=True))
uu1 = []
for i in adjacencyList3:
    uu1.append(i)

def swap(a,b,i,j):
    temp = a[i]
    a[i] = b[j]
    b[j] = temp

def domination(adjacencyList,v):
    visited = []
    l1 = []
    l2 = []
    for i in range(len(v)):
        visited.append(0)
    while 0 in visited:
        a = random.choice(v)
        visited[a] = 1
        if len(adjacencyList[a]) == 0:
            l1.append(a)
        else:
            l1.append(a)
            for i in adjacencyList[a]:
                visited[i] = 1
                l2.append(i)
    return list(set(l1))

def domination2(adjacencyList,v):
    visited = []
    l1 = []
    l2 = []
    for i in range(len(v)):
        visited.append(0)
    cm = 0
    while 0 in visited and cm < len(uu1):
        a = uu1[cm]
        visited[a] = 1
        if len(adjacencyList[a]) == 0:
            l1.append(a)
        else:
            l1.append(a)
            for i in adjacencyList[a]:
                visited[i] = 1
                l2.append(i)
        cm = cm + 1
    return list(set(l1))

start = time.time()
#population of domination set and secure domination set
for j in range(1000):
    domi_pop = []
    domi_pop_size = []
    if j <500:
        for i in range(500):
            domi = domination(adjacencyList,v)
            domi_pop.append(domi)
            domi_pop_size.append(len(domi))
    else:
        for i in range(500):
            domi = domination2(adjacencyList,v)
            domi_pop.append(domi)
            domi_pop_size.append(len(domi))

    domi_mini_pop = []
    for i in domi_pop:
        if len(i) == min(domi_pop_size):
            domi_mini_pop.append(i)
    p1 = []
    p2 = []
    q1 = []
    q2 = []
    r1 = []
    r2 = []
    p1 = random.choice(domi_mini_pop)
    for i in range(len(v)):
        if i not in p1:
            p2.append(i)
    def heuristic(adjacencyList):
        q1.extend(p1)
        q2.extend(p2)
        count3 = 0
        count4 = 0
        for jj in range(len(p2)):
            for ii in range(len(p1)):
                if p2[jj] in adjacencyList[p1[ii]]:
                    swap(p1,p2,ii,jj)
                    x = len(p1) - 1
                    y = len(p2) - 1
                    count1 = 0
                    count2 = 0
                    while x >= 0 and y >= 0:
                        if p2[y] in adjacencyList[p1[x]]:
                            y = y - 1
                            count1 = count1 + 1
                            x = len(p1) - 1
                        else:
                            x = x - 1
                            count2 = count2 + 1
                    if count1 == len(p2) :
                        count3 = count3 + 1
                        #print("it is dominating set", p1)
                    #else:
                        #print("it is not dominating set", p1)
                    p1.clear()
                    p2.clear()
                    p1.extend(q1)
                    p2.extend(q2)
            if count3 >= 1:
                count4 = count4 + 1
            else:
                r1.append(q2[jj])
            count3 = 0
        if(count4 == len(q2)):
            #print("it is secure dominating set", q1)
            list1.append(q1)
        else:
            r2 = list(set(r1) | set(q1))
            #print("it is secure dominating set",r2)
            list1.append(r2)
    domination(adjacencyList,v)
    heuristic(adjacencyList)

def feasibility(adjacencyList,d1,d11):
    #d1 is the secure dominating set that need to check the feasibility
    #d11 is the non-secure dominating set that need to check the feasibility
    e1.clear()
    e2.clear()
    f1.clear()
    e1.extend(d1)
    e2.extend(d11)
    e11 = []
    count_a = 0
    count_b = 0
    for j in range(len(d11)):
        for i in range(len(d1)):
            if(d11[j] in adjacencyList[d1[i]]):
                swap(d1,d11,i,j)
                #print("d1 : ",d1)
                #print("d11 : ",d11)
                x1 = len(d1) - 1
                y1 = len(d11) - 1
                count_c = 0
                count_d = 0
                while x1 >= 0 and y1 >= 0:
                    if d11[y1] in adjacencyList[d1[x1]]:
                        y1 = y1-1
                        count_c = count_c + 1
                        x1 = len(d1) - 1
                        #print("count_c : ",count_c)
                    else:
                        x1 = x1-1
                        count_d = count_d + 1
                        #print("count_d : ",count_d)

                if(count_c == len(d11)):
                    #print("it is dominating set" , d1)
                    count_a = count_a + 1
                #else:
                    #print("it is not dominating set" , d1)
                d1.clear()
                d11.clear()
                d1.extend(e1)
                d11.extend(e2)
        if (count_a >= 1) :
            count_b = count_b + 1
        else:
            #print("q1 :",e2[j])
            f1.append(e2[j])   
        count_a = 0
    if(count_b == len(e2)):
        #print("it is secure dominating set e1 ", e1, len(e1))
        #print(e1)
        #h1 = len(e1)
        h1 = len(e1)
        feasi_secure_dom.append(e1)
        e11.clear()
        #print("e1 ",e1)
        for i in v:
            if i not in e1:
                e11.append(i)
        #print("e2 ", e11)
        '''reducedsecure(adjacencyList,e1,e11)
        #print("e22 ", e11)
        #h11 = len(e1)'''
        #print("e12 ",e1)
        feasi_secure_dom_len.append(h1)
        #ans11.append(h11)
        
        #min_list.append(e1)
    else:
        f2 = list(set(f1) | set(e1))
        #print("it is secure dominating set f2 ", f2 ,len(f2))
        
        #print(f2)
        #h2 = len(f2)
        h2 = len(f2)
        feasi_secure_dom.append(f2)
        feasi_secure_dom_len.append(h2)
        #min_list.append(f2)
    '''e1.clear()
    e2.clear()
    f1.clear()'''

#crossover

def Crossover(l111,l222):
    v1 = v2 = 0
    while v1 == v2 :
        v1 = random.randrange(len(v))
        v2 = random.randrange(len(v))
    #print(v1,v2)
    i = min(v1,v2)
    j = max(v1,v2)
    for k in range(i+1,j):
        l111[k], l222[k] = l222[k], l111[k]
    '''print("after crossover chromosomes ")
    print(l111)
    print(l222)'''

# selection of patents
#print(list1)
min1 = sys.maxsize
min_list = []
min_list2 =[]

#method1 for selecting parents
for i in list1:
    if len(i) < min1:
        min1 = len(i)
#print(min1)
for i in list1:
    if len(i) == min1:
        min_list.append(i)
#print(min_list)
for i in min_list:
    if i not in min_list2:
        min_list2.append(i)
#print(min_list2)

'''#method 2 for selecting parents
for i in list1:
    if i not in min_list:
        min_list.append(i)
#print(min_list)'''
for k123 in range(1):
    feasi_secure_dom2 = []
    for i123 in range(1000):
        l11 = random.choice(min_list2)
        #print(l11)
        #min_list2.remove(l11)#(dought)
        #print(min_list2)
        l22 = random.choice(min_list2)
        #print(l22)

        '''l11 = random.choice(min_list)
        #min_list.remove(l11)
        #print(min_list)
        l22 = random.choice(min_list)'''


        '''print("selected parents are ")
        print(l11)
        print(l22)'''

        l111 = []
        l222 = []
        for i in range(len(v)):
            l111.append(0)
            l222.append(0)

        for i in l11:
            l111[i] = 1
        for j in l22:
            l222[j] = 1
        '''print("chromosomes of parents are ")
        print(l111)
        print(l222)'''
        Crossover(l111,l222)

        #feasibility
        d1 = [] 
        d11 = []
        d2 = []
        d22 = []
        e1 = []
        e2 = []
        f1 = []
        f2 = []
        gk1 = []
        gk2 = []
        gk3 = []
        gk4 = []
        gk5 = []
        feasi_secure_dom = []
        #feasi_secure_dom2 = []
        for i in range(len(l111)):
            if l111[i] == 1:
                #d1.append(i+1)
                d1.append(i)
        for i in range(len(l222)):
            if l222[i] == 1:
                #d2.append(i+1)
                d2.append(i)
        # d1 and d2 are after crossover childs
        '''print("after crossover childs are ")
        print(d1)
        print(d2)'''
        for i in v:
            if i not in d1:
                d11.append(i)
        for i in v:
            if i not in d2:
                d22.append(i)
        #print(d11)
        #print(d22)
        #print("after feasibility check childs are ")
        feasibility(adjacencyList,d1,d11)
        feasibility(adjacencyList,d2,d22)
        #print(" ")
    #print(feasi_secure_dom_len)
    
    for i in feasi_secure_dom_len:
        if i not in feasi_secure_dom_len2:
            feasi_secure_dom_len2.append(i)
    #print(feasi_secure_dom_len2)
    #print(feasi_secure_dom)
    
    for i in feasi_secure_dom:
        if i not in feasi_secure_dom2:
            feasi_secure_dom2.append(i)
    #print(feasi_secure_dom2)
    nm = min(feasi_secure_dom2)
    if nm not in min_list2:
        min_list2.append(nm)
    bb11 = random.choice(min_list2)
    bb22 = random.choice(min_list2)
    bb111 = []
    bb222 = []
    for i in range(len(v)):
        bb111.append(0)
        bb222.append(0)
    for i in bb11:
        bb111[i] = 1
    for j in bb22:
        bb222[j] = 1
    Crossover(bb111,bb222)
    dd1 = []
    dd11 = []
    dd2 = []
    dd22 = []
    for i in range(len(bb111)):
        if bb111[i] == 1:
            #dd1.append(i+1)
            dd1.append(i)
    for i in range(len(bb222)):
        if bb222[i] == 1:
            #dd2.append(i+1)
            dd2.append(i)
    for i in v:
        if i not in dd1:
            dd11.append(i)
    for i in v:
        if i not in dd2:
            dd22.append(i)
    feasibility(adjacencyList,dd1,dd11)
    feasibility(adjacencyList,dd2,dd22)
#print(feasi_secure_dom_len)
for i in feasi_secure_dom_len:
    if i not in feasi_secure_dom_len2:
        feasi_secure_dom_len2.append(i)
#print(feasi_secure_dom_len2)
print("The secure domination number is ",min(feasi_secure_dom_len2))
end = time.time()
print("time taken by the program is ",(end - start),"seconds")






