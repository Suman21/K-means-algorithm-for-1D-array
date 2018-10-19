import random
import sys
def cmp(a, b):
    return (a > b) - (a < b)
input1=input("Give comma(,) separated dataset:")
cluster=int(input("Enter number of cluster:"))
dataSet=input1.split(',')
myDict1={}
myDict2={}

try:
    means=random.sample(dataSet, cluster)
except ValueError:
    print("Number of cluster is greater than dataset!!!")
    sys.exit()

if cluster==1:
    print(dataSet)
elif cluster==len(dataSet):
    print(dataSet)
else:
    i=0
    while (i < cluster):
        myDict1[i]=[]
        myDict2[i]=[]
        i=i+1
    c=0
    while True and c<50:
        c=c+1
        minmumDist=sys.maxsize
        clusterNumber=-1
        for i in dataSet:
            minimumIndex=0
            minimumvalue=sys.maxsize
            key=0
            while(key<len(means)):
                if abs(int(means[key])-int(i))<minimumvalue:
                    minimumIndex=key
                    minimumvalue=abs(int(means[key])-int(i))
                key=key+1
            myDict1[minimumIndex].append(i)
        if(myDict1==myDict2):
            break
        for key in myDict1:
            sumOfCluster=0
            myDict2[key]=[]
            for j in myDict1[key]:
                sumOfCluster=sumOfCluster+int(j)
                myDict2[key].append(j)
            means[key]=sumOfCluster/len(myDict1[key])
            myDict1[key]=[]
        
    print(myDict2)