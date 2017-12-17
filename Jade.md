# PyJade

+ Store Zaim Data
+ Export Monthly HTML Files
+ python実行するには、pythonファイルとしてダウンロードしpyJade_outputHtml.pyに変更するだけでOK
+ v2.4 17/9/10 - 
 + issue#377 Monthly/Report 高額リストにカテゴリ順、と記載
 
+ v2.3 17/5/28 - 6/4
 + Yearly/Qレポートのカテゴリに住居を追加
 + Yearly/Qレポートのカテゴリに社会保障から投資・貯金を独立
 + Yearly/Qレポートのカテゴリのそれぞれの項目がどういうジャンルを含むかを記載。 

+ v2.1 17/1/14 - 1/29
 + 2017年対応 年のハードコーディングを修正した
 + print_nonPaymenttableの誤り訂正
 + issue#272 Yearly Reportに金融資産残高に対応 (手入力)
 + issue#000 Monthly/YearlyにFPレポートを掲載
 + issue#000 テーブルの幅に最小値を設定した
 + issue#000 確定申告レポートをYearlyに掲載した
 + issue#000 bug Cookieの名前をそれぞれのページ(monthly, yearly, total)でわけて、それぞれのページを移動した際にtabが保存されるようにした
 
+ rev1.16 -> v2.0にした 12/18
 + issue#000	スクリプト化。このファイルをpython形式<pyJade_outputHtml.py>で書き出せばOK。
 + issue#000 	iPhone対応はこのファイルをforkすれば良さそう
 + issue#000 	weekly reportは検討中 (保留)
+ rev1.14 12/4-12/10
 + issue#297	レポート名をQuarterly, YearlyからYearly, Totalに変更した
 + issue#297	Quarterly ReportをYearly Reportに変更, Yearly ReportをTotal Reportに変更"
 + issue#298	Yearly Reportを、レポート(M), レポート(Q)にする。
 + issue#299	出費詳細のタブは上に持って来る
 + issue#300	Yearly Reportのグラフを グラフ(M), グラフ(Q),にする
 + issue#175	金融資産まとめがない (Yearly月ごと)
 + issue#177	立替まとめ (Yearly月ごと)
 + issue#178	入金まとめ (月ごと)
 + issue#266	変動費はカテゴリごとに分ける
 + issue#302	カテゴリ計の計算が合っているか (小遣い、家賃、住まいの項目)
 + issue#303	Yearly Detail: 銀行口座、積み立てをそれぞれで表に変更した。
 + issue#304	Yearly Report 養育費が足りてない：小遣いが入ってない。→教育・教養に名前を変える
 + issue#305	Monthly Report 養育費が足りてない：書籍が入ってない。
 + issue#306	 家具・家電が変動費に入ってる。住まいに入れる
 + issue#307	"Yearly Reportの最後の表が1月から始まってる&小計がない"
 + issue#308	月ごとの小計が間違ってた
 + issue#309	"Yearly Reportの月次表について高めのもの安めのものを色分けし、高めのものにはTOP3をポップオーバー表示する"
 + issue#267	入金・振替はたかとさえで分ける
 + issue#268	口座もたかとさえで分ける

+ rev1.13 : 11/28 - 12/3
 + issue283: レポート出力の実装
  + add below
  + get_genressummaly
  + getBiggerAmountforReport
  + getBiggerAmountinGenreforReport
  + getGenrescount
  + getGenresdeltaforReport
  + getRestaurantforReport
  + datetxt2class = lambda txt:dt.strptime(txt,  '%Y-%m-%d')
  + getTatekaetextforReport
  + getMonthlydeltaforReport
  + getReportText
 + issue284, 287-292, 294-296: レポート出力の修正 (Summaryタブの追加など)
+ rev1.12 : 16/11/19 ~ 28
 + issuexxx: todoリストに公共料金を追加。print_monthly_checklist
 + issuexxx: ファイル出力先を output/jadeに変更した。mod:build_pyzaim, ftpput
 + issue280: dbの保存先を./dbに変更した
 + issue279: 銀行口座の支出名前2文字目までが日付の数値な場合、日付として扱うようにした。mod print_banktable
 ex) [23 UFJ入金]を[23日/UFJ入金]とした
 + issue285: 上記により銀行の日付がバラバラになったので修正。 add get_bankdata
 + issue286: 出納リストの入出金が色分けされていなかった mod print_banktable
 + issue281:詳細タブ出力の順序変更 mod get_detailtabbody
 + issue282:レポートタブ出力の順序変更 mod get_reporttabbody
 + issue261: 高額出勤リストのはじめに生活費(101)が来るように修正 mod select_ExpenceData
 
+ rev1.11: 16/11/12 ~ 
 + issue194: 公共料金チェックリストにした mod get_detailtabbody, add checkPediodicalfees
 + issue273, 274: テーブル右上の小計を500円単位の四捨五入にした
 + issue275: 月次で確認する事項のチェックリストを登録した add print_monthly_checklist(rubyからのcopy) mod select_nonPaymentData
 + issue276: mod:print_nonPaymenttableの対象口座IDから郵貯などが抜けてた
 + issue277: round500について,250円未満のときは100円刻みで四捨五入する
 + mod print_nonpaymenttable 立替・振替リストと銀行リストの両方を出力するようにしていたので分けた
 + issue259: 振替・入金リストを振替・立替詳細リストにする。 add get_tatekaeData, mod print_nonPaymenttable

+ r3(1.9):
 + いらない行の削除
 + issue149: select_expencedataが漏れていたので対応。
 + issue250: カテゴリごとのサマリを削除して、ジャンルごとのサマリをトップに持ってくる get_reporttabbody (del summarytable)
 + issue251: 月度詳細：変動と大型について何が含まれているかを表に書く

+ r2(1.8): 
 + issue149: SQLのGroup byを止めてpython側で集計するようにした。(select_WholeData, select_categorydata, select_genredata)
 + issue244: 高額リストから社会保障を除去。select_ExpenceData
 + issue245: 高額リスト、チェックリストに条件を記載 print_moneytable
 + issue246,247: 口座出納があっていない。コメント欄は左寄せ。 print_nonPaymenttable, print_banktable
 + issue240,248: genre表に各月の合計金額と、各月のカテゴリごとの合計金額を記載する get_genrestable
 + issue239,249: genre表にシッター代・家賃・小遣いを追加。家賃と家財は家関係として独立。detailgenres
 