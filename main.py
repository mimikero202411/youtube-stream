import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit 超入門")
######################################################################################
#   13.Webアプリの公開
######################################################################################
st.write("Webアプリの公開==================================================")
st.write("Webアプリの公開")

st.write("")
st.write("")
st.write("")
######################################################################################
#   12.プログレスバーの表示
######################################################################################
st.write("プログレスバーの表示==================================================")
#import time
"開始! しばらくお待ちください"
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
   latest_iteration.text(f"進行状況: {i+1}")
   bar.progress(i+1)
   time.sleep(0.1) #0.1秒
"完了!"
st.write("")
st.write("")
st.write("")
######################################################################################
#   11.レイアウトを整える
######################################################################################
st.write("サイドバー==================================================")
st.sidebar.write("サイドバー")
text=st.sidebar.text_input("あなたの趣味を教えてください。")
condition=st.sidebar.slider("あなたの今の調子は?",0,50,100)
"あなたの趣味は「",text,"」ですね。"
"あなたのコンディションは「",condition,"」ですね。"
st.write("2カラムのレイアウト==================================================")
st.write("画像を左右に並べて配置する時などに使う")
#left_column,right_column=st.beta_columns(2)  ※今はbeta_columns廃止
left_column,right_column=st.columns(2)
button=left_column.button("クリックすると右カラムに文字を表示")
if button:
   right_column.write("ここは右カラム") 
if left_column.button("クリックすると右カラムに文字を表示2"): #上と同じ効果
   right_column.write("ここは右カラム") 
st.write("エクスパンダー==================================================")
st.write("質問をクリックすると回答を表示します。")
expander=st.expander("質問1　〇〇〇〇〇〇")
expander.write("回答　〇〇〇〇〇〇〇〇〇〇〇〇")
expander.write("〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇")
expander.write("〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇")
expander=st.expander("質問2　〇〇〇〇〇〇")
expander.write("回答　〇〇〇〇〇〇〇〇〇〇〇〇")
expander.write("〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇")
expander.write("〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇〇")

# streamlitのAPIリファレンス:Displsy Interactive widget
#    https://docs.streamlit.io/develop/api-reference
st.write("")
st.write("")
st.write("")
######################################################################################
#   10.インタラクティブなウィジェット
######################################################################################
st.write("チェックボックスで画像の表示・非表示==================================================")
if st.checkbox("画像ON-OFF"):
    img=Image.open("Screenshot.png")
    st.image(img,caption="ScreenShot",use_container_width =True)
st.write("セレクトボックス==================================================")
option=st.selectbox(
    "1～10の間であなたが好きな数字を教えてください。",
    list(range(1,11))
)
st.write("あなたが好きな数字は「",option,"」ですね。") #下とどちらも同じ 
"あなたが好きな数字は「",option,"」ですね。"
st.write("テキスト入力==================================================")
text=st.text_input("あなたの趣味を教えてください。",key=2)
"あなたの趣味は「",text,"」ですね。"
st.write("スライダー==================================================")
condition=st.slider("あなたの今の調子は?",0,50,100,key=3)
"あなたのコンディションは「",condition,"」ですね。"

# streamlitのAPIリファレンス:Displsy Interactive widget
#    https://docs.streamlit.io/develop/api-reference
st.write("")
st.write("")
st.write("")
######################################################################################
#   9.Streamlitの基本的な使い方
######################################################################################
st.write("DataFrame(表)==================================================")
df =pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})
st.write("st.write")#--------------------
st.write(df)    #表の表示(動的な表:Web上でSortもできる)
#dataframeも表の表示 書式を設定できる(動的)
st.write("st.dataframe")#-----------------
st.dataframe(df.style.highlight_max(axis=0,color="red"),width=400,height=200)
#tableも表の表示 書式を設定できる(静的:sort出来ない。幅等指定できない)
st.write("st.table")#-------------------------
st.table(df.style.highlight_max(axis=0,color="blue"))
# streamlitのドキュメントのAPIリファレンスに様々な書式の記述方がある
#    https://docs.streamlit.io/develop/api-reference

st.write("マークダウン(テキスト)==============================================")
"""
# 章
## 節
### 項

バッククォーテーション「`」はShift+@で打つ\\
バッククォーテーション3つに続きpythonと記述すると、\\
下行にpythonコードが書け、それらをバッククォーテーション3つで閉じると、\\
Web上で表示されたpythonコードがコピーできる(pythonコード解説等に使える)
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
# 同様に、streamlitのドキュメントのAPIリファレンスのMagicのText elementsに
# 様々な書式の記述方がある
#    https://docs.streamlit.io/develop/api-reference

st.write("Chart(グラフ)==============================================")
df2 =pd.DataFrame(
    np.random.rand(20,3),    #20×3の行列をramdom生成
    columns=["a","b","c"]
)
st.line_chart(df2) #折れ線グラフ
st.area_chart(df2) #折れ線面グラフ
st.bar_chart(df2)  #棒グラフ

st.write("map(地図)==============================================")
df3 =pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],    
    #100×3の行列をramdom生成, /50で範囲を狭くする
    # 　　　　　+[35.69,139.70]で新宿付近の緯度経度を生成
    columns=["lat","lon"]  #緯度:"lat",経度:"lon"がパラメータ
)
st.map(df3)   #ブロット地図

st.write("Display Image(画像)==============================================")
img=Image.open("スクリーンショット.png")
st.image(img,caption="ScreenShot",use_column_width=True)
# 同様に、streamlitのドキュメントのAPIリファレンスのDisplay Mediaに
# 様々な書式の記述方がある　　(音楽、ビデオも表示できる)
#    https://docs.streamlit.io/develop/api-reference



