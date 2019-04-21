import sys
transaction_dict={}
start_ckpt_dict={}
prev_ckpt_dict={}
final_dict={}
w=0
tran=[]
res=[]
flag=0
trans_dict=dict()
filepath = sys.argv[1] 
count_empty=0
with open(filepath) as fp:  
   line = fp.readline()
   if len(line):
        line=line[0:-1]
        list1=line.split(" ")
        for i in range(0,len(list1),2):
            final_dict[list1[i]]=list1[i+1]
#    print(line)
   while line:
        line = fp.readline()
        # print "------",line 
        if len(line)!=1  and len(line)!=0:
            # print 'bb ',line
            line=line[1:-2]
            if line[0]=='T':
                # print 'line',line
                list1=line.split(", ")
                # print "ddd",list1
                res.append(list1)
            else:
                list1=line.split(" ")
                res.append(list1)
        else:
            count_empty+=1
            if count_empty>1:
                break
            line = fp.readline()
            line=line[1:-2]
            list1=line.split(" ")
            res.append(list1)

total_log=len(res)
fg1=0
dict_len=0
# print(res)
for inst in range(total_log-1,-1,-1):
    print "ddd ",res[inst] 
    if res[inst][0]=='COMMIT':
        appen=res[inst][1]
        tran.append(appen)
    if res[inst][0][0]=='T' and res[inst][0] not in tran:
        index=res[inst][1]
        value=res[inst][2]
        final_dict[index]=value
    if res[inst][0]=='START' and res[inst][1]=='CKPT':
        if flag==1:
            # break
            listlen=len(res[inst])
            for k in range(2,listlen):
                str1=res[inst][k]
                if k==2:
                    a1=str1[1:-1]
                elif k>2 and k<listlen-1:
                    a1=str1[0:-1]
                else:
                    a1=str1[0:-1]
                print("a ",a1)
                trans_dict[a1]=0
                fg1=1
                dict_len=len(trans_dict)
                # count_t
                
    if res[inst][0]=='END' and res[inst][1]=='CKPT':
        flag=1
    if res[inst][0]=='START' and res[inst][1]!='CKPT' and fg1==1:
        print("ss ",res[inst][1])
        trans_dict[res[inst][1]]=1
    if dict_len!=0:
        print(dict_len)
        r1=0
        for key,value in trans_dict.items():
            print("dd ",key," ",value)
            if value!=0:
                r1=r1+1
        if r1==dict_len:
            break



ans=""

list_key=final_dict.keys()
# print(list_key)
list_key.sort()
ans1=""
for key,values in final_dict.items():
    ans1+=key+" "+values+" "
for i in list_key:
    ans+=i+" "+final_dict[i]+" "
ans=ans[0:-1]
with open("2018201065_2.txt","w") as fp:
    fp.write(ans)
    fp.write("\n")
    fp.close()
    

