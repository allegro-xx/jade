
# coding: utf-8

# import PyJade_OutputHtml as pyJade
# run as
# pyJade.build_pyzaim(2017)


# # PyJade
# 
# + Store Zaim Data
# + Export Monthly HTML Files
# + python実行するには、pythonファイルとしてダウンロードしpyJade_outputHtml.pyに変更するだけでOK
# + v2.4 17/9/10 - 
#  + issue#377 Monthly/Report 高額リストにカテゴリ順、と記載
#  
# + v2.3 17/5/28 - 6/4
#  + Yearly/Qレポートのカテゴリに住居を追加
#  + Yearly/Qレポートのカテゴリに社会保障から投資・貯金を独立
#  + Yearly/Qレポートのカテゴリのそれぞれの項目がどういうジャンルを含むかを記載。 
# 
# + v2.1 17/1/14 - 1/29
#  + 2017年対応 年のハードコーディングを修正した
#  + print_nonPaymenttableの誤り訂正
#  + issue#272 Yearly Reportに金融資産残高に対応 (手入力)
#  + issue#000 Monthly/YearlyにFPレポートを掲載
#  + issue#000 テーブルの幅に最小値を設定した
#  + issue#000 確定申告レポートをYearlyに掲載した
#  + issue#000 bug Cookieの名前をそれぞれのページ(monthly, yearly, total)でわけて、それぞれのページを移動した際にtabが保存されるようにした
#  
# + rev1.16 -> v2.0にした 12/18
#  + issue#000	スクリプト化。このファイルをpython形式<pyJade_outputHtml.py>で書き出せばOK。
#  + issue#000 	iPhone対応はこのファイルをforkすれば良さそう
#  + issue#000 	weekly reportは検討中 (保留)
# + rev1.14 12/4-12/10
#  + issue#297	レポート名をQuarterly, YearlyからYearly, Totalに変更した
#  + issue#297	Quarterly ReportをYearly Reportに変更, Yearly ReportをTotal Reportに変更"
#  + issue#298	Yearly Reportを、レポート(M), レポート(Q)にする。
#  + issue#299	出費詳細のタブは上に持って来る
#  + issue#300	Yearly Reportのグラフを グラフ(M), グラフ(Q),にする
#  + issue#175	金融資産まとめがない (Yearly月ごと)
#  + issue#177	立替まとめ (Yearly月ごと)
#  + issue#178	入金まとめ (月ごと)
#  + issue#266	変動費はカテゴリごとに分ける
#  + issue#302	カテゴリ計の計算が合っているか (小遣い、家賃、住まいの項目)
#  + issue#303	Yearly Detail: 銀行口座、積み立てをそれぞれで表に変更した。
#  + issue#304	Yearly Report 養育費が足りてない：小遣いが入ってない。→教育・教養に名前を変える
#  + issue#305	Monthly Report 養育費が足りてない：書籍が入ってない。
#  + issue#306	 家具・家電が変動費に入ってる。住まいに入れる
#  + issue#307	"Yearly Reportの最後の表が1月から始まってる&小計がない"
#  + issue#308	月ごとの小計が間違ってた
#  + issue#309	"Yearly Reportの月次表について高めのもの安めのものを色分けし、高めのものにはTOP3をポップオーバー表示する"
#  + issue#267	入金・振替はたかとさえで分ける
#  + issue#268	口座もたかとさえで分ける
# 
# + rev1.13 : 11/28 - 12/3
#  + issue283: レポート出力の実装
#   + add below
#   + get_genressummaly
#   + getBiggerAmountforReport
#   + getBiggerAmountinGenreforReport
#   + getGenrescount
#   + getGenresdeltaforReport
#   + getRestaurantforReport
#   + datetxt2class = lambda txt:dt.strptime(txt,  '%Y-%m-%d')
#   + getTatekaetextforReport
#   + getMonthlydeltaforReport
#   + getReportText
#  + issue284, 287-292, 294-296: レポート出力の修正 (Summaryタブの追加など)
# + rev1.12 : 16/11/19 ~ 28
#  + issuexxx: todoリストに公共料金を追加。print_monthly_checklist
#  + issuexxx: ファイル出力先を output/jadeに変更した。mod:build_pyzaim, ftpput
#  + issue280: dbの保存先を./dbに変更した
#  + issue279: 銀行口座の支出名前2文字目までが日付の数値な場合、日付として扱うようにした。mod print_banktable
#  ex) [23 UFJ入金]を[23日/UFJ入金]とした
#  + issue285: 上記により銀行の日付がバラバラになったので修正。 add get_bankdata
#  + issue286: 出納リストの入出金が色分けされていなかった mod print_banktable
#  + issue281:詳細タブ出力の順序変更 mod get_detailtabbody
#  + issue282:レポートタブ出力の順序変更 mod get_reporttabbody
#  + issue261: 高額出勤リストのはじめに生活費(101)が来るように修正 mod select_ExpenceData
#  
# + rev1.11: 16/11/12 ~ 
#  + issue194: 公共料金チェックリストにした mod get_detailtabbody, add checkPediodicalfees
#  + issue273, 274: テーブル右上の小計を500円単位の四捨五入にした
#  + issue275: 月次で確認する事項のチェックリストを登録した add print_monthly_checklist(rubyからのcopy) mod select_nonPaymentData
#  + issue276: mod:print_nonPaymenttableの対象口座IDから郵貯などが抜けてた
#  + issue277: round500について,250円未満のときは100円刻みで四捨五入する
#  + mod print_nonpaymenttable 立替・振替リストと銀行リストの両方を出力するようにしていたので分けた
#  + issue259: 振替・入金リストを振替・立替詳細リストにする。 add get_tatekaeData, mod print_nonPaymenttable
# 
# + r3(1.9):
#  + いらない行の削除
#  + issue149: select_expencedataが漏れていたので対応。
#  + issue250: カテゴリごとのサマリを削除して、ジャンルごとのサマリをトップに持ってくる get_reporttabbody (del summarytable)
#  + issue251: 月度詳細：変動と大型について何が含まれているかを表に書く
# 
# + r2(1.8): 
#  + issue149: SQLのGroup byを止めてpython側で集計するようにした。(select_WholeData, select_categorydata, select_genredata)
#  + issue244: 高額リストから社会保障を除去。select_ExpenceData
#  + issue245: 高額リスト、チェックリストに条件を記載 print_moneytable
#  + issue246,247: 口座出納があっていない。コメント欄は左寄せ。 print_nonPaymenttable, print_banktable
#  + issue240,248: genre表に各月の合計金額と、各月のカテゴリごとの合計金額を記載する get_genrestable
#  + issue239,249: genre表にシッター代・家賃・小遣いを追加。家賃と家財は家関係として独立。detailgenres
#  

# In[1]:

# import pyJade_outputHtml
# pyJade_outputHtml.build_pyzaim()


# ## Store Zaim Data

# In[2]:

from datetime import datetime as dt
import calendar
import datetime
import sqlite3
from ftplib import FTP
import os
import statistics

DB="db/pyzaim_160422.sqlite3"
TABLE = "zaim"


# In[3]:

get_monthday = lambda year,month:["{year}-{month:02d}-{day:02d}".format(year=year,month=month,day=i+1) 
                                  for i in range(0,calendar.monthrange(year, month)[1])]
get_monthes = lambda year:["{year}-{month:02d}".format(year=year, month=month) for month in range(1,13)]


# In[ ]:




# In[4]:

def get_monthlyfrontgraph(objYearMonth):

    objYear = objYearMonth[0]
    objLYear = get_lastyear(objYearMonth[0])

    objYearMonthes = []
    for m in range (1,objYearMonth[1]+1):
        objYearMonthes.append((objYearMonth[0], m))

    tyearamount = get_monthes_amount(objYearMonthes)['all']
    # tyearamount = get_yearly_amount(objYear)['all']
    lyearamount = get_yearly_amount(objLYear)['all']

    if lyearamount == 0:
        lyearamount = 2400000


    #print(objYear)
    #print(tyearamount)
    #print(lyearamount)
    yearlyamountratio = int(tyearamount/lyearamount*100*10)/10


    headergraph1 = """
        <h4>{y}年{m}月のレポート</h4>
        <a href="./i/m{y}-{m:02}.html">iPhone版はこちら</a>

        <!-- ### Header Graph Area ここから ### -->
        <div class="container">
          <div class="col-sm-2 hidden-xs"></div>
          <div class="col-sm-6 hidden-xs">
            <canvas id="myChartDN"></canvas>
          </div>
          <div class="col-sm-1 col-xs-12" style="padding-top:30px;">
          """.format(y=objYearMonth[0],m=objYearMonth[1])
    if yearlyamountratio < 75:
        btndecoration = "primary"
    elif yearlyamountratio < 95:
        btndecoration = "warning"
    else:
        btndecoration = "danger"
    
    kingaku = """btn-{btndec}">
        <small class="text-info">{y}年の{m}月までの使用額</small>
        <br>{yen:,}円""".format(
        btndec = btndecoration, 
        y=objYearMonth[0],m=objYearMonth[1],
        yen=tyearamount)
    ritsu = """btn-{btndec}">
        <small class="text-info">{y}年の{m}月までの前年比<br>使用率</small>
        <br>{ratio}%""".format(
        btndec = btndecoration, 
        y=objYearMonth[0],m=objYearMonth[1],
        ratio=yearlyamountratio)


    headergraph2 = """
            <h4><a href="#" class="btn {kingaku}</a></h4>
            <h4><a href="#" class="btn {ritsu}</a></h4>
            """.format(kingaku = kingaku, ritsu = ritsu)

    headergraph3 = """
          </div>
          <div class="col-sm-3 hidden-xs"></div>

            <script>
                  var data = {
                      labels: [
                      ],
                      datasets: [
                          {"""

    if yearlyamountratio < 75:
        gratio = yearlyamountratio
        gcolor = "#008cba" # blue
    elif yearlyamountratio < 90:
        gratio = yearlyamountratio
        gcolor = "#e99002" # yellow
    elif yearlyamountratio <= 100:
        gratio = yearlyamountratio
        gcolor = "#f04124" # black
    elif yearlyamountratio > 100:
        gratio = 100
        gcolor = "#000" # black


    headergraph4 = """
                              data: [{ratio}, {invratio}],
                              backgroundColor: [
                                "{gcolor1}",
                                "#FFF"
                              ],
                              hoverBackgroundColor: [
                                "{gcolor1}",
                                "#FFF"
                              ],
                              borderWidth :[2,1],
                              borderColor : [
                              "#36A2EB",
                              "#36A2EB"
                              ],
                              """.format(
    ratio = gratio, invratio = 100 - gratio, gcolor1 =gcolor, gcolor2 = gcolor
    )


    headergraph5 = """
                              hoverBorderWidth: [1,1],
                              hoverBorderColor: [
                                  "#FF6384",
                                  "#FF6384",
                              ]
                          }]
                  };
                  var chartoption ={
                    title:{
                        display:true,
                        text:'今年の使用率'
                    }
                  };

                  var ctx = document.getElementById("myChartDN");
                  var myChart = new Chart(ctx, {
                      type: 'doughnut',
                      data: data,
                      options: chartoption
                          });


              </script>

        </div>
        <!-- ### Header Graph Area ここまで ### -->"""
    monthlyreport_headergraph = headergraph1 + headergraph2 + headergraph3 + headergraph4 + headergraph5
    return monthlyreport_headergraph



# In[5]:

# round500 = lambda x:round(x/500)*500

def round500(x):
    if x < 250:
        y = round(x/100)*100
    else:
        y = round(x/500)*500
    return y


# In[6]:

def connect_database(dbname="db/pyzaim_160422.sqlite3"):
#     DB = "./" + dbname
    con = sqlite3.connect(DB, detect_types = sqlite3.PARSE_DECLTYPES)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
#     print(DB)
    return cur


# In[7]:

# test v2.4

def select_from_sqlite(select):
    cur = connect_database()

    cur.execute(select)
    return cur.fetchall()    


def select_zeroAccount(objYearMonth):
    select = """select amount, zaim_date as date, category, category_id, genre , 
    place, max(name) as name, from_account , to_account 
    from {tablename} 
    where amount == 0 and 
    zaim_date like '{year}-{month:02}-%' and 
    mode == 'payment' 
    order by zaim_date 
    ;""".format(
        tablename = TABLE, year = objYearMonth[0], month = objYearMonth[1])    

    data1 = select_from_sqlite(select)
    


# In[8]:

# a = select_zeroAccount((2017,6))
# a


# In[ ]:




# In[ ]:




# In[9]:

def select_from_sqlite(select):
#     con = sqlite3.connect(DB, detect_types = sqlite3.PARSE_DECLTYPES)
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
    cur = connect_database()

    #cur.execute("select max(amount), name, sum(amount), zaim_date, place from zaim group by receipt_id")
    cur.execute(select)
    return cur.fetchall()    

# select
# localid:1, ['たか', 1], ['さえ', 4], ['家計', 7], [セブンカード,セブンカード 7992077]以外かどうか
# ['積立）たか', 827175], ['積立）さえ', 827184], ['積立）家計', 7656126], ['セブンカード・プラス・J(一体型)', 7943010]
# ['家の口座(UFJ)', 8105914]

def select_OutAccount(objYearMonth):
# 登録チェックリスト (対象口座外のリスト)
# account_idが1:たか, 4:さえ, 7:家計, 7992077:セブンカード, 8105914: 家の口座(UFJ), 
# 8105916: 家の口座 (ソニー), 8133263: 智花（ゆうちょ)
# でないもの。
# 

    select = """select sum(amount) as amount, zaim_date as date, category, category_id, genre , 
    place, max(name) as name, from_account , to_account 
    from {tablename} 
    where from_account_id not in (1,4,7,7992077,8105914,8105916,8133263) and 
    zaim_date like '{year}-{month:02}-%' and 
    mode == 'payment' 
    group by zaim_date,place,category_id  
    order by zaim_date 
    ;""".format(
        tablename = TABLE, year = objYearMonth[0], month = objYearMonth[1])    

    data1 = select_from_sqlite(select)
    
    # 
    select = """select sum(amount) as amount, zaim_date as date, category, category_id, genre , 
    place, max(name) as name, from_account , to_account 
    from {tablename} 
    where to_account_id not in (1,4,7, 8105937,8105914,8105916,8133263)  and 
    zaim_date like '{year}-{month:02}-%' and 
    mode != 'payment' 
    group by zaim_date,place,category_id  
    order by zaim_date 
    ;""".format(
        tablename = TABLE, year = objYearMonth[0], month = objYearMonth[1])    

    data2 = select_from_sqlite(select)

    data = data1 + data2

    
    return data

def select_OutAccount2015(objYearMonth):
# {0: [None, 0],
#  1: ['たか', 1],
#  2: ['生協', 2],
#  3: ['SUICA', 3],
#  4: ['さえ', 4],
#  7: ['家計', 7],
#  827175: ['積立）たか', 827175],
#  827184: ['積立）さえ', 827184],
#  862648: ['たか', 862648],
#  862650: ['さえ', 862650],
#  7656126: ['積立）家計', 7656126],
#  7943010: ['セブンカード', 7943010],
#  7992077: ['セブンカード', 7992077],
#  8092959: ['セブンカード・プラス・J(一体型)', 8092959],
#  8092961: ['三菱東京UFJ銀行 大森支店 普通 ****021 Eco通帳', 8092961],
#  8092980: ['ソニー銀行 円普通預金', 8092980],
#  8093016: ['ゆうちょ銀行 総合:*****-*****401(代表)', 8093016]}

    
    select = """select sum(amount) as amount, zaim_date as date, category, category_id, genre , 
    place, max(name) as name, from_account 
    from {tablename} 
    where from_account_id not in (1,4,7, 827175, 827184)  and 
    zaim_date like '{year}-{month:02}-%' and 
    mode == 'payment' 
    group by zaim_date,place,category_id 
    order by zaim_date 
    ;""".format(
        tablename = TABLE, year = objYearMonth[0], month = objYearMonth[1])    

    data = select_from_sqlite(select)
    return data

def select_fromAccount(objYearMonth,from_Account):
    select = """select amount, zaim_date as date, category, genre, place, name, from_account 
    from {tablename} 
    where from_account_id in ({from_account})  and 
    zaim_date like '{year}-{month:02}-%' 
    order by zaim_date;""".format(
        tablename = TABLE, year = objYearMonth[0], month = objYearMonth[1], from_account=from_Account)

    data = select_from_sqlite(select)
    return data

def select_toAccount(objYearMonth, to_Account):
    select = """select amount, zaim_date as date, category, genre, place, name, from_account, to_account  
    from {tablename} 
    where to_account_id in ({to_account})  and 
    zaim_date like '{year}-{month:02}-%' 
    order by zaim_date;""".format(
        tablename = TABLE, year = objYearMonth[0], month = objYearMonth[1], 
        to_account=''.join(str(to_Account))[1:-1], )
    

    data = select_from_sqlite(select)
    return data


    

def print_OutAccount(objYearMonth):
    moneydata = select_OutAccount(objYearMonth)
    print_moneydata(objYearMonth, moneydata)
    return moneydata
    


#    return


# In[10]:

def get_dbupdatetime_from_sqlite():
#     con = sqlite3.connect(DB, detect_types = sqlite3.PARSE_DECLTYPES)
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
    cur = connect_database()

    cur.execute("select dbupdate as utime from dbupdatetime order by utime")
    
    return cur.fetchall()    





# In[11]:

def select_OutCategory(objYearMonth):
    # 登録チェックリスト
    
    objCategory = [101, 
                # ('食費•日用品', 101),
           105,
                # ('公共', 105),
           25504225,
                # ('社会保障', 25504225),
           107, 109, 106, 108, 110,111,
                # ('積)住まい・家財', 106),('積)交際費', 107),('積)娯楽', 108),
                # ('積)教育・教養', 109),('積)医療・健康', 110)美容美容 111
           114, 
                # ('大型出費', 114),
           # 17503724, 11, 12, 13, 14, 15, 19,
                # ('事業所得', 15),('給与所得', 11),('立替金返済', 12),('賞与', 13),
                # ('臨時収入', 14),('その他', 19),('生活費清算', 17503724),
           25504271,
                # ('積)養育費', 25504271),
           28694950, 28269167, 28593839]
                # 住まい28269167, 小遣い28694950,口座c, , 28593839

    select = """select sum(amount) as amount, zaim_date as date, category, genre, 
        place, max(name) as name, from_account
        from {tablename} 
        where category_id not in ({cats})  and 
        zaim_date like '{year}-{month:02}-%' and 
        mode == 'payment' 
        group by zaim_date,place,category_id 
        order by zaim_date
        ;""".format(
            tablename = TABLE, cats=''.join(str(objCategory))[1:-1], 
            year = objYearMonth[0], month = objYearMonth[1])    

    data = select_from_sqlite(select)
    return data

def get_OutCategory(objYearMonth):
    moneydata = select_OutCategory(objYearMonth)
    print_moneydata(objYearMonth, moneydata)
    return moneydata
    


# In[ ]:




# In[ ]:




# In[ ]:




# In[12]:

def select_OutGenre(objYearMonth):
    # 登録チェックリスト
    genres = detailgenresFP()
    t = []
    for x in genres:
        for y in x['code']:
            t.append(y)
    genrecode = list(set(t))
    genrecode.append(11601304) #口座調整
    genrecode.append(13068828) # 登録確認

    select = """select sum(amount) as amount, zaim_date as date, category, genre, genre_id,
        place, max(name) as name, from_account
        from {tablename} 
        where genre_id not in ({genres})  and 
        zaim_date like '{year}-{month:02}-%' and 
        mode == 'payment' 
        group by zaim_date,place,category_id 
        order by zaim_date
        ;""".format(
            tablename = TABLE, genres=''.join(str(genrecode))[1:-1], 
            year = objYearMonth[0], month = objYearMonth[1])    

    data = select_from_sqlite(select)
    return data


# In[ ]:




# In[ ]:




# In[ ]:




# In[13]:

def select_nonPaymentData(objYearMonth):
    select = """select amount, zaim_date as date, category, category_id, genre, genre_id, comment, 
        place, name, from_account, to_account, mode, to_account_id, from_account_id 
        from {tablename} 
        where zaim_date like '{year}-{month:02}-%' 
        and (mode != 'payment' or category_id in (28593839))
        and genre_id not in (13068828) 
        order by zaim_date
        ;""".format(
            tablename = TABLE,
            year = objYearMonth[0], month = objYearMonth[1])    

    # 13068828 月次TODOチェックリスト
    # 28593839 口座出納
    #where zaim_date like '{year}-{month:02}-%' and (mode != 'payment' or category_id in (28593839))

    data = select_from_sqlite(select)
    return data


# In[14]:

# 立替清算用
def get_tatekaeData(objYearMonth):
    select = """select amount, zaim_date as date, category, category_id, genre, genre_id, comment, 
        place, name, from_account 
        from {tablename} 
        where zaim_date like '{year}-{month:02}-%' 
        and (mode = 'payment' and category_id not in (28593839)) 
        and from_account_id in (1, 827175, 862648)
        order by zaim_date
        ;""".format(
            tablename = TABLE,
            year = objYearMonth[0], month = objYearMonth[1])    

    tdata = select_from_sqlite(select)
    t = sum([x['amount'] for x in tdata])

#  1: ['たか', 1],
#  827175: ['積立）たか', 827175],
#  862648: ['たか', 862648],
    select = """select amount, zaim_date as date, category, category_id, genre, genre_id, comment, 
        place, name, from_account 
        from {tablename} 
        where zaim_date like '{year}-{month:02}-%' 
        and (mode = 'payment' and category_id not in (28593839)) 
        and from_account_id in (4, 827184, 862650)
        order by zaim_date
        ;""".format(
            tablename = TABLE,
            year = objYearMonth[0], month = objYearMonth[1])    

    sdata = select_from_sqlite(select)
    s = sum([x['amount'] for x in sdata])

#  4: ['さえ', 4],
#  827184: ['積立）さえ', 827184],
#  862650: ['さえ', 862650],

#     return sdata
    return t, s, tdata, sdata


# In[15]:

def get_YearlyIncomes(objYear=2015): #rev2.3
    incomes = []
    for objMonth in range(1,13):
        income0 = get_monthlyIncomes((objYear,objMonth))
        incomes.append(income0)
    return incomes
    




# In[16]:

def get_monthlyIncomes(objYearMonth=(2016,7)):#rev2.3
    a = select_nonPaymentData(objYearMonth)
    mincome = {}
    mincome['taka'] = sum([x['amount'] for x in a if (x['to_account'] == '家計' and x['place'][0:2]=='たか')])
    mincome['sae']  = sum([x['amount'] for x in a if (x['to_account'] == '家計' and x['place'][0:2]=='さえ')])
    mincome['other']= sum([x['amount'] for x in a if (x['to_account'] == '家計' and not (x['place'][0:2]=='さえ' or x['place'][0:2]=='たか'))])
    mincome['sum']= sum([x['amount'] for x in a if (x['to_account'] == '家計')])
    
    return mincome
    




get_monthlyIncomes()
get_YearlyIncomes()
# In[17]:

def incomes_month2Year(incomes):
    incomeY = {}
    for key in incomes[0].keys():
        incomeY[key] = sum([x[key] for x in incomes]) 



    return incomeY


# In[18]:

def incomes_month2Quarter(incomes):

    incomesQ = []
    Qrange= [slice(0,3), slice(3,6), slice(6,9), slice(9,12)]

    for Q in Qrange:
        aQ = {}
        for key in incomes[0].keys():
            aQ[key] = sum([x[key] for x in incomes[Q]])
        incomesQ.append(aQ)
    aQ ={}
    for key in incomes[0].keys():
        aQ[key] = sum([x[key] for x in incomesQ])
    incomesQ.append(aQ)

    return incomesQ


# In[19]:

def get_Yearly_incomestable():    
    incomesY = []
    (yearfrom,yearto)= get_objYearRange()
    for y in range(yearfrom,yearto):
        incomes = get_YearlyIncomes(y)
        incomeY = incomes_month2Year(incomes)
        incomesY.append(incomeY)
    aQ ={}
    for key in incomesY[0].keys():
        aQ[key] = sum([x[key] for x in incomesY])
    incomesY.append(aQ)
    
    renttable0 = """
        <!-- output from PyJade -->    
        <div class="panel panel-primary">
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed">
                    <thead class="bg-primary">
                        <tr>
                            <th class="text-center">入金</th>"""

    ty, tm, td = get_today()
    rm = range(1,13)
    ry = range(2011,ty+1)
    rm0 = range(1,tm+1)

    t = []
    for yy in ry:
        t0 = """\n\t\t\t\t\t\t<th class="text-center">{year}年</th>""".format(year=yy)
        t.append(t0)

    renttable1 = "".join(t)



    renttable2 = """
                            <th class="text-center"><strong>小計</strong></th>
                        </tr>
                    </thead>
                    <tbody class="text-center">
                        <tr>
                            <td>たか</td>"""
    income_taka = []
    income_sae = []
    income_other = []
    income_sum = []
    
    for incomet in incomesY:
        t0 = """\n\t\t\t\t\t\t<td>¥{amount:,}</td>""".format(amount=incomet['taka'])
        t1 = """\n\t\t\t\t\t\t<td>¥{amount:,}</td>""".format(amount=incomet['sae'])
        t2 = """\n\t\t\t\t\t\t<td>¥{amount:,}</td>""".format(amount=incomet['other'])
        t3 = """\n\t\t\t\t\t\t<td><strong>¥{amount:,}</strong></td>""".format(amount=incomet['sum'])

        income_taka.append(t0)
        income_sae.append(t1)
        income_other.append(t2)
        income_sum.append(t3)

    renttable_taka = "".join(income_taka)
    renttable_sae = "".join(income_sae)
    renttable_other = "".join(income_other)
    renttable_sum = "".join(income_sum)


    renttable3 = renttable_taka

    renttable4 = """
                        </tr>    

                        <tr>
                            <td>さえ</td>"""
    renttable5 = renttable_sae

    renttable6 = """
                        </tr>    

                        <tr>
                            <td>ほか</td>"""
    renttable7 = renttable_other

    renttable8 = """
                        </tr>    


                        <tr class="text-center info">
                            <td><strong>小計</strong></td>"""
    renttable9 = renttable_sum

    renttable10 = """
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        """
    
    renttable = renttable0 + renttable1 + renttable2 + renttable3 + renttable4 +     renttable5 + renttable6 + renttable7 + renttable8 + renttable9 + renttable10

    return renttable


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[20]:

def get_Quarterly_incomestable(objYear):    
    incomes = get_YearlyIncomes(objYear)
    incomesQ = incomes_month2Quarter(incomes)
    
    renttable = """
    <!-- output from PyJade -->    
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center">入金</th>
                        <th class="text-center">Q1</th>
                        <th class="text-center">Q2</th>
                        <th class="text-center">Q3</th>
                        <th class="text-center">Q4</th>
                        <th class="text-center"><strong>小計</strong></th>

                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>たか</td>
                        <td>¥{val1Q1:,}</td>
                        <td>¥{val1Q2:,}</td>
                        <td>¥{val1Q3:,}</td>
                        <td>¥{val1Q4:,}</td>
                        <td>¥{val1Q:,}</td>
                    </tr>    

                    <tr>
                        <td>さえ</td>
                        <td>¥{val2Q1:,}</td>
                        <td>¥{val2Q2:,}</td>
                        <td>¥{val2Q3:,}</td>
                        <td>¥{val2Q4:,}</td>
                        <td>¥{val2Q:,}</td>
                    </tr>    

                    <tr>
                        <td>ほか</td>
                        <td>¥{val3Q1:,}</td>
                        <td>¥{val3Q2:,}</td>
                        <td>¥{val3Q3:,}</td>
                        <td>¥{val3Q4:,}</td>
                        <td>¥{val3Q:,}</td>
                    </tr>    


                    <tr class="text-center info">
                        <td><strong>小計</strong></td>
                        <td><strong>¥{valSM1:,}</strong></td>
                        <td><strong>¥{valSM2:,}</strong></td>
                        <td><strong>¥{valSM3:,}</strong></td>
                        <td><strong>¥{valSM4:,}</strong></td>  
                        <td><strong>¥{valSM:,}</strong></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """.format(
                val1Q1 = round500(incomesQ[0]['taka']),
                val1Q2 = round500(incomesQ[1]['taka']),
                val1Q3 = round500(incomesQ[2]['taka']),
                val1Q4 = round500(incomesQ[3]['taka']),
                val1Q  = round500(incomesQ[4]['taka']),

                val2Q1 = round500(incomesQ[0]['sae']),
                val2Q2 = round500(incomesQ[1]['sae']),
                val2Q3 = round500(incomesQ[2]['sae']),
                val2Q4 = round500(incomesQ[3]['sae']),
                val2Q  = round500(incomesQ[4]['sae']),

                val3Q1 = round500(incomesQ[0]['other']),
                val3Q2 = round500(incomesQ[1]['other']),
                val3Q3 = round500(incomesQ[2]['other']),
                val3Q4 = round500(incomesQ[3]['other']),
                val3Q  = round500(incomesQ[4]['other']),

                valSM1 = round500(incomesQ[0]['sum']),
                valSM2 = round500(incomesQ[1]['sum']),
                valSM3 = round500(incomesQ[2]['sum']),
                valSM4 = round500(incomesQ[3]['sum']),
                valSM  = round500(incomesQ[4]['sum'])
        )

    return renttable


# In[21]:

def get_yearmonthly_incomestable(objYear):
    incomes = get_YearlyIncomes(objYear)
    incomer = {}
    for key in incomes[0]:
        t = []
        for i in incomes:
            t.append(i[key])
        incomer[key] = t
    
    key = "taka"
    incomer[key].append(sum(incomer[key]))
    texttaka  = "\n\t\t\t".join(["<td>¥{:,}</td>".format(round500(x)) for x in incomer[key]])
    key = "sae"
    incomer[key].append(sum(incomer[key]))
    textsae   = "\n\t\t\t".join(["<td>¥{:,}</td>".format(round500(x)) for x in incomer[key]])
    key = "other"
    incomer[key].append(sum(incomer[key]))
    textother = "\n\t\t\t".join(["<td>¥{:,}</td>".format(round500(x)) for x in incomer[key]])
    key = "sum"
    incomer[key].append(sum(incomer[key]))
    textsum   = "\n\t\t\t".join(["<td><strong>¥{:,}</strong></td>".format(round500(x)) for x in incomer[key]])
        
    
    renttable = """
    <!-- output from PyJade -->    
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center" style="min-width: 80px;">入金</th>
                        <th class="text-center">1月</th>
                        <th class="text-center">2月</th>
                        <th class="text-center">3月</th>

                        <th class="text-center">4月</th>
                        <th class="text-center">5月</th>
                        <th class="text-center">6月</th>

                        <th class="text-center">7月</th>
                        <th class="text-center">8月</th>
                        <th class="text-center">9月</th>

                        <th class="text-center">10月</th>
                        <th class="text-center">11月</th>
                        <th class="text-center">12月</th>

                        <th class="text-center" style="font-weight:bold">小計</th>
                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>たか</td>
                         {texttaka}
                    </tr>    

                    <tr>
                        <td>さえ</td>
                        {textsae}
                    </tr>    

                    <tr>
                        <td>ほか</td>
                        {textother}
                    </tr>    


                    <tr class="text-center info">
                        <td><strong>小計</strong></td>
                        {textsum}
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """.format(
        texttaka = texttaka, textsae = textsae, textother = textother, textsum = textsum
        )


    return renttable


# In[22]:

def select_RawWholedata(objYearMonth):
        
    select = """select amount, zaim_date as date, category, category_id, genre, genre_id, place, name, from_account
    from {tablename} 
    where zaim_date like '{year}-{month:02}-%' and 
    mode == 'payment' 
    order by zaim_date
    ;""".format(
        tablename = TABLE, year = objYearMonth[0], month = objYearMonth[1])    

    data = select_from_sqlite(select)
    return data


# In[23]:

def select_Wholedata(objYearMonth, TH=0):
    mdata0 = select_RawWholedata(objYearMonth)
    mdata1 = groupingZaimdata(mdata0, TH)
    return mdata1


# In[24]:

# select_CategoryDataをSqlでgroupingからPythonでgroupingに変更するためにサブ関数
def select_RawCategoryData(objYearMonth, objCategory, order = 'time'):

    #group by zaim_date,place,category_id  
    #having sum(amount)>{yen} 
    
    select = """select amount, zaim_date as date, category, category_id, genre, genre_id, place, name, from_account
    from {tablename} 
    where category_id in ({cats})  and 
    zaim_date like '{year}-{month:02}-%' 
    order by zaim_date
    ;""".format(
        tablename = TABLE, cats=''.join(str(objCategory))[1:-1], 
        year = objYearMonth[0], month = objYearMonth[1])    

    if order == 'place':
        select = """select amount, zaim_date as date, category, category_id, genre, genre_id, place, name, from_account
        from {tablename} 
        where category_id in ({cats})  and 
        zaim_date like '{year}-{month:02}-%' 
        order by place
        ;""".format(
            tablename = TABLE, cats=''.join(str(objCategory))[1:-1], 
            year = objYearMonth[0], month = objYearMonth[1])    

    
    
    data = select_from_sqlite(select)
    return data

#for test
# objCategory = [107, 109, 106, 108, 110]
# mdata0 = select_CategoryData2((2015,12), objCategory, 1000)
# mdata1 = groupingZaimdata(mdata0)

def groupingZaimdata(mdata0, TH=0):
    setlist = [(x['date'], x['place'], x['category']) for x in mdata0]
    grp = sorted(set(setlist), key=setlist.index)
    
    mdata1 = []

    # amount▶️sum, zaim_date as date▶️Grp, category▶️Grp, genre▶️Copy , place▶️Grp, name▶️max, from_account▶️Copy

    for grpkey in grp:
        t = {'date':grpkey[0],'place':grpkey[1],'category':grpkey[2],'amounts' : [], 'names' : []}
        for y in mdata0:
            if y['date'] == grpkey[0] and y['place'] == grpkey[1] and y['category'] == grpkey[2]:
                t['amounts'].append(y['amount'])
                t['names'].append(y['name'])
                t['genre'] = y['genre']
                t['genre_id'] = y['genre_id']
                t['from_account'] = y['from_account']
                t['category_id'] = y['category_id']
        # genreとfrom_accountはGrp内で共通とする。そのため、Grp構成要素の一つからコピーする。

        # 合計金額と、最大金額となるときの名前をゲット。
        # SQLのGroupByでは不定となるためPythonで処理.
        t0 = t['amounts']
        t1 = t['names']
        t['amount'] = sum(t0)
        t['name'] = t1[t0.index(max(t0))]
        if t['amount'] > TH :
            mdata1.append(t)

    return mdata1
    




# In[25]:

def select_CategoryData(objYearMonth, objCategory, TH=0):
    mdata0 = select_RawCategoryData(objYearMonth, objCategory)
    mdata1 = groupingZaimdata(mdata0, TH)
    return mdata1


# In[26]:

# 対象になるジャンルリストを入力し、レシートリストから探索、出力する

def select_RawGenreData(objYearMonth, objGenre):
    select = """select amount, zaim_date as date, category, category_id, genre, genre_id, 
    place, name, from_account
    from {tablename} 
    where genre_id in ({cats})  and 
    zaim_date like '{year}-{month:02}-%'
    order by zaim_date
    ;""".format(
        tablename = TABLE, cats=''.join(str(objGenre))[1:-1], 
        year = objYearMonth[0], month = objYearMonth[1])

    data = select_from_sqlite(select)
    return data


# In[27]:

def select_GenreData(objYearMonth, objGenre, TH=0):
    mdata0 = select_RawGenreData(objYearMonth, objGenre)
    mdata1 = groupingZaimdata(mdata0, TH)
    return mdata1


# In[28]:

# 対象になるカテゴリーリストを入力し、レシートリストから探索、出力する

def getDailyData_fromDB(receiptlist,objYearMonth):
    objMonthdayList = get_monthday(objYearMonth[0],objYearMonth[1])
    
    dailydata = {}
    for daystr in objMonthdayList:
        x = []
        for xx in receiptlist:
            if xx['date'] == daystr:
              x.append(xx)

        dailydata[daystr] = {'amount':None,'max_place':None, 'placelist':None}
        if x:
            #print(x)
            x2 = [y['amount'] for y in x]
            x3 = [y['place'] for y in x]
            # print(x3[x2.index(max(x2))])
            #print(daystr,x3, x2)
            dailydata[daystr]['amount'] = sum(x2)
            dailydata[daystr]['max_place'] = x3[x2.index(max(x2))]
            dailydata[daystr]['placelist'] = x3
            
    return dailydata


# In[29]:

# TH円以上のレシートを出力, 高額リスト

def select_RawExpenceData(objYearMonth):
    # これらは含まない
    # 含まない ['公共料金', 105]
    # 含まない ['口座出納', 28593839]
    # 含まない ['社会保障', 25504225]
    # 含まない ['住まい', 28269167]
    # 含まない [28694950 小遣い]
    
    select = """select amount, zaim_date as date, category, category_id, genre, genre_id,
    place, name, from_account 
    from {tablename} 
    where zaim_date like '{year}-{month:02}-%' and 
    category_id not in (105, 28269167, 28694950, 28593839, 25504225)  and 
    mode=='payment' 
    order by zaim_date 
    ;""".format(
        tablename = TABLE,
        year = objYearMonth[0], month = objYearMonth[1])    


    data = select_from_sqlite(select)
    return data




# In[30]:

def select_ExpenceDataYsummary(objYearMonth, TH=3000): #rev2.3
    mdata0 = select_RawExpenceDataYsummary(objYearMonth)
    mdata1 = groupingZaimdata(mdata0, TH)
    mdata2 = mdata1
#     key = 25504225
#     for m in mdata1:
#         if m['category_id'] != key:
#             mdata2.append(m)
#     for m in mdata1:
#         if m['category_id'] == key:
#             mdata2.append(m)

    return mdata2


# TH円以上のレシートを出力, 高額リスト

def select_RawExpenceDataYsummary(objYearMonth):
    # これらは含まない
    # 含む　　 ['公共料金', 105]
    # 含まない ['口座出納', 28593839]
    # 含む　　 ['社会保障', 25504225]
    # 含まない ['住まい', 28269167]
    # 含まない [28694950 小遣い]
    
    select = """select amount, zaim_date as date, category, category_id, genre, genre_id,
    place, name, from_account 
    from {tablename} 
    where zaim_date like '{year}-{month:02}-%' and 
    category_id not in (28269167, 28694950, 28593839)  and 
    mode=='payment' 
    order by zaim_date 
    ;""".format(
        tablename = TABLE,
        year = objYearMonth[0], month = objYearMonth[1])    


    data = select_from_sqlite(select)
    return data



# In[ ]:




# In[31]:

def select_ExpenceData(objYearMonth, TH=3000):
    mdata0 = select_RawExpenceData(objYearMonth)
    mdata1 = groupingZaimdata(mdata0, TH)
    mdata2 = []
    for m in mdata1:
        if m['category_id'] == 101:
            mdata2.append(m)
    for m in mdata1:
        if m['category_id'] != 101:
            mdata2.append(m)

    return mdata2


# In[32]:

def get_bigcats():
    #rev2.3
    c = [ 
    {'name':'食費', 'cat': [101]}, 
    {'name':'公共料金', 'cat': [105]}, 
    {'name':'社会保障', 'cat': [25504225]}, 
    {'name':'変動費', 'cat': [107, 108, 110, 111]}, 
    {'name':'大型出費', 'cat': [114]}, 
    {'name':'教育・養育', 'cat': [25504271, 109, 28694950]}, 
    {'name':'住まい', 'cat': [28269167, 106, 28035336]},
    {'name':'娯楽・交際', 'cat': [108, 107]},
    {'name':'医療・健康', 'cat': [110]},
    {'name':'美容', 'cat': [111]},
    ]
    return c






# In[ ]:




# In[ ]:




# In[33]:

def get_monthlyamount(objYearMonth, numflg = False): #rev2.3
    # (5) 生活費 : Category: ('食費•日用品', 101),
    monthlyamount = {}
    munthlyamountnum = {}
    obj0 = []

    def categoryamount(obj):
        moneylist = select_CategoryData(objYearMonth, obj)
        sumamount = sum([x['amount'] for x in moneylist])
        numamount = len([x['amount'] for x in moneylist])
        return sumamount, numamount

        
    obj = [101]
    key = '食費'
    obj0 += obj
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)

    # (5) 公共料金 : Category: ('公共', 105),
    obj = [105]
    obj0 += obj
    moneylist = select_RawCategoryData(objYearMonth, obj)
    monthlyamount['公共料金'] = sum([x['amount'] for x in moneylist])
    monthlyamount['通信費'] = sum([x['amount'] for x in moneylist if x['genre_id'] in (2918018, 2918020,)])
    monthlyamount['光熱費'] = sum([x['amount'] for x in moneylist if x['genre_id'] not in (2918018, 2918020,)])
#     testdata = [(x['amount'],x['date'],x['place'],x['genre'],x['genre_id'] )for x in moneylist if x['genre_id'] not in (2918018, 2918020,)]



    # (5) 社会保障 : Category: ('社会保障', 25504225),
    obj = [25504225]
    key = '社会保障'
    obj0 += obj
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)



    # (2) 積立出費のリスト
    # ,('交際費', 107),('娯楽',108),('教育・教養', 109),('医療・健康', 110), (美容111)
    obj = [107, 108, 110,111]
    key = '変動費'
    obj0 += obj
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)


    obj = [107, 108]
    obj0 += obj
    key = '娯楽・交際'
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)


    obj = [110]
    obj0 += obj
    key = '医療・健康'
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)


    obj = [111]
    obj0 += obj
    key = '美容'
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)


    
    # (3) その他出費のリスト
    # ('事業所得', 15),('給与所得', 11),('立替金返済', 12),('賞与', 13),
    # ('臨時収入', 14),('その他', 19),('大型出費', 114),('生活費清算', 17503724),
    #obj = [17503724, 11, 12, 13, 14, 15, 114, 19]
    obj = [114]
    obj0 += obj
    key = '大型出費'
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)


    # (4) Category: ('積)養育費', 25504271), 109 教育、教養, 28694950小遣い
    obj = [25504271, 109, 28694950]
    obj0 += obj
    key = '教育・養育'
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)

#     testdata = [(x['amount'],x['date'],x['place'],x['genre'],x['genre_id'] )for x in moneylist]
    
    # 家賃関係 28269167: ['住まい', 28269167]}, 28035336住まい ,('積)住まい・家財', 106)
    obj = [28269167, 106, 28035336]
    obj0 += obj
    key = '住まい'
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj)



    # All
    obj1 = list(set(obj0))
    key = 'all'
    monthlyamount[key], munthlyamountnum[key] = categoryamount(obj1)


    if numflg:
        return monthlyamount, munthlyamountnum
    else:
        return monthlyamount# ,testdata



# In[34]:

def get_monthlyamount_report(objYearMonth):
    monthlyamount = {}
    obj0 = []

    # (5) 生活費 : Category: ('食費•日用品', 101),
    key = '食費'
    obj = [101]
    obj0 += obj
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)

    # (5) 公共料金 : Category: ('公共', 105),
    key = '公共料金'
    obj = [105]
    obj0 += obj
    moneylist = select_RawCategoryData(objYearMonth, obj)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)

    key = '通信費'
    moneydata = [x for x in moneylist if x['genre_id'] in (2918018, 2918020,)]
    monthlyamount[key] = get_monthlyamount_top3cat(moneydata)
    
    key = '光熱費'
    moneydata = [x for x in moneylist if x['genre_id'] not in (2918018, 2918020,)]
    monthlyamount[key] = get_monthlyamount_top3cat(moneydata)

    # (5) 社会保障 : Category: ('社会保障', 25504225),
    key = '社会保障'
    obj = [25504225]
    obj0 += obj
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount['社会保障'] = get_monthlyamount_top3cat(moneylist)

    # (2) 積立出費のリスト
    # ,('交際費', 107),('娯楽',108),('教育・教養', 109),('医療・健康', 110), (美容111)
    key = '変動費'
    obj = [107, 108, 110,111]
    obj0 += obj
    # a = select_CategoryData(objYearMonth, [107, 109, 106, 108, 110])
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount['変動費'] = get_monthlyamount_top3cat(moneylist)

    obj = [107, 108]
    obj0 += obj
    key = '娯楽・交際'
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)

    obj = [110]
    obj0 += obj
    key = '医療・健康'
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)

    obj = [111]
    obj0 += obj
    key = '美容'
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)
    
    # (3) その他出費のリスト
    # ('事業所得', 15),('給与所得', 11),('立替金返済', 12),('賞与', 13),
    # ('臨時収入', 14),('その他', 19),('大型出費', 114),('生活費清算', 17503724),
    #obj = [17503724, 11, 12, 13, 14, 15, 114, 19]
    key = '大型出費'
    obj = [114]
    obj0 += obj
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)


    # (4) Category: ('積)養育費', 25504271), 109 教育、教養, 28694950小遣い
    key = '教育・養育'
    obj = [25504271, 109, 28694950]
    obj0 += obj
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)
    
    # 家賃関係 28269167: ['住まい', 28269167]}, 28035336住まい ,('積)住まい・家財', 106)
    key = '住まい'
    obj = [28269167, 106, 28035336]
    obj0 += obj
    moneylist = select_CategoryData(objYearMonth, obj)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)

    # All
    key = 'all'
    obj1 = list(set(obj0))
    moneylist = select_CategoryData(objYearMonth, obj1)
    monthlyamount[key] = get_monthlyamount_top3cat(moneylist)    

    return monthlyamount# ,testdata


# In[35]:

def get_monthlyamount_top3cat(moneydata):
    mdata1 = [(m['amount'],m['date'],m['place']) for m in moneydata]
    mdata2 = sorted(mdata1, key=lambda x: x[0])
    indx3 = mdata2[-3:]
    
    cnt = len(mdata1)
    ms = sum([m['amount'] for m in moneydata])
    mr = sum([m[0] for m in indx3])
    if ms == 0:
        mr0 = 100
    else:
        mr0 = round(mr/ms*100/5)*5
    return (ms, indx3, mr0, cnt)
            
            





# In[36]:

def get_lastmonth(thismonth):
    t0 = dt.strptime("{},{},1".format(thismonth[0],thismonth[1]), '%Y,%m,%d')
    t = t0 - datetime.timedelta(days=25)
    lastmonth = dt.strptime("{},{},1".format(t.year,t.month), '%Y,%m,%d')
    return lastmonth.year,lastmonth.month

def get_nextmonth(thismonth):
    t0 = dt.strptime("{},{},25".format(thismonth[0],thismonth[1]), '%Y,%m,%d')
    t = t0 + datetime.timedelta(days=25)
    lastmonth = dt.strptime("{},{},1".format(t.year,t.month), '%Y,%m,%d')
    return lastmonth.year,lastmonth.month



# objDT0 = objYearMonth 
# objDT1 = get_lastmonth(objDT0)
# objDT2 = get_lastmonth(objDT1)
# a =get_monthlyamount(objDT2)





# In[37]:

def print_moneytable(objYearMonth, moneydata, tabletitle, tableid, th=1000000):

    texts = []
    count = 0
    sum_amount = 0
    xdaymonth0 = 0
    catflg = False
    genreflg = True
    if tabletitle=="変動費" or tabletitle=="高額リスト" or tabletitle=="Zaim登録チェックリスト":
        catflg = True

    if tabletitle=="外食":
        genreflg = False

    
    if catflg:
        for x in moneydata:
            count = count + 1
            sum_amount = sum_amount + x['amount']
            xday = dt.strptime(x['date'], '%Y-%m-%d')
            xdaymonth = xday.month

            atext0 = """
                <tr style="border-top:solid 1px">
                """
            if x['amount'] > th: # rev2.3
                atext = """
                        <td>{date} ({wday})</td>
                        <td>{place}</td>
                        <td class="text-right" style="padding-right:1em;font-weight:bold;color:red;">¥{price:>6,}</td>
                        <td>{category}</td>
                        <td>{genre}</td>
                        <td>{fromaccount}</td>
                        <td>{name}</td>
                    </tr>""".format(
                        date=xday.strftime('%m/%d'),
                        wday = get_weekdayJP(xday.strftime('%w')),
                        place=x['place'], price=round500(x['amount']), 
                        name=x['name'], fromaccount = x['from_account'],
                        category = x['category'], genre = x['genre'])
            else:
                atext = """
                        <td>{date} ({wday})</td>
                        <td>{place}</td>
                        <td class="text-right" style="padding-right:1em">¥{price:>6,}</td>
                        <td>{category}</td>
                        <td>{genre}</td>
                        <td>{fromaccount}</td>
                        <td>{name}</td>
                    </tr>""".format(
                        date=xday.strftime('%m/%d'),
                        wday = get_weekdayJP(xday.strftime('%w')),
                        place=x['place'], price=round500(x['amount']), 
                        name=x['name'], fromaccount = x['from_account'],
                        category = x['category'], genre = x['genre'])

            if xdaymonth0 == xdaymonth or xdaymonth0 == 0:
                atext0 = """
                    <tr>
                    """

            texts.append(atext0+atext)
            xdaymonth0 = xdaymonth
            #print(atext)

        textheader = """

        <!-- tablelist ここから-->

        <div class="panel panel-primary">
            <div class="panel-heading">{cat}<span class="badge pull-right">{counter}件 ¥{sumamount:,}</span></div>
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
                    <thead>
                        <tr>
                            <th class="text-center">日付</th>
                            <th class="text-center">場所</th>
                            <th class="text-center">金額</th>
                            <th class="text-center">カテゴリ</th>
                            <th class="text-center">ジャンル</th>
                            <th class="text-center">出金元</th>
                            <th class="text-center">もの</th>
                        </tr>
                    </thead>
                    <tbody>""".format(tableid=tableid, cat = tabletitle, counter=count,sumamount=round500(sum_amount))
    elif not genreflg:
        for x in moneydata:
            count = count + 1
            sum_amount = sum_amount + x['amount']
            xday = dt.strptime(x['date'], '%Y-%m-%d')
            xdaymonth = xday.month

            atext0 = """
                <tr style="border-top:solid 1px">
                """
            
            if x['amount'] > th: # rev2.3
                atext = """
                        <td>{date} ({wday})</td>
                        <td style="font-weight:bold;color:red;">{place}</td>
                        <td class="text-right" style="padding-right:1em;font-weight:bold;color:red;">¥{price:>6,}</td>
                        <td>{fromaccount}</td>
                        <td>{name}</td>
                    </tr>""".format(
                        date=xday.strftime('%m/%d'),
                        wday = get_weekdayJP(xday.strftime('%w')),
                        place=x['place'], price=round500(x['amount']), 
                        name=x['name'], fromaccount = x['from_account'],
                        )
            else:
                atext = """
                        <td>{date} ({wday})</td>
                        <td>{place}</td>
                        <td class="text-right" style="padding-right:1em">¥{price:>6,}</td>
                        <td>{fromaccount}</td>
                        <td>{name}</td>
                    </tr>""".format(
                        date=xday.strftime('%m/%d'),
                        wday = get_weekdayJP(xday.strftime('%w')),
                        place=x['place'], price=round500(x['amount']), 
                        name=x['name'], fromaccount = x['from_account'],
                        )

            if xdaymonth0 == xdaymonth or xdaymonth0 == 0:
                atext0 = """
                    <tr>
                    """

            texts.append(atext0+atext)
            xdaymonth0 = xdaymonth
            #print(atext)

        textheader = """

        <!-- tablelist ここから-->

        <div class="panel panel-primary">
            <div class="panel-heading">{cat}<span class="badge pull-right">{counter}件 ¥{sumamount:,}</span></div>
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
                    <thead>
                        <tr>
                            <th class="text-center">日付</th>
                            <th class="text-center">場所</th>
                            <th class="text-center">金額</th>
                            <th class="text-center">出金元</th>
                            <th class="text-center">もの</th>
                        </tr>
                    </thead>
                    <tbody>""".format(tableid=tableid, cat = tabletitle, counter=count,sumamount=round500(sum_amount))


    else:
        for x in moneydata:
            count = count + 1
            sum_amount = sum_amount + x['amount']
            xday = dt.strptime(x['date'], '%Y-%m-%d')
            xdaymonth = xday.month

            atext0 = """
                <tr style="border-top:solid 1px">
                """
            if x['amount'] > th:
                atext = """
                        <td>{date} ({wday})</td>
                        <td style="font-weight:bold;color:red;">{place}</td>
                        <td class="text-right" style="padding-right:1em;font-weight:bold;color:red;">¥{price:>6,}</td>
                        <td>{genre}</td>
                        <td>{fromaccount}</td>
                        <td>{name}</td>
                    </tr>""".format(
                        date=xday.strftime('%m/%d'),
                        wday = get_weekdayJP(xday.strftime('%w')),
                        place=x['place'], price=round500(x['amount']), 
                        name=x['name'], fromaccount = x['from_account'],
                        genre = x['genre'])
            else:
                atext = """
                        <td>{date} ({wday})</td>
                        <td>{place}</td>
                        <td class="text-right" style="padding-right:1em">¥{price:>6,}</td>
                        <td>{genre}</td>
                        <td>{fromaccount}</td>
                        <td>{name}</td>
                    </tr>""".format(
                        date=xday.strftime('%m/%d'),
                        wday = get_weekdayJP(xday.strftime('%w')),
                        place=x['place'], price=round500(x['amount']), 
                        name=x['name'], fromaccount = x['from_account'],
                        genre = x['genre'])
                
            if xdaymonth0 == xdaymonth or xdaymonth0 == 0:
                atext0 = """
                    <tr>
                    """

            texts.append(atext0+atext)
            xdaymonth0 = xdaymonth
            #print(atext)

        textheader = """

        <!-- tablelist ここから-->

        <div class="panel panel-primary">
            <div class="panel-heading">{cat}<span class="badge pull-right">{counter}件 ¥{sumamount:,}</span></div>
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
                    <thead>
                        <tr>
                            <th class="text-center">日付</th>
                            <th class="text-center">場所</th>
                            <th class="text-center">金額</th>
                            <th class="text-center">ジャンル</th>
                            <th class="text-center">出金元</th>
                            <th class="text-center">もの</th>
                        </tr>
                    </thead>
                    <tbody>""".format(tableid=tableid, cat = tabletitle, counter=count,sumamount=round500(sum_amount))

    
    textfooter = """
                </tbody>
            </table>
        </div>
    </div>
    <!-- tablelist ここまで-->"""

    if tabletitle=="高額リスト":
        textfooter = """
                </tbody>
            </table>
            <p class="text-mute small">*) 3000円以上のリスト(カテゴリ順)。公共料金/社会保障/小遣い/家賃は含まない</p>    
        </div>
    </div>
    <!-- tablelist ここまで-->"""

    """v2.4 <p class="text-mute small">*) 3000円以上のリスト。公共料金/社会保障/小遣い/家賃は含まない</p>"""
    if tabletitle=="Zaim登録チェックリスト":
        textfooter = """
                </tbody>
            </table>
            <p class="text-mute small">*) 出金元がさえ/たか/家計/セブンカードでないもの。カテゴリが変なもの(ジャンルはみてない)</p>    
        </div>
    </div>
    <!-- tablelist ここまで-->"""



    
    
    textbody = textheader + '\n'.join(texts) + textfooter
        
    return (textheader, '\n'.join(texts), textfooter, textbody)
        


# In[38]:

def get_detailtabbody(objYearMonth):
    
    objCategory = [106, 107, 108, 110,111]
    # 106: ['積)家財', 106],['積)交際費', 107], ['娯楽', 108], 110: ['積)医療・健康', 110], ['積)美容・衣服', 111],
    tabletitle = "変動費 <small>*) 娯楽・家財・交際・医療・美容</small>"
    tableid = "table1"
    moneydata = select_CategoryData(objYearMonth, objCategory)
    t1 = print_moneytable(objYearMonth, moneydata, tabletitle, tableid)
    t10 = [0,0,0,0]
    t10[0] = t1[0]
    t10[1] = t1[1]
    t10[2] = """\n                </tbody>\n            </table>\n        </div>\n 
    <p class="text-mute small" style="border-top:solid 1px black; padding-left:1em;padding-top:0.5em;font-size:0.7em;">*) 変動費：交際費, 娯楽, 医療・健康, 美容・衣服, 住まい・家財</p></div>\n    <!-- tablelist ここまで-->"""
    t10[3] = t10[0] + t10[1] + t10[2]
    t1_hendo = t10
    
    #def print_CategoryTable(objYearMonth, objCategory):
    objCategory = [25504271,109]
    tabletitle = "教育・書籍"
    tableid = "table2"
    moneydata = select_CategoryData(objYearMonth, objCategory)
    t2_kyoiku = print_moneytable(objYearMonth, moneydata,tabletitle,tableid)

    objCategory = [114] #[17503724, 11, 12, 13, 14, 15, 114, 19]
    tabletitle = "大型出費"
    tableid = "table3"
    moneydata = select_CategoryData(objYearMonth, objCategory)
    t3 = print_moneytable(objYearMonth, moneydata,tabletitle,tableid)
    t30 = [0,0,0,0]
    t30[0] = t3[0]
    t30[1] = t3[1]
    t30[2] = """\n                </tbody>\n            </table>\n        </div>\n 
    <p class="text-mute small" style="border-top:solid 1px black; padding-left:1em;padding-top:0.5em;font-size:0.7em;">*) 大型出費：旅行・結婚/出産・帰省/親族実家・住宅関係その他(家賃・家具家財を除く) </p>  </div>\n    <!-- tablelist ここまで-->"""
    t30[3] = t30[0] + t30[1] + t30[2]
    t3_ogata = t30

    obj = [10103]
    tabletitle = "外食"
    tableid = "table4"
    moneydata = select_GenreData(objYearMonth, obj)
    t4_gaisyoku = print_moneytable(objYearMonth, moneydata,tabletitle,tableid)

    objCategory = [105,25504225]
    tabletitle = "公共料金"
    tableid = "table5"
    moneydata = select_RawCategoryData(objYearMonth, objCategory,'place')
    moneydata0 = checkPediodicalfees(moneydata, objYearMonth)
    t5_kokyo = print_moneytable(objYearMonth, moneydata0, tabletitle,tableid)

    t0a = """
    
    <!--- 出費詳細tab中身ここから --->
    """


    t0b = """
    <!--- 出費詳細tab中身ここまで --->
    
    """
    
    #     # 支払い以外リスト (口座)
    tabletitle = "入金・振り替えリスト"
    moneydata = select_nonPaymentData(objYearMonth)
    tatekae = print_nonPaymenttable(objYearMonth, moneydata, tabletitle, "tablerep0")
    banktable = print_banktable(objYearMonth, moneydata, "銀行口座出納", "monthlybanktable")

    #     return t0a + t1[3] + t2[3] + t3[3] + t4[3] + t5[3] + t0b
    return t0a + t4_gaisyoku[3] + t2_kyoiku[3] + t1_hendo[3] + t3_ogata[3]  + t5_kokyo[3]          + banktable[3] + tatekae[3] + t0b
    
#     "詳細を外食・書籍・変動・大型・公共・口座・立替・振替の順にする"


# In[ ]:




# In[ ]:




# In[ ]:




# In[39]:

def get_yearly_banktabletext(objYear=2016):
    bankid = (8105914, 8105916, 8105937, 8133263)
    bankname = {8105914:'家の口座(UFJ)', 8105916:'家の口座 (ソニー)', 8105937:'ソニー銀行（積み立て）', 8133263:'智花（ゆうちょ)'}
    banknname = {8105914:'bank_ufj', 8105916:'bank_sony', 8105937:'bank_sony2', 8133263:'bank_chika'}



    #  {('家の口座(UFJ)', 8105914), ('家の口座 (ソニー)', 8105916)}
    # {('ソニー銀行（積み立て）', 8105937), ('智花（ゆうちょ)', 8133263)}

    bdata = {}
    for bid in bankid:
        bdata[bid] = []

    for mm in range(0,12):
        objYearMonth=(objYear,mm)
        moneydata = select_nonPaymentData(objYearMonth)
        bankdata = get_bankdata(moneydata)
        # bankidごとの辞書に組み替え
        for bid in bankid:
            for bd in bankdata:
                if bd['from_account_id'] == bid:
                    bdata[bid].append(bd)

    bdtxt = {}
    amount = {}
    bdtxt0 = ''

    for key in bankid:
        txts = []
        m = 0
        wd0 = 0
        dp0 = 0
        for bd0 in bdata[key]:
            if bd0['deposit'] == 0:
                bd0deposit = """<td class="text-muted">¥0</td>"""
            else:
                bd0deposit = """<td>¥{:,}</td>""".format(bd0['deposit'])
            if bd0['withdraw'] == 0:
                bd0withdraw = """<td class="text-muted">¥0</td>"""
            else:
                bd0withdraw = """<td>¥{:,}</td>""".format(bd0['withdraw'])
            
            
            if bd0['date'].month == m or m == 0:
                txt = """<tr>
            \t<td>{}/{}</td>
            \t{}
            \t{}
            \t<td>{}</td>
            </tr>
            """.format(bd0['date'].month, bd0['date'].day, 
                       bd0deposit,bd0withdraw, 
                       bd0['name'])
            else:
                txt = """<tr style="border-top-color:red;">
            \t<td>{}/{}</td>
            \t{}
            \t{}
            \t<td>{}</td>
            </tr>
            """.format(bd0['date'].month, bd0['date'].day,
                       bd0deposit, bd0withdraw, 
                       bd0['name'])


            txts.append(txt)
            m = bd0['date'].month
            wd0 = wd0 + bd0['withdraw']
            dp0 = dp0 + bd0['deposit']
            

        s = wd0-dp0
        c = len(txts)
        (theader, tfooter) = get_yearly_bank_headerfooter(wd0, dp0, bankname[key], c, s, banknname[key])
        
        tbody = "".join(txts)
        bdtxt[key] = theader + tbody + tfooter
        bdtxt0 = bdtxt0 + bdtxt[key]
#         amount[key] = {'withdraw':wd0, 'deposit':dp0}
    
    return bdtxt, bankid, bdtxt0



# In[40]:

def get_yearly_bank_headerfooter(sumwd, sumdep, name, countbk, sumamount, tableid):
    tableheader = """<div class="panel panel-primary">
            <div class="panel-heading">{bankname}<span class="badge pull-right">{countbk}件 ¥{sumamount:,}</span></div>
            <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
                <thead>
                    <tr>
                        <th class="text-center">日付</th>
                        <th class="text-center">入金</th>
                        <th class="text-center">出金</th>
                        <th class="text-center">memo</th>
                    </tr>
                </thead>
                <tbody class="text-center">""".format(
        bankname = name, countbk = countbk, sumamount=sumamount, tableid=tableid)
    
    tablefooter = """
                </tbody>
                <tfoot>
                        <th class="text-center">小計</th>
                        <th class="text-center">¥{sum_withdraw:,}</th>
                        <th class="text-center">¥{sum_deposit:,}</th>
                        <th class="text-center"></th>
                </tfoot>
            </table>
        </div>
    </div>""".format(sum_withdraw = sumwd, sum_deposit = sumdep)
    
    return tableheader, tablefooter


# In[41]:

def checkPediodicalfees(moneydata, objYearMonth):
    periodicalfees = ['CATV品川',
     'IIJ (さえ)',
     'IIJ (たか)',
     '共済医療保険（たか）',
     '団体生命保険（たか）',
     '東京ガス',
     '東京電力',
     '育英会',
     'ひまわり生命',
     'プレデンシャル生命（さえ）',
     #'プレデンシャル生命（たか）',
     '東京都水道局',
     'NHK受信料']
    # 'ZAIM',
    # 'iCloud (さえ)',
    # 'iCloud (たか)']


    periodicalfeedata = []
    for place in periodicalfees:
        t = {}
        t['place'] = place
        t['amount'] = 0
        t['date'] = "{}-{:02d}-25".format(objYearMonth[0], objYearMonth[1])
        t['category'] = '公共料金'
        t['genre'] = '未入力'
        t['genre_id'] = '0'
        t['name'] = ''
        t['from_account'] = ''
#         t['comment'] = ''
        periodicalfeedata.append(t)


    for x in moneydata:
        t = {}
        t['place'] = x['place']
        t['amount'] = x['amount']
        t['date'] = x['date']
        t['category'] = x['category']
        t['genre'] = x['genre']
        t['genre_id'] = x['genre_id']
        t['name'] = x['name']
        t['from_account'] = x['from_account']
#         t['comment'] = x['comment']


        if t['place'] in periodicalfees:
            indx = periodicalfees.index(x['place'])
            if periodicalfeedata[indx]['genre_id'] == '0':
                periodicalfeedata[indx] = t
            else:
                periodicalfeedata[indx]['amount'] += t['amount']
        else:
            periodicalfeedata.append(t)
                
            

#             periodicalfeedata[indx]['amount'] = x['amount']
#             periodicalfeedata[indx]['date'] = x['date']
#             periodicalfeedata[indx]['category'] = x['category']
#             periodicalfeedata[indx]['genre'] = x['genre']
#             periodicalfeedata[indx]['genre_id'] = x['genre_id']
#             periodicalfeedata[indx]['name'] = x['name']
#             periodicalfeedata[indx]['from_account'] = x['from_account']

    return periodicalfeedata


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[42]:

def get_quarterly_detailtab_body(objYear):
    TH = 1000

    objCategory = [107,  106, 108, 110, 111]
    tabletitle = "変動費"
    tableid = "table1"
    
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_CategoryData((objYear,objMonth), objCategory, TH)
        moneydata = moneydata + monthlydata
    t1 = print_moneytable((objYear,objMonth), moneydata, tabletitle, tableid)
    
    # ====
    #                 # ('積)住まい・家財', 106),('積)交際費', 107),('積)娯楽', 108),
                # ('積)教育・教養', 109),('積)医療・健康', 110)美容美容 111


    objCategory = [106]
    tabletitle = "変動> 家財"
    tableid = "table106"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_CategoryData((objYear,objMonth), objCategory, TH)
        moneydata = moneydata + monthlydata
    t1_6 = print_moneytable((objYear,objMonth), moneydata, tabletitle, tableid, 10000) # rev2.3 add th=10000
    

    objCategory = [107]
    tabletitle = "変動> 交際費"
    tableid = "table1"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_CategoryData((objYear,objMonth), objCategory, TH)
        moneydata = moneydata + monthlydata
    t1_7 = print_moneytable((objYear,objMonth), moneydata, tabletitle, tableid, 10000) # rev2.3 add th=10000
    

    objCategory = [108]
    tabletitle = "変動> 娯楽費"
    tableid = "table108"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_CategoryData((objYear,objMonth), objCategory, TH)
        moneydata = moneydata + monthlydata
    t1_8 = print_moneytable((objYear,objMonth), moneydata, tabletitle, tableid, 10000) # rev2.3 add th=10000
    

    objCategory = [110]
    tabletitle = "変動> 医療・健康"
    tableid = "table110"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_CategoryData((objYear,objMonth), objCategory, TH)
        moneydata = moneydata + monthlydata
    t1_10 = print_moneytable((objYear,objMonth), moneydata, tabletitle, tableid, 10000) # rev2.3 add th=10000
    
    objCategory = [111]
    tabletitle = "変動> 服飾"
    tableid = "table111"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_CategoryData((objYear,objMonth), objCategory, TH)
        moneydata = moneydata + monthlydata
    t1_11 = print_moneytable((objYear,objMonth), moneydata, tabletitle, tableid, 10000) # rev2.3 add th=10000
    # --



    
    
    
    
    

    #def print_CategoryTable(objYearMonth, objCategory):
    objCategory = [25504271,109]
    tabletitle = "教育・書籍"
    tableid = "table2"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_CategoryData((objYear,objMonth), objCategory, TH)
        moneydata = moneydata + monthlydata
    t2 = print_moneytable((objYear,objMonth), moneydata,tabletitle,tableid, 26000) # rev2.3 add th=10000

    objCategory = [114] #[17503724, 11, 12, 13, 14, 15, 114, 19]
    tabletitle = "大型出費"
    tableid = "table3"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_CategoryData((objYear,objMonth), objCategory, TH)
        moneydata = moneydata + monthlydata
    t3 = print_moneytable((objYear,objMonth), moneydata,tabletitle,tableid, 10000) # rev2.3 add th=10000

    obj = [10103]
    tabletitle = "外食"
    tableid = "table4"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_GenreData((objYear,objMonth), obj, TH)
        moneydata = moneydata + monthlydata
    t4 = print_moneytable((objYear,objMonth), moneydata,tabletitle,tableid, 10000) # rev2.3 add th=10000

    # 口座リスト
    t5a = get_yearly_banktabletext(objYear) # 0:bankidごとにtable_textが入っている, 1:bankid, 2:一つのtableにまとめたもの
    
    # 支払い以外リスト (口座)
    tabletitle = "入金・振り替えリスト"
    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_nonPaymentData((objYear,objMonth))
        moneydata = moneydata + monthlydata

#     t5 = print_nonPaymenttable((objYear,objMonth), moneydata, tabletitle, "table5")
#     banktable = print_banktable((objYear,objMonth), moneydata, "銀行口座出納", "monthlybanktable")

    moneydata0 = []
    for m in moneydata:
        if (m['place'][0:2] == 'たか' or m['to_account'] == 'たか'):
            moneydata0.append(m)

    t5t = print_nonPaymenttable((objYear,objMonth), moneydata0, "入出金(たか)", "table5t")

    moneydata0 = []
    for m in moneydata:
        if (m['place'][0:2] == 'さえ' or m['to_account'] == 'さえ'):
            moneydata0.append(m)

    t5s = print_nonPaymenttable((objYear,objMonth), moneydata0, "入出金(さえ)", "table5s")
    
    t0a = """
    
    <!--- 出費詳細tab中身ここから --->
    """


    t0b = """
    <!--- 出費詳細tab中身ここまで --->
    
    """
#     return t0a + t1[3] + t2[3] + t5a[2] + t5[3]  + t3[3] + t4[3] + t0b
# rev2.3    return t0a + t1_7[3] + t1_8[3] + t1_11[3] + t1_10[3] + t1_6[3] + t2[3] + t5a[2] + t3[3] + t4[3] + t0b
    return t0a + t1_7[3] + t1_8[3] + t1_11[3] + t1_10[3] + t1_6[3] + t2[3] + t4[3] + t3[3] + t5a[2] + t5t[3] + t5s[3] + t0b


# In[ ]:




# In[ ]:




# In[ ]:




# In[43]:

def get_yearly_KStab_body(objYear):
    
    moneylist = get_kakuteishinkoku(objYear)
    #    moneylist.keys()
    cat0 = ['国民年金',  '確定拠出年金', '火災傷害保険', '生命保険', 'ふるさと納税', '医療費(病院・薬局・移動)','その他保険']
    tableid = 'hoken'

    t1 = print_moneytable((objYear,1), moneylist[cat0[0]], cat0[0], tableid)
    t2 = print_moneytable((objYear,1), moneylist[cat0[1]], cat0[1], tableid)
    t3 = print_moneytable((objYear,1), moneylist[cat0[2]], cat0[2], tableid)
    t4 = print_moneytable((objYear,1), moneylist[cat0[3]], cat0[3], tableid)
    t5 = print_moneytable((objYear,1), moneylist[cat0[4]], cat0[4], tableid)
    t6 = print_moneytable((objYear,1), moneylist[cat0[5]], cat0[5], tableid)
    t7 = print_moneytable((objYear,1), moneylist[cat0[6]], cat0[6], tableid)    
    
    t0a = """
    
    <!--- 出費詳細tab中身ここから --->
    """


    t0b = """
    <!--- 出費詳細tab中身ここまで --->
    
    """
#     return t0a + t1[3] + t2[3] + t5a[2] + t5[3]  + t3[3] + t4[3] + t0b
    return t0a + t1[3] + t2[3] + t3[3] + t4[3] + t5[3] + t6[3] + t0b


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[44]:

def get_monthlyRent(objYearMonth):
    #['たか', 1], ['さえ', 4], [家計, 7]
    
    rent_in = {}
    rent_out = {}
    
    
    if objYearMonth[0] >= 2016:
        # 2016年から積立) の運用をやめたため
        tosae = "さえ"
        totaka = "たか"
        fromsae = 4
        fromtaka = 1
    else:
        tosae = "積立）さえ"
        totaka = "積立）たか"
        fromsae = 827184
        fromtaka = 827175
        
    # 清算
    moneydata = select_nonPaymentData(objYearMonth)
    rent_in['home'] = sum([x['amount'] for x in moneydata if x['mode'] == 'income' and x['to_account_id'] ==7])
    rent_in['taka'] = sum(
        [x['amount'] for x in moneydata if x['mode'] == 'transfer' and x['to_account_id'] == 1]) + sum(
        [x['amount'] for x in moneydata if x['mode'] == 'transfer' and x['to_account_id'] == 827175])
    rent_in['sae'] = sum(
        [x['amount'] for x in moneydata if x['mode'] == 'transfer' and x['to_account_id'] == 4]) + sum(
        [x['amount'] for x in moneydata if x['mode'] == 'transfer' and x['to_account_id'] == 827184])

# {0: [None, 0],
#  1: ['たか', 1],
#  4: ['さえ', 4],
#  7: ['家計', 7],
#  827175: ['積立）たか', 827175],
#  827184: ['積立）さえ', 827184],
#  7656126: ['積立）家計', 7656126],
 
    moneylist = select_fromAccount(objYearMonth,1)
    rent_out['home'] = sum([x['amount'] for x in moneylist])

    moneylist0 = select_fromAccount(objYearMonth,4)
    moneylist1 = select_fromAccount(objYearMonth,827184)
    rent_out['sae'] = sum([x['amount'] for x in moneylist0]) + sum([x['amount'] for x in moneylist1])

    moneylist0 = select_fromAccount(objYearMonth,1)
    moneylist1 = select_fromAccount(objYearMonth,827175)
    rent_out['taka'] = sum([x['amount'] for x in moneylist0]) + sum([x['amount'] for x in moneylist1])
    
    return rent_in, rent_out

# (rentin, rentout) = get_monthlyRent(objYearMonth)


# In[45]:

def get_reporttabheader (objYearMonth):
    pagerlinks = get_pagerlinks(objYearMonth)

    headertext = """
    <ul class="nav nav-tabs" style="margin:20px 0">
      <li id="summarytab"><a href="#summary" data-toggle="tab">サマリー</a></li>
      <li id="reporttab" class="active"><a href="#report" data-toggle="tab">レポート</a></li>
      <li id="graphtab"><a href="#graph" data-toggle="tab">グラフ</a></li>
      <li id="detailtab"><a href="#moneylist" data-toggle="tab">出費詳細</a></li>
    </ul>

    <div class="tab-content">


      <!-- ### report tab ここから ### -->
      <div class="tab-pane" id="report">
        <div class="col-sm-1 hidden-xs"></div>
          <div class="col-sm-10 col-xs-12">
          <ul class="pager">
            {}
          </ul>

    """.format(pagerlinks)
    return headertext

def get_reporttabfooter(objYearMonth):
    pagerlinks = get_pagerlinks(objYearMonth)

    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
        <div class="col-sm-1 hidden-xs"></div>
      </div>
      <!-- ### report tab ここまで ### -->
      """.format(pagerlinks)

    return footertext


# In[46]:


def get_graphtabheader (objYearMonth):
    pagerlinks = get_pagerlinks(objYearMonth)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### graph tab ここから ### -->
      <div class="tab-pane" id="graph">
        <div class="col-sm-1 hidden-xs"></div>
          <div class="col-sm-10 col-xs-12">
            <ul class="pager">
              {}
            </ul>
    """.format(pagerlinks)
    return headertext

def get_graphtabfooter(objYearMonth):
    pagerlinks = get_pagerlinks(objYearMonth)

    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
        <div class="col-sm-1 hidden-xs"></div>
      </div>
      <!-- ### graph tab ここまで ### -->
      """.format(pagerlinks)
    return footertext

#get_graphtabfooter((objYear,objMonth))


# In[47]:

def get_pagerlinks(objYearMonth):
    #objDT1 = (objYear, objMonth)
    objDT0 = get_lastmonth(objYearMonth)
    objDT2 = get_nextmonth(objYearMonth)

    tnow = dt.now()
    if tnow.year == objYearMonth[0] and tnow.month == objYearMonth[1]:
        pagerlinks = """<li class = "previous"><a href="./m{}-{:02}.html">previous</a></li>
        """.format(objDT0[0],objDT0[1])
    elif objYearMonth[0] == 2011 and objYearMonth[1] == 1:
        pagerlinks = """<li class = "next"><a href="./m{}-{:02}.html">next</a></li>
        """.format(objDT2[0],objDT2[1])
    else:
        pagerlinks = """<li class = "previous"><a href="./m{}-{:02}.html">previous</a></li>
            <li class = "next"><a href="./m{}-{:02}.html">next</a></li>
        """.format(objDT0[0], objDT0[1],objDT2[0], objDT2[1])

        
    
#     prev_filename = ("m{}-{}.html").format(objDT0[0], objDT0[1])
#     next_filename = ("m{}-{}.html").format(objDT2[0], objDT2[1])
#     return prev_filename, next_filename

    return pagerlinks

    

    


# In[48]:

def get_categorydatastr(objYearMonth, obj=0):
    if obj == 0:
        receiptlist = select_Wholedata(objYearMonth)
    else:
        receiptlist = select_CategoryData(objYearMonth, obj)
        
    dailydata = getDailyData_fromDB(receiptlist,objYearMonth)
    objMonthdayList = get_monthday(objYearMonth[0], objYearMonth[1])

    places = []
    amounts = []
    cumsum = 0
    cumsums = []
    for d in objMonthdayList:
        if dailydata[d]['amount']:
            amounts.append('"{}"'.format(str(dailydata[d]['amount'])))
            places.append('"{}"'.format(dailydata[d]['max_place']))
            cumsum = cumsum + dailydata[d]['amount']
        else:
            amounts.append('""')
            places.append('""')
            cumsum = cumsum + 0
        
        cumsums.append(cumsum)

    tamounts = ','.join(amounts)
    tplaces = ','.join(places)
    tcumsum = ",".join(['"{}"'.format(str(x)) for x in cumsums])
    return tcumsum,tplaces


# In[49]:

get_monthdaya = lambda year,month:['"{day}"'.format(year=year,month=month,day=i+1) 
                                  for i in range(0,calendar.monthrange(year, month)[1])]



# In[50]:

def get_yearlypublickfees_reporttab_body(objYear):
    monthlyamounts = []
    pfeestd = {}

    for objMonth in range(1,13):
        monthlypf = get_monthlypublickfees((objYear,objMonth))
        monthlypf['all'] = sum([v for k,v in monthlypf.items()])
        monthlyamounts.append(monthlypf)

    for key in monthlyamounts[0].keys():
        #qdata[key] = [x[key] for x in monthlyamounts]
        y = ["<td>¥{:,}</td>".format(round500(x[key])) for x in monthlyamounts]
        y.append("<td><strong>¥{:,}</strong></td>".format(round500(sum([x[key] for x in monthlyamounts]))))
        pfeestd[key] = '\n\t\t\t'.join(y)
    

    summarytable0 = """
    <!-- output from PyJade -->
    
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center" style="min-width: 80px;">{objY}年</th>
                        <th class="text-center">1月</th>
                        <th class="text-center">2月</th>
                        <th class="text-center">3月</th>

                        <th class="text-center">4月</th>
                        <th class="text-center">5月</th>
                        <th class="text-center">6月</th>

                        <th class="text-center">7月</th>
                        <th class="text-center">8月</th>
                        <th class="text-center">9月</th>

                        <th class="text-center">10月</th>
                        <th class="text-center">11月</th>
                        <th class="text-center">12月</th>

                        <th class="text-center" style="font-weight:bold">小計</th>
                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>{key1}</td>
                        {td1}
                    </tr>    
                    <tr>
                        <td>{key2}</td>
                        {td2}
                    </tr>    
                    <tr>
                        <td>{key3}</td>
                        {td3}
                    </tr>    
                    <tr>
                        <td>{key4}</td>
                        {td4}
                    </tr>    
                    <tr>
                        <td>{key5}</td>
                        {td5}
                    </tr>    
                    <tr>
                        <td>{key6}</td>
                        {td6}
                    </tr>    
                    <tr>
                        <td>{key7}</td>
                        {td7}
                    </tr>
                  </tbody>
                  <tfoot class="bg-info">
                    <tr class="text-center" style="font-weight:bold;">
                        <td>{key8}</td>
                        {td8}
                    </tr>""".format(
            objY = objYear,
            key1 = '電気料金', 
            td1 = pfeestd['電気料金'],

            key2 = 'ガス料金', 
            td2 = pfeestd['ガス料金'],

            key3 = '水道料金', 
            td3 = pfeestd['水道料金'],

            key4 = 'TV', 
            td4 = pfeestd['NHK'],

            key5 = '家通信費', 
            td5 = pfeestd['家インターネット'],

            key6 = 'モバイル通信費', 
            td6 = pfeestd['モバイル通信費'],

            key7 = '社会保障', 
            td7 = pfeestd['社会保障'],

            key8 = '小計', 
            td8 = pfeestd['all'],)

    

    summarytable1 = """
                </tfoot>
            </table>
        </div>
    </div>
"""
    tabletabbody = "\n<!-- #### report tab ここから #### -->\n" + summarytable0 + summarytable1 +"\n<!-- #### report tab ここまで #### -->\n"

    
    return tabletabbody





# In[51]:


def get_detailtabheader (objYearMonth):
    pagerlinks = get_pagerlinks(objYearMonth)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### 詳細 tab ここから ### -->
        <div class="tab-pane" id="moneylist">
          <div class = "row">
            <div class="col-sm-1 hidden-xs"></div>
            <div class="col-sm-10 col-xs-12">
              <ul class="pager">
                {}
              </ul>
              
              <ul class="btn-group btn-group-justified  btn-group-sm" role="group" aria-label="testa" style="padding-left:0px;">
                <li type="button" class="btn btn-default"><a href="#table1">変動費</a></button>
                <li type="button" class="btn btn-default"><a href="#table2">教育・書籍</a></button>
                <li type="button" class="btn btn-default"><a href="#table3">大型出費</a></button>
                <li type="button" class="btn btn-default"><a href="#table4">外食</a></button>
                <li type="button" class="btn btn-default"><a href="#table5">公共料金</a></button>
              </ul>

    """.format(pagerlinks)
    return headertext

def get_detailtabfooter(objYearMonth):
    pagerlinks = get_pagerlinks(objYearMonth)

    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
      </div>
    </div>
    <!-- ### 詳細 tab ここまで ### -->
      """.format(pagerlinks)

    return footertext



# In[52]:

def get_summarytab(objYearMonth):
    pagerlinks = get_pagerlinks(objYearMonth)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### summary tab ここから ### -->
        <div class="tab-pane" id="summary">
          <div class = "row">
            <div class="col-sm-1 hidden-xs"></div>
            <div class="col-sm-10 col-xs-12">
              <ul class="pager">
                {}
              </ul>
    """.format(pagerlinks)

    # レポートテキスト
    reporttext = getReportText(objYearMonth)

    ttxt = "<hr>"
#     genretable = get_genressummarytable(objYearMonth)

    genretable = get_genressummarytableFP(objYearMonth)
    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
      </div>
    </div>
    <!-- ### 詳細 tab ここまで ### -->
      """.format(pagerlinks)

    return "".join([headertext, reporttext, ttxt, genretable[3], footertext])




# In[53]:

def monthly_inputcheck(objYearMonth): # rev2.3
    # 12608296: ['月度チェック', 12608296]}
    gdata = select_RawGenreData(objYearMonth, [13068828])

    t = {}
    #checklist = ['智花ゆうちょ', '給与・小遣い整理', '公共料金', 'クレジットカード', 'レシート', 'UFJ銀行', 'ソニー銀行']
    checklist0 = [
        {"type":"家賃", "name":"家賃", "flg":0},
        {"type":"生協", "name":"生協", "flg":0},
        {"type":"保育費", "name":"養育費", "flg":0},
        {"type":"奨学金", "name":"奨学金", "flg":0},
        {"type":"保険", "name":"保険", "flg":0},
        {"type":"公共料金", "name":"公共料金", "flg":0},
        {"type":"レシート",     "name":"レシート", "flg":0},
        {"type":"クレジットカード",     "name":"カード", "flg":0},
        {"type":"給与・小遣い整理", "name":"給与・小遣い", "flg":0},
        {"type":"智花ゆうちょ",     "name":"智花ゆうちょ", "flg":0},
        {"type":"ソニー銀行",     "name":"ソニー銀行", "flg":0},
        {"type":"UFJ銀行",     "name":"UFJ", "flg":0}
    ]
    
    checklist = [x['type'] for x in checklist0]


    
#     for chck in checklist:
#         t[chck] = """<input type="checkbox" name="">{}""".format(chck)
    t = ""

    for x in gdata:
        name = x['name']
        flg = abs(x['amount'])
        t0 = ""
        cnt = 0
        for chck in checklist:
            if name == chck:
                checklist0[cnt]['flg'] = flg
            cnt += 1

    return checklist0



# In[54]:

# monthly_inputcheck((2017,4))


# In[55]:

def inputcomment(commenttype, objYear, objMonth):
    f = open('inputcomment.json', 'r')
    comment = json.load(f)
    f.close()
    
#     comment = [
#         {'type':'quarter', 'year':'2017', 'month':'q1', 'comment':'aiueoaiueoaiueo'},
#         {'type':'quarter', 'year':'2017', 'month':'q2', 'comment':''},
#         {'type':'month', 'year':'2017', 'month':'10', 'comment':''},
#         {'type':'year', 'year':'2017', 'month':'0', 'comment':''}
#     ]
    
    icomment = ''

    for x in comment:
        if commenttype == x['type'] and objYear == x['year'] and objMonth == x['month']:
            icomment = x['comment']
            break
    
    if icomment != '':
        icomment = "<blockquote>" + icomment + '<footer class="blockquote-footer">comment</footer></blockquote>'
    return icomment




# In[ ]:




# In[ ]:




# In[56]:

def get_yearly_summarytab_body(objYear):
#     check, category, delta, amount, catn, expensive = get_yearly_summarytab_text(objYear)

    check, category, amount, catn, expensive = get_yearly_summarytab_text(objYear)

    htext = '<blockquote>ここでは1. 入出金, 2. カテゴリ毎の支出, 3. 大きなカテゴリとその明細, 4. 高額出費をまとめています。</blockquote>'
    
    
    qtext = []
    for cnt in range(0,4):
        comment = inputcomment("quarter", str(objYear), "q"+str(cnt+1))
        
        mtable = monthlytableforYsummary((objYear,cnt*3+3))
        qt = """<div class="panel panel-primary" id="q{}">
        <div class="panel-heading">
        {}年Q{}
        </div>
        <div class="panel-body">
        {}
        </div>
        </div>""".format(cnt+1, objYear, cnt+1, check[cnt] + htext + comment + category[cnt] + amount[cnt]+ mtable + catn[cnt] + expensive[cnt])
#         </div>""".format(objYear, cnt+1, check[cnt] + category[cnt]+ delta[cnt]+ amount[cnt]+ mtable + catn[cnt] + expensive[cnt])

        
        qtext.append(qt)
    
    return '\n\n\n'.join(qtext)
    
    


    
    
    



# In[ ]:




# In[57]:

def get_yearly_summarytab_text(objYear):

    ##############################
    def yearly_inputcheck(objYear):
        yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        qdata = []
        for qq in yq:
            qqdata = []
            for mm in qq:
                moneydata = monthly_inputcheck((objYear, mm))
                qqdata.append(moneydata)
            qdata.append(qqdata)
        return qdata
    
    def build_inputchecktext(checkresult):
        qtxts = []
        qq = 1
        mm = 1

        for qlist in checkresult:
            txth = "<p>家計簿入力状況は<ul>\n"
            qq += 1
            mtxts = []
            for mlist in qlist:
                txts = []
                for exp in mlist:
                    if exp['flg'] == 0:
                        txts.append("「"+exp['name']+"」")
                if len(txts)==0:
                    mtxt = "<li>{}月の家計簿は入力済みです</li>".format(mm)
                else:
                    mtxt = "<li>{}月は".format(mm) + ','.join(txts)+"の入力が残っています</li>"
                mtxts.append(mtxt)
                mm += 1
            qtxt = txth + '\n'.join(mtxts) + "</ul></p>"
            qtxts.append(qtxt)

        return qtxts

################################################

    chkresult = yearly_inputcheck(objYear)
    chktext = build_inputchecktext(chkresult)
    
################################################

    def yearly_incomes(objYear):
        yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        qdata = []
        for qq in yq:
            qqdata = 0
            for mm in qq:
                incomes = get_monthlyIncomes((objYear,mm))
                qqdata += incomes['sum']
            qdata.append(qqdata)

        #先期分
        qqdata = 0
        qq = yq[3]
        for mm in qq:
            incomes = get_monthlyIncomes((objYear-1,mm))
            qqdata += incomes['sum']
        qdata.append(qqdata)


        return qdata
    
    def yearly_monthlyamount(objYear):
        yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        qdata1 = []
        qdata0 = []
        for qq in yq:
            qqdata0 = []
            qqdata1s = 0
            qqdata1l = 0
            for mm in qq:
                t = select_Wholedata((objYear,mm))
                # 出費を計算するときは cat'口座'を引くこと。
                monthsum = [x['amount'] for x in t if x['category'] != '口座']
                qqdata1s += sum(monthsum)
                qqdata1l += len(monthsum)
                qqdata0.append([sum(monthsum),len(monthsum)])
            qdata0.append(qqdata0)
            qdata1.append([qqdata1s, qqdata1l])

        # 先期分
        qq = yq[3]
        qqdata0 = []
        qqdata1s = 0
        qqdata1l = 0
        for mm in qq:
            t = select_Wholedata((objYear-1,mm))
            # 出費を計算するときは cat'口座'を引くこと。
            monthsum = [x['amount'] for x in t if x['category'] != '口座']
            qqdata1s += sum(monthsum)
            qqdata1l += len(monthsum)
            qqdata0.append([sum(monthsum),len(monthsum)])
        qdata0.append(qqdata0)
        qdata1.append([qqdata1s, qqdata1l])


        return qdata0, qdata1

    def yearly_rentinout(objYear):
        yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        qdata = []
        for qq in yq:
            qqin = {}
            qqout = {}
            for k in ['sae', 'home', 'taka']:
                qqin[k] = 0
                qqout[k] = 0
            for mm in qq:
                tin, tout = get_monthlyRent((objYear,mm))
                # 出費を計算するときは cat'口座'を引くこと。
                for k in tin:               
                    qqin[k]  += tin[k]
                    qqout[k] += tout[k] 
            qdata.append({'clear':qqin, 'rent':qqout})    

        ## 先期分
        qqin = {}
        qqout = {}
        qq = yq[3]
        for k in ['sae', 'home', 'taka']:
            qqin[k] = 0
            qqout[k] = 0
        for mm in qq:
            tin, tout = get_monthlyRent((objYear-1,mm))
            # 出費を計算するときは cat'口座'を引くこと。
            for k in tin:               
                qqin[k]  += tin[k]
                qqout[k] += tout[k] 
        qdata.append({'clear':qqin, 'rent':qqout}) 


        return qdata



    def build_categoryamounttext(qincome, qamount, qrent):
        txts = []
        for cnt in range(0,4):
            income = qincome[cnt]
            outcome = qamount[1][cnt][0]
            outcomen = qamount[1][cnt][1]
            rent = qrent[cnt]['rent']['sae'] + qrent[cnt]['rent']['taka']
            clear = qrent[cnt]['clear']['sae'] + qrent[cnt]['clear']['taka']

            income0 = qincome[cnt-1]
            outcome0 = qamount[1][cnt-1][0]
            outcomen0 = qamount[1][cnt-1][1]
            rent0 = qrent[cnt-1]['rent']['sae'] + qrent[cnt-1]['rent']['taka']
            clear0 = qrent[cnt-1]['clear']['sae'] + qrent[cnt-1]['clear']['taka']

            incomedelta = income - income0
            outcomedelta = outcome - outcome0
            rentdelta = rent - rent0
            cleardelta = clear - clear0

            total = income - outcome - clear
            t1 = """
<p>入出金は<ol>
<li>入金: \t¥{income:,}</li>
<li>出金:   \t¥{outcome:,} ({outcomen}件)</li>
<li>立替:   \t¥{rent:,}</li>
<li>立替清算:\t¥{clear:,}</li>
<li>総計(入金-支出-清算)は\t¥{total:,}円でした。</li></ol></p>""".format(income = round500(income), 
                                     outcome = round500(outcome), outcomen = round500(outcomen),
                                     rent = round500(rent), clear = round500(clear), total = round500(total))

            t2 = """
<p>ちなみに先期は① ¥{income0:,}, ②¥{outcome0:,} ({outcomen0}件), ③¥{rent0:,}円, ④¥{clear0:,}円、<br>
比較すると①¥{incomedelta:,}, ②¥{outcomedelta:,}, ③¥{rentdelta:,}, ④¥{cleardelta:,}でした。</p>
             """.format(income0 = round500(income0), outcome0 = round500(outcome0), outcomen0 = round500(outcomen0),
                       rent0 = round500(rent0), clear0 = round500(clear0),
                       incomedelta = round500(incomedelta), outcomedelta = round500(outcomedelta), 
                        rentdelta = round500(rentdelta), cleardelta = round500(cleardelta))

            txts.append(t1 + "\n\n" + t2)

            """
            """
        #     ちなみに先期は①円, ② 円(件), ③ 円, ④ 円、
        #     比較すると①円, ② 円, ③ 円, ④ 円でした。
        #     """

        return txts

    ################################################


    qamount = yearly_monthlyamount(objYear)
    qrent = yearly_rentinout(objYear)
    qincome = yearly_incomes(objYear)
#     categorytext = build_categoryamounttext(qincome, qamount, qrent)
    categorytext = totaltableforYsummary(qincome, qamount, qrent)
    
#     result = yearly_categoryamount(objYear)
#     cattext = build_categoryamount(result)


##############################################################

    def categorykeys():
        t = get_monthlyamount((2017,4))
        amountkeys = [x for x in t]
        ignorekeys = ['変動費', 'all', '公共料金']
        for ik in ignorekeys:
            amountkeys.remove(ik)
        return amountkeys

        
        
    def yearly_categorydelta(objYear):
        yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        qqdata = []
        aqqdata = []
        
        amountkeys = categorykeys()

        qdata = {}
        aqdata = {}



        for qq in yq:
            for k in amountkeys:
                qdata[k] = 0
                aqdata[k] = []

            for mm in qq:
                moneydata = get_monthlyamount((objYear, mm))
                for k in amountkeys:
                    qdata[k] += moneydata[k]       
                    aqdata[k].append(moneydata[k])
            qqdata.append(qdata.copy())
            aqqdata.append(aqdata.copy())


        for k in amountkeys:
            qdata[k] = 0
        qq = yq[3]
        for mm in qq:
            moneydata = get_monthlyamount((objYear-1, mm))
            for k in amountkeys:
                qdata[k] += moneydata[k]        
        qqdata.append(qdata.copy())

        return qqdata, aqqdata
    
    def build_categorydeltatext(categorydata):
        amountkeys = categorykeys()
        qtxts = []
        cnt = 0
        th = 50000
        for qlist in categorydata:
            txts = []
            for cat in amountkeys:
                d = qlist[cat] - categorydata[cnt-1][cat]
                
                if d > 0 and d < th:
                    atxt = "<li>「{}」:\t{:,}円\t(+{:,}千円)</li>".format(cat, 
                                                                round500(qlist[cat]), round500(d)/1000)
                elif d > th:
                    atxt = '<li style="font-color:red;">「{}」:\t{:,}円\t(+{:,}千円)</li>'.format(cat, 
                                                                    round500(qlist[cat]), round500(d)/1000)
                elif d == 0:
                    atxt = "<li>「{}」:\t{:,}円 (先期と同額)</li>".format(cat, round500(qlist[cat]))
                elif d < 0 and d > -th:
                    atxt = "<li>「{}」:\t{:,}円\t(-{:,}千円)</li>".format(cat, 
                                                                round500(qlist[cat]), round500(abs(d)/1000))
                else:
                    atxt = '<li style="font-color:blue;">「{}」:\t{:,}円\t(-{:,}千円)</li>'.format(cat, 
                                                                        round500(qlist[cat]), round500(abs(d)/1000))
                txts.append(atxt)
            cnt += 1
            qtxt = "<p>支出をカテゴリ別に見ると <ul>\n" + '\n'.join(txts) + "\n</ul></p>"
            qtxts.append(qtxt)
        return qtxts

################################################
    
#     delta = yearly_categorydelta(objYear)
#     deltatext = build_categorydeltatext(delta[0])

################################################
    def yearly_monthlyamount(objYear):
        yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        qdata1 = []
        qdata0 = []
        for qq in yq:
            qqdata0 = []
            qqdata1s = 0
            qqdata1l = 0
            for mm in qq:
                t = select_Wholedata((objYear,mm))
                # 出費を計算するときは cat'口座'を引くこと。
                monthsum = [x['amount'] for x in t if x['category'] != '口座']
                qqdata1s += sum(monthsum)
                qqdata1l += len(monthsum)
                qqdata0.append([sum(monthsum),len(monthsum)])
            qdata0.append(qqdata0)
            qdata1.append([qqdata1s, qqdata1l])
        return qdata0, qdata1




    def build_monthlyamounttext(monthlyamountresult):
        qtxts = []
        txth = "<p>月別に見ると"
        mm = 1
        #     月別に見ると1月は111円(30件), 2月は234円(23件), 3月は23434円(34件)でした


        for qlist in monthlyamountresult:
            mtxts = []
            for mlist in qlist:
                txts = []
                mtxt = "{}月は{:,}円({}件)".format(mm, mlist[0], mlist[1])
                mtxts.append(mtxt)
                mm += 1
            qtxt = txth + ', '.join(mtxts) + "でした</p>"
            qtxts.append(qtxt)
        return qtxts

################################################

    amountresult = yearly_monthlyamount(objYear)
#     amounttext = build_monthlyamounttext(amountresult[0])
    amounttext = "     "


################################################


    def yearly_catN(objYear, per=80):

    # amountkeys = categorykeys()
        t,yamount = yearly_categorydelta(objYear)
        thcat = []

        mx = 0

        for qamount in yamount:
            for cat in qamount:

                sumcat = sum(qamount[cat])
                mincat = min(qamount[cat]) * 2.25
                aveth = 1.75
                minth = 9500
                maxth = 22000
                mm = 1
                for catmyen in qamount[cat]:
                    avecat = (sumcat - catmyen)/2 * aveth        
                    if (catmyen > avecat or catmyen > mincat or catmyen > (mincat + maxth)) and catmyen > minth:
                        if catmyen > avecat and catmyen > mincat:
        #                     print("ave*1.5&min*2: {}".format(tt))
                            thcat.append([mm + mx*3 , cat, catmyen, 'am'])
                        elif catmyen > avecat and catmyen <= mincat:
        #                     print("ave*1.5: {}".format(tt))
                            thcat.append([mm + mx*3 , cat, catmyen, 'a'])
                        elif catmyen <= avecat and catmyen > mincat:
        #                     print("min*2: {}".format(tt))
                            thcat.append([mm + mx*3 , cat, catmyen, 'm'])



                    mm += 1
            mx += 1

        ###
        catcodename = get_bigcats()

        cattopn = []
        for mdata in thcat:
            mm = mdata[0]
            catname = mdata[1]
            catcode= []
            for catt in catcodename:
                if catt['name'] == catname:
                    catcode = catt['cat']
            t = select_CategoryData((objYear, mm), catcode)

            catdata = [(x['amount'], x['date'] , x['place'],x['name']) for x in t]
            catdatayen = [x['amount'] for x in t]
            cd = sorted(catdatayen)

            sumyen = sum(cd)
            rateyen = 0
            cnt = -1
            indx = []
            cats = []
            while rateyen < per:
                if len(cd) <= abs(cnt)-1:
                    break
                if abs(cnt) > 5:
                    break

                rateyen += cd[cnt]/sumyen * 100
                indx0 = catdatayen.index(cd[cnt])
                cats.append(catdata[indx0])
                indx.append(indx0)

                cnt -= 1
            cattopn.append([mm, catname, sumyen, int(rateyen), cats])
        return cattopn



    def build_catNtext(cattopn):
        yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        qtext = []
        t0 = """<div class="panel panel-default">
        <div class="panel-heading">3. 特に出費の大きかったカテゴリの内訳</div>
                          <div class="panel-body">
                          <ul>"""

        for q in yq:
            tm = ''
            for m in q:
                for catn in cattopn:
                    if catn[0] == m:
                        t1 = "\n<li>{}月の{} {:,}円,支出の内訳は".format(m, catn[1], round500(catn[2]))
                        t2 = "({}件で{}%)</li>".format(len(catn[4]), catn[3])
                        t4 = []
                        for tn in catn[4]:
                            if len(tn[3]) > 10:
                                item = tn[3][:10]
                            else:
                                item = tn[3]
                            if len(tn[2]) > 10:
                                place = tn[2][:10]
                            else:
                                place = tn[2]

                            t3 = "{item}@{place} ¥{yen:,}".format(item = item, place = place, yen = round500(tn[0]))
                            t4.append(t3)
                        t5 = "\n" + t1+ t2 + '\n<ul>\n<li>' + '\n <li>'.join(t4) + "\n</ul>" 
                        tm += t5


            qtext.append('\n\n' + t0 + tm + "</ul></div></div>")
        return qtext

################################################

    catndata = yearly_catN(objYear)
    catntext = build_catNtext(catndata)



#     """
#     特に大きかった支出は (前3ヶ月比150%など)
#     1月の社会保障 円 (礼服 5万円)
#     3月の社会保障 円　（年金 3万円 カテゴリのうち75%以上のリスト)
#     3月の娯楽・交際 円
#     """

################################################
    def yearly_expensives(objYear, th = 10000):
        yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
        qdata = []
        for qq in yq:
            qqdata = []
            for mm in qq:
#                 moneydata = select_ExpenceData((objYear, mm), th)
                moneydata = select_ExpenceDataYsummary((objYear, mm), th)
                qqdata.append(moneydata)
            qdata.append(qqdata)
        return qdata

    def build_expensives0(expensives):
        qtxts = []
        key = 25504225

        for qlist in expensives:
            txts = []
            extxts = []
            for mlist in qlist:
                for exp in mlist:
                    atxt = "<li> {month}月{date}日\t[{cat}] ¥{amount:,}\t{name}@{place}</li>".format(
                        month=int(exp['date'][5:7]),date=int(exp['date'][8:]), name=exp['name'], 
                        place=exp['place'], amount=round500(exp['amount']),cat=exp['category'])
                    if m['category_id'] != key:    
                        txts.append(atxt)
                    else:
                        extxts.append(atxt)
            qtxt = "<p> 高額出費 (10,000円以上)は <ul>" + '\n'.join(txts) + '\n'.join(extxts) + "</ul></p>"
            qtxts.append(qtxt)
        return qtxts

    def build_expensives(expensives): #rev2.3

        key = 25504225 # rev2.4 社会保障は除く

        tableh0 = """
        <!-- output from PyJade -->
            <div class="panel panel-default">"""
        tableh2 = """
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed">
                    <thead class="bg-info">
                        <tr>
                            <th class="text-center">日付</th>
                            <th class="text-center">金額</th>
                            <th class="text-center">カテゴリ</th>
                            <th class="text-center">場所</th>
                            <th class="text-center">もの</th>
                        </tr>
                    </thead>
                    <tbody class="text-center">"""

        tablef =   """
                    </tbody>
                </table>
                </div>
                </div>
        """


        qtxts = []
        for qlist in expensives:
            txts = []
            extxts = [] #rev2.4 bug
            
            num = 0
            yen = 0

            for mlist in qlist:
                for exp in mlist:
                    atxt = """
                        \n\t\t<tr>\n\t\t\t<td>{month}月{day}日</td>\n\t\t\t<td>¥{amount:,}</td>
                        \t\t\t<td>{cat}</td>\n\t\t\t<td style="text-align:left;padding-left:1em">{place}</td>
                        \t\t\t<td style="text-align:left;padding-left:1em">{name}</td>\n\t\t</tr>
                        """.format( month=int(exp['date'][5:7]),day=int(exp['date'][8:]), name=exp['name'], 
                                        place=exp['place'], amount=round500(exp['amount']),cat=exp['category'])
                    if exp['category_id'] != key:    
                        txts.append(atxt)
                    else:
                        extxts.append(atxt)
                    num += 1
                    yen += exp['amount']

            tableh1 = """\t<div class="panel-heading">4. 高額出費 (10,000円以上) {}件 ¥{:,} + 家賃&小遣い63万円</div>""".format(num, round500(yen))

            qtxt = tableh0 + tableh1 + tableh2 + '\n'.join(txts) + tablef

            qtxts.append(qtxt)
        return qtxts


    result = yearly_expensives(objYear)
    expensivetext = build_expensives(result)

#     return chktext, categorytext, deltatext, amounttext, catntext, expensivetext
    return chktext, categorytext, amounttext, catntext, expensivetext




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[58]:

# print(monthlytableforYsummary((2017,3)))


# In[59]:


def monthlytableforYsummary(objYearMonth): #rev2.3
    objDT0 = objYearMonth 
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)
    m0yen, m0num =get_monthlyamount(objDT0, True)
    m1yen, m1num =get_monthlyamount(objDT1, True)
    m2yen, m2num =get_monthlyamount(objDT2, True)

#     TH = 1500
    mkey = ['食費', '光熱費', '通信費', '社会保障', '娯楽・交際', '医療・健康', '美容', '教育・養育', '大型出費', '住まい']
    
    def gettr(key, yen): # yen = [yen2, yen1, yen0]
        t0 = """
                        <tr>
                            <td>{}</td>\n""".format(key)
        t1 = []
        t2 =  """
                            <td style="text-align:right;padding-right:1em;"><strong>¥{:,}</strong></td>
                        </tr>        
        """.format(sum(yen))
        
        ### 
        mincat = min(yen) * 2.25
        aveth = 1.75
        minth = 9500
        maxth = 22000
        sumcat= sum(yen)
        mincat2 = min(yen) + maxth


        for myen in yen:
            avecat = (sumcat - myen)/2 * aveth
            if (myen > avecat or myen > mincat or myen > mincat2) and myen > minth:
                t1t = """\t\t\t\t<td style="font-weight:bold; color:red;text-align:right;padding-right:1em;">¥{val:,}</td>\n""".format(val = round500(myen))
            else:
                t1t = """\t\t\t\t<td style="text-align:right;padding-right:1em;">¥{val:,}</td>\n""".format(val = round500(myen))
            t1.append(t1t)
        return t0 + "".join(t1) + t2


    summarytableh = """
    <!-- output from PyJade -->
    <div class="panel panel-default">
        <div class="panel-heading">2. 月ごとのカテゴリ支出まとめ</div>
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-info">
                    <tr>
                        <th class="text-center">{objYear}年</th>
                        <th class="text-center">{monthM2}月 ({m2n}件)</th>
                        <th class="text-center">{monthM1}月 ({m1n}件)</th>
                        <th class="text-center">{monthM0}月 ({m0n}件)</th>
                        <th class="text-center"><strong>小計</strong></th>
                    </tr>
                </thead>
                <tbody class="text-center">""".format(
            objYear = objDT0[0],
            monthM0=objDT0[1],
            monthM1=objDT1[1],
            monthM2=objDT2[1],
            m2n = m2num['all'], m1n = m1num['all'], m0n = m0num['all'])
    
    st = []
    for key in mkey:
        st0 = gettr(key, [m2yen[key], m1yen[key], m0yen[key]])
        st.append(st0)


    summarytablef =   """
                </tbody>
                <tfoot class="bg-info">
                    <tr class="text-center">
                        <td><strong>小計</strong></td>
                        <td style="text-align:right;padding-right:1em;"><strong>¥{val0M2:,}</strong></td>
                        <td style="text-align:right;padding-right:1em;"><strong>¥{val0M1:,}</strong></td>
                        <td style="text-align:right;padding-right:1em;"><strong>¥{val0M0:,}</strong></td>
                        <td style="text-align:right;padding-right:1em;"><strong>¥{val0Ms:,}</strong></td>

                    </tr>
                </tfoot>
            </table>
            </div>
            </div>
    """.format(
            key1 = '食費/生活費', 
        key2 = '光熱費', 
            key3 = '通信費', 
            key4 = '社会保障', 
            key5 = '娯楽・交際', 
            key6 = '医療・健康', 
            key7 = '美容', 
            key8 = '教育・養育', 
            key9 = '大型出費', 
            keya = '住まい', 

        val0M0 = round500(m0yen['all']),
            val0M1 = round500(m1yen['all']),
            val0M2 = round500(m2yen['all']),
                val0Ms = round500(m2yen['all'] + m1yen['all'] + m0yen['all'])
        )
    

    tabletabbody = "\n<!-- #### report tab ここから #### -->\n"         + summarytableh + "\n".join(st) + summarytablef         + "\n<!-- #### report tab ここまで #### -->\n"

    
    return tabletabbody
    


# In[60]:


def totaltableforYsummary(qincome, qamount, qrent): #rev2.3
    incomey = 0
    outcomey = 0
    renty = 0
    cleary = 0
    
    tables = []
    for cnt in range(0,4):
        income = qincome[cnt]
        outcome = qamount[1][cnt][0]
        outcomen = qamount[1][cnt][1]
        rent = qrent[cnt]['rent']['sae'] + qrent[cnt]['rent']['taka']
        clear = qrent[cnt]['clear']['sae'] + qrent[cnt]['clear']['taka']

        income0 = qincome[cnt-1]
        outcome0 = qamount[1][cnt-1][0]
        outcomen0 = qamount[1][cnt-1][1]
        rent0 = qrent[cnt-1]['rent']['sae'] + qrent[cnt-1]['rent']['taka']
        clear0 = qrent[cnt-1]['clear']['sae'] + qrent[cnt-1]['clear']['taka']

        incomedelta = income - income0
        outcomedelta = outcome - outcome0
        rentdelta = rent - rent0
        cleardelta = clear - clear0

        incomey += income
        outcomey += outcome
        renty += rent
        cleary += clear
        
        
        total = income - outcome - clear


            
        summarytableh = """
        <!-- output from PyJade -->
        <div class="panel panel-default">
        \t<div class="panel-heading">1. 入出金のまとめ</div>
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed">
                    <thead class="bg-info">
                        <tr>
                            <th class="text-center">Q{}</th>
                            <th class="text-center">先期</th>
                            <th class="text-center">今期</th>
                            <th class="text-center">差分</th>
                            <th class="text-center">通年</th>
                        </tr>
                    </thead>
                    <tbody class="text-center">""".format(cnt+1)

        summarytableb0 = """
                            <tr>
                                <td>入金</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                            </tr>        
                            """.format(round500(income0), round500(income), round500(income-income0), 
                                       round500(incomey))

        summarytableb1 = """
                            <tr>
                                <td>出金</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                            </tr>        
                            """.format(round500(outcome0), round500(outcome), 
                                       round500(outcome-outcome0), round500(outcomey))

        summarytableb2 = """
                            <tr>
                                <td>立替</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                            </tr>        
                            """.format(round500(rent0), round500(rent), 
                                       round500(rent - rent0), round500(renty))

        summarytableb3 = """
                            <tr>
                                <td>立替清算</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                                <td style="text-align:right;padding-right:1em;">¥{:,}</td>
                            </tr>        
                            """.format(round500(clear0), round500(clear), 
                                       round500(clear - clear0), round500(cleary))

        total = income + rent - outcome - clear
        total0 = income0 + rent0 - outcome0 - clear0
        totald = total - total0
        totaly = incomey + renty - outcomey - cleary

        summarytablef =   """
                    </tbody>
                    <tfoot class="bg-info">
                        <tr class="text-center">
                            <td><strong>総計</strong></td>
                            <td style="text-align:right;padding-right:1em;"><strong>¥{:,}</strong></td>
                            <td style="text-align:right;padding-right:1em;"><strong>¥{:,}</strong></td>
                            <td style="text-align:right;padding-right:1em;"><strong>¥{:,}</strong></td>
                            <td style="text-align:right;padding-right:1em;"><strong>¥{:,}</strong></td>
                        </tr>
                    </tfoot>
                </table>
                </div>
                </div>
        """.format(round500(total0), round500(total), round500(totald), round500(totaly))


        tabletabbody = "\n<!-- #### report tab ここから #### -->\n"             + summarytableh + summarytableb0 + summarytableb1 + summarytableb2 + summarytableb3 + summarytablef             + "\n<!-- #### report tab ここまで #### -->\n"
        tables.append(tabletabbody)

    
    return tables
    


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




def build_catNtext(cattopn):
    yq = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
    qtext = []
    t0 = "特に大きかった支出は"
    for q in yq:
        tm = ''
        for m in q:
            for catn in cattopn:
                if catn[0] == m:
                    t1 = "\n<p>{}月の{} {:,}円,内訳はこちら".format(m, catn[1], round500(catn[2]))
                    t2 = "({}件で{}%です)</p>".format(len(catn[4]), catn[3])
                    t4 = []
                    for tn in catn[4]:
                        if len(tn[3]) > 10:
                            item = tn[3][:10]
                        else:
                            item = tn[3]
                        if len(tn[2]) > 10:
                            place = tn[2][:10]
                        else:
                            place = tn[2]

                        t3 = "{item}@{place} ¥{yen:,}".format(item = item, place = place, yen = round500(tn[0]))
                        t4.append(t3)
                    t5 = "\n" + t1+ t2 + '\n<ul>\n<li>' + '\n <li>'.join(t4) + "\n</ul>" 
                    tm += t5


        qtext.append('\n\n' + t0 + tm)
    return qtext
                

                
#     """
#     特に大きかった支出は (前3ヶ月比150%など)
#     1月の社会保障 円 (礼服 5万円)
#     3月の社会保障 円　（年金 3万円 カテゴリのうち75%以上のリスト)
#     3月の娯楽・交際 円


    
# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[61]:

#qincome = yearly_incomes(objYear) #homeのclearとtakaのclearが同額でおかしい


# qamount = yearly_monthlyamount0(objYear)
# qrent = yearly_rentinout(objYear)
# qincome = yearly_incomes(objYear)


def build_categoryamounttext(qincome, qamount, qrent):
    txts = []
    for cnt in range(0,4):
        income = qincome[cnt]
        outcome = qamount[1][cnt][0]
        outcomen = qamount[1][cnt][1]
        rent = qrent[cnt]['rent']['sae'] + qrent[cnt]['rent']['taka']
        clear = qrent[cnt]['clear']['sae'] + qrent[cnt]['clear']['taka']

        income0 = qincome[cnt-1]
        outcome0 = qamount[1][cnt-1][0]
        outcomen0 = qamount[1][cnt-1][1]
        rent0 = qrent[cnt-1]['rent']['sae'] + qrent[cnt-1]['rent']['taka']
        clear0 = qrent[cnt-1]['clear']['sae'] + qrent[cnt-1]['clear']['taka']

        incomedelta = income - income0
        outcomedelta = outcome - outcome0
        rentdelta = rent - rent0
        cleardelta = clear - clear0

        total = income - outcome - clear
        t1 = """
            <p>今期の入金は\t¥{income:,}<br>
            支出は   \t¥{outcome:,} ({outcomen}件)<br>
            立替は   \t¥{rent:,}<br>
            立替清算は\t¥{clear:,}<br>
            総計(入金-支出-清算)は\t¥{total:,}円でした。</p>""".format(income = income, 
                                 outcome = outcome, outcomen = outcomen,
                                 rent = rent, clear = clear, total = total)

        t2 = """
         <p>ちなみに先期は① ¥{income0:,}, ②¥{outcome0:,} ({outcomen0}件), ③¥{rent0:,}円, ④¥{clear0:,}円、</p>
         <p>比較すると①¥{incomedelta:,}円, ②¥{outcomedelta:,}円, ③¥{rentdelta:,}円, ④¥{cleardelta:,}円でした。</p>
         """.format(income0 = income0, outcome0 = outcome0, outcomen0 = outcomen0,
                   rent0 = rent0, clear0 = clear0,
                   incomedelta = incomedelta, outcomedelta = outcomedelta, rentdelta = rentdelta, cleardelta = cleardelta)

        txts.append(t1 + "\n\n" + t2)

    #     ちなみに先期は①円, ② 円(件), ③ 円, ④ 円、
    #     比較すると①円, ② 円, ③ 円, ④ 円でした。
    #     """

    return txts
# In[ ]:




# In[62]:

#     """家計簿の入力状況は
#     1月に が残っています
#     2月は全部済んでいます。
#     3月は全部済んでいます。
#     """
#     """
#     月別に見ると1月は111円(30件), 2月は234円(23件), 3月は23434円(34件)でした
#     """
#     """
#     支出について
#     カテゴリ別に見ると
#     食費は円で 円の+, 
#     光熱費は円の-, 
#     通信費は34円の+, 
#     社会保障費は 円の+, 
#     変動費は
#     教育・養育費は
#     大型出費はでした。
#     """

#     """
#     今期の入金は
#     支出は (件)
#     立て替えは
#     立て替え清算は
#     総計は + 円でした

#     ちなみに先期は①円, ② 円(件), ③ 円, ④ 円、
#     比較すると①円, ② 円, ③ 円, ④ 円でした。
#     """



"""
    高額出費 (10,000円以上)は
    - 3/4 あいうえお＠らぞーな　333えん"""




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[63]:

def get_monthly_htmlheader(objYearMonth):
    headertext1 = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <meta name="robots" content="noarchive">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <title>Garnet Reports (ZAIM)</title>

  <!-- Bootstrap -->
  <link href="css/bootstrap.min.css" rel="stylesheet">

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="./dist/Chart.min.js"></script>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="js/bootstrap.min.js"></script>

  <!-- jQ-Cookie -->
  <script src="js/jquery.cookie.js"></script>
  
  <script type="text/javascript">
  $(function() {
    function clearTabFunc(){
      console.log("clear tab");
      $('a[data-toggle="tab"]').parent().removeClass('active');
    }

    function readTabFunc(){
      activeTab = $.cookie("MactiveTabName");
      if (activeTab == null) {
        activeTab = "Mreport";
        console.log("no tab in cookie");
        $.cookie("MactiveTabName",activeTab, { expires: 700 });
        console.log("set cookie as MactiveTabName");
      }
      setTabActive();
    }

    function setTabActive(){
      console.log("set tab active:"+activeTab)
      activeTab0 = activeTab.substr(1) ;
      
      $('a[href=#' + activeTab0 +']').parent().addClass('active');
      $('#' + activeTab0).addClass('active');
    }

    $(function(){
      console.log("start")
      clearTabFunc();
      readTabFunc();
    
      $("#reporttab").click(function(){
        console.log("report tab activated");
        activeTab = "Mreport";
        $.cookie("MactiveTabName",activeTab, { expires: 700 });
      });

      $("#graphtab").click(function(){
        console.log("graph tab activated");
        activeTab = "Mgraph";
        $.cookie("MactiveTabName",activeTab, { expires: 700 });
      });

      $("#detailtab").click(function(){
        console.log("detail tab activated");
        activeTab = "Mmoneylist";
        $.cookie("MactiveTabName",activeTab, { expires: 700 });
      });

      $("#summarytab").click(function(){
        console.log("detail tab activated");
        activeTab = "Msummary";
        $.cookie("MactiveTabName",activeTab, { expires: 700 });
      });


    });
  });

  </script>
  <!-- jQ-Cookie -->


  <style>
  canvas{
      -moz-user-select: none;
      -webkit-user-select: none;
      -ms-user-select: none;
      border:solid 1px #ddf;
  }
  </style>

</head>
<body>
  <div id="header" class="container" style="margin:30px"></div>
  <nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="navbar-header">
      <button class="navbar-toggle" data-toggle="collapse" data-target=".target">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a href="./index.html" class="navbar-brand">Garnet</a>
    </div>

    <div class="collapse navbar-collapse target">
      <ul class="nav navbar-nav">
        """
    headertext2="""
        <li class="active"><a href="./m{mm1}-{mm2:02}.html">Monthly Report</a></li>
        <li><a href="./y{yy}.html">Yearly Report</a></li>
        <li><a href="./summary.html">Total Report</a></li>
      </ul>
    </div>
  </nav>

  <div class="container" style="padding:20px 0">
""".format(mm1 = dt.now().year, mm2 = dt.now().month, yy = objYearMonth[0])    
    
    
    return headertext1 + headertext2



def get_htmlfooter():
    rev = "2.1 (2016-12-25)"
    utime = get_dbupdatetime_from_sqlite()[-1]['utime'].strftime("%Y/%m/%d %H:%M")
    #a = get_dbupdatetime_from_sqlite()
    #a[-1]['utime']
    #utime = "0"
    
    htmlfooter = """
      </div> <!-- tab-content -->

    </div>
    <div id="footer" class="container text-muted" style="text-align:right; margin-bottom:2em;">
      <div class="col-sm-1 hidden-xs"></div>
      <div class="col-sm-10 col-xs-12">
          <small>PyJade rev.{}. {} @Udzuki, db updated at {}</small>
      </div>
      <div class="col-sm-1 hidden-xs"></div>
    </div>

  </body>
</html>
""".format(rev, dt.today().strftime("%Y/%m/%d %H:%M"), utime)
    return htmlfooter


# In[64]:

def build_index():
    htmlheader = """
        <!DOCTYPE html>
        <html lang="ja">
        <head>
          <meta charset="utf-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <meta name="robots" content="noindex,nofollow">
          <meta name="robots" content="noarchive">
          <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
          <title>Garnet Reports (ZAIM)</title>

          <!-- Bootstrap -->
          <link href="css/bootstrap.min.css" rel="stylesheet">

          <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
          <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
          <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
          <![endif]-->
          <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
          <script src="./dist/Chart.min.js"></script>
          <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

          <!-- Include all compiled plugins (below), or include individual files as needed -->
          <script src="js/bootstrap.min.js"></script>


        </head>"""

    htmlfooter = get_htmlfooter()
    ty, tm, td = get_today()


    htmlbody1 = """
        <body>
          <div id="header" class="container" style="margin:30px"></div>
          <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-header">
              <button class="navbar-toggle" data-toggle="collapse" data-target=".target">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a href="" class="navbar-brand">Garnet</a>
            </div>

            <div class="collapse navbar-collapse target">
              <ul class="nav navbar-nav">
                <li><a href="./m{year}-{month:02}.html">Monthly Report</a></li>
                <li><a href="./y{year}.html">Yearly Report</a></li>
                <li><a href="./summary.html">Total Report</a></li>
              </ul>
            </div>
          </nav>""".format(year = dt.now().year, month = dt.now().month)

    htmlbody2 = """
          <div class="container" style="padding:20px 0">
            <p>Zaimのデータをもとにナンチャラカンチャラ。</o>

            <!--
                <div class="list-group">
                  <div class="list-group-item" data-toggle="collapse" data-target="#demo">
                    <h4 class="list-group-item-heading hover">月度のグラフ</h4>
                  </div>
                  <ul  id="demo" class="collapse">
                    <li class="list-group-item">月ごとにまとめたもの</li>
                    <li class="list-group-item">月ごとにまとめたもの</li>
                  </ul>

            -->
            <div class="list-group">
              <a href="./m{year}-{month:02}.html" class="list-group-item">
                <h4 class="list-group-item-heading">月ごとのページ (Monthly Report)</h4>
                <p class="list-group-item-text" style="margin-left:1em">ここ3ヶ月の「家計簿/立て替えの状況」と、 今月の「高額購入リスト」「Zaimの登録が怪しいものリスト」
                  「出費推移グラフ」「出費詳細 (変動費, 養育費, 大型出費, 外食, 公共料金)」をまとめています</p>
                <ul style="padding-top:1em">
                  <li>表(1) 3ヶ月の出費状況, (2) ３ヶ月の立て替え状況, (3) 高額購入リスト, (4) 登録チェックリスト</li>
                  <li> グラフ(1) 1ヶ月の出費推移グラフ</li>
                </ul>
              </a>
              <ul style="list-style:none;">""".format(year=ty, month=tm)

    ### 

    rm = range(1,13)
    ry = range(2011,ty+1)
    rm0 = range(1,tm+1)

    yeartext = []

    for yy in reversed(ry):
        t = []
        body4A0 = """\n\n\t\t\t<li><a data-toggle="collapse" href="#acc{year2}" class="list-group-item" style="padding:5px 15px;">{year}年</a></li>
        \t\t\t<ul id="acc{year2}" class="collapse" style="list-style:none;">\n""".format(year=yy, year2 = str(yy)[-2:])


        body4A2 = """\t\t\t</ul>"""

        if yy == ty:
            for mm in rm0:
                t0 = """\t\t\t\t<li><a href="./m{year}-{month:02}.html" class="list-group-item" style="padding:5px 15px;">{year}年{month}月</a></li>\n""".format(year=yy, month=mm)
                t.append(t0)
        else:
            for mm in rm:
                t0 = """\t\t\t\t<li><a href="./m{year}-{month:02}.html" class="list-group-item" style="padding:5px 15px;">{year}年{month}月</a></li>\n""".format(year=yy, month=mm)
                t.append(t0)


        body4A1 = "".join(t)
        yeartext.append(body4A0 + body4A1 + body4A2)

    htmlbody31 = "".join(yeartext)


    htmlbody32 = """
            </ul>"""
    
    htmlbody3 = htmlbody31 + htmlbody32

    #####
    htmlbody4 = """
              <a href="./y{year}.html" class="list-group-item">
                <h4 class="list-group-item-heading">1年ごとのページ(Yearly Report)</h4>
                <p class="list-group-item-text" style="margin-left:1em">
                  1年間の出費のまとめとグラフ、1年間の公共料金のグラフをまとめています。また、グラフは出費割合の推移も表示しています</p>
                <ul style="padding-top:1em">
                  <li> 表(1) 1年間の出費まとめ</li>
                  <li>グラフ(1) 1年間の出費まとめ, (2) 公共料金推移, (3) 1年間の出費比率まとめ</li>
                </ul>
              </a>""".format(year=ty)


    ################ 年毎のリスト
    htmlbody50 = """
              <ul style="list-style:none;">\n"""
    htmlbody52 = """          </ul>"""


    t = []
    for yy in reversed(ry):
        t0 = """                <li><a href="./y{year}.html" class="list-group-item" style="padding:5px 15px;">{year}年</a></li>\n""".format(year=yy)
        t.append(t0)
    htmlbody51 = "".join(t)
    
    htmlbody5 = htmlbody50 + htmlbody51 + htmlbody52




    
    htmlbody6 = """
              <a href="./summary.html" class="list-group-item">
                <h4 class="list-group-item-heading">今までのまとめ (Total Report)</h4>
                <p class="list-group-item-text" style="margin-left:1em">
                  1年ごとの出費のまとめと推移のグラフをまとめています。また、グラフは出費割合の推移も表示しています</p>
                <ul style="padding-top:1em">
                  <li class="list-group-item-text">表(1) 2011年から1年ごとの出費まとめ</li>
                  <li class="list-group-item-text">グラフ(1) 2011年から1年ごとの出費まとめ, (2) 4半期ごとの出費まとめ, (3) 1を出費比率ごとにまとめたグラフ</li>
                </ul>
              </a>

              <div class="container" style="margin-top:20px">
                <div class="panel panel-primary">
                  <div class="panel-heading">
                    <h3 class="panel-title">カテゴリ/ジャンルについて</h3>
                  </div>
                  <div class="panel-body">
                    <table class="table table-striped table-hover ">
                      <thead>
                        <tr>
                          <th>項目</th>
                          <th>Zaimでのカテゴリ/ジャンル</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>食費/生活費</td>
                          <td>
                            <p>「<u>食費・日用品</u>」カテゴリに含まれるもの</p>
                            <li style="padding-left:1em;">食材・生協・外食・日用品・衛生用品を含む。<br>
                            例)  クイックルワイパー, オムツ：日用品・衛生用品, ミルク:食材</li>
                          </td>
                        </tr>
                        <tr>
                          <td>光熱費</td>
                          <td>
                            <p>「<u>公共料金</u>」カテゴリに含まれるうち、「<u>家インターネット</u>」「<u>モバイル通信費</u>」以外のもの</p>
                            <li style="padding-left:1em;">ガス・電気・水道・ テレビ</li>
                          </td>
                        </tr>

                        <tr>
                          <td>通信費</td>
                          <td>
                            <p>「<u>公共料金</u>」カテゴリに含まれるうち、「<u>家インターネット</u>」「<u>モバイル通信費</u>」のもの</p>
                            <li style="padding-left:1em;">ネット, 通信費</li>
                          </td>
                        </tr>

                        <tr>
                          <td>社会保障</td>
                          <td>
                            <p>「<u>社会保障</u>」カテゴリに含まれるもの</p>
                            <li style="padding-left:1em;">生命保険, 医療保険, 国民年金(滞納分), 奨学金</li>
                          </td>
                        </tr>

                        <tr>
                          <td>教育・書籍</td>
                          <td>
                            <p>「<u>養育費</u>」カテゴリに含まれるもの</p>
                            <li style="padding-left:1em;">洋服、医療費、学費、お小遣い他</li>
                          </td>
                        </tr>

                        <tr>
                          <td>変動費</td>
                          <td>
                            <p>「<u>積)住まい・家財</u>」「<u>積)交際費</u>」「<u>積)娯楽</u>」
                            「<u>積)教育・教養</u>」「<u>積)医療・健康</u>」カテゴリのもの</p>
                            <li style="padding-left:1em;">交際費, 娯楽, 書籍など, 家財, 医療, 健康</li>
                          </td>
                        </tr>

                        <tr>
                          <td>大型出費</td>
                          <td>
                            <p>「<u>大型出費</u>」カテゴリのもの (旅行, 出産, 妊活, 結婚など)</p>
                            <li style="padding-left:1em;">出産, 旅行 など</li>
                          </td>
                        </tr>

                        <tr>
                          <td>立て替え</td>
                          <td>
                            <p>出金元が「<u>たか</u>」「<u>さえ</u>」のもの (2016年以降)</p>
                            <li style="padding-left:1em;">入金は「収入」の「給与所得」「臨時収入」で「家」に入れる。<br>
                              立替の清算をするときは、「振替」を選択し、出金元「家計」から入金先「たか/さえ」に金額を移す。</li>
                            <li style="padding-left:1em;">例) x月25日に25万円給与から振り込み⇨「収入>給与所得」を選択し25日/25万円を入力, <br>x月28日に保険金20万円振り込み⇨「収入>臨時収入」を選択し28日/20万円を入力,
                            <br>x月1日にたかの立替清算10万円をする場合 ⇨ 「振替」から、出金元「家計」・入金先「たか」を選択し1日/10万円を入力する</li>
                            </p>
                          </td>
                        </tr>

                        <tr>
                          <td>高額リスト</td>
                          <td>
                            <p>レシート合計金額が3,000円以上のもの</p>
                            <!-- li style="padding-left:1em;"></li -->
                          </td>
                        </tr>

                        <tr>
                          <td>出金元不詳リスト</td>
                          <td>
                            <p>上記カテゴリ以外に記録されているもの。出金元が「<u>たか</u>」「<u>さえ</u>」「<u>家計</u>」以外かどうか</p>
                            <!-- li style="padding-left:1em;"></li -->
                          </td>
                        </tr>

                      </tbody>
                    </table>
                  </div>
                </div>

                <!-- -->
                <div class="panel panel-primary">
                  <div class="panel-heading">
                    <h3 class="panel-title">グラフについて</h3>
                  </div>
                  <div class="panel-body">
                    <table class="table table-striped table-hover ">
                      <thead>
                        <tr>
                          <th>項目</th>
                          <th>Zaimでのカテゴリ/ジャンル</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>月ごとのページ (Monthly Report)</td>
                          <td><p><u>今年の使用率グラフ</u></p>
                          昨年の出費合計に対する今年の出費の比率。
                          出費合計は家賃・公共料金を含む。グラフに併せて「その年の頭からその月の末までの使用額」と「昨年の出費合計に対する使用率」を表示する<br>
                          グラフは大きい画面でないと表示されません (iPhoneだと見えない/PC, iPadだとみれる)
                          </td>
                        </tr>

                        <tr>
                          <td></td>
                          <td><p><u>1ヶ月の出費推移グラフ</u></p>
                            <p>
                            １ヶ月間の出費を1日ごとに積み立てていったグラフ。<br>
                            変動費/養育費/生活費/公共料金/全カテゴリのそれぞれをグラフにしています。
                            全カテゴリは全カテゴリ以外全部(変動費/養育費/生活費/公共料金)の合計。<br>
                            初期状態では、合計と公共料金は隠されています。
                          </p>
                        </tr>

                        <tr>
                          <td>1年ごとのページ (Yearly Report)</td>
                          <td>
                            <p><u>1年間の出費まとめ</u></p>
                            <p>
                                期ごとに１年間の出費をまとめたグラフ。「生活費」「公共料金」「変動費」「養育費」「大型出費」を積み立て棒グラフにした。
                            </p>
                          </td>
                        </tr>

                        <tr>
                          <td></td>
                          <td>
                            <p><u>公共料金推移</u></p>
                            <p>
                                月ごとに１年間の公共料金をまとめたグラフ。<br>「ガス料金」「電気料金」「水道料金」「NHK」「家インターネット」「モバイル通信費」「社会保障」を積み立て棒グラフにした。
                            </p>
                          </td>
                        </tr>

                        <tr>
                          <td></td>
                          <td>
                            <p><u>1年間の出費比率まとめ</u></p>
                            <p>
                                「1年間の出費まとめ」のグラフを元に、その期の出費のうち「生活費」「公共料金」「変動費」「養育費」「大型出費」それぞれの項目がどのくらいの比率になるかをまとめたグラフ。
                            </p>
                          </td>
                        </tr>

                        <tr>
                          <td>今までのまとめ (Total Report)</td>
                          <td>
                            <p><u>1年ごとの出費まとめ</u></p>
                            <p>
                              2011年から1年ごとに出費をまとめたグラフ。「生活費」「公共料金」「変動費」「養育費」「大型出費」を積み立て棒グラフにした。                    </p>
                          </td>
                        </tr>

                        <tr>
                          <td></td>
                          <td><p><u>4半期ごとの出費まとめ</u></p>
                              2011年から4半期ごとの出費をまとめたグラフ。毎年の4半期ごとの出費を比較する。
                            </p>
                          </td>
                        </tr>

                        <tr>
                          <td></td>
                          <td><p><u>1年ごとの出費比率まとめ</u><p>
                            <p>
                              「1年ごとの出費まとめ」のグラフを元に、その年の出費のうち「生活費」「公共料金」「変動費」「養育費」「大型出費」それぞれの項目がどのくらいの比率になるかをまとめたグラフ。
                            </p>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
          """

    return htmlheader + htmlbody1 + htmlbody2 + htmlbody3 + htmlbody4 + htmlbody5 + htmlbody6 + htmlfooter


# In[65]:

# ty, tm, td = get_today()

# rm = range(1,13)
# ry = range(2011,ty+1)
# rm0 = range(1,tm+1)

# t = []

# for yy in reversed(ry):
#     if yy == ty:
#         for mm in rm0:
#             t0 = """<li><a href="./m{year}-{month:02}.html" class="list-group-item" style="padding:5px 15px;">{year}年{month:02}月</a></li>""".format(month=mm, year=yy)
#             t.append(t0)
#     else:
#         for mm in rm:
#             t0 = """<li><a href="./m{year}-{month:02}.html" class="list-group-item" style="padding:5px 15px;">{year}年{month:02}月</a></li>""".format(month=mm, year=yy)
#             t.append(t0)


# In[ ]:




# In[ ]:





# In[66]:

# ty, tm, td = get_today()

# rm = range(1,13)
# ry = range(2011,ty+1)
# rm0 = range(1,tm+1)

# yeartext = []

# for yy in reversed(ry):
#     t = []
#     body4A0 = """\n\n\t\t\t<li><a data-toggle="collapse" href="#acc{year2}" class="list-group-item" style="padding:5px 15px;">{year}年</a></li>
#     \t\t\t<ul id="acc{year2}" class="collapse" style="list-style:none;">\n""".format(year=yy, year2 = str(yy)[-2:])

#     body4A2 = """\t\t\t</ul>"""

#     if yy == ty:
#         for mm in rm0:
#             t0 = """\t\t\t\t<li><a href="./m{year}-{month:02}.html" class="list-group-item" style="padding:5px 15px;">{year}年{month}月</a></li>\n""".format(year=yy, month=mm)
#             t.append(t0)
#     else:
#         for mm in rm:
#             t0 = """\t\t\t\t<li><a href="./m{year}-{month:02}.html" class="list-group-item" style="padding:5px 15px;">{year}年{month}月</a></li>\n""".format(year=yy, month=mm)
#             t.append(t0)


#     body4A1 = "".join(t)
#     yeartext.append(body4A0 + body4A1 + body4A2)

# yearlist = "".join(yeartext)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[67]:

def get_reporttabbody(objYearMonth):
    objDT0 = objYearMonth 
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)
    m0amount =get_monthlyamount(objDT0)
    m1amount =get_monthlyamount(objDT1)
    m2amount =get_monthlyamount(objDT2)

    def cmpamount(t0, t1, TH):
        t = (t0 -t1)
        if t > TH:
            #cmpt = '<span class="glyphicon glyphicon-chevron-up text-danger" aria-hidden="true"></span>'
            cmpt = '<span class="label label-danger" style="padding:3px 4px;margin-left:1em;">(+)</span>'
        elif t < -TH:
            #cmpt = '<span class="glyphicon glyphicon-chevron-down text-info" aria-hidden="true"></span>'
            cmpt = '<span class="label label-primary" style="padding:3px 5px;margin-left:1em;">(-)</span>'
        else:
            cmpt = '<span class="label label-default" style="padding:3px 5px;margin-left:1em;">(0)</span>'

        return cmpt

    TH = 1500
    mkey = ['食費', '公共料金', '社会保障', '変動費', '教育・養育', '大型出費', '住まい']
    
    cmp1 = cmpamount(m0amount[mkey[0]], m1amount[mkey[0]], TH)
    cmp2 = cmpamount(m0amount[mkey[1]], m1amount[mkey[1]], TH)
#     cmp2 = cmpamount(m0amount['光熱費'], m1amount['光熱費'], TH)
#     cmp3 = cmpamount(m0amount['通信費'],  m1amount['通信費'], TH)

    cmp4 = cmpamount(m0amount[mkey[2]],  m1amount[mkey[2]], TH)
    cmp5 = cmpamount(m0amount[mkey[3]],  m1amount[mkey[3]], TH)
    cmp6 = cmpamount(m0amount[mkey[4]],  m1amount[mkey[4]], TH)
    cmp7 = cmpamount(m0amount[mkey[5]],  m1amount[mkey[5]], TH)
    cmp8 = cmpamount(m0amount[mkey[6]],  m1amount[mkey[6]], TH)

    cmp0 = cmpamount(m0amount['all'],  m1amount['all'], TH)

    allM0 = round500(m0amount['all']),
    allM1 = round500(m1amount['all']),
    allM2 = round500(m2amount['all']),

    sumM0 = sum([m0amount[x] for x in mkey])
    #         sum([m0amount[mkey[0]], m0amount['公共料金'],
    #         m0amount['社会保障'], m0amount['変動費'], m0amount['大型出費'], m0amount['養育費']])
    sumM1 = sum([m1amount[x] for x in mkey])
    #     ([m1amount['食費'], m1amount['公共料金'],
    #         m1amount['社会保障'], m1amount['変動費'], m1amount['大型出費'], m1amount['養育費']])
    sumM2 = sum([m2amount[x] for x in mkey])
    #     ([m2amount['食費'], m2amount['公共料金'],
    #         m2amount['社会保障'], m2amount['変動費'], m2amount['大型出費'], m2amount['養育費']])

    # sum([monthlyamount[k] for k in monthlyamount]) - 107029
    summarytable = """
    <!-- output from PyJade -->
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center">{objYear}年</th>
                        <th class="text-center">{monthM2}月</th>
                        <th class="text-center">{monthM1}月</th>
                        <th class="text-center"><u>{monthM0}月</u>
                        <span class="label label-primary" style="margin-left:10px">¥{amountall:,}</span></th>
                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>{key1}</td>
                        <td>¥{val1M2:,}</td>
                        <td>¥{val1M1:,}</td>
                        <td>¥{val1M0:,}{cmp1}</td>
                    </tr>    

                    <tr>
                        <td>{key2}</td>
                        <td>¥{val2M2:,}</td>
                        <td>¥{val2M1:,}</td>
                        <td>¥{val2M0:,}{cmp2}</td>
                    </tr>    

                    <tr>
                        <td>{key4}</td>
                        <td>¥{val4M2:,}</td>
                        <td>¥{val4M1:,}</td>
                        <td>¥{val4M0:,}{cmp4}</td>
                    </tr>    

                    <tr>
                        <td>{key5}</td>
                        <td>¥{val5M2:,}</td>
                        <td>¥{val5M1:,}</td>
                        <td>¥{val5M0:,}{cmp5}</td>
                    </tr>    

                    <tr>
                        <td>{key6}</td>
                        <td>¥{val6M2:,}</td>
                        <td>¥{val6M1:,}</td>
                        <td>¥{val6M0:,}{cmp6}</td>
                    </tr>    

                    <tr>
                        <td>{key7}</td>
                        <td>¥{val7M2:,}</td>
                        <td>¥{val7M1:,}</td>
                        <td>¥{val7M0:,}{cmp7}</td>
                    </tr>    

                    <tr>
                        <td>{key8}</td>
                        <td>¥{val8M2:,}</td>
                        <td>¥{val8M1:,}</td>
                        <td>¥{val8M0:,}{cmp7}</td>
                    </tr>    

                </tbody>
                <tfoot class="bg-info">
                    <tr class="text-center">
                        <td><strong>小計</strong></td>
                        <td><strong>¥{val0M2:,}</strong></td>
                        <td><strong>¥{val0M1:,}</strong></td>
                        <td><strong>¥{val0M0:,}{cmp0}</strong></td>
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>
    """.format(
            objYear = objDT0[0],
            monthM0=objDT0[1],
            monthM1=objDT1[1],
            monthM2=objDT2[1],
            amountall = round500(sumM0),
            key1 = '食費/生活費', 
                val1M0 = round500(m0amount[mkey[0]]),
                val1M1 = round500(m1amount[mkey[0]]),
                val1M2 = round500(m2amount[mkey[0]]),
            key2 = '公共料金', 
                val2M0 = round500(m0amount[mkey[1]]),
                val2M1 = round500(m1amount[mkey[1]]),
                val2M2 = round500(m2amount[mkey[1]]),
            key4 = '社会保障', 
                val4M0 = round500(m0amount[mkey[2]]),
                val4M1 = round500(m1amount[mkey[2]]),
                val4M2 = round500(m2amount[mkey[2]]),
            key5 = '変動費', 
                val5M0 = round500(m0amount[mkey[3]]),
                val5M1 = round500(m1amount[mkey[3]]),
                val5M2 = round500(m2amount[mkey[3]]),
            key6 = '教育・養育', 
                val6M0 = round500(m0amount[mkey[4]]),
                val6M1 = round500(m1amount[mkey[4]]),
                val6M2 = round500(m2amount[mkey[4]]),
            key7 = '大型出費', 
                val7M0 = round500(m0amount[mkey[5]]),
                val7M1 = round500(m1amount[mkey[5]]),
                val7M2 = round500(m2amount[mkey[5]]),
            key8 = '住まい', 
                val8M0 = round500(m0amount[mkey[6]]),
                val8M1 = round500(m1amount[mkey[6]]),
                val8M2 = round500(m2amount[mkey[6]]),


            val0M0 = round500(m0amount['all']),
            val0M1 = round500(m1amount['all']),
            val0M2 = round500(m2amount['all']),
        cmp0 = cmp0, cmp1 = cmp1, cmp2 = cmp2, cmp4 = cmp4,
        cmp5 = cmp5, cmp6 = cmp6, cmp7 = cmp7
        )
    #mkey = ['食費', '公共料金', '社会保障', '変動費', '養育費', '大型出費', '住まい']
    
    
    # 立て替えリスト
    renttable = get_renttable(objYearMonth)
    
#     # 支払い以外リスト (口座)
    tabletitle = "入金・振り替えリスト"
    moneydata = select_nonPaymentData(objYearMonth)
    tatekae = print_nonPaymenttable(objYearMonth, moneydata, tabletitle, "tablerep0")
    banktable = print_banktable(objYearMonth, moneydata, "銀行口座出納", "monthlybanktable")
    # issue281 Reportの順を 詳細、たてかえ、TODO, チェックリスト、高額リストにし、口座出納と入金振替を詳細に移動する


    # Genre table
    genretable = get_genrestable(objYearMonth)
    
    # not     where from_account_id not in (1,4,7)  and 
    tabletitle = "高額リスト"
    TH = 3000
    moneydata = select_ExpenceData(objYearMonth, TH)
    expencetable = print_moneytable(objYearMonth, moneydata, tabletitle, "tablerep1")

    # これらは含まない
    #  105: ['公共料金', 105],
    #  含む25504225: ['社会保障', 25504225],
    #  28269167: ['住まい', 28269167]}


    
    
    # 怪しいリスト
    tabletitle = "Zaim登録チェックリスト"
    if objYearMonth[0] >= 2016:
        # 2016年から登録方法変更のため
        moneydata0 = select_OutAccount(objYearMonth)
    else:
        moneydata0 = select_OutAccount2015(objYearMonth)
    moneydata1 = select_OutCategory(objYearMonth)
    moneydata2 = select_OutGenre(objYearMonth)
    moneydata_Ayashii = marge_AyashiiData(moneydata0, moneydata1, moneydata2)
    checktable = print_moneytable(objYearMonth, moneydata_Ayashii, tabletitle, "tablerep2")

    #     return (textheader, texts, textfooter)
    
    # 月次チェックリスト
    todotable = print_monthly_checklist(objYearMonth)
    
#     tabletabbody = "\n<!-- #### report tab ここから #### -->\n" + summarytable + renttable + expencetable[3] + checktable[3] + banktable[3] + genretable[3] + "\n<!-- #### report tab ここまで #### -->\n"
   
#     tabletabbody = "\n<!-- #### report tab ここから #### -->\n" \
#     + genretable[3] + renttable + expencetable[3] + checktable[3] + tatekae[3] + banktable[3] + todotable \
#     + "\n<!-- #### report tab ここまで #### -->\n"

    tabletabbody = "\n<!-- #### report tab ここから #### -->\n"         + genretable[3] + renttable + todotable + checktable[3] + expencetable[3]         + "\n<!-- #### report tab ここまで #### -->\n"
    # +  tatekae[3] + banktable[3]
    # issue281 Reportの順を 詳細、たてかえ、TODO, チェックリスト、高額リストにし、口座出納と入金振替を詳細に移動する

    
    return tabletabbody
    


# In[ ]:




# In[68]:

def marge_AyashiiData(outaccountdata, outcategorydata, outgenredata):
    m = []
    for m0 in outaccountdata:
        mt = {}
        for keys in m0.keys():
            mt[keys] = m0[keys]
        mt['from_account'] = "<u>{}</u>".format(m0['from_account'])
        m.append(mt)
    for m0 in outcategorydata:
        mt = {}
        for keys in m0.keys():
            mt[keys] = m0[keys]
        mt['category'] = "<u>{}</u>".format(m0['category'])
        m.append(mt)

    for m0 in outgenredata:
        mt = {}
        for keys in m0.keys():
            mt[keys] = m0[keys]
        mt['genre'] = "<u>{}</u>".format(m0['genre'])
        m.append(mt)


        
    return m



# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[69]:

def print_monthly_checklist(objYearMonth):

    # 12608296: ['月度チェック', 12608296]}
    gdata = select_RawGenreData(objYearMonth,[13068828])

    t = {}
    #checklist = ['智花ゆうちょ', '給与・小遣い整理', '公共料金', 'クレジットカード', 'レシート', 'UFJ銀行', 'ソニー銀行']
    checklist0 = [
        {"type":"家賃", "name":"家賃"},        
        {"type":"生協", "name":"生協"},          
        {"type":"保育費", "name":"養育費"},
        {"type":"奨学金", "name":"奨学金"},
        {"type":"保険", "name":"保険"},
        {"type":"公共料金",     "name":"公共料金"},
        {"type":"レシート",     "name":"レシート"},
        {"type":"クレジットカード",     "name":"カード"},
        {"type":"給与・小遣い整理", "name":"給与・小遣い"},
        {"type":"智花ゆうちょ",     "name":"智花ゆうちょ"},
        {"type":"ソニー銀行",     "name":"ソニー銀行"},
        {"type":"UFJ銀行",     "name":"UFJ"}
    ]
    
    checklist = [x['type'] for x in checklist0]


    
#     for chck in checklist:
#         t[chck] = """<input type="checkbox" name="">{}""".format(chck)
    t = ""

    for x in gdata:
        name = x['name']
        flg = abs(x['amount'])
        t0 = ""

        for chck in checklist:
            if name == chck and flg == 1:
                t0 = """<label class="checkbox-inline"><input type="checkbox" name="" checked = "checked">{}</label>\n\t\t\t""".format(chck)
                checklist.remove(chck)
                break
            elif name == chck and flg == 0:
                t0 = """<label class="checkbox-inline"><input type="checkbox" name="">{}</label>""".format(chck)
                checklist.remove(chck)
                break
        t += t0

    for chck in checklist:
        t0 = """<label class="checkbox-inline"><input type="checkbox" name="">{}</label>""".format(chck)
        t += t0


    checklisttext = """<div class="panel panel-primary">
        <form class="form-horizontal">
            <div class="form-group">
                <label class="control-label col-xs-2">チェックリスト</label>
                <div class="col-xs-10">
                    {}

                </div>
            </div>
        </form>
    </div>""".format(t)

#     checklist = ['智花ゆうちょ', '給与・小遣い整理', 'クレジットカード', 'レシート', 'UFJ銀行', 'ソニー銀行']


    return checklisttext




# In[ ]:




# In[ ]:




# In[70]:

def get_renttable(objYearMonth):
    objDT0 = objYearMonth 
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)


    (m0rin, m0rout) = get_monthlyRent(objDT0)
    (m1rin, m1rout) = get_monthlyRent(objDT1)
    (m2rin, m2rout) = get_monthlyRent(objDT2)
    rin = {}
    rout = {}
    
    for key in m0rin.keys():
        rin[key] = [m0rin[key],m1rin[key],m2rin[key]]
        rout[key] = [m0rout[key],m1rout[key],m2rout[key]]
    
    renttable = """
    <!-- output from PyJade -->
 

    <div class="panel panel-primary">
        <div class="panel-heading">立て替えまとめ</div>
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <!-- thead class="bg-primary" -->
                <thead>
                    <tr>
                        <th class="text-center"></th>
                        <th class="text-center"></th>
                        <th class="text-center">{monthM2}月</th>
                        <th class="text-center">{monthM1}月</th>
                        <th class="text-center">{monthM0}月</th>
                        <!-- th class="text-center"><strong>小計</strong></th -->

                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>たか</td>
                        <td>(立て替え)</td>
                        <td>¥{val1M2:,}</td>
                        <td>¥{val1M1:,}</td>
                        <td>¥{val1M0:,}</td>
                        <!-- td>¥{val1M:,}</td -->
                    </tr>    
                    <tr>
                        <td></td>
                        <td>(清算)</td>
                        <td>¥{valc1M2:,}</td>
                        <td>¥{valc1M1:,}</td>
                        <td>¥{valc1M0:,}</td>
                        <!-- td>¥{valc1M:,}</td -->
                    </tr>    

                    <tr class="text-center info">
                        <td></td>
                        <td><strong>小計</strong></td>
                        <td><strong>¥{valTM2:,}</strong></td>
                        <td><strong>¥{valTM1:,}</strong></td>
                        <td><strong>¥{valTM0:,}</strong></td>
                        <!-- td><strong>¥{valTM:,}</strong></td -->
                    </tr>

                    <tr>
                        <td>さえ</td>
                        <td>(立て替え)</td>
                        <td>¥{val2M2:,}</td>
                        <td>¥{val2M1:,}</td>
                        <td>¥{val2M0:,}</td>
                        <!-- td>¥{val2M:,}</td -->
                    </tr>    
                    <tr>
                        <td></td>
                        <td>(清算)</td>
                        <td>¥{valc2M2:,}</td>
                        <td>¥{valc2M1:,}</td>
                        <td>¥{valc2M0:,}</td>
                        <!-- td>¥{valc2M:,}</td -->
                    </tr>    
                    <tr class="text-center info">
                        <td></td>
                        <td><strong>小計</strong></td>
                        <td><strong>¥{valSM2:,}</strong></td>
                        <td><strong>¥{valSM1:,}</strong></td>
                        <td><strong>¥{valSM0:,}</strong></td>
                        <!-- td><strong>¥{valSM:,}</strong></td -->
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """.format(
            monthM0=objDT0[1],
            monthM1=objDT1[1],
            monthM2=objDT2[1],
                val1M0 = round500(rout['taka'][0]),
                val1M1 = round500(rout['taka'][1]),
                val1M2 = round500(rout['taka'][2]),
                val1M = round500(sum(rout['taka'])),

                val2M0 = round500(rout['sae'][0]),
                val2M1 = round500(rout['sae'][1]),
                val2M2 = round500(rout['sae'][2]),
                val2M = round500(sum(rout['sae'])),
                
                # 立替清算
                valc1M0 = round500(rin['taka'][0]),
                valc1M1 = round500(rin['taka'][1]),
                valc1M2 = round500(rin['taka'][2]),
                valc1M = round500(sum(rin['taka'])),

                valc2M0 = round500(rin['sae'][0]),
                valc2M1 = round500(rin['sae'][1]),
                valc2M2 = round500(rin['sae'][2]),
                valc2M = round500(sum(rin['sae'])),

            # それぞれの小計
            valTM0 = round500(rout['taka'][0] - rin['taka'][0]),
            valTM1 = round500(rout['taka'][1] - rin['taka'][1]),
            valTM2 = round500(rout['taka'][2] - rin['taka'][2]),
            valTM = round500(sum(rout['taka'])-sum(rin['taka'])),
                                 
            valSM0 = round500(rout['sae'][0] - rin['sae'][0]),
            valSM1 = round500(rout['sae'][1] - rin['sae'][1]),
            valSM2 = round500(rout['sae'][2] - rin['sae'][2]),
            valSM = round500(sum(rout['sae'])-sum(rin['sae']))
        )




    return renttable


# In[71]:

def get_quarterlyrenttable(objYear):
    tin = []
    tout = []
    rin = {}
    rout = {}

    for objMonth in range(1,13):
        (rentin,rentout) = get_monthlyRent((objYear, objMonth))
        tin.append(rentin)
        tout.append(rentout)

    routq ={}
    routqtd = {}

    rinq ={}
    rinqtd = {}
    rrqtd = {}
    t = []
    
    Q1 = slice(0,3)
    Q2 = slice(3,6)
    Q3 = slice(6,9)
    Q4 = slice(9,12)


    for key in tin[0].keys():
        rin[key] = [x[key] for x in tin]
        rout[key] = [x[key] for x in tout]
        t = []

        t.append("<td>¥{:,}</td>".format(round500(sum(rin[key][Q1]))))
        t.append("<td>¥{:,}</td>".format(round500(sum(rin[key][Q2]))))
        t.append("<td>¥{:,}</td>".format(round500(sum(rin[key][Q3]))))
        t.append("<td>¥{:,}</td>".format(round500(sum(rin[key][Q4]))))
        t.append("<td><strong>¥{:,}</strong></td>".format(round500(sum(rin[key]))))
        rinq[key] = t
        rinqtd[key] = '\n\t\t\t'.join(t)


        t[0] = "<td>¥{:,}</td>".format(round500(sum(rout[key][Q1])))
        t[1] = "<td>¥{:,}</td>".format(round500(sum(rout[key][Q2])))
        t[2] = "<td>¥{:,}</td>".format(round500(sum(rout[key][Q3])))
        t[3] = "<td>¥{:,}</td>".format(round500(sum(rout[key][Q4])))
        t[4] = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key])))
        routq[key] = t
        routqtd[key] = '\n\t\t\t'.join(t)

        t[0] = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key][Q1]) - sum(rin[key][Q1])))
        t[1] = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key][Q2]) - sum(rin[key][Q2])))
        t[2] = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key][Q3]) - sum(rin[key][Q3])))
        t[3] = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key][Q4]) - sum(rin[key][Q4])))
        t[4] = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key]) - sum(rin[key])))
        rrqtd[key] = '\n\t\t\t'.join(t)



        
    renttable = """
    <!-- output from PyJade -->
    
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center">立て替えまとめ</th>
                        <th class="text-center"></th>
                        <th class="text-center">Q1</th>
                        <th class="text-center">Q2</th>
                        <th class="text-center">Q3</th>
                        <th class="text-center">Q4</th>
                        <th class="text-center"><strong>小計</strong></th>

                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>たか</td>
                        <td>(立て替え)</td>
                        {rout_taka}
                    </tr>    
                    <tr>
                        <td></td>
                        <td>(清算)</td>
                        {rin_taka}
                    </tr>    

                    <tr class="text-center info">
                        <td></td>
                        <td><strong>(小計)</strong></td>
                        {rr_taka}
                    </tr>

                    <tr>
                        <td>さえ</td>
                        <td>(立て替え)</td>
                        {rout_sae}
                    </tr>    
                    <tr>
                        <td></td>
                        <td>(清算)</td>
                        {rin_sae}
                    </tr>    
                    <tr class="text-center info">
                        <td></td>
                        <td><strong>(小計)</strong></td>
                        {rr_sae}
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """.format(
        rin_taka = rinqtd['taka'],
        rout_taka = routqtd['taka'],
        rr_taka = rrqtd['taka'],
        rin_sae = rinqtd['sae'],
        rout_sae =routqtd['sae'],
        rr_sae = rrqtd['sae']
        )

    genretable = get_genrestableYear(objYear) #rev2.3

    return renttable     + "<hr>" + genretable[3] #rev2.3



# In[72]:

def get_yearmonthly_renttable(objYear):
    tin = []
    tout = []
    rin = {}
    rout = {}

    for objMonth in range(1,13):
        (rentin,rentout) = get_monthlyRent((objYear, objMonth))
        tin.append(rentin)
        tout.append(rentout)

    routtd ={}
    routtdt = {}

    rintd ={}
    rintdt = {}

    rdeltatd = {}
    rdeltatdt = {}

    t = []
    
    for key in tin[0].keys(): # 月:keyからkey:月の順に変更
        rin[key] = [x[key] for x in tin]
        rout[key] = [x[key] for x in tout]

    for key in rin:
        ti = []
        to = []
        td = []

        for indx in range(0,12):
            ti.append("<td>¥{:,}</td>".format(round500(rin[key][indx])))
            to.append("<td>¥{:,}</td>".format(round500(rout[key][indx])))
            td.append("<td><strong>¥{:,}</strong></td>".format(round500(rout[key][indx] - rin[key][indx])))
        
        ti.append("<td><strong>¥{:,}</strong></td>".format(round500(sum(rin[key]))))
        to.append("<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key]))))
        td.append("<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key]) - sum(rin[key]))))

        rintd[key]    = ti
        routtd[key]   = to
        rdeltatd[key] = td
        
        rintdt[key]    = '\n\t\t\t'.join(ti)
        routtdt[key]   = '\n\t\t\t'.join(to)
        rdeltatdt[key] = '\n\t\t\t'.join(td)

    renttable = ""
    renttable = """
    <!-- output from PyJade -->
    
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center" colspan="2" style="min-width: 80px;">立て替えまとめ</th>
                        <th class="text-center">1月</th>
                        <th class="text-center">2月</th>
                        <th class="text-center">3月</th>
                        <th class="text-center">4月</th>
                        <th class="text-center">5月</th>
                        <th class="text-center">6月</th>
                        <th class="text-center">7月</th>
                        <th class="text-center">8月</th>
                        <th class="text-center">9月</th>
                        <th class="text-center">10月</th>
                        <th class="text-center">11月</th>
                        <th class="text-center">12月</th>
                        <th class="text-center"><strong>小計</strong></th>

                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>たか</td>
                        <td>立替</td>
                        {rout_taka}
                    </tr>    
                    <tr>
                        <td></td>
                        <td>清算</td>
                        {rin_taka}
                    </tr>    

                    <tr class="text-center info">
                        <td></td>
                        <td><strong>小計</strong></td>
                        {rr_taka}
                    </tr>

                    <tr>
                        <td>さえ</td>
                        <td>立替</td>
                        {rout_sae}
                    </tr>    
                    <tr>
                        <td></td>
                        <td>清算</td>
                        {rin_sae}
                    </tr>    
                    <tr class="text-center info">
                        <td></td>
                        <td><strong>小計</strong></td>
                        {rr_sae}
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """.format(
        rin_taka = rintdt['taka'],
        rout_taka = routtdt['taka'],
        rr_taka = rdeltatdt['taka'],
        rin_sae = rintdt['sae'],
        rout_sae =routtdt['sae'],
        rr_sae = rdeltatdt['sae']
        )


    return renttable


# In[73]:

def get_yearlyrenttable():
    (yearfrom,yearto)= get_objYearRange()

    routq ={}
    routqtd = {}


    rry = []
    riny = []
    routy = []
    ytd = []


    for objYear in range(yearfrom, yearto):
        tin = []
        tout = []
        rr = {}
        rin = {}
        rout = {}
        ytd.append('<th class="text-center">{}年</th>'.format(objYear))



        for objMonth in range(1,13):
            (rentin,rentout) = get_monthlyRent((objYear, objMonth))
            tin.append(rentin)
            tout.append(rentout)

        for key in tin[0].keys():
            rin[key] = sum([x[key] for x in tin])
            rout[key] = sum([x[key] for x in tout])
            rr[key] = rout[key] - rin[key]

    #             t = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rin[key])))
    #             rinq[key] = sum(rin[key])
    #             rinqtd[key] = t

    #             t = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key])))
    #             routq[key] = sum(rout[key])
    #             routqtd[key] = t

    #             t = "<td><strong>¥{:,}</strong></td>".format(round500(sum(rout[key]) - sum(rin[key])))
    #             rrqtd[key] = t

        routy.append(rout)
        riny.append(rin)
        rry.append(rr)


    
    routytd = {}
    rinytd = {}
    rrytd = {}

    for key in tin[0].keys():
        routytd[key] = "\n\t\t".join(["<td>¥{:,}</td>".format(round500(x[key])) for x in routy] + ["<td><strong>¥{:,}</strong></td>".format(round500(sum([x[key] for x in routy])))]) 
        rinytd[key] = "\n\t\t".join(["<td>¥{:,}</td>".format(round500(x[key])) for x in riny] + ["<td><strong>¥{:,}</strong></td>".format(round500(sum([x[key] for x in riny])))]) 
        rrytd[key] = "\n\t\t".join(["<td><strong>¥{:,}</strong></td>".format(round500(x[key])) for x in rry] + ["<td><strong>¥{:,}</strong></td>".format(round500(sum([x[key] for x in rry])))]) 

    yeartd = "\n\t\t".join(ytd)
        
    renttable1 = """
    <!-- output from PyJade -->
    
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center">立て替えまとめ</th>
                        <th class="text-center"></th>
                        {}
                        <th class="text-center"><strong>小計</strong></th>
                        """.format(yeartd)
    renttable2 = """

                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>たか</td>
                        <td>(立て替え)</td>
                        {rout_taka}
                    </tr>    
                    <tr>
                        <td></td>
                        <td>(清算)</td>
                        {rin_taka}
                    </tr>    

                    <tr class="text-center info">
                        <td></td>
                        <td><strong>(小計)</strong></td>
                        {rr_taka}
                    </tr>

                    <tr>
                        <td>さえ</td>
                        <td>(立て替え)</td>
                        {rout_sae}
                    </tr>    
                    <tr>
                        <td></td>
                        <td>(清算)</td>
                        {rin_sae}
                    </tr>    
                    <tr class="text-center info">
                        <td></td>
                        <td><strong>(小計)</strong></td>
                        {rr_sae}
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """.format(
        rin_taka = rinytd['taka'],
        rout_taka = routytd['taka'],
        rr_taka = rrytd['taka'],
        rin_sae = rinytd['sae'],
        rout_sae =routytd['sae'],
        rr_sae = rrytd['sae']
        )



    
    return renttable1 + renttable2


# In[74]:

def get_MonthlyBankAccount(objYearMonth):
    
    # 'セブンカード':7992077,  いれない
    BankAccounts = {'家の口座(UFJ)':8105914, '家の口座 (ソニー)':8105916, 
                    'ソニー銀行（積み立て）':8105937, '智花（ゆうちょ)':8133263}
    
    sumamount = {}
    for key in BankAccounts.keys():
        toAccount = [BankAccounts[key],]

        moneylist = select_toAccount(objYearMonth,toAccount)
        sumamount[key] = sum([x['amount'] for x in moneylist])
    
    return sumamount

# (rentin, rentout) = get_monthlyRent(objYearMonth)


# In[75]:

def get_YearlyBankAccount(objYear):
    # 1年分の月ごと
    # 1年分の4半期ごとの和
    # 1年分の和
    
    monthlyamounts = []
    for m in range(1,13):
        monthlyamount = get_MonthlyBankAccount((objYear,m))
        monthlyamounts.append(monthlyamount)
        
    yearlyamount_atmonth = {}
    yearlyamount_atquarter = {}
    yearlyamount = {}
    
    for key in monthlyamounts[0].keys():
        t = [x[key] for x in monthlyamounts]
        yearlyamount_atmonth[key] = t
        yearlyamount[key] = sum(t)
        yearlyamount_atquarter[key] = [sum(t[0:3]), sum(t[3:6]), sum(t[6:9]), sum(t[9:12])]
        
    return yearlyamount_atmonth, yearlyamount_atquarter, yearlyamount


# In[76]:

def get_Quarterly_bankaccounttable(objYear):    
    [bankaccountM, bankaccountQ, bankaccountY] = get_YearlyBankAccount(objYear)
    
    qtds = ""
    keys = bankaccountQ.keys()
    for key in keys:
        accountQ = bankaccountQ[key]

        qtd = """
        <tr>
            <td>{bankname}</td>
            <td>¥{valQ1:,}</td>
            <td>¥{valQ2:,}</td>
            <td>¥{valQ3:,}</td>
            <td>¥{valQ4:,}</td>
            <td>¥{valSum:,}</td>
        </tr>
        
        """.format(bankname = key,
            valQ1 = round500(accountQ[0]),
            valQ2 = round500(accountQ[1]),
            valQ3 = round500(accountQ[2]),
            valQ4 = round500(accountQ[3]),
            valSum = round500(sum([accountQ[0], accountQ[1], accountQ[2], accountQ[3]])) 
                  )
        qtds = qtds + qtd
    
    sq1 = sum([bankaccountQ[key][0] for key in keys])
    sq2 = sum([bankaccountQ[key][1] for key in keys])
    sq3 = sum([bankaccountQ[key][2] for key in keys])
    sq4 = sum([bankaccountQ[key][3] for key in keys])
    sMs = sum([sq1, sq2, sq3, sq4])

    qtdsum = """
    <tr class="text-center info">
        <td><strong>小計</strong></td>
        <td><strong>¥{valSM1:,}</strong></td>
        <td><strong>¥{valSM2:,}</strong></td>
        <td><strong>¥{valSM3:,}</strong></td>
        <td><strong>¥{valSM4:,}</strong></td>
        <td><strong>¥{valSMs:,}</strong></td>
    </tr>

    """.format(valSM1 = sq1,
               valSM2 = sq2,
               valSM3 = sq3,
               valSM4 = sq4,
               valSMs = sMs)

    renttable = """
    <!-- output from PyJade -->    
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center">口座出納</th>
                        <th class="text-center">Q1</th>
                        <th class="text-center">Q2</th>
                        <th class="text-center">Q3</th>
                        <th class="text-center">Q4</th>
                        <th class="text-center"><strong>小計</strong></th>

                    </tr>
                </thead>
                <tbody class="text-center">
                    {tds}
                                        
                    {tdsum}
                </tbody>
            </table>
        </div>
    </div>
    """.format(
                tds = qtds,
                tdsum = qtdsum)


    return renttable


# In[77]:

def print_nonPaymenttable(objYearMonth, moneydata, tabletitle,tableid):

    texts = []
    count = 0
    sum_amount = 0
    
    #     {0: [None, 0],
    #  1: ['たか', 1],
    #  4: ['さえ', 4],
    #  7: ['家計', 7],
    #  827175: ['積立）たか', 827175],
    #  827184: ['積立）さえ', 827184],
    #  7656126: ['積立）家計', 7656126],
    #  7992077: ['セブンカード', 7992077],
    #  8105914: ['家の口座(UFJ)', 8105914],
    #  8105916: ['家の口座 (ソニー)', 8105916],
    #  8105937: ['ソニー銀行（積み立て）', 8105937]}
    #  8133263: ['智花（ゆうちょ)', 8133263]}
    
    for x in moneydata:
        if not x['to_account_id'] in (1,4,7,827175,827184,7656126,7992077, 8105914,8105916,8105937,8133263):
            continue
        if x['genre_id'] == 13068828: # 月次TODOチェックリスト
            continue


        count = count + 1
        sum_amount = sum_amount + x['amount']
        xday = dt.strptime(x['date'], '%Y-%m-%d')
        

            #「日付」「種類」「金額」「出金元」「入金先」「こめんと」 / 種類は入金と振替
        if x['from_account'] == None:
            #f_account_text = '-'    
            if x['place'][0:2] == 'たか' or x['place'][0:2] == '貴宏':
                f_account_text = 'たか'
            elif x['place'][0:2] == 'さえ':
                f_account_text = 'さえ'
            else:
                f_account_text = 'その他'

            
        else:
            f_account_text = x['from_account']
        if x['mode'] == 'transfer':
            modetext = '<span class="label label-pill label-warning">振り替え</span>'
        elif x['mode'] == 'income':
            modetext = '<span class="label label-pill label-info">入金</span>'


        atext = """
                    <tr class="text-center">
                        <td>{date} ({wday})</td>
                        <td>{mode}</td>
                        <td class="text-right" style="padding-right:1em">¥{price:>6,}</td>
                        <td>{fromaccount}</td>
                        <td>{toaccount}</td>
                        <td style="text-align:left; padding-left:2em;">{comment}</td>
                    </tr>""".format(
            date=xday.strftime('%m/%d'),
            wday = get_weekdayJP(xday.strftime('%w')),
            price=x['amount'], 
            toaccount=x['to_account'], fromaccount = f_account_text,
            mode = modetext,
            comment = x['comment']
        )
        texts.append(atext)
        #print(atext)
    
    # 
    # t, s, tdata, sdata = get_tatekaeData([2016,10])

    t, s, tdata, sdata = get_tatekaeData(objYearMonth)

    
    xday = get_lastdayofmonth(objYearMonth)
    amount = t
    t_account = "たか"
    modetext = '<span class="label label-pill label-success">立替</span>'
    t_comment = "今月の立替は{}件".format(len(tdata))
        
    atext = """
            <tr class="text-center">
                <td>{date} ({wday})</td>
                <td>{mode}</td>
                <td class="text-right" style="padding-right:1em">¥{price:>6,}</td>
                <td>{fromaccount}</td>
                <td>{toaccount}</td>
                <td style="text-align:left; padding-left:2em;">{comment}</td>
            </tr>""".format(
    date=xday.strftime('%m/%d'),
    wday = get_weekdayJP(xday.strftime('%w')),
    price = amount, 
    toaccount = t_account, fromaccount ='-',
    mode = modetext,
    comment = t_comment)
    texts.append(atext)

    amount = s
    t_account = "さえ"
    t_comment = "今月の立替は{}件".format(len(sdata))
        
    atext = """
            <tr class="text-center">
                <td>{date} ({wday})</td>
                <td>{mode}</td>
                <td class="text-right" style="padding-right:1em">¥{price:>6,}</td>
                <td>{fromaccount}</td>
                <td>{toaccount}</td>
                <td style="text-align:left; padding-left:2em;">{comment}</td>
            </tr>""".format(
    date=xday.strftime('%m/%d'),
    wday = get_weekdayJP(xday.strftime('%w')),
    price = amount, 
    toaccount = t_account, fromaccount ='-',
    mode = modetext,
    comment = t_comment)
    texts.append(atext)
    
    
    textheader = """

    <!-- tablelist ここから-->

    <div class="panel panel-primary">
        <div class="panel-heading">{cat}<span class="badge pull-right">{counter}件 ¥{sumamount:,}</span></div>
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
                <thead>
                    <tr>
                        <th class="text-center">日付</th>
                        <th class="text-center">種類</th>
                        <th class="text-center">金額</th>
                        <th class="text-center">出金元</th>
                        <th class="text-center">入金先</th>
                        <th class="text-center">メモ</th>
                    </tr>
                </thead>
                <tbody>""".format(tableid=tableid, cat = tabletitle, counter=count,sumamount=round500(sum_amount))
    
    
    textfooter = """
                </tbody>
            </table>
        </div>
    </div>
    <!-- tablelist ここまで-->"""
    
    
    textbody = textheader + '\n'.join(texts) + textfooter

    #banktable = print_banktable(objYearMonth, moneydata, "銀行口座出納", "monthlybanktable")
    # return (textheaderA, textsA, textfooter, textbodyA)
        
#    return (textheader, texts, textfooter, textbody+banktable[3])

    return (textheader, texts, textfooter, textbody)

        


# In[78]:

def get_lastdayofmonth(objYearMonth):
    if objYearMonth[1] == 12:
        date = datetime.date(objYearMonth[0]+1, 1, 1)-datetime.timedelta(days=1)
    else:
        date = datetime.date(objYearMonth[0], objYearMonth[1]+1, 1)-datetime.timedelta(days=1)
    return date


# In[79]:

# bankdataだけ抜き出す
# 日付の修正
# 日付順に並び替える

def get_bankdata(mdata0):
    mdata1 = []
    for x in mdata0:
        if x['category'] != "口座":
            continue
        
        y = {}
        xday = dt.strptime(x['date'], '%Y-%m-%d')
        
        xname = x['name']
        if xname[0:2].isdigit():
            xday0 = x['date'][:-2] + xname[0:2]
            xday = dt.strptime(xday0, '%Y-%m-%d')
            xname = x['name'][3:]
        
        y['name'] = xname
        y['date'] = xday
        y['amount'] = x['amount']
        y['from_account'] = x['from_account']
        y['from_account_id'] = x['from_account_id']
        y['withdraw'] = 0
        y['deposit'] = 0
        if y['amount'] < 0: y['deposit'] = abs(x['amount'])
        else: y['withdraw'] = x['amount']


        

        mdata1.append(y)
    
    mdata2 = sorted(mdata1, key=lambda x: x['date'])
    return mdata2




# In[80]:

def print_banktable(objYearMonth, moneydata, tabletitle, tableid):
    
    # mode payment and category == 口座

    # 銀行口座
    textsA = []
    countA = 0
    sum_amountA = 0
    
    moneydata1 = get_bankdata(moneydata)

    for x in moneydata1:
        
        countA = countA + 1
        sum_amountA = sum_amountA + x['amount']
        xday = x['date']
        xname = x['name']            
        
        # 家の口座はinfo色, ソニー銀行はsuccess色, それ以外 (ゆうちょ)はprimary色
        if x['from_account_id'] == 8105914:
            labeltext = '<span class="label label-pill label-info">'
        elif x['from_account_id'] == 8105937:
            labeltext = '<span class="label label-pill label-success">'
        elif x['from_account_id'] == 8105916:
            labeltext = '<span class="label label-pill label-primary">'
        else:
            labeltext = '<span class="label label-pill label-warning">'


        if x['amount'] < 0:
            atext = """
                        <tr class="text-center">
                            <td>{toaccount}</span></td>
                            <td>{date} ({wday})</td>
                            <td class="text-right" style="color:blue; padding-right:1em;">入金: ¥{price:>6,}</td>
                            <td style="text-align:left; padding-left:2em;">{comment}</td>
                        </tr>""".format(
                date=xday.strftime('%m/%d'),
                wday = get_weekdayJP(xday.strftime('%w')),
                price=abs(x['amount']), 
                toaccount=labeltext+x['from_account'], 
                comment = xname
                )
        else:
            # fortest : 場当たり
            if x['from_account'] == None:
                f_account_text = ''
            else:
                f_account_text = x['from_account']
                
            atext = """
                    <tr class="text-center">
                        <td>{toaccount}</span></td>
                        <td>{date} ({wday})</td>
                        <td class="text-right" style="color:red;padding-right:1em;">出金: ¥{price:>6,}</td>
                        <td style="text-align:left; padding-left:2em;">{comment}</td>
                    </tr>""".format(
            date=xday.strftime('%m/%d'),
            wday = get_weekdayJP(xday.strftime('%w')),
            price=x['amount'], 
            toaccount=labeltext+f_account_text, #+x['from_account'], 
            comment = xname
            )
        
                
        

        textsA.append(atext)
        #print(atext)
    
    
    
    textheaderA = """

    <!-- tablelist ここから-->

    <div class="panel panel-primary">
        <div class="panel-heading">{cat}<span class="badge pull-right">{counter}件 ¥{sumamount:,}</span></div>
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
                <thead>
                    <tr>
                        <th class="text-center">口座</th>
                        <th class="text-center">日付</th>
                        <th class="text-center">金額</th>
                        <th class="text-center">メモ</th>
                    </tr>
                </thead>
                <tbody>""".format(tableid=tableid, cat = tabletitle, counter=countA,sumamount=round500(sum_amountA))
    
    textfooter = """
                </tbody>
            </table>
        </div>
    </div>
    <!-- tablelist ここまで-->"""


    textbodyA = textheaderA + '\n'.join(textsA) + textfooter

        
    return (textheaderA, textsA, textfooter, textbodyA)
        


# In[81]:

def get_graphtabbodytext(objYearMonth):
    graphdays = ",".join(get_monthdaya(objYearMonth[0],objYearMonth[1]))

    obj = [25504271, 109]
    # 養育費
    catdatastr_CHIKA = get_categorydatastr(objYearMonth,obj)

    obj = [107,  106, 108, 110,111]
    # objtitle = "積立金"
    catdatastr_HENDO = get_categorydatastr(objYearMonth,obj)

    obj = [105, 25504225]
    # objtitle = "公共料金・税金"
    catdatastr_KOUKYO = get_categorydatastr(objYearMonth,obj)

    obj = [101]
    # objtitle = "生活費"
    catdatastr_SEIKATSU = get_categorydatastr(objYearMonth,obj)

    #               label1 = "全カテゴリ";
    catdatastr_ALL = get_categorydatastr(objYearMonth)



    graphbodyheader = """
                <div>
                    <canvas id="canvas"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                  var DAYS = [{graphdays}];
                  data1 = [{data_all}];
                  data2 = [{data_hendo}];
                  data3 = [{data_chika}];
                  data4 = [{data_seikatsu}];
                  data5 = [{data_kokyo}];
                  """.format(graphdays = graphdays, data_all = catdatastr_ALL[0], 
                             data_hendo = catdatastr_HENDO[0], data_chika = catdatastr_CHIKA[0], 
                             data_seikatsu = catdatastr_SEIKATSU[0], data_kokyo = catdatastr_KOUKYO[0])

    graphbodybody2 = """
                  label1 = "全カテゴリ";
                  label2 = "変動費";
                  label3 = "智花";
                  label4 = "生活費";
                  label5 = "公共料金";

                    var config = {
                        type: 'line',
                        data: {
                            labels: DAYS,
                            datasets: [{
                                hidden: true,
                                label: label1,
                                data: data1,
                                fill: false,
                                borderColor : "#B2C7E8",
                                borderWidth:5,
                                pointBorderColor:"#fff",
                                pointBorderWidth:2,
                                pointBackgroundColor:"#B2C7E8",
                                radius:4,
                                tension:0,
                            }, {
                                hidden: false,
                                label: label2,
                                data: data2,
                                fill: false,
                                borderColor : "#1abc9c",
                                borderWidth:5,
                                pointBorderColor:"#fff",
                                pointBorderWidth:2,
                                pointBackgroundColor:"#1abc9c",
                                radius:4,
                                tension:0,
                            }, {
                                label: label3,
                                data: data3,
                                fill: false,
                                borderColor : "#fc2e41",
                                borderWidth:5,
                                pointBorderColor:"#fff",
                                pointBorderWidth:2,
                                pointBackgroundColor:"#fc2e41",
                                radius:4,
                                tension:0,
                            }, {
                              // hidden:true,
                              //display:false,
                              label: label4,
                              data: data4,
                              fill: false,
                              borderColor : "#3498db",
                              borderWidth:5,
                              pointBorderColor:"#fff",
                              pointBorderWidth:2,
                              pointBackgroundColor:"#3498db",
                              radius:4,
                              tension:0,
                            }, {
                              hidden:true,
                              label: label5,
                              data: data5,
                              fill: false,
                              borderColor : "#FFD25A",
                              borderWidth:5,
                              pointBorderColor:"#fff",
                              pointBorderWidth:2,
                              pointBackgroundColor:"#FFD25A",
                              radius:4,
                              tension:0,
                            }
                          ]
                        },
                        options: {
                            responsive: true,
                            title:{
                                display:true,
                                """
    
    graphbodybody3 = """
                                text:'{objmonth}月の出金推移'
                                """.format(objmonth = objYearMonth[1])

    graphbodybody4 = """
                            },
                            tooltips: {
                                mode: 'single',
                                caretSize:5,
                                callbacks: {
                                  title: function(tooltipItem,data){
                                  },
                                  label: function(tooltipItem,data){
                                    var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                                    return tooltipItem.xLabel + ': ¥' + tooltipItem.yLabel.toLocaleString();
                                  },
                                  afterLabel: function(tooltipItem, data) {
                                  """

    graphbodybody5 = """
                                    var myArr1 = [{label_all}];
                                    var myArr2 = [{label_hendo}];
                                    var myArr3 = [{label_chika}];
                                    var myArr4 = [{label_seikatsu}];
                                    var myArr5 = [{label_kokyo}];
                                    """.format(label_all = catdatastr_ALL[1], 
                             label_hendo = catdatastr_HENDO[1], label_chika = catdatastr_CHIKA[1], 
                             label_seikatsu = catdatastr_SEIKATSU[1], label_kokyo = catdatastr_KOUKYO[1])

    graphbodybody6 = """
                                    var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                                    //This will be the tooltip.body
                                    // return datasetLabel + ': ' + tooltipItem.yLabel +' :'+ myArr[tooltipItem.index];
                                    if (tooltipItem.datasetIndex == 0){
                                      var myArr = myArr1
                                    } else if (tooltipItem.datasetIndex == 1){
                                      var myArr = myArr2
                                    } else if (tooltipItem.datasetIndex == 2){
                                      var myArr = myArr3
                                    } else if (tooltipItem.datasetIndex == 3){
                                      var myArr = myArr4
                                    } else if (tooltipItem.datasetIndex == 4){
                                      var myArr = myArr5
                                    }
                                    return  myArr[tooltipItem.index];
                                   },
                                }
                            },
                            custom: function(tooltip) {
                                                       var tooltipEl = $('#chartjs-tooltip');
                                                       if (!tooltip) {
                                                           tooltipEl.css({
                                                               opacity: 0
                                                           });
                                                           return;
                                                       }
                                                       if (typeof  tooltip.body != 'undefined') {
                                                           var bodyText = tooltip.body[0].split(":");
                                                           var innerHtml = '<span class="chartjs-tooltip-header"><b>'+tooltip.title[0]+'</b></span><br>'
                                                                           +'<span>' + bodyText[0].trim() + '</span> : <span><b>' + bodyText[1].trim() +'</b></span>'
                                                                           +'<span>' + bodyText[2].trim() + '</span>';
                                                           tooltipEl.html(innerHtml);
                                                           tooltipEl.css({
                                                               opacity: 1,
                                                               left: (tooltip.xPadding * 3) + tooltip.x + 'px',
                                                               top: (tooltip.yPadding * 3) + tooltip.y + 'px',
                                                           });
                                                       }
                                                   },
                            hover: {
                                mode: 'dataset'
                            },
                            scales: {
                                xAxes: [{
                                    display: true,
                                    gridLines: {
                                      display:true,
                                      lineWidth:1,
                                      drawOnChartArea:false,
                                      zeroLineWidth:1,
                                   },
                                    scaleLabel: {
                                        show: true,
                                        labelString: 'Month'
                                    }
                                }],
                                yAxes: [{
                                    display: true,
                                    scaleLabel: {
                                        show: true,
                                        labelString: 'Value'
                                    },
                                    ticks: {
                                        suggestedMin: 0,
                                        suggestedMax: 2500,
                                        userCallback: function(value, index, values) {
                                          return "¥" + value.toLocaleString();
                                        }
                                      }
                                }]
                            }
                        }
                    };

                    window.onload = function() {
                        var ctx = document.getElementById("canvas").getContext("2d");
                        window.myLine = new Chart(ctx, config);
                    };

                </script>
                <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2 + graphbodybody3 + graphbodybody4 + graphbodybody5 + graphbodybody6


# In[82]:

def output_monthly(objYear=2016, objMonth=3):
    
    objYearMonth = objYear,objMonth

    htmlheader = get_monthly_htmlheader(objYearMonth)
    htmlfooter = get_htmlfooter()

    fgraph = get_monthlyfrontgraph(objYearMonth)
    
    stab = get_summarytab(objYearMonth)
    
    rtab_header = get_reporttabheader(objYearMonth)
    rtab_body = get_reporttabbody(objYearMonth)
    rtab_footer = get_reporttabfooter(objYearMonth)

    gtab_header = get_graphtabheader(objYearMonth)
    gtab_body = get_graphtabbodytext(objYearMonth)
    gtab_footer = get_graphtabfooter(objYearMonth)

    dtab_header = get_detailtabheader(objYearMonth)
    dtab_body = get_detailtabbody(objYearMonth)
    dtab_footer = get_detailtabfooter(objYearMonth)

    filename = ("output/jade/m{}-{:02}.html").format(objYear, objMonth)
    f = open(filename, 'w') # 書き込みモードで開く
    f.write(htmlheader) # 引数の文字列をファイルに書き込む

    f.write(fgraph) # 引数の文字列をファイルに書き込む


    f.write(rtab_header) # 引数の文字列をファイルに書き込む
    f.write(rtab_body) # 引数の文字列をファイルに書き込む
    f.write(rtab_footer) # 引数の文字列をファイルに書き込む

    f.write(stab) # 引数の文字列をファイルに書き込む


    f.write(gtab_header) # 引数の文字列をファイルに書き込む
    f.write(gtab_body) # 引数の文字列をファイルに書き込む
    f.write(gtab_footer) # 引数の文字列をファイルに書き込む

    f.write(dtab_header) # 引数の文字列をファイルに書き込む
    f.write(dtab_body) # 引数の文字列をファイルに書き込む
    f.write(dtab_footer) # 引数の文字列をファイルに書き込む


    f.write(htmlfooter) # 引数の文字列をファイルに書き込む
    f.close() # ファイルを閉じる


# In[83]:

def output_indexpage():
    indexhtml = build_index()
    
    filename = ("output/jade/index.html")
    f = open(filename, 'w') # 書き込みモードで開く
    f.write(indexhtml) # 引数の文字列をファイルに書き込む
    f.close() # ファイルを閉じる


# In[84]:


def get_weekdayJP(weekdaynum):
    weekdayJP = ''
    if weekdaynum == '0':
        weekdayJP = '日'
    elif weekdaynum == '1':
        weekdayJP = '月'
    elif weekdaynum == '2':
        weekdayJP = '火'
    elif weekdaynum == '3':
        weekdayJP = '水'
    elif weekdaynum == '4':
        weekdayJP = '木'
    elif weekdaynum == '5':
        weekdayJP = '金'
    elif weekdaynum == '6':
        weekdayJP = '土'

    return weekdayJP
        


# # 年間家計レポート
# ## module定義
# import dt
# import datetime
# round500
# get_monthlyamount
# select_CategoryData
# select_RawCategoryData
# select_Wholedata
# TABLE, sqlite3
# select_from_sqlite
# 
# ## HTML全体
# 
# + html_header() /変更なし
# + html_footer() /変更なし
# 
# ## Report tab
# 表1. 四半期ごとの支出
# (表2. 月ごとの公共料金表)
# (表3. 月ごとの支出表)
# 
# + get_quarterly_reporttab_header(objYear) : 
# + get_quartelyamounts_reporttab_body(objYear) : 表1
# + get_monthlypublicfees_reporttab_body(objYear)  : 表2 まだ
# + get_yearmonthlyamounts_reporttab_body(objYear)  : 表3
# + get_quarterly_reporttab_footer(objYear) : 
# 
# ## Graph tab
# グラフ1a. 四半期ごとの支出推移
# グラフ2a. 月ごとの公共料金支出推移
# グラフ3a. 月ごとの支出推移
# 
# グラフ1b. 四半期ごとの支出率推移
# グラフ2b. 月ごとの公共料金支出率推移
# グラフ3b. 月ごとの支出率推移
# 
# + get_quarterly_graphtab_header() : 
# + get_yearByquarterly_graphtab_body(objYear) : グラフ1a
# + get_publicfeesbymonthly_graphtab_body(objYear) : グラフ2a
# + get_yearBymonthly_graphtab_body(objYear) : グラフ3a
# ++ get_yearByquarterlyR_graphtab_body(objYear) : グラフ1b
# ++ get_publicfeesbymonthlyR_graphtab_body(objYear) : グラフ2b
# ++ get_yearBymonthlyR_graphtab_body(objYear) : グラフ3b
# + get_quarterly_graphtab_footer() : 
# 
# ## Detail tab
# 保留
# + get_quarterly_detailtab_header() : 
# + get_quarterly_detailtab_body
# + get_quarterly_datailtab_footer() : 
# 
# 
# 
# 

# In[85]:

def get_yearlyatmonth_amounts(objYear):
    monthlyamounts = []
    for m in range(1,13):
        monthlyamount = get_monthlyamount((objYear,m))
        monthlyamounts.append(monthlyamount)
        
    return monthlyamounts

def get_yearlyatmonth_amounts_report(objYear):
    monthlyamounts = []
    for m in range(1,13):
        monthlyamount = get_monthlyamount_report((objYear,m))
        monthlyamounts.append(monthlyamount)
        
    return monthlyamounts


def get_yearlyatquarter_amounts(objYear):
    quarterlyamounts = []
    
    quarterlyamounts.append(get_monthes_amount([(objYear,1),(objYear,2),(objYear,3)]))
    quarterlyamounts.append(get_monthes_amount([(objYear,4),(objYear,5),(objYear,6)]))
    quarterlyamounts.append(get_monthes_amount([(objYear,7),(objYear,8),(objYear,9)]))
    quarterlyamounts.append(get_monthes_amount([(objYear,10),(objYear,11),(objYear,12)]))
    return quarterlyamounts


def get_monthesatmonth_amounts(objYearMonthes=[(2015,7), (2015,8),(2015,9)]):
    monthlyamounts = []
    for objYearMonth in objYearMonthes:
        monthlyamount = get_monthlyamount(objYearMonth)
        monthlyamounts.append(monthlyamount)
    return monthlyamounts

def get_yearly_amount(objYear):
#     monthlyamounts = get_yearlyatmonth_amounts_report(objYear)
    monthlyamounts = get_yearlyatmonth_amounts(objYear)
    sumamount = {}
    for key in monthlyamounts[0].keys():
        sumamount[key] = sum([x[key] for x in monthlyamounts])
    return sumamount



def get_monthes_amount(objYearMonthes):
    monthlyamounts = get_monthesatmonth_amounts(objYearMonthes)
    sumamount = {}
    for key in monthlyamounts[0].keys():
        sumamount[key] = sum([x[key] for x in monthlyamounts])
    return sumamount
# get_monthes_amount([(2014,1),(2014,2),(2014,3)])


# In[86]:

def get_yearly_statamount(objYear = 2015):
    # get_yearly_amount
    monthlyamounts = get_yearlyatmonth_amounts_report(objYear)
    sumamount = {}
    statamount = {}
    top5a = ()
    for key in monthlyamounts[0].keys():
        keyamount = [x[key][0] for x in monthlyamounts]
        suma = sum(keyamount)
        maxa = max(keyamount)
        mina = min(keyamount)
        meana = statistics.mean(keyamount)
        mediana = statistics.median(keyamount)
        top5a = get_top5forkey(monthlyamounts, key)
        
        sumamount[key] = suma
        statamount[key] = {'sum':suma, 'mean':meana, 'median':mediana,                           'top5':top5a[0], 'cnt':top5a[1], 'max':maxa, 'min':mina}
    return statamount
        


# In[ ]:




# In[ ]:




# In[ ]:




# In[87]:

def get_top5forkey(monthlyamount, key):
    t = []
    cnt = 0
    for m in monthlyamount:
        cnt = cnt + m[key][3]
        for n in m[key][1]:
            t.append(n)
    
    top50 = sorted(t, key=lambda x: x[0], reverse=True)

    if key == 'all':
        tt = []
        for t5 in top50:
            if t5[2] == 'グレイス大森':
                None
            else:
                tt.append(t5)
        top5 = tt[:5]
            
    else:
        top5 = top50[:5]
    return top5, cnt
    
    #monthlyamounts[0]


# In[ ]:




# In[ ]:




# In[88]:

def get_yearlyamounts_stat_table():
    (yearfrom,yearto) = get_objYearRange()

    yearlyamounts = []
    for objYear in range(yearfrom,yearto):
        yearlyamounts.append(get_yearly_statamount(objYear))

    y = ['<th class="text-center"><a href="./y{yy}.html" style="color:#fff;">{yy}年</a></th>'         .format(yy=x) for x in range(yearfrom,yearto)]
    y0= """\t\t<tr>\n\t\t\t<th class="text-center"></th>\n\t\t\t"""
    y1 = "\n\t\t</tr>\n"
    
    yearlyth = y0 + '\n\t\t\t'.join(y) + y1


    yearlytd = {}
    for key in yearlyamounts[0].keys():
        y0 = "\t\t<tr>\n\t\t\t<td>{}</td>\n".format(key)
        y = ["\t\t\t<td>合計¥{:,}<br>平均¥{:,}<br>最大¥{:,}<br>{}件</td>\n"             .format(round500(x[key]['sum']), round500(x[key]['median']),                      round500(x[key]['max']), x[key]['cnt']) for x in yearlyamounts]
#         y = ["\t\t\t<td>{}件</td>\n".format(x[key]['min'] for x in yearlyamounts] #min, max, cnt, median, sum
#         y = ["\t\t\t<td>平均{:,}円</td>\n".format(round500(x[key]['median'])) for x in yearlyamounts]
        y1 = "\t\t</tr>\n"
        
        yearlytd[key] = y0 + '\n\t\t\t'.join(y) + y1


    summarytable0 = """
    <!-- output from PyJade -->
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                        {yheader}
                </thead>
                <tbody class="text-center">
                        {val1}
                        {val2}
                        {val3}
                        {val4}
                        {val5A}
                        {val5B}
                        {val5C}
                        {val6}
                        {val7}
                        {val8}
                    """.format(
            yheader=yearlyth,
                val1 = yearlytd['食費'],
                val2 = yearlytd['光熱費'],
                val3 = yearlytd['通信費'],
                val4 = yearlytd['社会保障'],
                val5A = yearlytd['娯楽・交際'],
                val5B = yearlytd['医療・健康'],
                val5C = yearlytd['美容'],
                val7 = yearlytd['大型出費'],
                val6 = yearlytd['教育・養育'],
                val8 = yearlytd['住まい'])




    summarytable1 = """
                <tfoot class="bg-info">
                </tfoot>
            </table>
        </div>
    </div>
""".format( 
            val0 = yearlytd['all']
    )
    
    
    
    tabletabbody = "\n<!-- #### report tab ここから #### -->\n"    + summarytable0 + summarytable1 +"\n<!-- #### report tab ここまで #### -->\n"

    
    return tabletabbody


# In[89]:

def get_yearlyamounts_top5_table():
    
    
    (yearfrom,yearto) = get_objYearRange()

    yearfromto = range(yearfrom,yearto)


#     yearlyamounts = []
    
#     for objYear in yearfromto:
#         yearlyamounts.append(get_yearly_statamount(objYear))

#     y = ['<th class="text-center"><a href="./y{yy}.html" style="color:#fff;">{yy}年</a></th>'\
#          .format(yy=x) for x in range(yearfrom,yearto)]
#     y0= """\t\t<tr>\n\t\t\t<th class="text-center"></th>\n\t\t\t"""
#     y1 = "\n\t\t</tr>\n"
    
#     yearlyth = y0 + '\n\t\t\t'.join(y) + y1


#     yearlytd = {}
#     for key in yearlyamounts[0].keys():
#         y0 = "\t\t<tr>\n\t\t\t<td>{}</td>\n".format(key)
#         y = ["\t\t\t<td>合計¥{:,}<br>平均¥{:,}<br>最大¥{:,}<br>{}件</td>\n"\
#              .format(round500(x[key]['sum']), round500(x[key]['median']), \
#                      round500(x[key]['max']), x[key]['cnt']) for x in yearlyamounts]
# #         y = ["\t\t\t<td>{}件</td>\n".format(x[key]['min'] for x in yearlyamounts] #min, max, cnt, median, sum
# #         y = ["\t\t\t<td>平均{:,}円</td>\n".format(round500(x[key]['median'])) for x in yearlyamounts]
#         y1 = "\t\t</tr>\n"
        
#         yearlytd[key] = y0 + '\n\t\t\t'.join(y) + y1


    
    
    tabletd = ""
#     for key in get_yearly_statamount(2016).keys():
    key = "all"
    thk = """<thead><th colspan="3">{}</th></thead>""".format(key)

    for objYear in yearfromto:
        y = get_yearly_statamount(objYear)
        th =  """<tr><td coldpan="3" style="text:center;">{}年</td></tr>""".format(objYear)

        for m in y[key]['top5']:
            t = """
            <tr>
            <td>{}月{}日</td>
            <td>{}</td>
            <td>¥{:,}</td></tr>""".format(datetxt2class(m[1]).month, datetxt2class(m[1]).day, m[2], m[0])
            th = th + t

        tabletd = tabletd + thk + th
        thk = ""
       
    
    summarytable0 = """
    <!-- output from PyJade -->
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                {}""".format(tabletd)


    summarytable1 = """
                <tfoot class="bg-info">
                </tfoot>
            </table>
        </div>
    </div>
""" 
    
    
    tabletabbody = "\n<!-- #### report tab ここから #### -->\n"    + summarytable0 + summarytable1 +"\n<!-- #### report tab ここまで #### -->\n"
    
    
    return tabletabbody


# In[ ]:




# In[90]:

def get_monthlypublickfees(objYearMonth):
    publickfees ={}
    # (5) 公共料金 : Category: ('公共', 105),
    obj = [105]
    moneylist = select_RawCategoryData(objYearMonth, obj)
    # monthlyamount['公共'] = sum([x['amount'] for x in moneylist])
    #publickfees['通信費'] = sum([x['amount'] for x in moneylist if x['genre_id'] in (2918018, 2918020,)])
    #publickfees['光熱費'] = sum([x['amount'] for x in moneylist if x['genre_id'] not in (2918018, 2918020,)])

    publickfees['モバイル通信費'] = sum([x['amount'] for x in moneylist if x['genre_id'] in (2918018,)])
    publickfees['家インターネット'] = sum([x['amount'] for x in moneylist if x['genre_id'] in (2918020,)])

    publickfees['ガス料金'] = sum([x['amount'] for x in moneylist if x['genre_id'] in (10503,)])
    publickfees['水道料金'] = sum([x['amount'] for x in moneylist if x['genre_id'] in (10501,)])
    publickfees['電気料金'] = sum([x['amount'] for x in moneylist if x['genre_id'] in (10502,)])
    publickfees['NHK'] = sum([x['amount'] for x in moneylist if x['genre_id'] in (2918017,)])


    # (5) 社会保障 : Category: ('社会保障', 25504225),
    obj = [25504225]
    moneylist = select_CategoryData(objYearMonth, obj)
    publickfees['社会保障'] = sum([x['amount'] for x in moneylist])
    return publickfees




# In[91]:

def get_quarterly_reporttab_header (objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### report tab ここから ### -->
      <div class="tab-pane" id="quarterlyreport">
        <div class="col-sm-1 hidden-xs"></div>
        <div class="col-sm-10 col-xs-12">
          <ul class="pager">
            {}
          </ul>

    """.format(pagerlinks)
    return headertext

def get_quarterly_reporttab_footer(objYear):
    pagerlinks = get_yearlypagerlinks(objYear)
    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
        <div class="col-sm-1 hidden-xs"></div>
      </div>
      <!-- ### report tab ここまで ### -->
      """.format(pagerlinks)

    return footertext


# In[92]:

def get_quarterly_Mreporttab_header (objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### 月ごとのreport tab ここから ### -->
      <div class="tab-pane" id="report">
        <div class="col-sm-1 hidden-xs"></div>
        <div class="col-sm-10 col-xs-12">
          <ul class="pager">
            {}
          </ul>

    """.format(pagerlinks)
    return headertext

def get_quarterly_Mreporttab_footer(objYear):
    pagerlinks = get_yearlypagerlinks(objYear)
    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
        <div class="col-sm-1 hidden-xs"></div>
      </div>
      <!-- ### report tab ここまで ### -->
      """.format(pagerlinks)

    return footertext


# In[93]:


def get_quarterly_graphtab_header (objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### graph tab ここから ### -->
      <div class="tab-pane" id="quarterlygraph">
        <div class="col-sm-1 hidden-xs"></div>
        <div class="col-sm-10 col-xs-12">
          <ul class="pager">
            {}
          </ul>
      """.format(pagerlinks)
    return headertext

def get_quarterly_graphtab_footer(objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
        <div class="col-sm-1 hidden-xs"></div>
      </div>
      <!-- ### graph tab ここまで ### -->
      """.format(pagerlinks)
    return footertext

#get_graphtabfooter((objYear,objMonth))


# In[94]:


def get_quarterly_Mgraphtab_header (objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### Mgraph tab ここから ### -->
      <div class="tab-pane" id="graph">
        <div class="col-sm-1 hidden-xs"></div>
        <div class="col-sm-10 col-xs-12">
          <ul class="pager">
            {}
          </ul>
      """.format(pagerlinks)
    return headertext

def get_quarterly_Mgraphtab_footer(objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
        <div class="col-sm-1 hidden-xs"></div>
      </div>
      <!-- ### Mgraph tab ここまで ### -->
      """.format(pagerlinks)
    return footertext

#get_graphtabfooter((objYear,objMonth))



# In[95]:

def get_quarterly_detailtab_header (objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### 詳細 tab ここから ### -->
        <div class="tab-pane" id="moneylist">
          <div class = "row">
            <div class="col-sm-1 hidden-xs"></div>
            <div class="col-sm-10 col-xs-12">
              <ul class="pager">
                {}
              </ul>
              
              <!-- #rev2.3 順番入れ替え -->
              <ul class="btn-group btn-group-justified  btn-group-sm" role="group" aria-label="testa" style="padding-left:0px;">
                <li type="button" class="btn btn-default"><a href="#table1">変動費</a></button>
                <li type="button" class="btn btn-default"><a href="#table2">教育・書籍</a></button>
                <li type="button" class="btn btn-default"><a href="#table4">外食</a></button>
                <li type="button" class="btn btn-default"><a href="#table3">大型出費</a></button>
                <li type="button" class="btn btn-default"><a href="#table5">銀行出納</a></button>
                <li type="button" class="btn btn-default"><a href="#table5t">入金リスト</a></button>

              </ul>
    """.format(pagerlinks)
    return headertext

def get_quarterly_detailtab_footer(objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    footertext = """
          <ul class="pager">
            {}
          </ul>
        </div>
      </div>
    </div>
    <!-- ### 詳細 tab ここまで ### -->
      """.format(pagerlinks)

    return footertext




# In[96]:

def get_yearly_KStab_header(objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### KS tab ここから ### -->
        <div class="tab-pane" id="reportkakutei">
          <div class = "row">
            <div class="col-sm-1 hidden-xs"></div>
            <div class="col-sm-10 col-xs-12">
              <ul class="pager">
                {}
              </ul>
              
    """.format(pagerlinks)
    return headertext

def get_yearly_summarytab_header(objYear):  # rev2.3
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### FP tab ここから ### -->
        <div class="tab-pane" id="summaryq">
          <div class = "row">
            <div class="col-sm-1 hidden-xs"></div>
            <div class="col-sm-10 col-xs-12">
              <ul class="pager">
                {}
              </ul>
              
              <ul class="btn-group btn-group-justified  btn-group-sm" role="group" aria-label="testa" style="padding-left:0px;">
                <li type="button" class="btn btn-default"><a href="#q1">Q1</a></button>
                <li type="button" class="btn btn-default"><a href="#q2">Q2</a></button>
                <li type="button" class="btn btn-default"><a href="#q3">Q3</a></button>
                <li type="button" class="btn btn-default"><a href="#q4">Q4</a></button>
                <li type="button" class="btn btn-default"><a href="#year">Year</a></button>
              </ul>


              
    """.format(pagerlinks)
    return headertext

def get_yearly_FPtab_header(objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### FP tab ここから ### -->
        <div class="tab-pane" id="reportfp">
          <div class = "row">
            <div class="col-sm-1 hidden-xs"></div>
            <div class="col-sm-10 col-xs-12">
              <ul class="pager">
                {}
              </ul>
              
    """.format(pagerlinks)
    return headertext

def get_yearly_moneyreporttab_header(objYear):
    pagerlinks = get_yearlypagerlinks(objYear)

    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### Money report tab ここから ### -->
        <div class="tab-pane" id="reportmoney">
          <div class = "row">
            <div class="col-sm-1 hidden-xs"></div>
            <div class="col-sm-10 col-xs-12">
              <ul class="pager">
                {}
              </ul>
              
    """.format(pagerlinks)
    return headertext



# In[97]:

def get_quarterly_htmlheader(objYear):
    headertext1 = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <meta name="robots" content="noarchive">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <title>Garnet Reports (ZAIM)</title>

  <!-- Bootstrap -->
  <link href="css/bootstrap.min.css" rel="stylesheet">

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="./dist/Chart.min.js"></script>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="js/bootstrap.min.js"></script>

  <!-- jQ-Cookie -->
  <script src="js/jquery.cookie.js"></script>
  
  <script type="text/javascript">
  $(function() {
    function clearTabFunc(){
      console.log("clear tab");
      $('a[data-toggle="tab"]').parent().removeClass('active');
    }

    function readTabFunc(){
      activeTab = $.cookie("QactiveTabName");
      if (activeTab == null) {
        activeTab = "Qreport";
        console.log("no tab in cookie");
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
        console.log("set cookie as QactiveTabName");
      }
      setTabActive();
    }

    function setTabActive(){
      console.log("set tab active:"+activeTab)
      activeTab0 = activeTab.substr(1) ;

      $('a[href=#' + activeTab0 +']').parent().addClass('active');
      $('#' + activeTab0).addClass('active');
    }

    $(function(){
      console.log("start")
      clearTabFunc();
      readTabFunc();
    
      $("#reporttab").click(function(){
        console.log("report tab activated");
        activeTab = "Qreport";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });

      $("#qreporttab").click(function(){
        console.log("Qreport tab activated");
        activeTab = "Qquarterlyreport";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });

      $("#graphtab").click(function(){
        console.log("graph tab activated");
        activeTab = "Qgraph";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });

      $("#qgraphtab").click(function(){
        console.log("Qgraph tab activated");
        activeTab = "Qquarterlygraph";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });

      $("#detailtab").click(function(){
        console.log("detail tab activated");
        activeTab = "Qmoneylist";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });

      $("#reporttabkakutei").click(function(){
        console.log("kakutei tab activated");
        activeTab = "Qreportkakutei";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });

      $("#reporttabfp").click(function(){
        console.log("fp tab activated");
        activeTab = "Qreportfp";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });
      $("#qtabsummary").click(function(){
        console.log("summary tab activated");
        activeTab = "Qsummaryq";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });


      $("#reporttabmoney").click(function(){
        console.log("moneyreport tab activated");
        activeTab = "Qreportmoney";
        $.cookie("QactiveTabName",activeTab, { expires: 700 });
      });




    });
  });
  $(function () {
    $('[data-toggle="popover"]').popover({ html: true,});
  });
  </script>
  <!-- jQ-Cookie -->
  <!-- rev2.3 qsummary.clickを追加 -->



  <style>
  canvas{
      -moz-user-select: none;
      -webkit-user-select: none;
      -ms-user-select: none;
      border:solid 1px #ddf;
  }
  </style>

</head>
<body>
  <div id="header" class="container" style="margin:30px"></div>
  <nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="navbar-header">
      <button class="navbar-toggle" data-toggle="collapse" data-target=".target">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a href="./index.html" class="navbar-brand">Garnet</a>
    </div>

    <div class="collapse navbar-collapse target">
      <ul class="nav navbar-nav">
      """

    tnow = dt.now()
    oyear = objYear
    if objYear == tnow.year:
        omonth = tnow.month
    else:
        omonth = 12
    
#     print(oyear)
#     print(omonth)
    headertext2 = """
        <li><a href="./m{}-{:02}.html">Monthly Report</a></li>
        """.format(oyear,omonth)

    
    headertext3 = """
        <li class="active"><a href="">Yearly Report</a></li>
        <li><a href="./summary.html">Total Report</a></li>
      </ul>
    </div>
  </nav>

  <div class="container" style="padding:20px 0">
  <h4>{y}年のレポート</h4>
        <a href="./i/y{y}.html">iPhone版はこちら</a>
    <ul class="nav nav-tabs" style="margin:20px 0">
      <li id="qtabsummary"><a href="#summaryq" data-toggle="tab">サマリー</a></li> <!-- rev2.3 -->
      <li id="reporttab" class="active"><a href="#report" data-toggle="tab">レポート(M)</a></li>
      <li id="qreporttab"><a href="#quarterlyreport" data-toggle="tab">レポート(Q)</a></li>
      <li id="graphtab"><a href="#graph" data-toggle="tab">グラフ(M)</a></li>
      <li id="qgraphtab"><a href="#quarterlygraph" data-toggle="tab">グラフ(Q)</a></li>
      <li id="detailtab"><a href="#moneylist" data-toggle="tab">出費詳細</a></li>
      <li id="reporttabkakutei"><a href="#reportkakutei" data-toggle="tab">確定申告用</a></li>
      <li id="reporttabfp"><a href="#reportfp" data-toggle="tab">FP用</a></li>
      <li id="reporttabmoney"><a href="#reportmoney" data-toggle="tab">金融資産推移</a></li>
    </ul>

    <div class="tab-content">
""".format(y=objYear)
    return headertext1+headertext2+headertext3




# In[98]:

def get_yearlypagerlinks(objYear):
    objDT0 = get_lastyear(objYear)
    objDT2 = get_nextyear(objYear)

#     prev_filename = ("y{}.html").format(objDT0)
#     next_filename = ("y{}.html").format(objDT2)
    
    (yearfrom,yearto)= get_objYearRange()
    if objYear == yearfrom:
        pagerlinks = """
            <li class = "next"><a href="./y{}.html">next</a></li>
        """.format(objDT2)
    elif objYear == yearto-1:
        pagerlinks = """
            <li class = "previous"><a href="./y{}.html">previous</a></li>
        """.format(objDT0)
    else:
        pagerlinks = """<li class = "previous"><a href="./y{}.html">previous</a></li>
            <li class = "next"><a href="./y{}.html">next</a></li>
        """.format(objDT0,objDT2)
        
    return pagerlinks

# (prev_link, next_link) = get_pagerlinks(objYearMonth)

def get_lastyear(thisyear):
    t0 = dt.strptime("{},1,1".format(thisyear), '%Y,%m,%d')
    t = t0 - datetime.timedelta(days=25)
    lastyear = dt.strptime("{},1,1".format(t.year), '%Y,%m,%d')
    return lastyear.year

def get_nextyear(thisyear):
    t0 = dt.strptime("{},12,31".format(thisyear), '%Y,%m,%d')
    t = t0 + datetime.timedelta(days=25)
    nextyear = dt.strptime("{},1,1".format(t.year), '%Y,%m,%d')
    return nextyear.year


def get_today():
    tnow = dt.now()
    return tnow.year, tnow.month, tnow.day


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[99]:

def get_categorynotes(catkey): #rev2.3 やめた
#     t = ['食費','光熱費', '通信費', '社会保障', '変動費',  '教育・養育', '大型出費', '住まい']
#     for tt in t:
#         print(get_categorynotes(tt))
    
    ca = get_bigcats()
    cl = getZaimList('cat')

    cnames = []
    for x in ca:
        if x['name'] == catkey and len(x['cat']) > 1:
            for cn in x['cat']:            
                for cc in cl[1]:
                    if cn == cc[1]:
                        cnames.append(cc[0])
                        break
    notes = catkey
    if len(cnames)>1:
        notes = catkey + '<br><span style="font-size:small;">' + ', '.join(cnames) + '</span>'
    
    return notes


# In[ ]:




# In[ ]:




# In[100]:

def get_quartelyamounts_reporttab_body(objYear):

    quarterlyamounts = get_yearlyatquarter_amounts(objYear)
    quarterlytd = {}
    for key in quarterlyamounts[0].keys():
        y = ["<td>¥{:,}</td>".format(round500(x[key])) for x in quarterlyamounts]
        y.append("<td><strong>¥{:,}</strong></td>".format(round500(sum([x[key] for x in quarterlyamounts]))))
        quarterlytd[key] = '\n\t\t\t'.join(y)
    
    # sum([monthlyamount[k] for k in monthlyamount]) - 107029
    summarytable0 = """
    <!-- output from PyJade -->
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center">{objYear}年</th>
                        <th class="text-center"><a href="./m{objYear}-03.html" style="color:#fff;">Q1</a></th>
                        <th class="text-center"><a href="./m{objYear}-06.html" style="color:#fff;">Q2</a></th>
                        <th class="text-center"><a href="./m{objYear}-09.html" style="color:#fff;">Q3</a></th>
                        <th class="text-center"><a href="./m{objYear}-12.html" style="color:#fff;">Q4</a></th>
                        <th class="text-center"><strong>小計</strong></th>
                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>{key1}</td>
                        {val1}
                    </tr>    
                    <tr>
                        <td>{key2}</td>
                        {val2}
                    </tr>    
                    <tr>
                        <td>{key3}</td>
                        {val3}
                    </tr>    
                    <tr>
                        <td>{key4}</td>
                        {val4}
                    </tr>
                    <!-- tr>
                        <td>{key5}</td>
                        {val5}
                    </tr -->

                    <tr>
                        <td>{key5A}</td>
                        {val5A}
                    </tr>
                    <tr>
                        <td>{key5B}</td>
                        {val5B}
                    </tr>
                    <tr>
                        <td>{key5C}</td>
                        {val5C}
                    </tr>
                    <tr>
                        <td>{key6}</td>
                        {val6}
                    </tr>
                    <tr>
                        <td>{key7}</td>
                        {val7}
                    </tr>
                    <!-- rev 2.3 -->
                    <tr>
                        <td>{key8}</td>
                        {val8}
                    </tr>

                    """.format(
            objYear=objYear,
            key1 = '食費/生活費', 
                val1 = quarterlytd['食費'],
            key2 = '光熱費', 
                val2 = quarterlytd['光熱費'],
            key3 = '通信費', 
                val3 = quarterlytd['通信費'],
            key4 = '社会保障', 
                val4 = quarterlytd['社会保障'],
            key5 = '変動費', 
                val5 = quarterlytd['変動費'],
            key5A = '娯楽・交際', 
                val5A = quarterlytd['娯楽・交際'],
            key5B = '医療・健康', 
                val5B = quarterlytd['医療・健康'],
            key5C = '美容', 
                val5C = quarterlytd['美容'],
            key6 = '教育・養育', 
                val6 = quarterlytd['教育・養育'],
            key7 = '大型出費', 
                val7 = quarterlytd['大型出費'],
            key8 = '住まい', 
                val8 = quarterlytd['住まい'])




    summarytable1 = """
                <tfoot class="bg-info">
                    <tr class="text-center" style="font-weight:bold;">
                        <td>小計</td>
                        {val0}
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>
""".format( 
            val0 = quarterlytd['all']
    )
    
    tabletabbody = "\n<!-- #### report tab ここから #### -->\n" + summarytable0 + summarytable1 + "\n<!-- #### report tab ここまで #### -->\n"

    
    return tabletabbody
    



# In[101]:

def get_yearmonthlyamounts_reporttab_body(objYear):
    monthlyamounts = get_yearlyatmonth_amounts_report(objYear)
    
    # sum([monthlyamount[k] for k in monthlyamount]) - 107029
    summarytable0 = """
    <!-- output from PyJade -->
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center" style="min-width: 80px;">{objY}年</th>
                        <th class="text-center">1月</th>
                        <th class="text-center">2月</th>
                        <th class="text-center">3月</th>

                        <th class="text-center">4月</th>
                        <th class="text-center">5月</th>
                        <th class="text-center">6月</th>

                        <th class="text-center">7月</th>
                        <th class="text-center">8月</th>
                        <th class="text-center">9月</th>

                        <th class="text-center">10月</th>
                        <th class="text-center">11月</th>
                        <th class="text-center">12月</th>
                        <th class="text-center"><strong>小計</strong></th>

                    </tr>
                </thead>
                <tbody class="text-center">
                    """.format(
            objY = objYear)

    def get_monthlyrow(tablekey, data, key = None):
        if key is None:
            key = tablekey
            
        td0 = ""
        cnt = 0
        for m0 in monthlyamounts:
            cnt += 1
            textamount = round500(m0[key][0])
            cmp0 = [x[key][0] for x in monthlyamounts]
            cmp1 = sum(cmp0) - max(cmp0) - textamount # 最大値と当月の値を引く。外れ値対策。 0は？
            cmp = (cmp1)/10
            if textamount > cmp*1.4:
                txt = '全{}件 (内上位{}件で{}%)'.format(m0[key][3], len(m0[key][1]),  m0[key][2])
                for a in reversed(m0[key][1]):
                    d = datetxt2class(a[1])
                    txt0 = "{}/{} {} ¥{:,}".format(d.month, d.day, a[2][:10], round500(a[0]))
                    txt = txt + "<br>" + txt0
                poptext = txt
                
                rightleft = "right"
                if cnt > 6:
                    rightleft = "left"
                
                td1 = """
                            <td>
                                <a data-toggle="popover" data-content="{}" data-placement="{}" style="color:red;">¥{:,}</a>
                            </td>""".format(poptext,rightleft,textamount)

            elif textamount < cmp/2:
                poptext = '{}件'.format(m0[key][3])
                td1 = """
                            <td>
                                <a data-toggle="popover" data-content="{}" style="color:#009;">¥{:,}</a>
                            </td>""".format(poptext, textamount)
            else:
                td1 = """
                            <td>¥{:,}</td>""".format(textamount)
            td0 = td0 + td1
            
        # 月ごとの小計を追加
        td1 = """
                        <td>¥{:,}</td>""".format(round500(sum([x[key][0] for x in data])))
        td0 = td0 + td1

#                       <td><a data-toggle="popover" title="ポップオーバーのタイトル" data-content="ポップオーバーの内容。">¥{:,}</a></td>""".format(round500(sum([x[key] for x in data])))
        monthlyrow0 = """
                    <tr>
                        <td>{title}</td>
                        {tds}
                    </tr>""".format(title=tablekey, tds=td0)
        
        return monthlyrow0


    tablekey1 = '食費/生活費'
    key1 = '食費'
    key2 = '光熱費'
    key3 = '通信費' 
    key4 = '社会保障' 
    key_51 = '娯楽・交際'
    key_52 = '医療・健康'
    key_53 = '美容'
    key6 = '教育・養育'
    key7 = '大型出費'
    key8 = '住まい'
    summarytable1 = get_monthlyrow(tablekey1, monthlyamounts, key1)
    summarytable2 = get_monthlyrow(key2, monthlyamounts)
    summarytable3 = get_monthlyrow(key3, monthlyamounts)
    summarytable4 = get_monthlyrow(key4, monthlyamounts)
    summarytable5_1 = get_monthlyrow(key_51, monthlyamounts)
    summarytable5_2 = get_monthlyrow(key_52, monthlyamounts)
    summarytable5_3 = get_monthlyrow(key_53, monthlyamounts)
    summarytable6  = get_monthlyrow(key6, monthlyamounts)
    summarytable7  = get_monthlyrow(key7, monthlyamounts)
    summarytable8  = get_monthlyrow(key8, monthlyamounts)



    summarytableSUM = """
                <tfoot class="bg-info">
                    <tr class="text-center">
                        <td><strong>小計</strong></td>
                        <td><strong>¥{val0M1:,}</strong></td>
                        <td><strong>¥{val0M2:,}</strong></td>
                        <td><strong>¥{val0M3:,}</strong></td>

                        <td><strong>¥{val0M4:,}</strong></td>
                        <td><strong>¥{val0M5:,}</strong></td>
                        <td><strong>¥{val0M6:,}</strong></td>

                        <td><strong>¥{val0M7:,}</strong></td>
                        <td><strong>¥{val0M8:,}</strong></td>
                        <td><strong>¥{val0M9:,}</strong></td>

                        <td><strong>¥{val0MA:,}</strong></td>
                        <td><strong>¥{val0MB:,}</strong></td>
                        <td><strong>¥{val0MC:,}</strong></td>

                        <td><strong>¥{val0M0:,}</strong></td>


</tr>
                </tfoot>
            </table>
        </div>
    </div>
""".format( 
            val0M1 = round500(monthlyamounts[0]['all'][0]),
            val0M2 = round500(monthlyamounts[1]['all'][0]),
            val0M3 = round500(monthlyamounts[2]['all'][0]),

            val0M4 = round500(monthlyamounts[3]['all'][0]),
            val0M5 = round500(monthlyamounts[4]['all'][0]),
            val0M6 = round500(monthlyamounts[5]['all'][0]),

            val0M7 = round500(monthlyamounts[6]['all'][0]),
            val0M8 = round500(monthlyamounts[7]['all'][0]),
            val0M9 = round500(monthlyamounts[8]['all'][0]),

            val0MA = round500(monthlyamounts[9]['all'][0]),
            val0MB = round500(monthlyamounts[10]['all'][0]),
            val0MC = round500(monthlyamounts[11]['all'][0]),
                val0M0 = round500(sum([x['all'][0] for x in monthlyamounts]))

    )
    
    tabletabbody = "\n<!-- #### report tab ここから #### -->\n" +     summarytable0 + summarytable1 + summarytable2 + summarytable3 + summarytable4 +    summarytable5_1+ summarytable5_2 + summarytable5_3 +    summarytable6 + summarytable7 + summarytable8 + summarytableSUM +    "\n<!-- #### report tab ここまで #### -->\n"

    
    return tabletabbody


# In[102]:

def get_yearByquarterly_graphtab_body(objYear):
    graphtitle = "{}年の期ごとの推移".format(objYear)
    quarterlyamounts = get_yearlyatquarter_amounts(objYear)
    qdata = {}
    for key in quarterlyamounts[0].keys():
        qdata[key] = [x[key] for x in quarterlyamounts]
    qdata['公共'] = [x['光熱費']+x['社会保障']+x['通信費'] for x in quarterlyamounts]



#                <div style="width:100%;">

    graphbodyheader = """
                <div>
                    <canvas id="myChart1"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = ["Q1", "Q2", "Q3", "Q4"];
                    var data1 = {data_hendo};
                    var data2 = {data_chika};
                    var data3 = {data_seikatsu};
                    var data4 = {data_kokyo};
                    var data5 = {data_ogata};
                  """.format(graphtitle = graphtitle,
                             data_hendo = qdata['変動費'], 
                             data_chika = qdata['教育・養育'], 
                             data_seikatsu = qdata['食費'],
                             data_kokyo = qdata['公共'],
                             data_ogata = qdata['大型出費'])
    
    #     var  data1 = [48375,3234,12324,98462];
    #                     var  data2 = [20983,83962,3234,42384];
    #                     var  data3 = [3235,33905,49835,98729];
    #                     var  data4 = [106257,16257,86257,46457];
    graphbodybody2 = """
                    var  label1 = "変動費";
                    var  label2 = "養育費";
                    var  label3 = "生活費";
                    var  label4 = "公共料金";
                    var  label5 = "大型出費";


                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(48,255,192,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,132,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(132,99,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                        stacked: true
                                }],
                                yAxes: [{
                                        stacked: true,
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 25000,
                                    userCallback: function(value, index, values) {
                                      return "¥" + value.toLocaleString();
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ¥' + tooltipItem.yLabel.toLocaleString();
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChart1");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[103]:

def get_publicfeesbymonthly_graphtab_body(objYear):
    graphtitle = "{}年の公共料金の推移".format(objYear)
    monthlyamounts = []
    for objMonth in range(1,13):
        monthlyamounts.append(get_monthlypublickfees((objYear,objMonth)))
    qdata = {}
    for key in monthlyamounts[0].keys():
        qdata[key] = [x[key] for x in monthlyamounts]

#                <div style="width:100%;">

    graphbodyheader = """
                <div>
                    <canvas id="myChartPFR"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = ["1月", "2月", "3月", "4月", "5月", "6月","7月","8月","9月","10月", "11月","12月"];
                    var data1 = {data1};
                    var data2 = {data2};
                    var data3 = {data3};
                    var data4 = {data4};
                    var data5 = {data5};
                    var data6 = {data6};
                    var data7 = {data7};
                  """.format(graphtitle = graphtitle,
                             data1 = qdata['ガス料金'], 
                             data2 = qdata['電気料金'], 
                             data3 = qdata['水道料金'],
                             data4 = qdata['NHK'], 
                             data5 = qdata['家インターネット'], 
                             data6 = qdata['モバイル通信費'], 
                             data7 = qdata['社会保障'])
    
    
    graphbodybody2 = """
                    var  label1 = "ガス料金";
                    var  label2 = "電気料金";
                    var  label3 = "水道料金";
                    var  label4 = "NHK";
                    var  label5 = "家インターネット";
                    var  label6 = "モバイル通信費";
                    var  label7 = "社会保障";




                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(132,99,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,132,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label6,
                              data: data6,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label7,
                              data: data7,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                        stacked: true
                                }],
                                yAxes: [{
                                        stacked: true,
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 25000,
                                    userCallback: function(value, index, values) {
                                      return "¥" + value.toLocaleString();
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ¥' + tooltipItem.yLabel.toLocaleString();
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChartPFR");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[104]:



def get_restaurantnumbymonthly_graphtab_body(objYear):
    
    
    
    
    graphtitle = "{}年の外食件数の推移".format(objYear)
    obj = [10103]
    TH = 1000

    moneydata = []
    for objMonth in range(1,13):
        monthlydata = select_GenreData((objYear,objMonth), obj, TH)
        moneydata.append(len(monthlydata))
    

#                <div style="width:100%;">

    graphbodyheader = """
                <div>
                    <canvas id="myChartRestraurtant"></canvas>
                </div>

                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = ["1月", "2月", "3月", "4月", "5月", "6月","7月","8月","9月","10月", "11月","12月"];
                    var data1 = {data1};
                  """.format(graphtitle = graphtitle,
                             data1 = moneydata)
    
    
    graphbodybody2 = """
                    var  label1 = "外食件数";

                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                yAxes: [{
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0
                                  }
                              }]
                            }
                        }

                    var ctx = document.getElementById("myChartRestraurtant");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[105]:

def get_yearBymonthly_graphtab_body(objYear):
    graphtitle = "{}年の月ごとの推移".format(objYear)
    monthlyamounts = get_yearlyatmonth_amounts(objYear)
    qdata = {}
    for key in monthlyamounts[0].keys():
        qdata[key] = [x[key] for x in monthlyamounts]
    qdata['公共'] = [x['光熱費']+x['社会保障']+x['通信費'] for x in monthlyamounts]

#                <div style="width:100%;">

    graphbodyheader = """
                <div>
                    <canvas id="myChart2"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = ["1月", "2月", "3月", "4月", "5月", "6月","7月","8月","9月","10月", "11月","12月"];
                    var data1 = {data_hendo};
                    var data2 = {data_chika};
                    var data3 = {data_seikatsu};
                    var data4 = {data_kokyo};
                    var data5 = {data_ogata};
                  """.format(graphtitle = graphtitle,
                             data_hendo = qdata['変動費'], 
                             data_chika = qdata['教育・養育'], 
                             data_seikatsu = qdata['食費'],
                             data_kokyo = qdata['公共'],
                             data_ogata = qdata['大型出費'])
    
    graphbodybody2 = """
                    var  label1 = "変動費";
                    var  label2 = "養育費";
                    var  label3 = "生活費";
                    var  label4 = "公共料金";
                    var  label5 = "大型出費";


                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(132,99,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,132,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                        stacked: true
                                }],
                                yAxes: [{
                                        stacked: true,
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 25000,
                                    userCallback: function(value, index, values) {
                                      return "¥" + value.toLocaleString();
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ¥' + tooltipItem.yLabel.toLocaleString();
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChart2");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[106]:

def get_yearByquarterlyR_graphtab_body(objYear):
    graphtitle = "{}年の期ごとの支出率推移 (%)".format(objYear)
    quarterlyamounts = get_yearlyatquarter_amounts(objYear)
    qdata = {}
    for key in quarterlyamounts[0].keys():
        qdata[key] = [int(x[key]/x['all']*100*10)/10 if not x['all'] ==0 else 0 for x in quarterlyamounts]
    qdata['公共'] = [int((x['光熱費']+x['社会保障']+x['通信費'])/x['all']*100*10)/10 if not x['all'] ==0 else 0 for x in quarterlyamounts]



#                <div style="width:100%;">

    graphbodyheader = """
                <div>
                    <canvas id="myChartQR"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = ["Q1", "Q2", "Q3", "Q4"];
                    var data1 = {data_hendo};
                    var data2 = {data_chika};
                    var data3 = {data_seikatsu};
                    var data4 = {data_kokyo};
                    var data5 = {data_ogata};
                  """.format(graphtitle = graphtitle,
                             data_hendo = qdata['変動費'], 
                             data_chika = qdata['教育・養育'], 
                             data_seikatsu = qdata['食費'],
                             data_kokyo = qdata['公共'],
                             data_ogata = qdata['大型出費'])
    
    #     var  data1 = [48375,3234,12324,98462];
    #                     var  data2 = [20983,83962,3234,42384];
    #                     var  data3 = [3235,33905,49835,98729];
    #                     var  data4 = [106257,16257,86257,46457];
    graphbodybody2 = """
                    var  label1 = "変動費";
                    var  label2 = "智花";
                    var  label3 = "生活費";
                    var  label4 = "公共料金";
                    var  label5 = "大型出費";


                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(132,99,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,132,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                        stacked: true
                                }],
                                yAxes: [{
                                        stacked: true,
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 100,
                                    userCallback: function(value, index, values) {
                                      return value+"%";
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ' + tooltipItem.yLabel.toLocaleString() +'%';
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChartQR");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[107]:

def get_publicfeesbymonthlyR_graphtab_body(objYear):
    graphtitle = "{}年の公共料金出勤割合の推移(%)".format(objYear)
    monthlyamounts = []
    for objMonth in range(1,13):
        t = get_monthlypublickfees((objYear,objMonth))
        s = sum([v for k,v in t.items()])
        if s == 0:
            s = 1
        monthlypf = {k:int(v/s*100*10)/10 for k,v in t.items()}
        monthlyamounts.append(monthlypf)
    qdata = {}
    for key in monthlyamounts[0].keys():
        qdata[key] = [x[key] for x in monthlyamounts]
        
        
        #                <div style="width:100%;">

    graphbodyheader = """
                <div>
                    <canvas id="myChart3"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = ["1月", "2月", "3月", "4月", "5月", "6月","7月","8月","9月","10月", "11月","12月"];
                    var data1 = {data1};
                    var data2 = {data2};
                    var data3 = {data3};
                    var data4 = {data4};
                    var data5 = {data5};
                    var data6 = {data6};
                    var data7 = {data7};
                  """.format(graphtitle = graphtitle,
                             data1 = qdata['ガス料金'], 
                             data2 = qdata['電気料金'], 
                             data3 = qdata['水道料金'],
                             data4 = qdata['NHK'], 
                             data5 = qdata['家インターネット'], 
                             data6 = qdata['モバイル通信費'], 
                             data7 = qdata['社会保障'])
    
    
    graphbodybody2 = """
                    var  label1 = "ガス料金";
                    var  label2 = "電気料金";
                    var  label3 = "水道料金";
                    var  label4 = "NHK";
                    var  label5 = "家インターネット";
                    var  label6 = "モバイル通信費";
                    var  label7 = "社会保障";




                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(132,99,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,132,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label6,
                              data: data6,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label7,
                              data: data7,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                        stacked: true
                                }],
                                yAxes: [{
                                        stacked: true,
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 100,
                                    userCallback: function(value, index, values) {
                                      return value+"%";
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ' + tooltipItem.yLabel.toLocaleString()+'%';
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChart3");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[108]:

def get_yearBymonthlyR_graphtab_body(objYear):
    graphtitle = "{}年の月ごとの出勤割合の推移".format(objYear)
    monthlyamounts = get_yearlyatmonth_amounts(objYear)
    qdata = {}
    for key in monthlyamounts[0].keys():
        qdata[key] = [int(x[key]/x['all']*100*10)/10 if not x['all'] ==0 else 0 for x in monthlyamounts]
    qdata['公共'] = [int((x['光熱費']+x['社会保障']+x['通信費'])/x['all']*100*10)/10 if not x['all'] ==0 else 0 for x in monthlyamounts]

#                <div style="width:100%;">


    graphbodyheader = """
                <div>
                    <canvas id="myChartMR"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = ["1月", "2月", "3月", "4月", "5月", "6月","7月","8月","9月","10月", "11月","12月"];
                    var data1 = {data_hendo};
                    var data2 = {data_chika};
                    var data3 = {data_seikatsu};
                    var data4 = {data_kokyo};
                    var data5 = {data_ogata};
                  """.format(graphtitle = graphtitle,
                             data_hendo = qdata['変動費'], 
                             data_chika = qdata['教育・養育'], 
                             data_seikatsu = qdata['食費'],
                             data_kokyo = qdata['公共'],
                             data_ogata = qdata['大型出費'])
    
    graphbodybody2 = """
                    var  label1 = "変動費";
                    var  label2 = "養育費";
                    var  label3 = "生活費";
                    var  label4 = "公共料金";
                    var  label5 = "大型出費";


                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(48,255,192,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,132,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(132,99,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                        stacked: true
                                }],
                                yAxes: [{
                                        stacked: true,
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 100,
                                    userCallback: function(value, index, values) {
                                      return value+"%";
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ' + tooltipItem.yLabel.toLocaleString()+'%';
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChartMR");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# # その月のサマリーレポート用の関数

# In[109]:

def get_genressummaly(objYearMonth):
    
    ###
    
    objDT0 = objYearMonth 
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)

    monthlyamount = {}
    monthlycatamount = {}
    genres =  detailgenres()
    #     zaimcat = genres.keys() => dict_keys(['食費•日用品', '公共・社会保障', '教育・教養', '変動費', '大型出費'])
    zaimcat = ['食費•日用品', '公共・社会保障', '教育・教養', '変動費', '大型出費', '住まい']

    monthlyallamount0 = 0
    monthlyallamount1 = 0
    monthlyallamount2 = 0
    
    for cat0 in zaimcat:
        monthlycatamount[cat0] = []
        monthlyamount0 = []
        monthlyamount[cat0] = []
        sumamounts = {}
        monthlycatamount0 = 0
        monthlycatamount1 = 0
        monthlycatamount2 = 0

        for genrecode in genres[cat0]:
            moneylist = select_GenreData(objDT2, genrecode[1])
            samount2 = round500(sum([x['amount'] for x in moneylist]))
            # 2ヶ月前のジャンルごとの合計金額

            moneylist = select_GenreData(objDT1, genrecode[1])
            samount1 = round500(sum([x['amount'] for x in moneylist]))
            # 1ヶ月前のジャンルごとの合計金額

            moneylist = select_GenreData(objDT0, genrecode[1])
            samount0 = round500(sum([x['amount'] for x in moneylist]))
            # 0ヶ月前のジャンルごとの合計金額

#             aveamount = (samount0+samount1+samount2)/3
            aveamount = (samount1+samount2)/2
            
            if aveamount==0:aveamount=1
            ratio = samount0/aveamount
            samounts = {'y2':samount2, 'y1':samount1, 'y0':samount0, 'ave':aveamount, 'ratio':ratio}
            monthlyamount0.append([genrecode, samounts])
            
            # 月ごとのカテゴリー計
            monthlycatamount2 = monthlycatamount2 + samount2
            monthlycatamount1 = monthlycatamount1 + samount1
            monthlycatamount0 = monthlycatamount0 + samount0
            
#             monthlycatamount[cat0] = monthlycatamount[cat0] + samount0
            # catごとの計
        monthlyamount[cat0] = monthlyamount0
        monthlycatamount[cat0] = [monthlycatamount0, monthlycatamount1, monthlycatamount2]
        
        monthlyallamount0 = monthlyallamount0 + monthlycatamount0
        monthlyallamount1 = monthlyallamount1 + monthlycatamount1
        monthlyallamount2 = monthlyallamount2 + monthlycatamount2
        # 月額出費の計
        
    return (monthlyallamount0, monthlyallamount1, monthlyallamount2), monthlyamount, (objDT0, objDT1, objDT2)


# In[110]:

# objYearMonth = (2016,9)
# (a,b,objYM) = get_genressummaly(objYearMonth)
# o = getBiggerAmountforReport(b)
def getBiggerAmountforReport(monthlyamounts, objYearMonth):
    c = [monthlyamounts[x] for x in monthlyamounts] 
    # get_genressummalyのmonthlyamountは階層構造になっているのでそれを解除
    f = []
    for d in c:
        for e in d:
            f.append(e)
    
    # 三ヶ月平均で最も大きかったの
    ratios = [g[1]['ratio'] for g in f] # genreの中からRatioだけ抜き出す
    sratios = sorted(ratios)
    t = -1
    m = sratios[t]
    i = ratios.index(m)

    while f[i][1]['y1']+f[i][1]['y2'] <= 1000 or f[i][1]['y0'] <= 3000:
        if f[i][1]['y0'] > 17500:
            break
        # 最小値判定を入れる
        # 先月 + 先々月 >= 1000 and 今月 > 3000
        t = t -1
        if sratios[t] < 2:
            t= t + 1
            break

        m = sratios[t]
        i = ratios.index(m)

    genre1 = f[i][0][1]
    genre1name = f[i][0][0]
#     print(f[i])
    text1 = "この3ヶ月に対し特に大きかった支出は{}です。平均の{}倍です。".format(genre1name, round(m*10)/10)
    text1 = "この3ヶ月に対し特に大きかった支出は<u>{}</u>です。前2ヶ月の平均{:,}円に対し今月は<u>{:,}円</u>です。".format(genre1name, 
                                                                round500(f[i][1]['ave']), round500(f[i][1]['y0']))


    # 三ヶ月平均に対し２倍のもの
    ratios2 = [g[1]['ratio'] for g in f if g[1]['ratio'] >= 2]
    ii = [ratios.index(r) for r in ratios2]

    if len(ii) >= 1:
        iitext = "と".join([f[i3][0][0]  for i3 in ii])
        iiratio = "それぞれ{}".format("と".join([str(round(i4*10)/10) for i4 in ii]))
    else:
        iitext = "ありません。"
        iiratio = "N/A"

    textdouble = "この三ヶ月に対して2倍以上の支出は<u>{}</u>です。比率は{}です".format(iitext, iiratio)
#     print(text01)


    # 特に大きかった支出一個で何%を占めるか
    amounts = [g[1]['y0'] for g in f] 
    if sum(amounts) == 0: #rev2.3
        return "まだ登録がありません", "", "", [""], "", "", ""
    amountratios = [r/sum(amounts) for r in amounts]
    sm = sorted(amountratios)
    m = sm[-1]
    i0 = amountratios.index(m)
    amountratio = round(m*100/5)*5
    if amountratio > 29:
        textratio = "特に大きかった支出は<u>{}</u>で、今月の支出の約<u>{}%</u>を占めます。".format(f[i0][0],amountratio)
    else:
        textratio = ''
        
    # 支出三つで何%をしめるか
    sms = sm[-1] + sm[-2] + sm[-3]
    amountratio = round(sms*100/5)*5
    i1 = amountratios.index(sm[-2])
    i2 = amountratios.index(sm[-3])
    
    textratio3 = """上位のジャンル3件は①<u>{g1}</u>({g1yen:,}千円), ②<u>{g2}</u>({g2yen:,}千円), ③<u>{g3}</u>({g3yen:,}千円)で計{gyen:,}千円。
<br>これらで今月の支出計の約<u>{gratio}%</u>を占めます。""".format(
        g1 = f[i0][0][0], g2 = f[i1][0][0], g3 = f[i2][0][0], 
        g1yen = round500(f[i0][1]['y0'])/1000,
        g2yen = round500(f[i1][1]['y0'])/1000,
        g3yen = round500(f[i2][1]['y0'])/1000,
        gyen = int((f[i0][1]['y0']+f[i1][1]['y0']+f[i2][1]['y0'])/1000),
        gratio = amountratio)

    # 支出5つで何%をしめるか
    sms5 = sm[-1] + sm[-2] + sm[-3] + sm[-4] + sm[-5]
    amountratio5 = round(sms5*100/5)*5
    i3 = amountratios.index(sm[-4])
    i4 = amountratios.index(sm[-5])

    textratio5 = """上位のジャンル5件は①<u>{g1}</u>({g1yen:,}千円), 
    ②<u>{g2}</u>({g2yen:,}千円), 
    ③<u>{g3}</u>({g3yen:,}千円),
    ④<u>{g4}</u>({g4yen:,}千円), 
    ⑤<u>{g5}</u>({g5yen:,}千円)で計{gyen:,}千円。
    <br>これらで今月の支出計の約<u>{gratio}%</u>を占めます。""".format(
        g1 = f[i0][0][0], g2 = f[i1][0][0], g3 = f[i2][0][0],  g4 = f[i3][0][0],  g5 = f[i4][0][0], 
        g1yen = round500(f[i0][1]['y0'])/1000,
        g2yen = round500(f[i1][1]['y0'])/1000,
        g3yen = round500(f[i2][1]['y0'])/1000,
        g4yen = round500(f[i3][1]['y0'])/1000,
        g5yen = round500(f[i4][1]['y0'])/1000,
        gyen = int((f[i0][1]['y0']+f[i1][1]['y0']+f[i2][1]['y0']+f[i3][1]['y0']+f[i4][1]['y0'])/1000),
        gratio = amountratio5)


    
    
    genreratio = f[i0][0][1]
    # text1genre = getBiggerAmountinGenreforReport(objYearMonth, genreratio)
    text1genre = getBiggerAmountinGenreforReport(objYearMonth, genre1)
    textdoublegenre = getBiggerAmountinGenreforReport(objYearMonth, genre1)



    return text1, textdouble, textratio, text1genre, textdoublegenre,textratio3, textratio5


# In[111]:

def getBiggerAmountinGenreforReport(objYearMonth, objGenres):

    m = select_GenreData(objYearMonth, objGenres, TH=0)
    g0 = [(n['amount'],n['date'], n['place']) for n in m]
    g1 = [n['amount'] for n in m]

    gr = [l/sum(g1) for l in g1]
    gm = max(gr)
    gi = gr.index(gm)
    xday = datetxt2class(g0[gi][1])
    if g0[gi][2] == '':
        place = m[gi]['name']
    else:
        place = g0[gi][2]+'での買い物'
#     g0[gi]
    textgenre = "このジャンル({})の中で特に大きい支出は{}日の{}で{:,}円です。ジャンルのうち{}%を占めます".format(
        m[0]['genre'],xday.day, place, round500(g0[gi][0]), round(gm*100/5)*5)

    # TOP3
    g2 = sorted(g1)
    if len(g2) > 3:
        indx1 = g1.index(g2[-1])
        indx2 = g1.index(g2[-2])
        indx3 = g1.index(g2[-3])
        gr = round(100*(sum(g2[-3:]) / sum(g2))) # TOP3で占める割合

        textgenretop3 = "このジャンルのTOP3は、1){}@{}日 {:,}円, 2){}@{}日 {:,}円, 3){}@{}日 {:,}円です。ジャンルのうち{}%を占めます".format(
        g0[indx1][2], datetxt2class(g0[indx1][1]).day, round500(g0[indx1][0]),
        g0[indx2][2], datetxt2class(g0[indx2][1]).day, round500(g0[indx2][0]),
        g0[indx3][2], datetxt2class(g0[indx3][1]).day, round500(g0[indx3][0]),
        gr)

    textgenretop3 = ''
    
    return textgenre, textgenretop3


# In[112]:


def getGenrescount(objYearMonth, objGenre):
    m0 = select_GenreData(objYearMonth, objGenre, TH=0)
    gcount0 = len([n['amount'] for n in m0])
    gsum0 = sum([n['amount'] for n in m0])

    return gcount0, gsum0, m0


# In[113]:

def getGenresdeltaforReport(objYM, obj):
    gcount0, gsum0, m0 = getGenrescount(objYM[0], obj)
    gcount1, gsum1, m1 = getGenrescount(objYM[1], obj)
    gcount2, gsum2, m2 = getGenrescount(objYM[1], obj)

    avesum = round500((gsum0 + gsum1 + gsum2)/3)
    avecount = round((gcount0 + gcount1 + gcount2)/3)

    otext = "平均{:,}円/{}件の支出のところ、今月は<u>{:,}円/{}件</u>でした。".format(
    avesum, avecount, round500(gsum0), gcount0)

    return otext

# 平均10件の支出が出費が今月は10件でした。



# In[114]:

def getRestaurantforReport(objYearMonth):

    #外食 件数と値段
    obj = [10103]
    gcount0, gsum0, m0 = getGenrescount(objYearMonth,  obj)
    objYearMonth1 = get_lastmonth(objYearMonth)
    gcount1, gsum1, m1 = getGenrescount(objYearMonth1, obj)


    countdelta  = gcount1 - gcount0 #先月件数-今月件数 (0より大きい：先月の方が多い=先月より減ってる )
    amountdelta = gsum1 - gsum0
    
    
    if countdelta > 0 and amountdelta > 0:
        textdelta = "先月から<u>{}件減</u>, {:,}円減です。".format(countdelta, round500(amountdelta))
    elif countdelta > 0 and amountdelta < 0:
        textdelta = "先月から<u>{}件減</u>, {:,}円増です。".format(countdelta, round500(abs(amountdelta)))
    elif countdelta < 0 and amountdelta > 0:
        textdelta = "先月から<u>{}件増</u>, {:,}円減です。".format(abs(countdelta), round500(amountdelta))
    elif countdelta < 0 and amountdelta < 0:
        textdelta = "先月から<u>{}件増</u>, {:,}円増です。".format(abs(countdelta), round500(abs(amountdelta)))

    elif countdelta == 0 and amountdelta > 0:
        textdelta = "先月と<u>同件数</u>, {:,}円減です。".format(round500(amountdelta))
    elif countdelta == 0 and amountdelta < 0:
        textdelta = "先月と<u>同件数</u>, {:,}円増です。".format(round500(abs(amountdelta)))
    elif countdelta > 0 and amountdelta == 0:
        textdelta = "先月から<u>{}件減</u>, 金額は同額です。".format(countdelta)
    elif countdelta < 0 and amountdelta == 0:
        textdelta = "先月から<u>{}件増</u>, 金額は同額です。".format(abs(countdelta))
    elif countdelta == 0 and amountdelta == 0:
        textdelta = "先月とは<u>同件数</u>, 同額です。"
 

    m1 = []
    for n in m0:
        m0t = {}
        m0t['day'] = datetxt2class(n['date']).day
        m0t['date'] = get_weekdayJP(datetxt2class(n['date']).strftime('%w'))

        m0t['place0'] = n['place']
        s = n['place'].split()
        v = ""
        for u in s:
            if (len(v) + len(u)) < 15:
                v = " ".join([v,u])
        m0t['place'] = v[1:]

        m1.append(m0t)




    gplace0 = "".join(["<li>{}@{}日({})</li>".format(n['place'], n['day'], n['date']) for n in m1])
    otext = """外食は<u>{}件/計{:,}円</u>。{}
    <br>
外食の場所は<ul>{}</ul>です。""".format(
        gcount0, round500(gsum0), textdelta, gplace0)

    return otext


# In[115]:

def getFoodforReport(objYearMonth):

    #外食 件数と値段
    obj = [10101, 10199, 11315234]
    #         {'name':'食費', 'code': [10101, 10199, 11315234], 'sname':'食費', 'catFP':'生活'}, # 食材, 生協, 子ども関係食材日用品
    #     {'name':'外食費', 'code':[10103], 'sname':'外食費', 'catFP':'生活'},
    #     {'name':'日用雑貨', 'code':[2890990], 'sname':'日用雑貨', 'catFP':'生活'},

    gcount0, gsum0, m0 = getGenrescount(objYearMonth,  obj)
    objYearMonth1 = get_lastmonth(objYearMonth)
    gcount1, gsum1, m1 = getGenrescount(objYearMonth1, obj)


    countdelta  = gcount1 - gcount0 #先月件数-今月件数 (0より大きい：先月の方が多い=先月より減ってる )
    amountdelta = gsum1 - gsum0
    
    
    if countdelta > 0 and amountdelta > 0:
        textdelta = "先月から<u>{}件減</u>, {:,}円減です。".format(countdelta, round500(amountdelta))
    elif countdelta > 0 and amountdelta < 0:
        textdelta = "先月から<u>{}件減</u>, {:,}円増です。".format(countdelta, round500(abs(amountdelta)))
    elif countdelta < 0 and amountdelta > 0:
        textdelta = "先月から<u>{}件増</u>, {:,}円減です。".format(abs(countdelta), round500(amountdelta))
    elif countdelta < 0 and amountdelta < 0:
        textdelta = "先月から<u>{}件増</u>, {:,}円増です。".format(abs(countdelta), round500(abs(amountdelta)))

    elif countdelta == 0 and amountdelta > 0:
        textdelta = "先月と<u>同件数</u>, {:,}円減です。".format(round500(amountdelta))
    elif countdelta == 0 and amountdelta < 0:
        textdelta = "先月と<u>同件数</u>, {:,}円増です。".format(round500(abs(amountdelta)))
    elif countdelta > 0 and amountdelta == 0:
        textdelta = "先月から<u>{}件減</u>, 金額は同額です。".format(countdelta)
    elif countdelta < 0 and amountdelta == 0:
        textdelta = "先月から<u>{}件増</u>, 金額は同額です。".format(abs(countdelta))
    elif countdelta == 0 and amountdelta == 0:
        textdelta = "先月とは<u>同件数</u>, 同額です。"
 
    otext = """食料品・生協は<u>{}件/計{:,}円</u>。{}
""".format(
        gcount0, round500(gsum0), textdelta)

    return otext



# In[116]:

datetxt2class = lambda txt:dt.strptime(txt,  '%Y-%m-%d')


# In[117]:

def getYearlyTatekae(objYearMonth):
    y = objYearMonth[0]
    m = objYearMonth[1]
    ms = [t for t in range(1,m+1)]

    mrin = []
    mout = []

    amountins = 0
    amountouts = 0

    amountint = 0
    amountoutt = 0


    for mm in ms:
        objDT = (y,mm)
        (m0rin, m0out) = get_monthlyRent(objDT)
        mrin.append(m0rin)
        mout.append(m0out)

        amountins = amountins + m0rin['sae']
        amountouts = amountouts + m0out['sae']

        amountint = amountint + m0rin['taka']
        amountoutt = amountoutt + m0out['taka']



    return (amountoutt - amountint, amountouts - amountins)


# In[118]:

def getCreditCardtextforReport(objYearMonth):

    AccountCreditCard = 7992077
    moneylist = select_fromAccount(objYearMonth,AccountCreditCard)

    num = len(set((x['date'],x['place']) for x in moneylist))
    ammount = sum([x['amount'] for x in moneylist])


    otext = """今月のクレジットカード支払いは{:,}円、{}件でした。""".format(
        round500(ammount), num)

    return otext


def getTatekaetextforReport(objYearMonth):
    objDT0 = objYearMonth 
    (m0rin, m0rout) = get_monthlyRent(objDT0)

    
    
    m0sumt = round500(m0rout['taka']-m0rin['taka'])
    m0sums = round500(m0rout['sae'] -m0rin['sae'])

    if m0sumt > 0:
        m0txtt = "差し引き<u>{:,}円の立替</u>です。".format(m0sumt)
    elif m0sumt < 0:
        m0txtt = "差し引き<u>{:,}円の精算</u>です。".format(abs(m0sumt))
    else:
        m0txtt = "今月分は精算済みです。"

    if m0sums > 0:
        m0txts = "差し引き<u>{:,}円の立替</u>です。".format(m0sums)
    elif m0sums < 0:
        m0txts = "差し引き<u>{:,}円の精算</u>です。".format(abs(m0sums))
    else:
        m0txts = "今月分は<u>精算済み</u>です。"

    (tatekaet,tatekaes) = getYearlyTatekae(objYearMonth)   
    yearlytatekae = "<br>今年の今月までのたかの立替は{:,}円, さえは{:,}円です。".format(round500(tatekaet), round500(tatekaes))
    if objYearMonth[1] ==1 :
        yearlytatekae = ""
      
        
    otext = """今月のたかの立替は{:,}円、精算は{:,}円でした。{}
    <br>さえの立替は{:,}円、精算は{:,}円、{}
    {}""".format(
        round500(m0rout['taka']), round500(m0rin['taka']), m0txtt,
        round500(m0rout['sae']),  round500(m0rin['sae']),  m0txts,
        yearlytatekae)

    return otext



# In[119]:

# 今月の総額は...円。先月に比べて...多いです。
def getMonthlydeltaforReport(objYearMonth):
    (monthlyamounts,b,objYM) = get_genressummaly(objYearMonth)
    t0 = monthlyamounts[0] # 今月
    t1 = monthlyamounts[1] 
    t2 = monthlyamounts[2]
    
    delta10 = t1 - t0
    avet = (t0 + t1 + t2)/3

    text0 = "今月の総額は<u>{:,}円</u>、".format(round500(t0))
    if(delta10 < 0):
        text1 = "先月に比べて<u>{:,}円高い</u>です。".format(round500(abs(delta10)))
    else:
        text1 = "先月に比べて<u>{:,}円安い</u>です。".format(round500(delta10))
    return text0 + text1


# In[120]:

def getReportText(objYearMonth):
    #objYearMonth = (2016,9)
    (a,b,objYM) = get_genressummaly(objYearMonth)
    textbig = getBiggerAmountforReport(b, objYearMonth)

    #     print(textbig[0])
#     print(textbig[1])
#     print(textbig[2])
#     print(textbig[3])
#     print(textbig[4])
#     print(textbig[5])

    textsyokuzai = getFoodforReport(objYearMonth)
    textgaisyoku = getRestaurantforReport(objYearMonth)
    texttatekae = getTatekaetextforReport(objYearMonth)
    textccard = getCreditCardtextforReport(objYearMonth)
    textsum = getMonthlydeltaforReport(objYearMonth)
    # print(o)
    obj = [10103]
    o = getGenresdeltaforReport(objYM, obj)
    # print()

    # print(o)
    reporttext = """<p>{tsum}</p>

    <p>{biggenre0}<br>
    {biguchiwake3}</p>

    <p>また、{big35}</p>
    <p>{tatekae}</p>
    <p>また、{ccard}</p>
    
    <p>{syokuzai}<br>
    また、{gaisyoku}</p>""".format(tsum=textsum, gaisyoku=textgaisyoku, tatekae=texttatekae,
                        biggenre0 = textbig[0], biguchiwake3 = textbig[3][0], big35 = textbig[6],
                                syokuzai = textsyokuzai, ccard = textccard
                       )



    #平均10件の支出が出費が今月は10件でした。
    # この三ヶ月の中で平均より特に低い費目は、「」です。
    # 先月10件の出費が今月は2件でした。
                  
    return reporttext



# # レポートテキスト出力はここまで
# getReportText(objYearMonth)

# In[121]:

def get_genrestable(objYearMonth):
    objDT0 = objYearMonth 
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)

    monthlyamount = {}
    monthlycatamount = {}
    genres =  detailgenres()
    #     zaimcat = genres.keys() => dict_keys(['食費•日用品', '公共・社会保障', '教育・教養', '変動費', '大型出費'])
    zaimcat = ['食費•日用品', '公共・社会保障', '資産形成','教育・教養', '変動費', '大型出費', '住まい'] #rev2.3

    monthlyallamount0 = 0
    monthlyallamount1 = 0
    monthlyallamount2 = 0
    
    for cat0 in zaimcat:
        monthlycatamount[cat0] = []
        monthlyamount0 = []
        monthlyamount[cat0] = []
        sumamounts = {}
        monthlycatamount0 = 0
        monthlycatamount1 = 0
        monthlycatamount2 = 0

        for genrecode in genres[cat0]:
            moneylist = select_GenreData(objDT2, genrecode[1])
            samount2 = round500(sum([x['amount'] for x in moneylist]))
            # 2ヶ月前のジャンルごとの合計金額

            moneylist = select_GenreData(objDT1, genrecode[1])
            samount1 = round500(sum([x['amount'] for x in moneylist]))
            # 1ヶ月前のジャンルごとの合計金額

            moneylist = select_GenreData(objDT0, genrecode[1])
            samount0 = round500(sum([x['amount'] for x in moneylist]))
            # 0ヶ月前のジャンルごとの合計金額

            samounts = {'y2':samount2, 'y1':samount1, 'y0':samount0}
            monthlyamount0.append([genrecode[0], samounts])
            
            # 月ごとのカテゴリー計
            monthlycatamount2 = monthlycatamount2 + samount2
            monthlycatamount1 = monthlycatamount1 + samount1
            monthlycatamount0 = monthlycatamount0 + samount0
            
#             monthlycatamount[cat0] = monthlycatamount[cat0] + samount0
            # catごとの計
        monthlyamount[cat0] = monthlyamount0
        monthlycatamount[cat0] = [monthlycatamount0, monthlycatamount1, monthlycatamount2]
        
        monthlyallamount0 = monthlyallamount0 + monthlycatamount0
        monthlyallamount1 = monthlyallamount1 + monthlycatamount1
        monthlyallamount2 = monthlyallamount2 + monthlycatamount2
        # 月額出費の計
        
        texts = []

    def cmpamount0(t0, t1, TH=1000):
        t = (int(t0) -int(t1))
        if t > TH:
            #cmpt = '<span class="glyphicon glyphicon-chevron-up text-danger" aria-hidden="true"></span>'
            cmpt = '<span class="label label-danger" style="padding:3px 4px;margin-left:1em;">(+)</span>'
        elif t < -TH:
            #cmpt = '<span class="glyphicon glyphicon-chevron-down text-info" aria-hidden="true"></span>'
            cmpt = '<span class="label label-primary" style="padding:3px 5px;margin-left:1em;">(-)</span>'
        else:
            cmpt = '<span class="label label-default" style="padding:3px 5px;margin-left:1em;">(0)</span>'
        return cmpt
    

    for cat0 in zaimcat:
        #sumyen = sum([x[1] for x in monthlyamount[cat0]])
        atext = """            <tr class="info">
                    <td>{cat}</td>
                    <td class="text-muted text-right small"><u>¥{catamount2:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{catamount1:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{catamount0:,}</u></td>
                </tr>""".format(cat = cat0, catamount0=monthlycatamount[cat0][0],
                               catamount1=monthlycatamount[cat0][1],catamount2=monthlycatamount[cat0][2])
        texts.append(atext)

        
        
        for item in monthlyamount[cat0]:

            atext = """\t\t\t\t<tr>
            \t\t\t\t\t<td style="padding-left:2em">{item}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen2:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen1:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen0:,}{badge}</td>
            \t\t\t\t</tr>""".format(item = item[0], 
                                    yen2 = item[1]['y2'], yen1 = item[1]['y1'], yen0 = item[1]['y0'],
                                   badge = cmpamount0(item[1]['y0'], item[1]['y1']))
            texts.append(atext)

    tablebody = '\n'.join(texts)

    textheader = """

    <!-- tablelist ここから-->

    <div class="panel panel-primary">
    \t<div class="panel-heading">{cat}</div>
    \t<div class ="table-responsive">
    \t\t<table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
    \t\t\t<thead>
    \t\t\t\t<tr>
    \t\t\t\t\t<th class="text-center">ジャンル</th>
    \t\t\t\t\t<th class="text-center">{m2}月 <span class="text-muted text-right small">¥{amount2:,}</span></th>
    \t\t\t\t\t<th class="text-center">{m1}月 <span class="text-muted text-right small">¥{amount1:,}</span></th>
    \t\t\t\t\t<th class="text-center">{m0}月 <span class="text-muted text-right small">¥{amount0:,}</span></th>
    \t\t\t\t</tr>
    \t\t\t</thead>
    \t\t\t<tbody>""".format(
        tableid="tablegenres", cat = "月度詳細",
        m2 = objDT2[1], m1 = objDT1[1], m0 = objDT0[1],
        amount2 = monthlyallamount2, amount1= monthlyallamount1, 
        amount0 = monthlyallamount0)

    textfooter = """
    \t\t\t</tbody>
    \t\t</table>
    \t</div>
    </div>
    <!-- tablelist ここまで-->"""
    
#     print(textheader)
#     for atext in texts:
#         print(atext)
#     print(textfooter)
    
    genretable = textheader + tablebody + textfooter
        
    return (textheader, tablebody, textfooter, genretable)


# In[ ]:




# In[ ]:




# In[122]:

def get_genrestableYear(objYear): # rev2.3
    objDT0 = (objYear,1)
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)

    monthlyamount = {}
    monthlycatamount = {}
    genres =  detailgenres()
    #     zaimcat = genres.keys() => dict_keys(['食費•日用品', '公共・社会保障', '教育・教養', '変動費', '大型出費'])
    zaimcat = ['食費•日用品', '公共・社会保障', '資産形成','教育・教養', '変動費', '大型出費', '住まい'] #rev2.3

    monthlyallamount0 = 0
    monthlyallamount1 = 0
    monthlyallamount2 = 0
    monthlyallamount3 = 0

    
    for cat0 in zaimcat:
        monthlycatamount[cat0] = []
        monthlyamount0 = []
        monthlyamount[cat0] = []
        sumamounts = {}
        monthlycatamount0 = 0
        monthlycatamount1 = 0
        monthlycatamount2 = 0
        monthlycatamount3 = 0

        
        for genrecode in genres[cat0]:
            qamount = []
            samountq0 = 0
            for mm in range(1,4):
                moneylist = select_GenreData((objYear, mm), genrecode[1])
                samountq0 += round500(sum([x['amount'] for x in moneylist]))

            qamount.append(samountq0)
            samountq0 = 0
            for mm in range(4,7):
                moneylist = select_GenreData((objYear, mm), genrecode[1])
                samountq0 += round500(sum([x['amount'] for x in moneylist]))

            qamount.append(samountq0)
            samountq0 = 0
            for mm in range(7,10):
                moneylist = select_GenreData((objYear, mm), genrecode[1])
                samountq0 += round500(sum([x['amount'] for x in moneylist]))

            qamount.append(samountq0)
            samountq0 = 0
            for mm in range(10,13):
                moneylist = select_GenreData((objYear, mm), genrecode[1])
                samountq0 += round500(sum([x['amount'] for x in moneylist]))

            qamount.append(samountq0)
            monthlyamount0.append([genrecode[0], qamount])
            
#             月ごとのカテゴリー計
            monthlycatamount0 = monthlycatamount0 + qamount[0]
            monthlycatamount1 = monthlycatamount1 + qamount[1]
            monthlycatamount2 = monthlycatamount2 + qamount[2]
            monthlycatamount3 = monthlycatamount3 + qamount[3]

            
            # catごとの計
        monthlyamount[cat0] = monthlyamount0
        monthlycatamount[cat0] = [monthlycatamount0, monthlycatamount1, monthlycatamount2, monthlycatamount3]
        
        monthlyallamount0 = monthlyallamount0 + monthlycatamount0
        monthlyallamount1 = monthlyallamount1 + monthlycatamount1
        monthlyallamount2 = monthlyallamount2 + monthlycatamount2
        monthlyallamount3 = monthlyallamount3 + monthlycatamount3
        # 月額出費の計
        
        texts = []
    

    for cat0 in zaimcat:
        #sumyen = sum([x[1] for x in monthlyamount[cat0]])
        atext = """            <tr class="info">
                    <td>{cat}</td>
                    <td class="text-muted text-right small"><u>¥{catamount0:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{catamount1:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{catamount2:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{catamount3:,}</u></td>
                </tr>""".format(cat = cat0, 
                                catamount0=monthlycatamount[cat0][0],
                                catamount1=monthlycatamount[cat0][1],
                                catamount2=monthlycatamount[cat0][2],
                               catamount3=monthlycatamount[cat0][3])
        texts.append(atext)

        
        
        for item in monthlyamount[cat0]:

            atext = """\t\t\t\t<tr>
            \t\t\t\t\t<td style="padding-left:2em">{item}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen0:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen1:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen2:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen3:,}</td>
            \t\t\t\t</tr>""".format(item = item[0], 
                                    yen0 = item[1][0], 
                                    yen1 = item[1][1], 
                                    yen2 = item[1][2],
                                    yen3 = item[1][3])
            texts.append(atext)

    tablebody = '\n'.join(texts)

    textheader = """

    <!-- tablelist ここから-->

    <div class="panel panel-primary">
    \t<div class="panel-heading">{cat}</div>
    \t<div class ="table-responsive">
    \t\t<table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
    \t\t\t<thead>
    \t\t\t\t<tr>
    \t\t\t\t\t<th class="text-center">ジャンル</th>
    \t\t\t\t\t<th class="text-center">Q1 <span class="text-muted text-right small">¥{amount0:,}</span></th>
    \t\t\t\t\t<th class="text-center">Q2 <span class="text-muted text-right small">¥{amount1:,}</span></th>
    \t\t\t\t\t<th class="text-center">Q3 <span class="text-muted text-right small">¥{amount2:,}</span></th>
    \t\t\t\t\t<th class="text-center">Q4 <span class="text-muted text-right small">¥{amount3:,}</span></th>
    \t\t\t\t</tr>
    \t\t\t</thead>
    \t\t\t<tbody>""".format(
        tableid="tablegenres", cat = "月度詳細",
        amount3 = monthlyallamount3, 
        amount2 = monthlyallamount2, 
        amount1 = monthlyallamount1, 
        amount0 = monthlyallamount0)

    textfooter = """
    \t\t\t</tbody>
    \t\t</table>
    \t</div>
    </div>
    <!-- tablelist ここまで-->"""
    
#     print(textheader)
#     for atext in texts:
#         print(atext)
#     print(textfooter)
    
    genretable = textheader + tablebody + textfooter
        
    return (textheader, tablebody, textfooter, genretable)


# In[ ]:




# In[ ]:




# In[123]:

def get_genressummarytable(objYearMonth):
    objDT0 = objYearMonth 
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)
    objDT3 = get_lastmonth(objDT2)


    monthlyamount = {}
    monthlycatamount = {}
    genres =  detailgenres()
    #     zaimcat = genres.keys() => dict_keys(['食費•日用品', '公共・社会保障', '教育・教養', '変動費', '大型出費'])
    zaimcat = ['食費•日用品', '公共・社会保障', '教育・教養', '変動費', '大型出費', '住まい']

    monthlyallamount0 = 0
    monthlyallamount1 = 0
    monthlyallamount2 = 0
    monthlyallamount3 = 0

    
    for cat0 in zaimcat:
        monthlycatamount[cat0] = []
        monthlyamount0 = []
        monthlyamount[cat0] = []
        sumamounts = {}
        monthlycatamount0 = 0
        monthlycatamount1 = 0
        monthlycatamount2 = 0
        monthlycatamount3 = 0


        for genrecode in genres[cat0]:
            moneylist = select_GenreData(objDT3, genrecode[1])
            samount3 = round500(sum([x['amount'] for x in moneylist]))
            # 3ヶ月前のジャンルごとの合計金額

            moneylist = select_GenreData(objDT2, genrecode[1])
            samount2 = round500(sum([x['amount'] for x in moneylist]))
            # 2ヶ月前のジャンルごとの合計金額

            moneylist = select_GenreData(objDT1, genrecode[1])
            samount1 = round500(sum([x['amount'] for x in moneylist]))
            # 1ヶ月前のジャンルごとの合計金額

            moneylist = select_GenreData(objDT0, genrecode[1])
            samount0 = round500(sum([x['amount'] for x in moneylist]))
            # 0ヶ月前のジャンルごとの合計金額

            ave = round500((samount3 + samount2 + samount1)/3)
            samounts = {'y3':samount3, 'y2':samount2, 'y1':samount1, 'y0':samount0, 'ave':ave}
            monthlyamount0.append([genrecode[0], samounts])
            
            # 月ごとのカテゴリー計
            monthlycatamount3 = monthlycatamount3 + samount2
            monthlycatamount2 = monthlycatamount2 + samount2
            monthlycatamount1 = monthlycatamount1 + samount1
            monthlycatamount0 = monthlycatamount0 + samount0
            
#             monthlycatamount[cat0] = monthlycatamount[cat0] + samount0
            # catごとの計
        monthlyamount[cat0] = monthlyamount0
        
        avea = round500((monthlycatamount3 + monthlycatamount2 + monthlycatamount1)/3)
        monthlycatamount[cat0] = [monthlycatamount0, monthlycatamount1, monthlycatamount2, monthlycatamount3, avea]
        
        monthlyallamount0 = monthlyallamount0 + monthlycatamount0
        monthlyallamount1 = monthlyallamount1 + monthlycatamount1
        monthlyallamount2 = monthlyallamount2 + monthlycatamount2
        monthlyallamount3 = monthlyallamount3 + monthlycatamount3
        # 月額出費の計
        
        texts = []

    def cmpamount0(t0, t1, TH=1000):
        t = (int(t0) -int(t1))
        if t > TH:
            #cmpt = '<span class="glyphicon glyphicon-chevron-up text-danger" aria-hidden="true"></span>'
            cmpt = '<span class="label label-danger" style="padding:3px 4px;margin-left:1em;">(+)</span>'
        elif t < -TH:
            #cmpt = '<span class="glyphicon glyphicon-chevron-down text-info" aria-hidden="true"></span>'
            cmpt = '<span class="label label-primary" style="padding:3px 5px;margin-left:1em;">(-)</span>'
        else:
            cmpt = '<span class="label label-default" style="padding:3px 5px;margin-left:1em;">(0)</span>'
        return cmpt
    

    for cat0 in zaimcat:
        #sumyen = sum([x[1] for x in monthlyamount[cat0]])
        atext = """            <tr class="info">
                    <td>{cat}</td>
                    <td class="text-muted text-right small"><u>¥{catamount2:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{catamount1:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{catamount0:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{catamount4:,}</u></td>
                </tr>""".format(cat = cat0, catamount0=monthlycatamount[cat0][0],
                               catamount1=monthlycatamount[cat0][1],catamount2=monthlycatamount[cat0][2],
                               catamount4=monthlycatamount[cat0][4])
        texts.append(atext)

        
        
        for item in monthlyamount[cat0]:

            atext = """\t\t\t\t<tr>
            \t\t\t\t\t<td style="padding-left:2em">{item}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen2:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen1:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen0:,}{badge}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen4:,}</td>
            \t\t\t\t</tr>""".format(item = item[0], 
                                    yen2 = item[1]['y2'], yen1 = item[1]['y1'], yen0 = item[1]['y0'],
                                   badge = cmpamount0(item[1]['y0'], item[1]['y1']),
                                   yen4 = item[1]['ave'])
            texts.append(atext)

    tablebody = '\n'.join(texts)

    monthlyallave = round500((monthlyallamount1 + monthlyallamount2 + monthlyallamount3 )/3)
    
    textheader = """

    <!-- tablelist ここから-->

    <div class="panel panel-primary">
    \t<div class="panel-heading">{cat}</div>
    \t<div class ="table-responsive">
    \t\t<table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
    \t\t\t<thead>
    \t\t\t\t<tr>
    \t\t\t\t\t<th class="text-center">ジャンル</th>
    \t\t\t\t\t<th class="text-center">{m2}月 <span class="text-muted text-right small">¥{amount2:,}</span></th>
    \t\t\t\t\t<th class="text-center">{m1}月 <span class="text-muted text-right small">¥{amount1:,}</span></th>
    \t\t\t\t\t<th class="text-center">{m0}月 <span class="text-muted text-right small">¥{amount0:,}</span></th>
    \t\t\t\t\t<th class="text-center">{m3}〜{m1}月の平均 <span class="text-muted text-right small">¥{amount4:,}</span></th>
    \t\t\t\t</tr>
    \t\t\t</thead>
    \t\t\t<tbody>""".format(
        tableid="tablegenres", cat = "月度詳細",
        m2 = objDT2[1], m1 = objDT1[1], m0 = objDT0[1],
        amount2 = monthlyallamount2, amount1= monthlyallamount1, 
        amount0 = monthlyallamount0, amount4 = monthlyallave,
        m3 = objDT3[1]
    )

    textfooter = """
    \t\t\t</tbody>
    \t\t</table>
    \t</div>
    </div>
    <!-- tablelist ここまで-->"""
    
#     print(textheader)
#     for atext in texts:
#         print(atext)
#     print(textfooter)
    
    genretable = textheader + tablebody + textfooter
        
    return (textheader, tablebody, textfooter, genretable)


# In[ ]:




# In[ ]:




# In[124]:

def get_kakuteishinkoku(objYear):
    #確定申告
    genres = detailgenres_kakuteishinkoku()
    moneylist = {}
    for genre in genres:
        genrecode = genre['code']
        moneylist[genre['name']] = []
        for mm in range(1,13):
            moneydata = select_GenreData((objYear, mm), genrecode)
            moneylist[genre['name']] += moneydata
    return moneylist



# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[125]:

def monthlyFP(objYearMonth):
    genres =  detailgenresFP()
    fpcatamount = {'生活':0, 'インフラ':0, 'その他':0, '住宅':0, '教育':0, '社会保障':0, '自動車':0, '資産形成':0}
    fpamounts = []

    for genre in genres:
        genrecode = genre['code']
        moneylist = select_GenreData(objYearMonth, genrecode)
        samount = round500(sum([x['amount'] for x in moneylist]))

        fpamounts.append({'amount':samount, 'name':genre['name'], 'catFP':genre['catFP'], 'sname':genre['sname']})
        fpcatamount[genre['catFP']] += samount
    
    return fpamounts, fpcatamount



# In[ ]:




# In[ ]:




# In[ ]:




# In[126]:

def get_YearlyFP(objYear):
    fpcategory = ['住宅', '生活', 'インフラ', '教育', '自動車', '社会保障','資産形成', 'その他']    

    # initialize
    cyen = {}
    for cat in fpcategory:
        cyen[cat] =[]
    (fp0, fpcat0) = monthlyFP((objYear,1))
    yen = {}
    catfp = {}
    sname = {}
    for fp in fp0:
        yen[fp['name']] = []
        catfp[fp['name']] = []
        name = fp['name']
        sname[fp['name']] = []
        cat = fp['catFP']
    fpsum = []
    
    # aiueo
    for mm in range(1,13):
        (fp0, fpcat0) = monthlyFP((objYear,mm))
        for fp in fp0:
            yen[fp['name']].append(fp['amount'])
            sname[fp['name']] = fp['sname']
            catfp[fp['name']] = fp['catFP']
        for cat in fpcategory:
            cyen[cat].append(fpcat0[cat])
        fpsum.append(sum([x['amount'] for x in fp0]))
    
    fp = []
    for key in [x['name'] for x in fp0]:# yen.keys():
        suma = sum(yen[key])
        ave = int(sum(yen[key])/len(yen[key]))
        name = key
        sname0 = sname[key]
        cat = catfp[key]
        fp.append({'name':name, 'yen':yen[key], 'ave':int(ave), 'sum':suma, 'catFP':cat, 'sname':sname0})
    
    fpcat = []
    
    for cat in fpcategory:
        cy = cyen[cat]
        suma = sum(cy)
        ave = int(sum(cy)/len(cy))
        fpcat.append({'catFP':cat, 'yen' : cy, 'ave' : ave, 'sum' : suma})
    
    return fp, fpcat, fpsum


# In[ ]:




# In[ ]:




# In[ ]:




# In[127]:

def get_yearly_FPtab_body(objYear):
    (fpamounts, fpcat, fpsum) = get_YearlyFP(objYear)

    texts = []
    for cat in fpcat:
        atext = """
                <tr class="info">
                    <td>{catFP}</td>
                    <td class="text-muted text-right small"><u>¥{cyen0:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen1:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen2:,}</u></td>

                    <td class="text-muted text-right small"><u>¥{cyen3:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen4:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen5:,}</u></td>

                    <td class="text-muted text-right small"><u>¥{cyen6:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen7:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen8:,}</u></td>

                    <td class="text-muted text-right small"><u>¥{cyen9:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen10:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen11:,}</u></td>

                    <td class="text-muted text-right small"><u><strong>¥{cyensum:,}</strong></u></td>
                    <td class="text-muted text-right small"><u>¥{cyenave:,}</u></td>
                </tr>""".format(catFP = cat['catFP'], 
                                cyen0=cat['yen'][0], cyen1 = cat['yen'][1], cyen2 = cat['yen'][2],
                                cyen3=cat['yen'][0], cyen4 = cat['yen'][1], cyen5 = cat['yen'][2],
                                cyen6=cat['yen'][0], cyen7 = cat['yen'][1], cyen8 = cat['yen'][2],
                                cyen9=cat['yen'][0], cyen10 = cat['yen'][1], cyen11 = cat['yen'][2],
                                cyenave = cat['ave'], cyensum = cat['sum'])
        texts.append(atext)



        for fp in fpamounts:
            if not fp['catFP'] == cat['catFP']:
                continue

            atext = """
            \t\t\t\t<tr>
            \t\t\t\t\t<td style="padding-left:2em">{item}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen0:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen1:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen2:,}</td>

            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen3:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen4:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen5:,}</td>

            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen6:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen7:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen8:,}</td>

            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen9:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen10:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yen11:,}</td>

            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em"><strong>¥{yensum:,}</strong></td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:.5em">¥{yenave:,}</td>
            \t\t\t\t</tr>""".format(item = fp['sname'], 
                                    yen0 = fp['yen'][0], yen1 = fp['yen'][1], yen2 = fp['yen'][2],
                                    yen3 = fp['yen'][3], yen4 = fp['yen'][4], yen5 = fp['yen'][5],
                                    yen6 = fp['yen'][6], yen7 = fp['yen'][7], yen8 = fp['yen'][8],
                                    yen9 = fp['yen'][9], yen10 = fp['yen'][10], yen11 = fp['yen'][11],
                                   yenave = fp['ave'], yensum = fp['sum'])
            texts.append(atext)

    tablebody = '\n'.join(texts)

    textheader = """

    <!-- tablelist ここから-->

    <div class="panel panel-primary">
    \t<div class="panel-heading">{cat}</div>
    \t<div class ="table-responsive">
    \t\t<table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
    \t\t\t<thead>
    \t\t\t\t<tr>
    \t\t\t\t\t<th class="text-center" style="min-width: 100px;">ジャンル</th>
    \t\t\t\t\t<th class="text-center">1月<br /><span class="text-muted text-right small">¥{amount0:,}</span></th>
    \t\t\t\t\t<th class="text-center">2月<br /><span class="text-muted text-right small">¥{amount1:,}</span></th>
    \t\t\t\t\t<th class="text-center">3月<br /><span class="text-muted text-right small">¥{amount2:,}</span></th>

    \t\t\t\t\t<th class="text-center">4月<br /><span class="text-muted text-right small">¥{amount3:,}</span></th>
    \t\t\t\t\t<th class="text-center">5月<br /><span class="text-muted text-right small">¥{amount4:,}</span></th>
    \t\t\t\t\t<th class="text-center">6月<br /><span class="text-muted text-right small">¥{amount5:,}</span></th>

    \t\t\t\t\t<th class="text-center">7月<br /><span class="text-muted text-right small">¥{amount6:,}</span></th>
    \t\t\t\t\t<th class="text-center">8月<br /><span class="text-muted text-right small">¥{amount7:,}</span></th>
    \t\t\t\t\t<th class="text-center">9月<br /><span class="text-muted text-right small">¥{amount8:,}</span></th>

    \t\t\t\t\t<th class="text-center">10月<br /><span class="text-muted text-right small">¥{amount9:,}</span></th>
    \t\t\t\t\t<th class="text-center">11月<br /><span class="text-muted text-right small">¥{amount10:,}</span></th>
    \t\t\t\t\t<th class="text-center">12月<br /><span class="text-muted text-right small">¥{amount11:,}</span></th>

    \t\t\t\t\t<th class="text-center"><strong>合計</strong><br /><span class="text-muted text-right small">¥{sum:,}</span></th>
    \t\t\t\t\t<th class="text-center">平均 <span class="text-muted text-right small">¥{ave:,}</span></th>

    \t\t\t\t</tr>
    \t\t\t</thead>
    \t\t\t<tbody>""".format(
        tableid="tablegenres", cat = "月度詳細(FP)",
        amount0 = fpsum[0], amount1 = fpsum[1], amount2 = fpsum[2], 
        amount3 = fpsum[3], amount4 = fpsum[4], amount5 = fpsum[5], 
        amount6 = fpsum[6], amount7 = fpsum[7], amount8 = fpsum[8], 
        amount9 = fpsum[9], amount10 = fpsum[10], amount11 = fpsum[11], 
        ave = int(sum(fpsum)/12), sum = sum(fpsum)
    )

    textfooter = """
    \t\t\t</tbody>
    \t\t</table>
    \t</div>
    </div>
    <!-- tablelist ここまで-->"""


    genretable = textheader + tablebody + textfooter
    return genretable






# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[128]:

def get3monthesFP(objYearMonth):
    objDT0 = objYearMonth 
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)
    objDT3 = get_lastmonth(objDT2)


    (fp0, fpcat0) = monthlyFP(objDT0)
    (fp1, fpcat1) = monthlyFP(objDT1)
    (fp2, fpcat2) = monthlyFP(objDT2)
    (fp3, fpcat3) = monthlyFP(objDT3)

    fp = []
    for ind in range(0,len(fp0)):
        name = fp0[ind]['name']
        cat = fp0[ind]['catFP']
        amount = [fp0[ind]['amount'], fp1[ind]['amount'], fp2[ind]['amount']]
        suma = sum([fp1[ind]['amount'], fp2[ind]['amount'], fp3[ind]['amount']]) #前３ヶ月
        ave = suma/3
        month = [objDT0, objDT1, objDT2]
        fp.append({'name':name, 'yen':amount, 'ave':int(ave), 'sum':suma, 'catFP':cat, 'month':month})
        

    fpcategory = ['住宅', '生活', 'インフラ', '教育', '自動車', '社会保障','資産形成', 'その他']    
    fpcat = []
    
    for cat in fpcategory:
        yen = [fpcat0[cat], fpcat1[cat], fpcat2[cat]]
        yen1 = [fpcat1[cat], fpcat2[cat], fpcat3[cat]]
        fpcat.append({'catFP':cat, 'yen' : yen, 'ave' : int(sum(yen1)/3), 'sum' : sum(yen1)})
    
    sum0 = sum([x['amount'] for x in fp0])
    sum1 = sum([x['amount'] for x in fp1])
    sum2 = sum([x['amount'] for x in fp2])
    sum3 = sum([x['amount'] for x in fp3])
    ave0 = int((sum1+sum2+sum3)/3)
    fpsum = [sum0, sum1, sum2, ave0]
    return fp, fpcat, fpsum
        
        



# In[129]:

import json


# In[130]:

# f = open('test.json', 'r')
# jsonData = json.load(f)
# f.close()


# In[ ]:




# In[ ]:




# In[131]:

# jsonData


# In[132]:


def getLoanText(loandata,year):

    name = ""
    income = ""
    balance = ""

    for x in loandata:
        t0 = """\t\t\t\t\t\t\t<th class="text-center"><a style="color:#fff;">{}</a></th>\n""".format(x['name'])
        name += t0

        t1 = """\t\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['input'])
        income += t1

        t2 = """\t\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['balance'])
        balance += t2

    name += """\t\t\t\t\t\t\t<th class="text-center"><a style="color:#fff;"><strong>小計</strong></a></th>\n"""
    income += """\t\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(sum([x[year]['input'] for x in loandata]))
    balance += """\t\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(sum([x[year]['balance'] for x in loandata]))


    return name, income, balance


def getLoanTable(moneydata,year):
    t = getLoanText(moneydata,str(year))

    thead = """    <!-- #### 金融report ここから #### -->
        <div class="panel panel-primary">
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed">
                    <thead class="bg-primary">
                        <tr>
                            <th class="text-center">{title}</th>\n""".format(title="負債")

    tbody_input = """                    \t</tr>
                    </thead>
                    <tbody class="text-center">
                        <tr>
                            <th class="text-center">入金</th>\n"""

    tbody_balance = """                    \t</tr>    

                    <tfoot class="bg-info">
                        <tr class="text-center" style="font-weight:bold;">
                            <th class="text-center">残高</th>\n"""

    tfooter = """                    \t</tr>
                    </tfoot>
                </table>
            </div>
        </div>

    <!-- #### 金融report ここまで #### -->\n"""
    
    return thead + t[0] + tbody_input + t[1] + tbody_balance + t[2] + tfooter 



# moneydata = [x for x in jsonData if x['type'] == 'loan']
# t = getLoanTable(moneydata)

# print(t)


# In[133]:


def getSavingsText(savingsdata,year):

    name = ""
    income = ""
    outcome = ""
    delta = ""
    balance = ""

    for x in savingsdata:
        t0 = """\t\t\t\t\t\t<th class="text-center"><a style="color:#fff;">{}</a></th>\n""".format(x['name'])
        name += t0

        t1 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['input'])
        income += t1

        t2 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['output'])
        outcome += t2

        t3 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['input'] - x[year]['output'])
        delta += t3

        t4 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['balance'])
        balance += t4

    incomes = sum([x[year]['input'] for x in savingsdata])
    outcomes = sum([x[year]['output'] for x in savingsdata])
    
    name += """\t\t\t\t\t\t<th class="text-center"><a style="color:#fff;"><strong>小計</strong></a></th>\n"""
    income += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(incomes)
    outcome += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(outcomes)
    delta += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(incomes - outcomes)
    balance += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(sum([x[year]['balance'] for x in savingsdata]))

    return name, income, outcome, delta, balance



def getSavingsTable(moneydata,year):
    t = getSavingsText(moneydata,str(year))

    thead = """    <!-- #### 金融report ここから #### -->
        <div class="panel panel-primary">
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed">
                    <thead class="bg-primary">
                        <tr>
                            <th class="text-center">{title}</th>\n""".format(title="預金")

    
    tbody_input = """                    \t</tr>
                    </thead>
                    <tbody class="text-center">
                        <tr>
                            <th class="text-center">{}</th>\n""".format("入金")


    tbody_output = """                    \t</tr>    
                    <tr>
                        <th class="text-center">{}</th>\n""".format("出金")

    tbody_delta = """                    \t</tr>    

                    <tr>
                        <th class="text-center">{}</th>\n""".format("Δ")
    
    tbody_balance = """                    \t</tr>    

                <tfoot class="bg-info">
                    <tr class="text-center" style="font-weight:bold;">
                        <th class="text-center">{}</th>\n""".format("残高")


    tfooter = """                    \t</tr>
                    </tfoot>
                </table>
            </div>
        </div>

    <!-- #### 金融report ここまで #### -->\n"""
    
    return thead + t[0] + tbody_input + t[1] + tbody_output + t[2] + tbody_delta + t[3] + tbody_balance + t[4] + tfooter 



# moneydata = [x for x in jsonData if x['type'] == 'savings']
# t = getSavingsTable(moneydata)

# print(t)





# In[134]:

#  'name': '確定拠出(た)',
#   'type': 'investmentdetail'},
#  {'2010': {'balance': 141990, 'input': 0, 'output': 0},
#   '2011': {'balance': 89687, 'input': 0, 'output': 0},
#   '2012': {'balance': 29487, 'input': 0, 'output': 0},
#   '2013': {'balance': 129450, 'input': 0, 'output': 0},
#   '2014': {'balance': 169576, 'input': 0, 'output': 0},
#   '2015': {'balance': 135799, 'input': 0, 'output': 0},
#   '2016': {'balance': 135557, 'input': 0, 'output': 0},


def getInvestmentsText(investmentdata,year):

    name = ""
    income = ""
    outcome = ""
    delta = ""
    balance = ""
    value = ""

    for x in investmentdata:
        t0 = """\t\t\t\t\t\t<th class="text-center"><a style="color:#fff;">{}</a></th>\n""".format(x['name'])
        name += t0

        t1 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['input'])
        income += t1

        t2 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['output'])
        outcome += t2

        t3 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['input'] - x[year]['output'])
        delta += t3

        t4 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['balance'])
        balance += t4

        t5 = """\t\t\t\t\t\t<td>¥{:,}</td>\n""".format(x[year]['value'])
        value += t5


    incomes = sum([x[year]['input'] for x in investmentdata])
    outcomes = sum([x[year]['output'] for x in investmentdata])
    
    name += """\t\t\t\t\t\t<th class="text-center"><a style="color:#fff;"><strong>小計</strong></a></th>\n"""
    income += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(incomes)
    outcome += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(outcomes)
    delta += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(incomes - outcomes)
    balance += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(sum([x[year]['balance'] for x in investmentdata]))
    value += """\t\t\t\t\t\t<th class="text-center">¥{:,}</th>\n""".format(sum([x[year]['value'] for x in investmentdata]))


    return name, income, outcome, delta, balance, value




def getInvestmentsTable(moneydata,year):
    t = getInvestmentsText(moneydata,str(year))
    

    thead = """    <!-- #### 金融report ここから #### -->
        <div class="panel panel-primary">
            <div class ="table-responsive">
                <table class="table table-striped table-bordered table-hover table-condensed">
                    <thead class="bg-primary">
                        <tr>
                            <th class="text-center">{title}</th>\n""".format(title="投資・保険")

    
    tbody_input = """                    \t</tr>
                    </thead>
                    <tbody class="text-center">
                        <tr>
                            <th class="text-center">{}</th>\n""".format("入金")


    tbody_output = """                    \t</tr>    
                    <tr>
                        <th class="text-center">{}</th>\n""".format("出金")

    tbody_delta = """                    \t</tr>    

                    <tr>
                        <th class="text-center">{}</th>\n""".format("Δ")
    
    tbody_balance = """                    \t</tr>    

                <tfoot class="bg-info">
                    <tr class="text-center" style="font-weight:bold;">
                        <th class="text-center">{}</th>\n""".format("残高")

    tbody_value = """                    \t</tr>    

                <tfoot class="bg-info">
                    <tr class="text-center" style="font-weight:bold;">
                        <th class="text-center">{}</th>\n""".format("評価額")


    
    tfooter = """                    \t</tr>
                    </tfoot>
                </table>
            </div>
        </div>

    <!-- #### 金融report ここまで #### -->\n"""
    
    return thead + t[0] + tbody_input + t[1] + tbody_output + t[2] + tbody_delta + t[3] + tbody_balance + t[4] +tbody_value + t[5] + tfooter 





# year = '2016'
# moneydata = [x for x in jsonData if x['type'] == 'investment']
# t = getInvestmentsTable(moneydata, '2011')
# print(t)








# In[135]:

# year = '2016'
# moneydata = [x for x in jsonData if x['type'] == 'investment']
# investmentsTable = getInvestmentsTable(moneydata)

# moneydata = [x for x in jsonData if x['type'] == 'savings']
# savingsTable = getSavingsTable(moneydata)

# moneydata = [x for x in jsonData if x['type'] == 'loan']
# loanTable = getLoanTable(moneydata)



# In[ ]:




# In[137]:

def get_yearly_moneyreporttab_body(objYear):
    #REV2.4 とりあえず
    f = open('test.json', 'r')
    jsonData = json.load(f)
    f.close()
    #REV2.4 とりあえず
    
    
    moneydata = [x for x in jsonData if x['type'] == 'investment']
    investmentsTable = getInvestmentsTable(moneydata, objYear)

    moneydata = [x for x in jsonData if x['type'] == 'savings']
    savingsTable = getSavingsTable(moneydata, objYear)

    moneydata = [x for x in jsonData if x['type'] == 'loan']
    loanTable = getLoanTable(moneydata, objYear)
    
    table = savingsTable + loanTable + investmentsTable

    return table







# In[ ]:




# In[ ]:




# In[138]:

def get_genressummarytableFP(objYearMonth):
    objDT0 = objYearMonth 
    objDT1 = get_lastmonth(objDT0)
    objDT2 = get_lastmonth(objDT1)
    objDT3 = get_lastmonth(objDT2)
    
    (fpamounts, fpcat, fpsum) = get3monthesFP(objDT0)

    texts = []


    for cat in fpcat:
        atext = """
                <tr class="info">
                    <td>{catFP}</td>
                    <td class="text-muted text-right small"><u>¥{cyen2:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen1:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyen0:,}</u></td>
                    <td class="text-muted text-right small"><u>¥{cyenave:,}</u></td>
                </tr>""".format(catFP = cat['catFP'], 
                                cyen0=cat['yen'][0], cyen1 = cat['yen'][1], cyen2 = cat['yen'][2],
                                cyenave = cat['ave'])
        texts.append(atext)



        for fp in fpamounts:
            if not fp['catFP'] == cat['catFP']:
                continue

            atext = """
            \t\t\t\t<tr>
            \t\t\t\t\t<td style="padding-left:2em">{item}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen2:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen1:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yen0:,}</td>
            \t\t\t\t\t\t<td class="text-right" style="padding-right:1em">¥{yenave:,}</td>
            \t\t\t\t</tr>""".format(item = fp['name'], 
                                    yen2 = fp['yen'][2], yen1 = fp['yen'][1], yen0 = fp['yen'][0],
                                   yenave = fp['ave'])
            texts.append(atext)

    tablebody = '\n'.join(texts)

    textheader = """

    <!-- tablelist ここから-->

    <div class="panel panel-primary">
    \t<div class="panel-heading">{cat}</div>
    \t<div class ="table-responsive">
    \t\t<table class="table table-striped table-bordered table-hover table-condensed" id="{tableid}">
    \t\t\t<thead>
    \t\t\t\t<tr>
    \t\t\t\t\t<th class="text-center">ジャンル</th>
    \t\t\t\t\t<th class="text-center">{m2}月 <span class="text-muted text-right small">¥{amount2:,}</span></th>
    \t\t\t\t\t<th class="text-center">{m1}月 <span class="text-muted text-right small">¥{amount1:,}</span></th>
    \t\t\t\t\t<th class="text-center">{m0}月 <span class="text-muted text-right small">¥{amount0:,}</span></th>
    \t\t\t\t\t<th class="text-center">{m3}〜{m1}月の平均 <span class="text-muted text-right small">¥{amount3:,}</span></th>
    \t\t\t\t</tr>
    \t\t\t</thead>
    \t\t\t<tbody>""".format(
        tableid="tablegenres", cat = "月度詳細",
        m2 = objDT2[1], m1 = objDT1[1], m0 = objDT0[1],
        amount2 = fpsum[2], 
        amount1 = fpsum[1], 
        amount0 = fpsum[0], 
        amount3 = fpsum[3],
        m3 = objDT3[1]
    )

    textfooter = """
    \t\t\t</tbody>
    \t\t</table>
    \t</div>
    </div>
    <!-- tablelist ここまで-->"""


    genretable = textheader + tablebody + textfooter
    return (textheader, tablebody, textfooter, genretable)


# In[ ]:




# In[139]:

def detailgenres_kakuteishinkoku():    
    # 確定申告
    t = [
        # 医療費/セルフメディケア
        {'name':'医療費(病院・薬局・移動)', 'code':[11406, 11001, 11002], 'cat':'', 'catFP':'生活'}, #妊娠, 病院代, 薬代

        
        # 生命保険
        {'name':'生命保険', 'code':[9991457, 9991527], 'cat':'', 'catFP':'社会保障'}, #生命保険
        
        # その他保険・年金
        {'name':'国民年金', 'code':[9991544], 'cat':'', 'catFP':'社会保障'}, #年金・国保
        {'name':'火災傷害保険', 'code':[11427650], 'cat':'', 'catFP':'社会保障'},
        {'name':'その他保険', 'code':[9991459, 9991538, 9991564, 10906], 'cat':'', 'catFP':'社会保障'}, #医療保険, 医療保険, 学資保険, 学資保険
        
        # 確定拠出/NISA
        {'name':'確定拠出年金', 'code':[13918135], 'cat':'', 'catFP':'資産形成'},

        
        # ふるさと納税
        {'name':'ふるさと納税', 'code':[9991553], 'cat':'', 'catFP':'社会保障'}, #住民税・所得税
    ]

    return t


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[140]:

def detailgenresFP():    
    t = [
    {'name':'食費', 'code': [10101, 10199, 11315234], 'sname':'食費', 'catFP':'生活'}, # 食材, 生協, 子ども関係食材日用品
    {'name':'外食費', 'code':[10103], 'sname':'外食費', 'catFP':'生活'},
    {'name':'日用雑貨', 'code':[2890990], 'sname':'日用雑貨', 'catFP':'生活'},

    {'name':'電気代', 'code':[10502], 'sname':'電気代', 'catFP':'インフラ'},
    {'name':'水道代', 'code':[10501], 'sname':'水道代', 'catFP':'インフラ'},
    {'name':'ガス代', 'code':[10503], 'sname':'ガス代', 'catFP':'インフラ'},
    {'name':'新聞/公文書', 'code':[10902,13918033], 'sname':'新聞他', 'catFP':'インフラ'},
    {'name':'固定通信費 (電話・パソコン・プロバイダ・NHK)', 'code':[2918017,2918020], 'sname':'固定通信/TV', 'catFP':'インフラ'}, #家インターネット, NHK
    {'name':'+ モバイル通信費', 'code':[2918018], 'sname':'+携帯通信', 'catFP':'インフラ'},
    
    {'name':'衣服費 (服・靴・クリーニング)', 'code':[11101,11102,11108], 'sname':'服飾', 'catFP':'生活'}, # 服飾 , アクセサリー・手芸関係, クリーニング
    {'name':'美容・理容', 'code':[11105], 'sname':'美容', 'catFP':'生活'}, # 美容院
    
    {'name':'医療・健康', 'code':[11001, 11002, 4566974, 11099], 'sname':'医療/健康', 'catFP':'生活'}, #病院代, 薬代, 運動, 衛生
    
    {'name':'教養娯楽費 (趣味・カルチャー)', 'code':[10806, 10903, 2918021,4562150], 'sname':'教育娯楽', 'catFP':'生活'}, # 書籍, 新聞, 参考書, 書籍, 博物館など
    {'name':'+習い事', 'code':[10901, 10904, 10905, 10907], 'sname':'+教育', 'catFP':'教育'}, #習い事, 受験, 学費, 塾, 学校
    {'name':'+シッターサービス', 'code':[11395977], 'sname':'+シッター', 'catFP':'教育'},


    {'name':'レジャー費', 'code':[10801, 10803, 10802, 11987674, 11940480], 'sname':'レジャー費', 'catFP':'生活'}, #レジャー, 映画・動画, イベント, 子供娯楽, 写真
    {'name':'交際費', 'code':[10701, 10702, 10703], 'sname':'交際費', 'catFP':'生活'}, #交際, プレゼント, 贈答
    {'name':'+交際費 (親族実家)', 'code':[2891006], 'sname':'+実家関係', 'catFP':'生活'}, #親族実家
    
    {'name':'お小遣い', 'code':[11657498], 'sname':'小遣い', 'catFP':'生活'},
    
    #rev2.3    {'name':'その他ローン', 'code':[999], 'sname':'各種ローン', 'catFP':'生活'},
    {'name':'その他ローン', 'code':[999, 9991569], 'sname':'ローン(奨学金)', 'catFP':'生活'},
    {'name':'その他支出', 'code':[999], 'sname':'その他支出', 'catFP':'生活'},
    
    {'name':'自動車関係', 'code':[999], 'sname':'自動車関係', 'catFP':'自動車'},
    
    {'name':'火災傷害保険', 'code':[11427650], 'sname':'火災傷害保', 'catFP':'社会保障'},
    {'name':'生命保険', 'code':[9991457, 9991527], 'sname':'生命保険', 'catFP':'社会保障'}, #生命保険
    {'name':'+その他保険', 'code':[9991459, 9991538, 9991564, 10906], 'sname':'+その他保険', 'catFP':'社会保障'}, #医療保険, 医療保険, 学資保険, 学資保険, その他
    {'name':'+年金・国保/住民税・所得税', 'code':[9991544, 9991553], 'sname':'+年金・税金', 'catFP':'社会保障'}, #年金・国保, 住民税・所得税
    #rev2.3
    #{'name':'+奨学金返済', 'code':[9991569], 'sname':'+奨学金', 'catFP':'資産形成'}, # 奨学金
    {'name':'貯金・積立', 'code':[13918146], 'sname':'貯金', 'catFP':'資産形成'},
    {'name':'投資(確定拠出)', 'code':[13918135], 'sname':'+確定拠出', 'catFP':'資産形成'},

        
    {'name':'家賃', 'code':[11427646], 'sname':'家賃', 'catFP':'住宅'},
    {'name':'住宅費関係 (固定資産税・管理費等)', 'code':[11402], 'sname':'住宅関係', 'catFP':'住宅'}, # 住宅
        

    # 以下は大型出費
    {'name':'旅行', 'code': [11401], 'sname':'+旅行', 'catFP':'その他'},
    {'name':'結婚/出産/介護', 'code': [11405, 11406, 11407], 'sname':'+結婚/出産', 'catFP':'その他'},
    {'name':'帰省・親族旅行', 'code': [12534806], 'sname':'+親族旅行', 'catFP':'その他'},
    {'name':'家具/家電', 'code': [10603, 11408, 10604, 11409, 10699], 'sname':'+家具/家電', 'catFP':'その他'} # 家具, 家具11408, 家電, 家電11409, その他
        ]

    return t


# In[141]:

def getZaimList(functype):
    # rev2.3
    if functype == 'cat':
        outputjsonfile = "list_categories.json"
        tfunc = select_CategoryDataNum
    elif functype == 'genre':
        outputjsonfile = "list_genres.json"
        tfunc = select_GenreDataNum
    elif functype == 'account':
        outputjsonfile = "list_accounts.json"
        tfunc = select_fromAccountNum


    f = open(outputjsonfile, "r")
    jdata = json.load(f)
    f.close()

    deletelist = []


    for x in jdata:
        cnt = tfunc([x])
        if cnt == 0:
            #print("{}:登録データなしなので削除リストに載せる".format(x))
            deletelist.append(x)


    catlist = []
    catlist0 = []
    catlist1 = []
    for data in jdata:
        if data not in deletelist:
            catlist.append(jdata[data][0]) # 名称
            catlist0.append(jdata[data])   # 名称とコード
            catlist1.append(data)          # コード

    return catlist,catlist0,catlist1

        #return catlist




# In[142]:

#rev2.3
# select_CategoryDataをSqlでgroupingからPythonでgroupingに変更するためにサブ関数
def select_CategoryDataNum(objCategory):

    select = """select amount
    from {tablename} 
    where category_id in ({cats})
    ;""".format(tablename = TABLE, cats=''.join(str(objCategory))[1:-1])    
    
    data = select_from_sqlite(select)
    return len(data)


# 対象になるジャンルリストを入力し、レシートリストから探索、出力する

def select_GenreDataNum(objGenre):
    select = """select amount 
    from {tablename} 
    where genre_id in ({cats})
    ;""".format(tablename = TABLE, cats=''.join(str(objGenre))[1:-1])

    data = select_from_sqlite(select)
    return len(data)

def select_fromAccountNum(from_Account):
    select = """select amount 
    from {tablename} 
    where from_account_id in ({from_account})
    ;""".format(tablename = TABLE, from_account=''.join(str(from_Account))[1:-1])
#    ;""".format(tablename = TABLE, from_account=from_Account)

    data = select_from_sqlite(select)
    return len(data)



# In[ ]:




# In[ ]:




# In[ ]:




# In[143]:

def detailgenres():
    t = {}
    # ('食費•日用品', 101),
    key = '食費•日用品'
    t[key] = [
        ['外食', [10103]],
        ['食料品/生協', [10101, 10199]],
        ['子供関係食費', [11315234]],
        ['日用品', [2890990]],
    ]


    # ('公共', 105),# ('社会保障', 25504225),
    key = '公共・社会保障'
    t[key] = [
        ['光熱費',[10501,10502,10503]],    # 電気ガス、水道
        ['TV/固定通信費',[2918017,2918020]],    #家インターネット, NHK
        ['モバイル通信費', [2918018]],
        ['生命/医療/学資保険', [9991457, 9991527, 9991459, 9991538, 9991564]],
        ['奨学金返済',[9991569]],
        ['年金・国保/住民税・所得税',  [9991544, 9991553]],
        ['公文書出力', [13918033]]
    ]

    key = '資産形成' #rev2.3
    t[key] = [
        ['投資, 確定拠出',[13918135]],
        ['貯金',[13918146]],
        ['子供貯金', [1111111]]
    ]

    # 変動費
    # ('積)住まい・家財', 106), ⇨家財
    # ('積)交際費', 107),
    # ('積)娯楽', 108),
    # ('積)医療・健康', 110) ,
    # (美容, 111)
    key = '変動費'
    t[key] = [
        ['交際/ご祝儀・贈答',[10701, 10702, 10703]],
        ['親族実家', [ 2891006]],
        ['レジャー/映画/写真/イベント/子供娯楽', [10801, 10803, 10802, 11987674,11940480]],
        ['病院代/薬代', [11001, 11002, 11099]],
        ['運動', [4566974]],
        ['服飾', [11101]],
        ['アクセサリー・手芸関係',[11102]],
        ['美容院/クリーニング',[11105, 11108]]
    ]

    # ('大型出費', 114),   
    key = '大型出費'
    t[key] = [
        ['旅行', [11401]],
        ['結婚/出産/介護', [11405, 11406, 11407]],
        ['住宅関係', [11402]],
        ['帰省・親族旅行', [12534806]]
    ]


    # ('積)教育・教養', 109), 変動⇨教育費
    key = '教育・教養'
    t[key] = [
        ['書籍/参考書', [10806, 10902, 10903, 2918021]],
        ['博物館、美術館', [4562150]],
        ['習い事/受験/学費/塾/学校', [10901, 10904, 10905, 10907]],
        ['学資保険', [10906]],
        ['シッターサービス',[11395977]],
        ['小遣い', [11657498]]
            ]
            
    key = '住まい'
    t[key] = [
            ['家賃', [11427646]],
            ['家具/家電', [10603, 10604, 10699]],
            ['火災傷害保険',[11427650]]
        ]

    return t


# In[ ]:




# In[ ]:




# In[ ]:




# In[144]:

def output_quarterly(objYear=2016):
    
    # ## HTML全体
    # + html_header() /変更なし
    # + html_footer() /変更なし

    # ## Report tab
    # + get_quarterly_reporttab_header(objYear) : 
    # + get_quartelyamounts_reporttab_body(objYear) : 表1
    # + get_yearlypublickfees_reporttab_body(objYear)  : 表2
    # + get_yearlyamounts_reporttab_body(objYear)  : 表3
    #get_yearlyrenttable
    # + get_quarterly_reporttab_footer(objYear) : 

    # ## Graph tab
    # + get_quarterly_graphtab_header() : 
    # + get_yearByquarterly_graphtab_body(objYear) : グラフ1a
    # + get_publicfeesbymonthly_graphtab_body(objYear) : グラフ2a
    # + get_yearBymonthly_graphtab_body(objYear) : グラフ3a
    # ++ get_yearByquarterlyR_graphtab_body(objYear) : グラフ1b
    # ++ get_publicfeesbymonthlyR_graphtab_body(objYear) : グラフ2b
    # ++ get_yearBymonthlyR_graphtab_body(objYear) : グラフ3b
    # + get_quarterly_graphtab_footer() : 

    # ## Detail tab
    # + get_quarterly_detailtab_header() : 
    # + get_quarterly_datailtab_footer() : 

    htmlheader = get_quarterly_htmlheader(objYear)
    htmlfooter = get_htmlfooter()

    rtab_header = get_quarterly_reporttab_header(objYear)
    rtab_body1 = get_quartelyamounts_reporttab_body(objYear)
    rtab_body3 = get_quarterlyrenttable(objYear)
    rtab_body2 = get_Quarterly_incomestable(objYear)
    rtab_footer = get_quarterly_reporttab_footer(objYear)
    
    mtab_header = get_quarterly_Mreporttab_header(objYear)
    rtab_body5 = get_yearmonthlyamounts_reporttab_body(objYear)
    rtab_body4 = get_yearlypublickfees_reporttab_body(objYear)
    rtab_body6 = get_yearmonthly_renttable(objYear)
    rtab_body7 = get_yearmonthly_incomestable(objYear)
    mtab_footer = get_quarterly_Mreporttab_footer(objYear)
    
    gtab_header = get_quarterly_graphtab_header(objYear)
    gtab_body1 = get_yearByquarterly_graphtab_body(objYear)
    gtab_body4 = get_yearByquarterlyR_graphtab_body(objYear)
    gtab_footer = get_quarterly_graphtab_footer(objYear) 

    gMtab_header = get_quarterly_Mgraphtab_header(objYear)
    gtab_body2 = get_publicfeesbymonthly_graphtab_body(objYear)
    gtab_body3 = get_yearBymonthly_graphtab_body(objYear)
    gtab_body5 = get_publicfeesbymonthlyR_graphtab_body(objYear)
    gtab_body6 = get_yearBymonthlyR_graphtab_body(objYear)
    gtab_body7 = get_restaurantnumbymonthly_graphtab_body(objYear)
    gMtab_footer = get_quarterly_Mgraphtab_footer(objYear) 

    
    dtab_header = get_quarterly_detailtab_header(objYear)
    dtab_body = get_quarterly_detailtab_body(objYear)
    dtab_footer = get_quarterly_detailtab_footer(objYear)

    
    KStab_header = get_yearly_KStab_header(objYear)
    KStab_body = get_yearly_KStab_body(objYear)
    KStab_footer = get_quarterly_detailtab_footer(objYear)
    
    FPtab_header = get_yearly_FPtab_header(objYear)
    FPtab_body = get_yearly_FPtab_body(objYear)
    FPtab_footer = get_quarterly_detailtab_footer(objYear)

    Stab_header = get_yearly_summarytab_header(objYear) #rev2.3
    Stab_body = get_yearly_summarytab_body(objYear) #rev2.3
    Stab_footer = get_quarterly_detailtab_footer(objYear) #rev2.3
    
    MRtab_header = get_yearly_moneyreporttab_header(objYear)
    MRtab_body = get_yearly_moneyreporttab_body(objYear)
    MRtab_footer = get_quarterly_detailtab_footer(objYear)


    
    filename = ("output/jade/y{}.html").format(objYear)
    f = open(filename, 'w') # 書き込みモードで開く
    f.write(htmlheader) # 引数の文字列をファイルに書き込む

    f.write(Stab_header) # rev2.3
    f.write(Stab_body)   # rev2.3
    f.write(Stab_footer) # rev2.3

    f.write(rtab_header) # 引数の文字列をファイルに書き込む
    f.write(rtab_body1) # 引数の文字列をファイルに書き込む
    f.write(rtab_body2) # 引数の文字列をファイルに書き込む
    f.write(rtab_body3) # 引数の文字列をファイルに書き込む
    f.write(rtab_footer) # 引数の文字列をファイルに書き込む

    f.write(mtab_header) # 引数の文字列をファイルに書き込む
    f.write(rtab_body5) # 引数の文字列をファイルに書き込む
    f.write(rtab_body4) # 引数の文字列をファイルに書き込む
    f.write(rtab_body6) # 引数の文字列をファイルに書き込む
    f.write(rtab_body7) # 引数の文字列をファイルに書き込む
    f.write(mtab_footer) # 引数の文字列をファイルに書き込む

    f.write(gtab_header) # 引数の文字列をファイルに書き込む
    f.write(gtab_body1) # 引数の文字列をファイルに書き込む
    f.write(gtab_body4) # 引数の文字列をファイルに書き込む
    f.write(gtab_footer) # 引数の文字列をファイルに書き込む

    f.write(gMtab_header) # 引数の文字列をファイルに書き込む
    f.write(gtab_body2) # 引数の文字列をファイルに書き込む
    f.write(gtab_body3) # 引数の文字列をファイルに書き込む
    f.write(gtab_body5) # 引数の文字列をファイルに書き込む
    f.write(gtab_body6) # 引数の文字列をファイルに書き込む
    f.write(gtab_body7) # 引数の文字列をファイルに書き込む
    f.write(gMtab_footer) # 引数の文字列をファイルに書き込む


    
    f.write(dtab_header) # 引数の文字列をファイルに書き込む
    f.write(dtab_body) # 引数の文字列をファイルに書き込む
    f.write(dtab_footer) # 引数の文字列をファイルに書き込む

    f.write(KStab_header) # 引数の文字列をファイルに書き込む
    f.write(KStab_body) # 引数の文字列をファイルに書き込む
    f.write(KStab_footer) # 引数の文字列をファイルに書き込む


    f.write(FPtab_header) # 引数の文字列をファイルに書き込む
    f.write(FPtab_body) # 引数の文字列をファイルに書き込む
    f.write(FPtab_footer) # 引数の文字列をファイルに書き込む

    f.write(MRtab_header) # 引数の文字列をファイルに書き込む
    f.write(MRtab_body) # 引数の文字列をファイルに書き込む
    f.write(MRtab_footer) # 引数の文字列をファイルに書き込む



    
    f.write(htmlfooter) # 引数の文字列をファイルに書き込む
    f.close() # ファイルを閉じる



# In[145]:

def output_yearly():
    
# + get_yearly_htmlheader()
# + html_footer()

# ## Report tab
# + get_yearly_reporttab_header(objYear) : 
# + get_yearlyamounts_reporttab_body(objYear) : 表1
# + get_yearly_reporttab_footer(objYear) : 

# ## Graph tab
# + get_quarterly_graphtab_header() : 
# + get_years_graphtab_body(objYear) : グラフ1a
# + get_quarterByyearly_graphtab_body(objYear) : グラフ2a
# + get_yearsR_graphtab_body(objYear) : グラフ1a
# + get_quarterly_graphtab_footer() : 

       
# ## Detail tab
# + get_yearly_detailtab_header() : 
# + get_yearly_datailtab_footer() : 

    htmlheader = get_yearly_htmlheader()
    htmlfooter = get_htmlfooter()

    rtab_header = get_yearly_reporttab_header()
    rtab_body1 = get_yearlyamounts_reporttab_body()
    rtab_body2 = get_Yearly_incomestable()
    rtab_body3 = get_yearlyrenttable()
    rtab_footer = get_yearly_reporttab_footer()
    
    gtab_header = get_yearly_graphtab_header()
    gtab_body1 = get_years_graphtab_body()
    gtab_body2 = get_quarterByyearly_graphtab_body()
    gtab_body3 = get_yearsR_graphtab_body()
    gtab_footer = get_yearly_graphtab_footer() 

    dtab_header = get_yearly_detailtab_header()
    dtab_body1 = get_yearlyamounts_stat_table()
    dtab_body2 = get_yearlyamounts_top5_table()
#     dtab_body
    dtab_footer = get_yearly_detailtab_footer()

    filename = ("output/jade/summary.html")
    f = open(filename, 'w') # 書き込みモードで開く
    f.write(htmlheader) # 引数の文字列をファイルに書き込む

    f.write(rtab_header) # 引数の文字列をファイルに書き込む
    f.write(rtab_body1) # 引数の文字列をファイルに書き込む
    f.write(rtab_body2) # 引数の文字列をファイルに書き込む
    f.write(rtab_body3) # 引数の文字列をファイルに書き込む
    f.write(rtab_footer) # 引数の文字列をファイルに書き込む

    f.write(gtab_header) # 引数の文字列をファイルに書き込む
    f.write(gtab_body1) # 引数の文字列をファイルに書き込む
    f.write(gtab_body2) # 引数の文字列をファイルに書き込む
    f.write(gtab_body3) # 引数の文字列をファイルに書き込む
    f.write(gtab_footer) # 引数の文字列をファイルに書き込む

    f.write(dtab_header) # 引数の文字列をファイルに書き込む
    f.write(dtab_body1) # 引数の文字列をファイルに書き込む
    f.write(dtab_body2) # 引数の文字列をファイルに書き込む
    f.write(dtab_footer) # 引数の文字列をファイルに書き込む


    f.write(htmlfooter) # 引数の文字列をファイルに書き込む
    f.close() # ファイルを閉じる




# # 全部のまとめレポート
# ## module定義
# import dt
# import datetime
# round500
# get_monthlyamount
# select_CategoryData
# select_RawCategoryData
# select_Wholedata
# TABLE, sqlite3
# select_from_sqlite
# 
# ## HTML全体
# 
# + get_yearly_htmlheader()
# + html_footer()
# 
# ## Report tab
# 表1. 1年ごとの支出
# 
# + get_yearly_reporttab_header(objYear) : 
# + get_yearlyamounts_reporttab_body(objYear) : 表1
# + get_yearly_reporttab_footer(objYear) : 
# 
# ## Graph tab
# グラフ1a. 年ごとの支出推移
# グラフ2a. 四半期ごとにまとめた年ごとの支出推移
# グラフ1b. 年ごとの支出率推移
# グラフ2b. 四半期ごとにまとめた年ごとの支出率推移
# 
# 
# + get_yearly_graphtab_header() : 
# + get_years_graphtab_body(objYear) : グラフ1a
# + get_quarterByyearly_graphtab_body(objYear) : グラフ2a
# + get_yearsR_graphtab_body(objYear) : グラフ1a
# + get_yearly_graphtab_footer() : 
# 
#        
# ## Detail tab
# 保留
# + get_yearly_detailtab_header() : 
# + N/A
# + get_yearly_datailtab_footer() : 

# In[146]:

def get_yearly_reporttab_header ():
    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### report tab ここから ### -->
      <div class="tab-pane" id="report">
        <div class="col-sm-1 hidden-xs"></div>
        <div class="col-sm-10 col-xs-12">

    """
    return headertext

def get_yearly_reporttab_footer():
    footertext = """
        </div>
        <div class="col-sm-1 hidden-xs"></div>
      </div>
      <!-- ### report tab ここまで ### -->
      """
    return footertext


# In[147]:

def get_yearly_graphtab_header():
    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### graph tab ここから ### -->
      <div class="tab-pane" id="graph">
        <div class="col-sm-1 hidden-xs"></div>
        <div class="col-sm-10 col-xs-12">
      """
    return headertext

def get_yearly_graphtab_footer():
    footertext = """
        </div>
        <div class="col-sm-1 hidden-xs"></div>
      </div>
      <!-- ### graph tab ここまで ### -->
      """
    return footertext

#get_graphtabfooter((objYear,objMonth))


# In[148]:

def get_yearly_detailtab_header ():
    headertext = """
      <!-- ################## tab ################## -->
      <!-- ### 詳細 tab ここから ### -->
        <div class="tab-pane" id="moneylist">

          <div class = "row">
            <div class="col-sm-2 hidden-xs">
              <ul class="list-group">
                <li class="list-group-item"><a href="#table1">変動費</a></li>
                <li class="list-group-item"><a href="#table2">教育・書籍</a></li>
                <li class="list-group-item"><a href="#table3">大型出費</a></li>
                <li class="list-group-item"><a href="#table4">外食</a></li>
                <li class="list-group-item"><a href="#table5">公共料金</a></li>
              </ul>
            </div>
            <div class="col-sm-10 col-xs-12" >
    """
    return headertext

def get_yearly_detailtab_footer():
    footertext = """
        </div>
      </div>
    </div>
    <!-- ### 詳細 tab ここまで ### -->
      """
    return footertext


# In[149]:

def get_yearly_htmlheader():
    headertext1 = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <meta name="robots" content="noarchive">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <title>Garnet Reports (ZAIM)</title>

  <!-- Bootstrap -->
  <link href="css/bootstrap.min.css" rel="stylesheet">

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="./dist/Chart.min.js"></script>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="js/bootstrap.min.js"></script>

  <!-- jQ-Cookie -->
  <script src="js/jquery.cookie.js"></script>
  
  <script type="text/javascript">
  $(function() {
    function clearTabFunc(){
      console.log("clear tab");
      $('a[data-toggle="tab"]').parent().removeClass('active');
    }

    function readTabFunc(){
      activeTab = $.cookie("TactiveTabName");
      if (activeTab == null) {
        activeTab = "Yreport";
        console.log("no tab in cookie");
        $.cookie("TactiveTabName",activeTab, { expires: 700 });
        console.log("set cookie as TactiveTabName");
      }
      setTabActive();
    }

    function setTabActive(){
      console.log("set tab active:"+activeTab)
      activeTab0 = activeTab.substr(1) ;
      $('a[href=#' + activeTab0 +']').parent().addClass('active');
      $('#' + activeTab0).addClass('active');
    }

    $(function(){
      console.log("start")
      clearTabFunc();
      readTabFunc();
    
      $("#reporttab").click(function(){
        console.log("report tab activated");
        activeTab = "Yreport";
        $.cookie("TactiveTabName",activeTab, { expires: 700 });
      });

      $("#graphtab").click(function(){
        console.log("graph tab activated");
        activeTab = "Ygraph";
        $.cookie("TactiveTabName",activeTab, { expires: 700 });
      });

      $("#detailtab").click(function(){
        console.log("detail tab activated");
        activeTab = "Ymoneylist";
        $.cookie("TactiveTabName",activeTab, { expires: 700 });
      });

    });
  });

  </script>
  <!-- jQ-Cookie -->

  <style>
  canvas{
      -moz-user-select: none;
      -webkit-user-select: none;
      -ms-user-select: none;
      border:solid 1px #ddf;
  }
  </style>

</head>
<body>
  <div id="header" class="container" style="margin:30px"></div>
  <nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="navbar-header">
      <button class="navbar-toggle" data-toggle="collapse" data-target=".target">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a href="./index.html" class="navbar-brand">Garnet</a>
    </div>

    <div class="collapse navbar-collapse target">
      <ul class="nav navbar-nav">
      """
    
    headertext2 = """
        <li><a href="./m{}-{:02}.html">Monthly Report</a></li>
        <li><a href="./y{}.html">Yearly Report</a></li>
        <li class="active"><a href="">Total Report</a></li>
        """.format(dt.now().year,dt.now().month,dt.now().year)
    
    headertext3 = """
      </ul>
    </div>
  </nav>

  <div class="container" style="padding:20px 0">
        <a href="./i/summary.html">iPhone版はこちら</a>
    <ul class="nav nav-tabs" style="margin:20px 0">
      <li id="reporttab" class="active"><a href="#report" data-toggle="tab">レポート</a></li>
      <li id="graphtab"><a href="#graph" data-toggle="tab">グラフ</a></li>
      <li id="detailtab"><a href="#moneylist" data-toggle="tab">出費詳細</a></li>
  </ul>

    <div class="tab-content">
"""
    return headertext1+headertext2+headertext3



# In[150]:

def get_objYearRange():
    yearfrom = 2011
    yearto = dt.now().year+1  
    return (yearfrom,yearto)


# In[151]:

def get_years_graphtab_body():
    (yearfrom,yearto) = get_objYearRange()
    graphtitle = "年のごとの推移"
    
    monthlyamounts = []
    for objYear in range(yearfrom,yearto):
        monthlyamounts.append(get_yearly_amount(objYear))
    qdata = {}
    count = 0
    for key in monthlyamounts[0].keys():
        qdata[key] = [x[key] for x in monthlyamounts]
        count = count+1
    xticklabels = ', '.join(['"{}年"'.format(x) for x in range(yearfrom,yearto)])
    qdata['公共'] = [x['光熱費']+x['社会保障']+x['通信費'] for x in monthlyamounts]

#                <div style="width:100%;">
    graphbodyheader = """
                <div>
                    <canvas id="myChartY"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = [{xticklabels}];
                    var data1 = {data_hendo};
                    var data2 = {data_chika};
                    var data3 = {data_seikatsu};
                    var data4 = {data_kokyo};
                    var data5 = {data_ogata};
                  """.format(graphtitle = graphtitle,
                             xticklabels = xticklabels,
                             data_hendo = qdata['変動費'], 
                             data_chika = qdata['教育・養育'], 
                             data_seikatsu = qdata['食費'],
                             data_kokyo = qdata['公共'],
                             data_ogata = qdata['大型出費'])
    
    graphbodybody2 = """
                    var  label1 = "変動費";
                    var  label2 = "養育費";
                    var  label3 = "生活費";
                    var  label4 = "公共料金";
                    var  label5 = "大型出費";


                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(48,255,192,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,132,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(132,99,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                        stacked: true
                                }],
                                yAxes: [{
                                        stacked: true,
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 25000,
                                    userCallback: function(value, index, values) {
                                      return "¥" + value.toLocaleString();
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ¥' + tooltipItem.yLabel.toLocaleString();
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChartY");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[152]:

def get_yearsR_graphtab_body():
    (yearfrom,yearto) = get_objYearRange()
    graphtitle = "年のごとの推移"
    
    monthlyamounts = []
    for objYear in range(yearfrom,yearto):
        t = get_yearly_amount(objYear)
        if not t['all'] == 0:
            sr = {k:int(v/t['all']*100*10)/10 for k,v in t.items()}
        monthlyamounts.append(sr)

    qdata = {}
    for key in monthlyamounts[0].keys():
        qdata[key] = [x[key] for x in monthlyamounts]
    xticklabels = ', '.join(['"{}年"'.format(x) for x in range(yearfrom,yearto)])
    qdata['公共'] = [x['光熱費']+x['社会保障']+x['通信費'] for x in monthlyamounts]

#                <div style="width:100%;">
    graphbodyheader = """
                <div>
                    <canvas id="myChartYR"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = [{xticklabels}];
                    var data1 = {data_hendo};
                    var data2 = {data_chika};
                    var data3 = {data_seikatsu};
                    var data4 = {data_kokyo};
                    var data5 = {data_ogata};
                  """.format(graphtitle = graphtitle,
                             xticklabels = xticklabels,
                             data_hendo = qdata['変動費'], 
                             data_chika = qdata['教育・養育'], 
                             data_seikatsu = qdata['食費'],
                             data_kokyo = qdata['公共'],
                             data_ogata = qdata['大型出費'])
    
    graphbodybody2 = """
                    var  label1 = "変動費";
                    var  label2 = "養育費";
                    var  label3 = "生活費";
                    var  label4 = "公共料金";
                    var  label5 = "大型出費";


                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(48,255,192,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,132,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(132,99,255,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(255,99,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }
                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                        stacked: true
                                }],
                                yAxes: [{
                                        stacked: true,
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 100,
                                    userCallback: function(value, index, values) {
                                      return value+"%";
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ' + tooltipItem.yLabel.toLocaleString()+'%';
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChartYR");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[153]:

def get_quarterByyearly_graphtab_body():
    (yearfrom,yearto) = get_objYearRange()

    graphtitle = "期ごとの推移"

    monthlyamounts = []
    for objYear in range(yearfrom,yearto):
        monthlyamounts.append([x ['all'] for x in get_yearlyatquarter_amounts(objYear)])

#                <div style="width:100%;">

    graphbodyheader = """
                <div>
                    <canvas id="myChartQY"></canvas>
                </div>


                <script>
                """

    graphbodybody1 = """
                    var graphtitle = "{graphtitle}";
                    var xticklabels = ["Q1", "Q2", "Q3", "Q4"];
                    var data1 = {d1};
                    var data2 = {d2};
                    var data3 = {d3};
                    var data4 = {d4};
                    var data5 = {d5};
                    var data6 = {d6};
                  """.format(graphtitle = graphtitle,
                             d1 = monthlyamounts[0], 
                             d2 = monthlyamounts[1], 
                             d3 = monthlyamounts[2], 
                             d4 = monthlyamounts[3], 
                             d5 = monthlyamounts[4],
                             d6 = monthlyamounts[5])
    
    graphbodybody2 = """
                    var  label1 = "2011";
                    var  label2 = "2012";
                    var  label3 = "2013";
                    var  label4 = "2014";
                    var  label5 = "2015";
                    var  label6 = "2016";


                    var data = {
                      labels: xticklabels,
                      datasets: [
                          {
                              label: label1,
                              data: data1,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label2,
                              data: data2,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label3,
                              data: data3,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label4,
                              data: data4,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label5,
                              data: data5,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          },
                          {
                              label: label6,
                              data: data6,
                              backgroundColor: "rgba(99,255,132,0.2)",
                              borderColor: "rgba(255,99,132,1)",
                              borderWidth: 1,
                              hoverBorderColor: "rgba(255,99,132,1)",
                              hoverBorderWidth: 2,
                          }

                      ]
                  };

                  var options =  {
                      maintainAspectRatio:true,
                      responsive: true,
                      title:{
                          display:true,
                          text:graphtitle
                      },
                      scales: {
                                xAxes: [{
                                }],
                                yAxes: [{
                                scaleLabel: {
                                    show: true,
                                    labelString: 'Value'
                                },
                                ticks: {
                                    suggestedMin: 0,
                                    suggestedMax: 25000,
                                    userCallback: function(value, index, values) {
                                      return "¥" + value.toLocaleString();
                                    }
                                  }
                              }]
                            },
                      tooltips: {
                        callbacks: {
                          label: function(tooltipItem,data){
                            var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ¥' + tooltipItem.yLabel.toLocaleString();
                              }
                            }
                          }
                        }

                    var ctx = document.getElementById("myChartQY");
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: data,
                        options: options
                    });
                    </script>
                    <!-- Chart.js ######################　-->
    """
    return graphbodyheader + graphbodybody1 + graphbodybody2


# In[154]:

def get_yearlyamounts_reporttab_body():
    (yearfrom,yearto) = get_objYearRange()

    yearliamounts = []
    for objYear in range(yearfrom,yearto):
        yearliamounts.append(get_yearly_amount(objYear))

    y = ['<th class="text-center"><a href="./y{yy}.html" style="color:#fff;">{yy}年</a></th>'.format(yy=x) for x in range(yearfrom,yearto)]
    y.append('<th class="text-center">小計</th>')
    yearlyth = '\n\t\t\t'.join(y)


    yearlytd = {}
    for key in yearliamounts[0].keys():
        y = ["<td>¥{:,}</td>".format(round500(x[key])) for x in yearliamounts]
        y.append("<td><strong>¥{:,}</strong></td>".format(round500(sum([x[key] for x in yearliamounts]))))
        yearlytd[key] = '\n\t\t\t'.join(y)


    summarytable0 = """
    <!-- output from PyJade -->
    <div class="panel panel-primary">
        <div class ="table-responsive">
            <table class="table table-striped table-bordered table-hover table-condensed">
                <thead class="bg-primary">
                    <tr>
                        <th class="text-center"></th>
                        {yheader}
                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr>
                        <td>{key1}</td>
                        {val1}
                    </tr>    
                    <tr>
                        <td>{key2}</td>
                        {val2}
                    </tr>    
                    <tr>
                        <td>{key3}</td>
                        {val3}
                    </tr>    
                    <tr>
                        <td>{key4}</td>
                        {val4}
                    </tr>
                    <tr>
                        <td>{key5A}</td>
                        {val5A}
                    </tr>
                    <tr>
                        <td>{key5B}</td>
                        {val5B}
                    </tr>
                    <tr>
                        <td>{key5C}</td>
                        {val5C}
                    </tr>
                    <tr>
                        <td>{key6}</td>
                        {val6}
                    </tr>
                    <tr>
                        <td>{key7}</td>
                        {val7}
                    </tr>
                    <tr>
                        <td>{key8}</td>
                        {val8}
                    </tr>
                    """.format(
            yheader=yearlyth,
        
            key1 = '食費/生活費', 
                val1 = yearlytd['食費'],
            key2 = '光熱費', 
                val2 = yearlytd['光熱費'],
            key3 = '通信費', 
                val3 = yearlytd['通信費'],
            key4 = '社会保障', 
                val4 = yearlytd['社会保障'],
#            key5 = '変動費', 
#                val5 = yearlytd['変動費'],
            key5A = '娯楽・交際', 
                val5A = yearlytd['娯楽・交際'],
            key5B = '医療・健康', 
                val5B = yearlytd['医療・健康'],
            key5C = '美容', 
                val5C = yearlytd['美容'],
            key7 = '大型出費', 
                val7 = yearlytd['大型出費'],
            key6 = '教育・養育', 
                val6 = yearlytd['教育・養育'],
            key8 = '住まい', 
                val8 = yearlytd['住まい'])




    summarytable1 = """
                <tfoot class="bg-info">
                    <tr class="text-center" style="font-weight:bold;">
                        <td>小計</td>
                        {val0}
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>
""".format( 
            val0 = yearlytd['all']
    )
    
    
    
    tabletabbody = "\n<!-- #### report tab ここから #### -->\n" + summarytable0 + summarytable1 +"\n<!-- #### report tab ここまで #### -->\n"

    
    return tabletabbody


# In[155]:
import ftpaccount

def ftpput(putfile):
    try:
        _ftp = FTP(ftpaccount. path,ftpaccount.id, ftpaccount.password)  # open(username, password)
        # _ftp.cwd("/var/tmp/")            # cd /var/tmp ディレクトリの移動
        _file = open(putfile, 'rb')      # bin バイナリモード
        command = "STOR " + putfile
        _ftp.storbinary(command, _file)  # put putfile
        _file.close()
        _ftp.quit()                      # bye
        print("ftpput:"+putfile)
    except:
        print("ftpput_failed :" + putfile)
# ftpput("index000.html")


# In[ ]:




# In[ ]:




# In[156]:

TABLE = "zaim"
# DB = "./pyzaim_{}.sqlite3".format(dt.today().strftime("%y%m%d"))
# DB = "./pyzaim_160425.sqlite3"

def build_pyzaim(startYear=2016):
    outputdir = "output/jade"
    devdir = "../../"
    
    
    print("output at "+dt.now().strftime('%Y-%m-%d %H:%M'))
    output_indexpage()
    os.chdir(outputdir)
    ftpput("index.html")
    os.chdir(devdir)
    
    (y00,m0,d0) = get_today()
    y0 = y00 + 1

    
#     objYears = range(2011,2017)
    objYears = range(startYear,y0)
    objMonthes = range(1,13)

    for objYear in objYears:
        for objMonth in objMonthes:
            if (objYear == y00) & (objMonth > m0):
                print('passed {}-{}'.format(objYear, objMonth))
                continue
            output_monthly(objYear,objMonth)

            os.chdir(outputdir)
            ftpput("m{}-{:02}.html".format(objYear,objMonth))
            os.chdir(devdir)


    
    
#     for objYear in range(2011,y0):
    for objYear in range(2016,2018):
        output_quarterly(objYear)

        os.chdir(outputdir)
        ftpput("y{}.html".format(objYear))
        os.chdir(devdir)


    output_yearly()
    
    os.chdir(outputdir)
    ftpput("summary.html")
    os.chdir(devdir)

    print("output done at:" + dt.now().strftime('%H:%M'))

    


# In[157]:

# build_pyzaim(2017)


# In[ ]:




# In[158]:

# from datetime import datetime
# from datetime import date

# t = datetime.now().timestamp()
# datetime.fromtimestamp(t).strftime("%Y-%m-%d_%H-%M-%S")


# In[ ]:

# t = datetime.now().timestamp()-4000
# day = datetime.fromtimestamp(1489097913.146002)


# In[ ]:



