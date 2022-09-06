#!/usr/bin/env python
# coding: utf-8

# # 1. データの読み込み
# ここでは、test.csvファイルをDataframeの形で読み込みます。

# In[ ]:


import pandas as pd


# In[ ]:


df = pd.read_csv("test.csv", encoding="utf-8", index_col=0)
df


# In[ ]:


df1 = pd.read_csv("test.csv", header=None)
df1


# In[ ]:


df2 = pd.read_csv("test.csv", header=0)
df2


# In[ ]:


df3 = pd.read_csv("test.csv", header=1)
df3


# # 2. さまざまなグラフ

# In[ ]:


import matplotlib.pyplot as plt


# ## 2-1. 折れ線グラフ
# 時系列データの変動を可視化

# In[ ]:


# Matplotlibでの日本語表示
# (参考)https://www.yutaka-note.com/entry/matplotlib_japanese
plt.rcParams['font.family'] = "MS Gothic"

df.plot()


# In[ ]:


df.plot(y='A大学')


# In[ ]:


df.plot(y=['A大学', 'B大学'])


# In[ ]:


df.plot(subplots=True, figsize=(28.00, 10.00), grid=True ,lw=3, ylim=(1000, 5000))
plt.subplots_adjust(hspace=0.1)


# In[ ]:


df.plot(y=["A大学", "B大学"], xlabel="年度", ylabel="学生数", title="入学者数の変遷")


# In[ ]:


df.plot(y=["A大学", "B大学"], xlabel="年度", ylabel="学生数")
plt.legend(loc="upper left")


# In[ ]:


df.plot(y=["A大学", "B大学"], xlabel="年度", ylabel="学生数")
plt.legend(loc=(0.01, 0.8))


# In[ ]:


df.plot(y=["A大学", "B大学"], xlabel="年度", ylabel="学生数")
plt.legend(loc=(0.01, 0.8) ,ncol=2)


# **折れ線グラフの主要な引数**
# 
# - linewidth：線の太さ
# - linestyle：線の種類（solid（実践　※デフォルト）, dashed（破線）, dashdot（破線＆点線）, dotted（点線））
# - color：線の色
# - marker：マーカの種類（“.”（ポイント）,“o”（円）,  “^”（上向き三角形）, ・・・）
# - markersize：マーカの大きさ

# ## 2-2. ヒストグラム
# データの分布を可視化しやすい

# In[ ]:


plt.hist(df["A大学"])


# In[ ]:


plt.hist(df["A大学"], bins=2)
plt.savefig("test.png")


# In[ ]:


plt.savefig("test.png")


# In[ ]:


import seaborn as sns
sns.distplot(df["A大学"], kde=False, rug=False, bins=5) 
plt.show()


# ## 2-3. 円グラフ
# ある量に占める内訳を可視化しやすい

# In[ ]:


df


# In[ ]:


df.iloc[:,3]


# In[ ]:


df.iloc[:,3].plot.pie()


# In[ ]:


df.loc[["2019年"]]


# In[ ]:


df.loc[["2019年"]].plot.pie()
# エラーが返ってきます。


# In[ ]:


df.loc[["2019年"]].plot.pie(subplots=True)
# こんなはずではなかったグラフ


# In[ ]:


df.T


# In[ ]:


df.T.iloc[:,1].plot.pie()


# In[ ]:




