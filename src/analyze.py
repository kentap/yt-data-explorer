import pandas as pd

def analyze_posting_days(df: pd.DataFrame):
    df["publishedAt"] = pd.to_datetime(df["publishedAt"])
    df["weekday"] = df["publishedAt"].dt.day_name()
    df["date"] = df["publishedAt"].dt.strftime("%Y-%m-%d")
    df["week_label"] = df["weekday"] + " (" + df["date"] + ")"

    df["viewCount"] = df["viewCount"].astype(int)
    df["isShorts"] = df["isShorts"].astype(bool)

    summary = df.groupby(["week_label", "isShorts"]).agg(
        count=("videoId", "count"),
        avg_views=("viewCount", "mean")
    ).reset_index()

    print("\n--- 曜日別（+日付） × Shorts/長編 投稿傾向 ---")
    for label in summary["week_label"].unique():
        print(f"\n{label}")
        sub = summary[summary["week_label"] == label]
        for _, row in sub.iterrows():
            vtype = "Shorts" if row["isShorts"] else "長編"
            print(f" - {vtype}: {int(row['count'])}本 / 平均再生数 {int(row['avg_views']):,}")

    return summary

def analyze_growth(df: pd.DataFrame):
    df["publishedAt"] = pd.to_datetime(df["publishedAt"])
    df["days_since_posted"] = (pd.Timestamp.utcnow() - df["publishedAt"]).dt.days.clip(lower=1)
    df["viewCount"] = df["viewCount"].astype(int)
    df["growth_rate"] = df["viewCount"] / df["days_since_posted"]

    df_sorted = df.sort_values("growth_rate", ascending=False)

    print("\n--- 急成長している動画ランキング（再生数 / 日数） ---")
    for idx, row in df_sorted.head(10).iterrows():
        print(f"{row['title']} | {int(row['viewCount']):,} 回再生 / {row['days_since_posted']}日 → 平均 {int(row['growth_rate']):,} 回/日")

    return df_sorted
