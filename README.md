# web_scraping_cosme_ranking_hourly

"web_scraping_cosme_ranking_hourly"は各 EC サイトの化粧品ランキングを 1 時間ごとに自動取得するスクレイピングファイルです。

- cloud_function_scraping_prod.ipynb: Google Cloud Function 実行用
- cloud_function_scraping_local.ipynb: ローカル実行用

# 出力結果

スクレイピングの結果を所定の Google SpreadSheet へ転記します。

# 事前準備

- Google Cloud Function の場合

1.  headress-chrome v1.0.0-37 と chromedriver 2.37 をインストール
2.  headress-chrome と chromedriver のバイナリファイルを Cloud Strage バケットに保存
3.  転記先スプレッドシートへアクセス可能なサービスアカウントを GCP にて作成
4.  Secret Manager へサービスアカウントキーを登録
5.  env_prod 内を各自の環境に合わせて変更
6.  Google Cloud Function へ関数転記, logging_config.json/requirement.txt 追加

※　 Google Cloud Platform 設定一覧

1. Google Cloud Project 作成
2. Google Cloud Function 作成
3. Cloud Pub/Sub 作成(イベントトリガ用)
4. Cloud Strage のバケット作成 (chrome/ドライバのバイナリ保存用)
5. Google Spread sheet API 有効化
6. Google Drive API 有効化
7. Secret Manager 有効化
8. Cloud Scheduler ジョブの作成

- ローカル実行の場合

1.  headress-chrome v1.0.0-37 と chromedriver 2.37 をインストール
2.  headress-chrome と chromedriver のバイナリファイルをまとめた zip ファイル作成
3.  作成した zip ファイルを/workspace 配下に置く
4.  転記先スプレッドシートへアクセス可能なサービスアカウントを GCP にて作成
5.  サービスアカウントキーを/workspace 配下に置く
6.  env_local 内を各自の環境に合わせて変更

※ headless-chrome のインストール先
https://github.com/adieuadieu/serverless-chrome/releases?page=2
