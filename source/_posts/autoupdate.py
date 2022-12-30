import os,time
l=os.listdir()
a=[]
for i in l:
    if i.split(".")[-1]=="md":
        a.append(i)
for p in a:
    mtime=os.stat(p).st_mtime
    with open(p,"r",encoding="utf-8") as f:
        txt=f.read()
    front=txt.split("---")[1]
    if not "updated" in front:
        with open(p,"w",encoding="utf-8") as f:
            tfront=front+"\nupdated: "+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(mtime)))+"\n"
            txt=txt.replace(front,tfront)
            f.write(txt)
    else:
        pass
        # f.write(txt)
        # # tfront=front+"\nupdated: "+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(os.stat(p).st_mtime)))
        # # txt.replace(front,tfront)
        # # f.write(txt)