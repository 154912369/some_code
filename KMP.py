pattern="abcabd"
search_str="abcabcabcabd"
next_pointer=[0] #表示下次比较的地址

i=1 #表示第i个节点的next_ans
compare_pointer=0 # 表示前缀的最后一个char 再加一
while i<len(pattern):
    if pattern[i]==pattern[compare_pointer]:
        next_pointer.append(next_pointer[i-1]+1)
        compare_pointer+=1
        i+=1
    elif compare_pointer==0:
        next_pointer.append(0)
        i+=1
    else:
        #表示最大前后字串在 next_pointer[compare_pointer-1]-1子内
        compare_pointer=next_pointer[compare_pointer-1]



start=0 # 表示search_str正在比较的值
compare_pointer=0 # 表示前缀的最后一个char 再加一
while start<len(search_str):
    if search_str[start]==pattern[compare_pointer]:
        start+=1
        compare_pointer+=1
    elif compare_pointer!=0:
        compare_pointer=next_pointer[compare_pointer-1]
    else:
        start+=1
    if compare_pointer==len(pattern):
        print(len(search_str),start)
