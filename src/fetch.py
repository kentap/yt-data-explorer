import os
from typing import List
from datetime import datetime, timedelta, timezone
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv
import isodate

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_video_metadata(query: str, loops: int = 1, order: str = "date") -> pd.DataFrame:
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    valid_items = []
    target_count = loops * 5

    request = youtube.search().list(q=query, part='snippet', type='video', order=order, maxResults=5)
    response = request.execute()

    while len(valid_items) < target_count:
        items = response.get("items", [])
        new_valids = [item for item in items if item.get("id", {}).get("videoId")]
        valid_items.extend(new_valids)

        request = youtube.search().list_next(request, response)
        if not request:
            break
        response = request.execute()

    if not valid_items:
        print("⚠️ No valid videos with videoId found.")
        return pd.DataFrame()

    data = pd.DataFrame(valid_items[:target_count])  # 最大 target_count 件に制限
    video_ids = pd.DataFrame(list(data['id']))['videoId']
    snippet_data = pd.DataFrame(list(data['snippet']))[['channelTitle', 'publishedAt', 'channelId', 'title']]
    merged = pd.concat([video_ids, snippet_data], axis=1)

    # フィルター（過去7日間）← viewCount のときはスキップ
    if order != "viewCount":
        merged["publishedAt"] = pd.to_datetime(merged["publishedAt"])
        one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)
        merged = merged[merged["publishedAt"] >= one_week_ago]
        merged = merged[merged["title"].str.contains(query, case=False, na=False)]


        if merged.empty:
            print("⚠️ No videos found in the last 7 days for the given query.")
            return pd.DataFrame()

    return merged

def get_statistics_bulk(video_ids: List[str]) -> pd.DataFrame:
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    results = []

    for i in range(0, len(video_ids), 50):
        ids = video_ids[i:i+50]
        response = youtube.videos().list(
            part='statistics,contentDetails',
            id=",".join(ids)
        ).execute()

        for item in response.get('items', []):
            stats = item.get('statistics', {})
            stats['videoId'] = item['id']
            duration = item['contentDetails']['duration']
            seconds = isodate.parse_duration(duration).total_seconds()
            stats['duration_sec'] = seconds
            stats['isShorts'] = seconds <= 60
            results.append(stats)

    return pd.DataFrame(results)

def create_output(df_meta: pd.DataFrame, df_stats: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(df_meta, df_stats, on="videoId")

def display_summary(df: pd.DataFrame):
    print("\\n--- 検索結果サマリ ---")
    print(f"動画数: {len(df)}")
    print(f"平均再生数: {df['viewCount'].astype(int).mean():,.0f}")
    print(f"平均高評価数: {df['likeCount'].astype(int).mean():,.0f}")
    print(df[['title', 'viewCount', 'likeCount']].head(10))