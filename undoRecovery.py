import sys

filepath = sys.argv[1] 
transaction_dict={}
start_ckpt_dict={}
prev_ckpt_dict={}
final_dict={}
tran=[]
res=[]
w=0
flag=0

with open(filepath) as fp:  
   line = fp.readline()
   if len(line):
        line=line[0:-1]
        list1=line.split(" ")
        for i in range(0,len(list1),2):
            final_dict[list1[i]]=list1[i+1]
   
   while line:
        line = fp.readline()
        if len(line)!=1  and len(line)!=0:
            line=line[1:-2]
            if line[0]=='T':
                list1=line.split(", ")
                res.append(list1)
            else:
                list1=line.split(" ")
                res.append(list1)
        else:
            line = fp.readline()
total_log=len(res)
for inst in range(total_log-1,-1,-1):
    if res[inst][0]=='COMMIT':
        tran.append(res[inst][1])
    if res[inst][0][0]=='T' and res[inst][0] not in tran:
        final_dict[res[inst][1]]=res[inst][2]
    if res[inst][0]=='START' and res[inst][1]=='CKPT':
        if flag==1:
            break
    if res[inst][0]=='END' and res[inst][1]=='CKPT':
        flag=1

ans=""

list_key=final_dict.keys()
list_key.sort()
for i in list_key:
    ans+=i+" "+final_dict[i]+" "
ans=ans[0:-1]
with open("2018201005_2.txt","w") as fp:
    fp.write(ans)
    fp.write("\n")
    fp.close()