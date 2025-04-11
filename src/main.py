import click
import os
from dotenv import load_dotenv
from fetch import get_video_metadata, get_statistics_bulk, create_output, display_summary
from analyze import analyze_posting_days, analyze_growth as run_growth_analysis

load_dotenv()

@click.command()
@click.option("--query", required=True, help="検索キーワード")
@click.option("--loops", default=1, help="繰り返し数（1回で最大5件 × ループ回数）")
@click.option("--order", default="date", help="検索順序: date（新着） or viewCount（人気）")
@click.option("--analyze-weekday", is_flag=True, help="投稿曜日の傾向を分析")
@click.option("--analyze-growth", is_flag=True, help="再生数の急増傾向を分析")
def main(query, loops, order, analyze_weekday, analyze_growth):
    print(f"キーワード: {query}, 取得件数: {loops * 5}, 順序: {order}")

    df_meta = get_video_metadata(query=query, loops=loops, order=order)

    if df_meta.empty:
        return

    video_ids = df_meta["videoId"].tolist()
    df_stats = get_statistics_bulk(video_ids)
    df_result = create_output(df_meta, df_stats)
    display_summary(df_result)

    if analyze_weekday:
        analyze_posting_days(df_result)
    if analyze_growth:
        run_growth_analysis(df_result)

if __name__ == "__main__":
    main()
