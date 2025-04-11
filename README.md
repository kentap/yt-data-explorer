# yt-insights-analyzer

🎥 YouTube動画の投稿傾向を分析するCLIツール  
YouTube Data API v3を使って、特定キーワードやチャンネルの動画情報を収集・分析できます。

---

## 🔧 機能一覧

- YouTube動画の検索（キーワード指定）
- 動画ごとの再生数・高評価数の取得
- 投稿日の曜日ごとの投稿傾向の分析
- CLIベースでシンプルに操作可能

---

## 🚀 セットアップ手順

### 1. このリポジトリをクローン

```bash
git clone https://github.com/yourname/yt-insights-analyzer.git
cd yt-insights-analyzer
```

### 2. 仮想環境を作成・依存関係をインストール

```bash
pip install -r requirements.txt
```

### 3. `.env` を設定

`.env.example` を `.env` にコピーし、自分のYouTube APIキーを設定してください。

```bash
cp .env.example .env
# .env ファイル内
YOUTUBE_API_KEY=your_actual_api_key_here
```

---

## 📊 使用方法

```bash
python src/main.py --query "生成AI" --loops 2 --analyze-weekday
```

### オプション説明

| オプション | 説明 |
|------------|------|
| `--query` | 検索キーワード（必須） |
| `--loops` | API呼び出しの繰り返し回数（1回で5件×ループ数） |
| `--order` | 検索順序を指定（`date`: 新着順 / `viewCount`: 再生数順） |
| `--analyze-weekday` | 曜日ごとの投稿傾向を分析して表示 |
| `--analyze-growth` | 再生数の急成長傾向をランキング表示 |


| オプション | 説明 |
|------------|------|
| `--query` | 検索キーワード（必須） |
| `--loops` | API呼び出しの繰り返し回数（1回で5件×ループ数） |
| `--analyze-weekday` | 曜日ごとの投稿傾向を分析して表示 |

---

## 📌 注意事項（必ずお読みください）

本ツールは [YouTube Data API v3](https://developers.google.com/youtube/v3) を使用しています。  
ご利用にあたっては、以下の利用規約・ポリシーに必ず従ってください。

- [YouTube API サービス利用規約（英語）](https://developers.google.com/youtube/terms/api-services-terms-of-service)
- [YouTube 利用規約（日本語）](https://www.youtube.com/t/terms)
- [YouTube API ポリシー](https://developers.google.com/youtube/terms/developer-policies)

本ツールの開発者および本リポジトリは、利用者がAPIを用いて取得したデータの利用・管理に関して一切の責任を負いません。  
**APIキーはご自身で取得・管理し、規約に違反しないようにご利用ください。**

---

## 📘 参考リンク

- [YouTube Data API v3 ドキュメント](https://developers.google.com/youtube/v3/docs)
- [APIキーの取得方法](https://developers.google.com/youtube/registering_an_application)

---

## 📄 ライセンス

[MIT License](LICENSE)

---

## 🌐 English Version Below

# yt-insights-analyzer

🎥 A CLI tool to analyze publishing trends of YouTube videos.  
It leverages the YouTube Data API v3 to fetch and analyze video metadata for specific keywords or channels.

---

## 🔧 Features

- Search YouTube videos by keyword
- Retrieve view counts, likes, and publish dates
- Analyze trends by publishing day of the week
- Simple and fast CLI interface

---

## 🚀 Setup

### 1. Clone this repository

```bash
git clone https://github.com/yourname/yt-insights-analyzer.git
cd yt-insights-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up `.env`

Copy `.env.example` to `.env` and insert your YouTube API key.

```bash
cp .env.example .env
# Inside .env:
YOUTUBE_API_KEY=your_actual_api_key_here
```

---

## 📊 Usage

```bash
python src/main.py --query "Generative AI" --loops 2 --analyze-weekday
```

### Options

| Option | Description |
|--------|-------------|
| `--query` | Search keyword (required) |
| `--loops` | Number of pages to fetch (each fetch gets 5 results) |
| `--analyze-weekday` | Analyze posting trends by day of the week |

---

## ⚠️ Terms of Use

This tool uses the [YouTube Data API v3](https://developers.google.com/youtube/v3).  
You must comply with the following terms and policies:

- [YouTube API Terms of Service](https://developers.google.com/youtube/terms/api-services-terms-of-service)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube API Developer Policies](https://developers.google.com/youtube/terms/developer-policies)

The developer of this tool assumes no responsibility for any misuse of the API or data.  
**Please obtain and manage your own API key responsibly, and follow all applicable terms.**

---

## 📘 References

- [YouTube Data API v3 Documentation](https://developers.google.com/youtube/v3/docs)
- [How to get a YouTube API Key](https://developers.google.com/youtube/registering_an_application)

---

## 📄 License

[MIT License](LICENSE)
