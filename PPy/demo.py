#num=1
#string='1'
#num2=int(string) 
#print(num+num2)   
#words='words' * 3
#print(words)

#word='a loooooong word'
#num = 12
#string ='zhurui!'
#total =string*(len(word)-num)
#print(total)

#name ='My Name is Mike'
#
#print(name[0])
#print(name[-4])
#print(name[11:14])
#print(name[11:15])
#print(name[5:])
#print(name[:5])

#word ='friends'
#find_the_evil_in_your_friends=word[0]+word[2:4]+word[-3:-1]
#print(find_the_evil_in_your_friends)


#url = 'http://ww1.site.cn/14d2e8ejogbxdxhj20ci0kuwex.jpg'
#fileName=url[-10:]
#print(fileName)

#phone_number='1386-666-0006'
#hiding_number=phone_number.replace(phone_number[: 9],'*' * 9)
#print(hiding_number)


#earch='168'
#num_a='1386-168-0006'
#num_b='1681-222-ooo6'
#print(search+' is at '+str(num_b.find(search)+ 1)+' to '+str(num_b.find(search)+len (search))+' of num_ b')
#print(search+' is at '+str(num_a.find(search)+ 1)+' to '+str(num_a.find(search)+len (search))+' of num_ a')


#字符串 替换,遮挡

#search='168'
#num_a='1386-168-0006' #1386-168-0006
#num_b='1681-222-0006' #1681-222-0006
#
#aaa_a=num_a.find(search) #5
#bbb_b=num_b.find(search) #0
#
#search_l=len(search)
#print(search+' is at '+str(aaa_a+1)+' to '+str(aaa_a+search_l)+' of num_a')  #168 is at 6 to 8 of num_a
#print(search+' is at '+str(bbb_b+1)+' to '+str(bbb_b+search_l)+' of num_b')  #168 is at 6 to 8 of num_b



# def fahrenheit_converter(C):
#     fahrenheit = C * 9/5+32
#     print(fahrenheit)+'˚ F'
 
# C2F=fahrenheit_converter(35)
# print(C2F)

#lyric_length=len('I Cry Out For Magic!')
#print(lyric_length)


#字符串格式化符

# str1 = '{} a word she can get what she {} for.'
# str2 ='{qwe} a word she cna get what she {verb} for.'
# str3 ='{1} a word she can get what she {0} for.'
  
# print(str1.format('came','with'))
# print(str2.format(verb='came',qwe='with'))
# print(str3.format('came','with'))


#str1 = 'xxx'
#str2 = ' ooo '
#str3 = 'bbb'
#'xxx' + ' ooo ' + 'bbb'
#print('nmjk')

#这是代码优化,将两行具有共性的代码进行合并
#open ('./demo.py','w').write("print'(123 Lian xi you hua )'")


#string (字符串的意思)是python种的一种数据类型
 #num = 1
 #string = '1'
 #print (num+string)
# 注:输出的结果是语法错误,因为不同的数据类型不能够进行合并,需要通过一些方法做转换



#num = 1
#string = '1' 
#num2 = 1
#string = num2
#print(num+num2)



#interesting (整数的意思)数据库类型的转换
 #num = 1
 #string ='1'
 #num2 =int(string)  #注:代码中只能缩写int,若写全称interesting结果会报错"名称整数未定义"
 #print(num+num2)



#words ="words"*3
#print(words)



#word = 'a loooooong word'
#num = 12
#string ='bang!'
#total =string * (len(word)-num)
#print(total) 
#输出结果：bang!bang!bang!bang!

#word = 'a loooooong word'
#num = 12
#string ='bang!'
#total =(len(word)-num)
#print(total)
#输出结果：4


#[ ] 字符串的索引、分片
 #练习1
# name = 'my name is zhourui'
#print(name[0])
#'m'
#print(name[-10])
#'i'
#print(name[11:17])
#'zhouru'
#print(name[11:16])
#'zhour'
#print(name[6:])
#'e is zhourui'
#print(name[:11])
#'my name is'

 #练习2
#word = 'friends'
#find_the_evil_in_your_feiends = word[0]+word[2:4]+word[-3:-1]
#print(find_the_evil_in_your_feiends)
#输出结果:fiend

 #练习3
#'http://wwl.site.cn/14d2e8ejwlexjogbxdxhj20ci0kuwex.jpg'
#'http://wwl.site.cn/85cc87jwlex23yhwws5hj20ci0kuwex.png'
#'http://wwl.site.cn/7802fnjaghnbja3nka3nj20ci0kuwex.jpg'
#'http://wwl.site.cn/749hjkagjak38hfak83nk20ci0kuwex.gif'
#url = 'http://wwl.site.cn/14d2e8ejwlexjogbxdxhj20ci0kuwex.jpg'
#file_name =url[-10:]
#print(file_name)
#输出结果：0kuwex.jpg



#replace 替换
 #练习1
#phone_number = '1535-391-0643'
#hiding_number = phone_number.replace(phone_number[:9],'*' *9)
#print(hiding_number)
#输出结果：*********0643

 #练习2
#search = '168'
#num_a ='1386-168-0006'
#num_b ='1681-222-0006'
#print(search + ' is at '+str(num_a.find(search)+ 1 )+' to '+str(num_a.find(search)) +' of num_a')
#print(search + ' is at '+str(num_b.find(search)+ 1 )+' to '+str(num_b.find(search)) +' of num_b')
#输出结果：168 is at 6 to 5 of num_a
#输出结果：168 is at 1 to 0 of num_b


#.format（） 格式  多用于填空
 #练习
#print('{} a word she can get what she {} for'.format('with','came'))
#输出结果:with a word she can get what she came for
#print('{preposition} a word she can get what she {verb} for'.format(preposition = 'with',verb ='came'))
#输出结果:with a word she can get what she came for




print('{0} a word she can get what she {1} for.'.format('with','came'))

