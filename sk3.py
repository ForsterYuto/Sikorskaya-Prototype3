#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import random

def main():
    st.title('革命的プロレタリア知能・シコルスカヤ試作機1号')
    word = st.text_input(label="同志の名前を入力してください！")
    name = word
    
    selected_item = st.selectbox('ご用件を選択してください',
                                 ['項目', 'おみくじ', '運勢ポイント', '人権ポイント', 'ソーシャルクレジット'])
    if selected_item == "おみくじ":
        unsei = ["ウルトラ吉","スーパー吉","テラ吉","ギガ吉","メガ吉","大大吉","大吉","中吉","吉","小吉","末吉","凶","大凶","大大凶","ウルトラ凶","絶望","死","惨死","阿鼻叫喚","奈落","末代まで祟られている"]
        list_len = len(unsei)
        num = random.randrange(list_len)
        st.write("シコルスカヤ：" + name + "同志の運勢は『" + str(unsei[num]) + "』です！")
    
    elif selected_item == "運勢ポイント":
        num=random.randrange(1,7875000000)
        point=random.randrange(1,999)
        st.write("シコルスカヤ：同志"+name+"の運勢ポイントは"+str(point)+"プロレタリアポイント、\n 世界第"+str(num)+"位です！")
    
    elif selected_item == "ソーシャルクレジット":
        num=random.randrange(0,125459999)
        point=random.randrange(0,9999999)
        st.write("シコルスカヤ：現在の同志" + name + "のソーシャルクレジットは" + str(point) + "ポイント、日本第" + str(num) +"位です。")
    
    elif selected_item == "人権ポイント":
        num=random.randrange(0,125459999)
        point=random.randrange(0,9999999)
        st.write("シコルスカヤ：現在の同志" + name + "の人権ポイントは" + str(point) + "ポイント、日本第" + str(num) +"位です。\nあるいは最高位人権道徳者を目指しなさい。")
    
    elif selected_item == "項目":
        st.write("同志のご用件は何ですか")


if __name__ == '__main__':
    main()

