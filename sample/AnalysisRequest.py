#最初に動画の解析リクエストを送るサンプル
import requests
import json
#送信先ＵＲＬ（笑顔、笑声解析サーバーのホスト）
url = "http://192.168.17.94/Web015"
headers = {
    "Content-Type": "application/json"
}

#JSON内のＵＲＬはベルフェースの動画ダウンロードリンク（ＩＰによるフィルタを想定それ以外の認証は現在設定なし）
body = {
    "config":{
        "analysys_sequence":10,
        "climax_count_lower_limit":30,
        "detect_count":2
    },
    "videos":[
        {"url":"http://192.168.17.94/Bell001.mp4"},
        {"url":"http://192.168.17.94/Bell002.mp4"},
        {"url":"http://192.168.17.94/Bell003.mp4"},
        {"url":"http://192.168.17.94/Bell004.mp4"},
        {"url":"http://192.168.17.94/Bell005.mp4"},
        {"url":"http://192.168.17.94/Bell006.mp4"},
        {"url":"http://192.168.17.94/Bell007.mp4"},
        {"url":"http://192.168.17.94/Bell008.mp4"},
        {"url":"http://192.168.17.94/ext1.mp4"},
        {"url":"http://192.168.17.94/ext2.mp4"},
        {"url":"http://192.168.17.94/ext3.mp4"},
    ]
}
r = requests.post(url, data=json.dumps(body), headers=headers)
print(r.status_code)
print(r.text)