# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:36:32 2020

@author: Administrator
"""

#傻瓜斗地主小程序
import time
import random

dic = {'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'10':8,'J':9,'Q':10,'K':11,'A':12,'2':13,'小王':14,'大王':15}
guize_dic = {'一张':1, '一对':2, '三个':300, '炸弹,四个':400, '王炸':11, '三带一':301, '三带一对':302, '小飞机':303, '四带一对': 402, '四带两个':411, '三连对':222, '四带两对':422, '四连对':2222, '顺子':888, '连对':666}
def strr_2_lst(strr): #出牌转换成列表
    strr = strr.strip()
    lst = strr.split(' ')
    return lst

def lst_paixu(lst):   #手牌排序
    new_lst = []
    for item in lst:
        new_lst.append((item, dic[item]))
    new_lst.sort(key=lambda x:x[1])
    lst.clear()
    for tup in new_lst:
        lst.append(tup[0])
    return lst, new_lst


def count_pai(new_lst):  #手牌同牌计次
    countpai = {}
    for tup in new_lst:
        countpai[tup[0]] = countpai.get(tup[0], 0) + 1
    items_lst = list(countpai.items())
    items_lst.sort(key=lambda x:x[1])
    if len(items_lst) > 1:
        for i in range(len(items_lst)):
            for j in range(i+1,len(items_lst)):
                if items_lst[i][1] == items_lst[j][1]:
                    if dic[items_lst[i][0]] > dic[items_lst[j][0]]:
                        a = items_lst[j]
                        items_lst[j] = items_lst[i]
                        items_lst[i] = a
    return items_lst


def print_(str_):   #连续输出风格
    print('\n')
    for item in str_:
        print(item, end='')
        time.sleep(0.05)
    print('\n')

def puke():     #创建一副扑克牌
    puke_1 = '3456789JQKA2' * 4
    pukepai = list(puke_1) + ['10', '10', '10', '10', '大王', '小王']
    return pukepai


def fapai():    #发牌4堆：玩家1，玩家2，玩家3，底牌
    wanjia_A = []
    wanjia_B = []
    wanjia_C = []
    dipai = []
    pukepai = puke()
    random.shuffle(pukepai)
    for i in range(0, 54, 3):
        if i <= 48:
            wanjia_A.append((pukepai[i], dic[pukepai[i]]))
            wanjia_B.append((pukepai[i+1], dic[pukepai[i+1]]))
            wanjia_C.append((pukepai[i+2], dic[pukepai[i+2]]))
        else:
            for item in pukepai[51:54]:
                dipai.append((item, dic[item]))
    wanjia_A.sort(key=lambda x:x[1])
    wanjia_B.sort(key=lambda x:x[1])
    wanjia_C.sort(key=lambda x:x[1])
    dipai.sort(key=lambda x:x[1])
    return wanjia_A, wanjia_B, wanjia_C, dipai


def kanpai():   #以字符串的形式显示手牌并记录上一次发的牌
    wanjia_A = ''
    wanjia_B = ''
    wanjia_C = ''
    dipai = ''
    lst = fapai()
    for i in range(4):
        for tup in lst[i]:
            for item in tup[0]:
                if i == 0:
                    wanjia_A += item
                elif i == 1:
                    wanjia_B += item
                elif i == 2:
                    wanjia_C += item
                else:
                    dipai += item
    return wanjia_A, wanjia_B, wanjia_C, dipai, lst


def xipai():   #洗牌进度条
    for i in range(1, 31):
        a = '😘' * i
        b = '😭' * (30-i)
        bili = (i/30) * 100
        time.sleep(0.2)
        print('\r{}: {:.1f}%[{}{}]'.format('小傻瓜洗牌完成' if bili == 100 else '小傻瓜在洗牌中', bili, a, b), end='')


def xuanpai():   #玩家选牌
    global youpai, Apai, Bpai, xuan_pai
    xuan_pai = []
    for item in kanpai():
        xuan_pai.append(item)
    ipt = input('输入(我爱小傻瓜)看牌：')
    if ipt in ['我爱小傻瓜', '(我爱小傻瓜)']:
        print_('小傻瓜也爱{}哟,先偷偷让你看牌哟'.format(chenghu))
        print_('{:^4}:显示\n{:^4}: {}\n{:^4}: {}\n{:^4}: {}\n{:^4}: {}'.format('编号', '玩家1', xuan_pai[0], '玩家2', xuan_pai[1], '玩家3', xuan_pai[2], '随机', '随机'))
        print_('现在轮到{}选择属于自己的扑克牌啦(❤ ω ❤)'.format(chenghu))
        ID = input('请输入编号: ')
        dic_1 = {'玩家1': 0, '玩家2': 1, '玩家3': 2}
        if ID in dic_1:
            you_pai = xuan_pai[dic_1[ID]]
            youpai = xuan_pai[4][dic_1[ID]]
            i_d = []
            for key in dic_1:
                if key != ID:
                    i_d.append(dic_1[key])
            Apai = xuan_pai[4][i_d[0]]
            Bpai = xuan_pai[4][i_d[1]]
        else:
            r = random.randint(0, 2)
            you_pai = xuan_pai[r]
            youpai = xuan_pai[4][r]
            i_d = []
            for key in dic_1:
                if dic_1[key] != r:
                    i_d.append(dic_1[key])
            Apai = xuan_pai[4][i_d[0]]
            Bpai = xuan_pai[4][i_d[1]]
    else:
         xuanpai()
    print_('你的手牌是: {}'.format(you_pai))


def jiaodizhu():
    global youpai, xuan_pai, new_you_pai
    print_('亲爱的{},你的手牌这么好，叫个地主吧(●ˇ∀ˇ●)'.format(chenghu))
    j = input('我要叫地主(Y or N)：')
    if j in ['Y', 'y']:
        new_you_pai = ''
        youpai += xuan_pai[4][3]
        youpai.sort(key=lambda x:x[1])
        for tup in youpai:
            for item in tup[0]:
                new_you_pai += item
        dipai = xuan_pai[3]
        print_('底牌是:{}'.format(dipai))
        print_('{}地主你好,你的手牌是: {}'.format(chenghu, new_you_pai))
    else:
        jiaodizhu()


def shunzi(lst, new_lst):
    for item in lst:
        if item in ['2', '小王', '大王']:
            return False  #不是顺子
    for i in range(len(new_lst)-1):
        if (new_lst[i+1][1] - new_lst[i][1]) != 1:
            return False   #不是顺子
    else:
        return True  #是顺子


def liandui(lst, new_lst):
    for item in lst:
        if item in ['2', '小王', '大王']:
            return False  #不是连对
    for i in range(0, len(new_lst)-2, 2):
        if (new_lst[i+2][1] - new_lst[i][1]) != 1:
            return False   #不是连对
    else:
        return True  #连对


def xianshi_chupai(lst):
    global mark_xianshi_chupai
    new_lst = lst_paixu(lst)[1]
    items_lst = count_pai(new_lst)
    chupai = ''
    for item in items_lst[::-1]:
        chupai += item[0] * item[1]
    ID = guize(lst)
    if ID:
        for key in guize_dic:
            if guize_dic[key] == ID:
                print("\033[1;31;40m{}:{}\033[0m".format(key, chupai))
                mark_xianshi_chupai = True
    else:
        print("\033[1;31;40m按规则出牌哟,重新出牌！\033[0m")
        mark_xianshi_chupai = False      
               
def guize(lst):
    new_lst = lst_paixu(lst)[1]
    items_lst = count_pai(new_lst)
    if len(items_lst) == 1:
        if items_lst[0][1] == 1:
            return 1  #单张
        elif items_lst[0][1] == 2:
            return 2  #对子
        elif items_lst[0][1] == 3:
            return 300  #三不带
        else:
            return 400 #四个炸弹
    elif len(items_lst) == 2:
        if len(new_lst) == 2:
            if new_lst==['小王', '大王']:
                return 11 #王炸
            else:
                return False  #出牌不符合规则
        elif len(new_lst) == 4:
            if items_lst[1][1] == 3:
                return 301  #三带一
            else:
                return False  #出牌不符合规则
        elif len(new_lst) == 5:
            if items_lst[1][1] == 3:
                return 302  #三带二
            else:
                return False #出牌不符合规则
        elif len(new_lst) == 6:
            if items_lst[0][1] == 3:
                return 303 #小飞机
            else:
                return 402 #四带一对
        else:
            return False    #出牌不符合规则
    elif len(items_lst) == 3:
        if len(new_lst) == 6:
            if items_lst[2][1] == 4:
                return 411  #四带二
            elif items_lst[2][1] == 2:
                if liandui(lst, new_lst):
                    return 222   #三连对
                else:
                    return False   #出牌不符合规则
            else:
                return False   #出牌不符合规则
        elif len(new_lst) == 8:
            if items_lst[2][1] == 4:
                return 422 #四带两对
            else:
                return False   #出牌不符合规则
        else:
            return False   #出牌不符合规则
    elif len(items_lst) == 4:
        if len(new_lst) == 8:
            if items_lst[3][1] == 2:
                if liandui(lst, new_lst):
                    return 2222   #四连对
                else:
                    return False   #出牌不符合规则
            elif items_lst[2][1] == items_lst[3][1] == 3:
                return 313   #大飞机
            else:
                return False
        else:
            return False    #出牌不符合规则
    else:
        if shunzi(lst, new_lst):
            return 888   #顺子
        elif liandui(lst, new_lst):
            return 666   #连对
        else:
            return False   #出牌不符合规则


def youchu():  
    global youpai, new_you_pai, mark_xianshi_chupai, youchu_lst, mark_A_Bchu, mark
    _you_pai = []
    for item in youpai:
        _you_pai.append(item[0])
    print_('{}你好,你的手牌是: {}'.format(chenghu, new_you_pai))
    you_chu = input('牌之间空格隔开哟{比如连顺:7 8 9 10 J}: ')     
    youchu_lst = strr_2_lst(you_chu)
    if youchu_lst == ['']:
        print("\033[1;31;40m要不起！\033[0m")
        mark = True
    else:     
        for item in youchu_lst:
            if item in _you_pai:
                xianshi_chupai(youchu_lst)
                if mark_xianshi_chupai:
                    _you_pai.remove(item)
                else:
                    youchu()
            else:
                print("\033[1;31;40m不存在,重新出牌！\033[0m")
                youchu()
        new_you_pai = ''.join(_you_pai)
        print_('{}你好,你剩余的手牌是: {}'.format(chenghu, new_you_pai))
        youpai.clear()
        for item in _you_pai:
            youpai.append((item, dic[item]))
        mark = False
    mark_A_Bchu = False


def A_Bchu(ABpai):
    global Apai, Bpai, youchu_lst, mark_A_Bchu, mark
    if (youchu_lst == ['']):
        t = -1
        if ABpai == Apai:
            print_('{}:请让我思考该出啥！>>>'.format('小学学'))
        else:
            print_('{}:请让我思考该出啥！>>>'.format('小星星'))
        while not mark_A_Bchu:
            ABchu = []
            SUM = random.randint(1,len(ABpai))
            items = random.sample(ABpai, SUM)
            for item in items:
                ABchu.append(item[0])
            if guize(ABchu) in guize_dic.values():
                mark_A_Bchu = True
                for item in items:
                    ABpai.remove(item)
                break
    else:
        ID_str = str(guize(youchu_lst))
        SUM = len(youchu_lst)
        t = 0
        for i in range(1000):
            t += 1
            ABchu = []
            items = random.sample(ABpai, SUM)
            for item in items:
                ABchu.append(item[0])
            if guize(ABchu) == int(ID_str):
                ABchu_items_lst = count_pai(items)
                youchu_items_lst = count_pai(lst_paixu(youchu_lst)[1])
                if dic[ABchu_items_lst[-1][0]] > dic[youchu_items_lst[-1][0]]:
                    mark_A_Bchu = True
                    for item in items:
                        ABpai.remove(item)
                    break
        if mark_A_Bchu == False:
            for item in count_pai(ABpai):
                if item[1] == 4:
                    ABchu = list(item[0]*item[1])
                    for tup in ABpai:
                        if tup[0] in ABchu:
                            ABpai.remove(tup)
                            mark_A_Bchu = True
        if mark_A_Bchu == False:
            if ABpai[-2:] == [('小王', 14), ('大王', 15)]:
                ABchu = []
                ABchu.append(ABpai[-2][0])
                ABchu.append(ABpai[-1][0])
                ABpai.remove( ABpai[-2])
                ABpai.remove( ABpai[-1])
                mark_A_Bchu = True
    if youchu_lst == ['']:
        if ABpai == Apai:
            print_('{}:我出！>>>'.format('小学学'))
        else:
            print_('{}:我出！>>>'.format('小星星'))
        xianshi_chupai(ABchu)
    elif mark_A_Bchu:
        if ABpai == Apai:
            print_('{}:大你！>>>'.format('小学学'))
        else:
            print_('{}:大你！>>>'.format('小星星'))
        xianshi_chupai(ABchu)
    else:
        if ABpai == Apai:
            print_('{}:不要！>>>'.format('小学学'))
        else:
            print_('{}:不要！>>>'.format('小星星'))
    print(ABpai)
    print(t)


def chupai():
    global mark_A_Bchu, Apai, Bpai, youpai
    mark = False
    print_('亲爱的{},你是地主哦,请出牌\^o^/'.format(chenghu))
    while (len(youpai)>0) or (len(Apai)>0) or (len(Bpai)>0):
        if len(youpai) == 0:
            print_('{:-^20}'.format('恭喜你，你赢啦'))
        elif (len(Apai)==0) or (len(Bpai)==0):
            print_('{:-^20}'.format('/(ㄒoㄒ)/~~输了'))
        else:
            if (len(Apai)==2) or (len(Bpai)==2):
                print_('{:-^20}'.format('注意咯，我只有两张牌啦！！！'))
            youchu()
            if (mark_A_Bchu==False) and (mark==False):
                A_Bchu(Apai)
            else:
                print_('{}:不要！>>>'.format('小学学'))
            if not mark_A_Bchu:
                A_Bchu(Bpai)
                if mark_A_Bchu:
                    mark = True
            else:
                print_('{}:不要！>>>'.format('小星星'))
                mark = False

      
print_('嗨,请问你是GG还是MM？(自己脑补语音QAQ)')
chenghu = input("请输入称呼: ")
print_('{}你好,欢迎来到傻瓜斗地主，现在开始你的斗地主旅程吧QAQ❤'.format(chenghu))
print_('小傻瓜准备洗牌哦，请稍等')
xipai()
print_('亲爱的{},想看所有玩家的牌吗😏😏😏'.format(chenghu))
xuanpai()
jiaodizhu()
chupai()