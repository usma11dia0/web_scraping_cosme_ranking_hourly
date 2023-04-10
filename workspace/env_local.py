###スクレイピングファイル関連###
FILE_NAME = 'テスト用_化粧品売れ筋ランキング1~100位'
RAKUTEN_URL = 'https://ranking.rakuten.co.jp/realtime/100939/'
AMAZON_URL = 'https://www.amazon.co.jp/gp/bestsellers/beauty/170040011/ref=zg_bs_nav_beauty_2_5267100051'
YAHOO_URL = 'https://shopping.yahoo.co.jp/category/2501/1752/ranking/'
QOO10_URL = 'https://www.qoo10.jp/gmkt.inc/Bestsellers/?g=2'
COSME_URL = 'https://www.cosme.net/ranking/products'
LESAGE_URL = 'https://www.lesage-store.jp/products/list?mode=&category_id=&maker_id=&name=&pageno=1&disp_number=2&orderby=4'
#ドライバ待機時間
DRIVER_WAIT_TIME = 5
SCROLL_PAUSE_TIME = 1
MAX_SCROLL_ATTEMPTS = 30
TIME_ZONE = 'Asia/Tokyo'
#ローカル用ドライバ格納先
TEMP_DIR = '/workspace/'

###GOOGLE API関連###
PROJECT_ID = "extended-study-382401"
#Secret Managerのシークレット名
SECRET_ID = 'extended_study_service_account_key'
VERSION_ID = 'latest'
#Googleドライバ/Chromeバイナリの格納先
BUCKET_NAME = 'your-bucket-name'
ZIP_BLOB_NAME = 'chrome-headless.zip'
ZIP_FILE = '/workspace/chrome-headless.zip'
#転記先ファイルの格納フォルダ指定
GOOGLE_DRIVE_FOLDER = '1TgrrK3jA0tRpX3mm_xSTs7GJ2kleqIuo'
#Googleスプレッドシートプロパティ更新用の設定値
GOOGLE_SPREADSHEET_PROPERTY = {
    'requests': [
        {
            'updateSheetProperties': {
                'properties': {
                    'sheetId': '',
                    'hidden': False
                },
                'fields': 'hidden'
            }
        },
        {
            'updateSheetProperties': {
                'properties': {
                    'sheetId': '',
                    'index': 0
                },
                'fields': 'index'
            }
        }
    ]
}
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
