# get_imassc
アイドルマスター シャイニーカラーズ公式（@imassc_official）から動画・画像を取得するスクリプトです。
製作者都合でMac（intel・M1）環境の動作確認しかしていません。
@imassc_officialのタイムラインから300件取得した時のディレクトリ構成は以下のようになります（2022/02/23時点）。
```
get_imassc
├── README.md
├── __pycache__
│   └── config.cpython-37.pyc
├── birth
│   └── 三峰 結華2022-01-15 15:01:00+00:00.mp4
├── card
│   ├── 【Fallin' Snow in】大崎 甜花.png
│   ├── 【Howling】芹沢 あさひ.png
│   ├── 【LATE】緋田 美琴      .png
│   ├── 【WtoW】風野 灯織.png
│   ├── 【カラメル】樋口 円香.png
│   ├── 【きゅん♡コメ】八宮 めぐる.png
│   ├── 【午・燦・娘・娘】幽谷 霧子.png
│   ├── 【雪、えとせとら】月岡 恋鐘.png
│   ├── 【ひとつ、はたたく】櫻木 真乃.png
│   ├── 【マイバレンタイン】有栖川 夏葉.png
│   ├── 【チョコレー党、起立！】浅倉 透        .png
│   ├── 【ソー・ディフィカルト！】小宮 果穂.png
│   ├── 【殴打、その他の夢について】浅倉 透.png
│   └── 【つよがりのためのララバイ】桑山 千雪.png
├── comic
│   ├── 第316話『探しに行こう』.png
│   ├── 第317話『引っ越し屋さん』.png
│   ├── 第318話『天使と騎士』.png
│   ├── 第319話『ややこしい』.png
│   ├── 第320話『おまじない』.png
│   ├── 第321話『透inカート』.png
│   ├── 第322話『気持ちを込めて』.png
│   ├── 第323話『チョコの置き場所』.png
│   └── 第324話『懐かしくて嬉しい』.png
├── config.py
├── event
│   └── はこぶものたち.mp4
├── ssr
│   ├── 【Howling】芹沢 あさひ.mp4
│   ├── 【きゅん♡コメ】八宮 めぐる.mp4
│   ├── 【ひとつ、はたたく】櫻木 真乃.mp4
│   ├── 【マイバレンタイン】有栖川 夏葉.mp4
│   └── 【つよがりのためのララバイ】桑山 千雪.mp4
└── tweet.py
```


## 取得する画像・動画
- SSRアイドル登場時の動画
- イベントの予告動画
- 誕生日ミニコミュ動画
- web4コマ漫画
- カードイラスト

## 使用方法

### 前提条件
- Pythonインストール済
- tweepyインストール済
- Twitter APIキーとトークンの取得済


### get_imasscのクローン
ターミナル(Winはコマンドプロンプト)上の任意のディレクトリで`git clone`を実行する。
```ターミナル
git clone git@github.com:zakiii0124/get_imassc.git
```

### config.pyの編集
config coppy.pyの名前をconfig.pyに変更し、取得したAPIキーとトークンを追記する。
```config.py
consumer_key = "Twitter APIキー"
consumer_secret = "Twitter APIキー secret"
access_token = "Access token"
access_token_secret = "Access token secret"
```

### 件数指定取得
ターミナル(Winはコマンドプロンプト)上で`python tweet.py n`を実行する。
nは任意の数字。nの数だけ@imassc_officialのタイムラインからツイートを取得します。
@imassc_officialは投稿数が多いため、思い切って多めに指定することをおすすめします。
取得したファイル名がターミナル上に出力されます。

```ターミナル
任意のディレクトリ %cd get_imassc
get_imassc % python tweet.py 100
【つよがりのためのララバイ】桑山 千雪
【殴打、その他の夢について】浅倉 透
第324話『懐かしくて嬉しい』
【マイバレンタイン】有栖川 夏葉
第323話『チョコの置き場所』
【LATE】緋田 美琴
【マイバレンタイン】有栖川 夏葉
【雪、えとせとら】月岡 恋鐘
第322話『気持ちを込めて』
```