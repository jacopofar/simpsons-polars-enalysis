import polars as pl

df_c = pl.read_csv("dataset/simpsons_characters.csv")

# NOTE: for some reason one of the line (id 152461) was corrupted
# and needed an added quote sign. Once done, it worked
df_sl = pl.read_csv(
    "dataset/simpsons_script_lines.csv",
    columns=[
        # "id",
        # "episode_id",
        # "number",
        "speaking_line",
        "character_id",
        # "location_id",
        "normalized_text",
    ],
)
df_sl = df_sl.filter(
    (pl.col("speaking_line") == "true")
    & (pl.col("character_id").is_not_null())
    & (pl.col("normalized_text").is_not_null())
)


def to_ngrams(l: list[str]) -> list[str]:
    ret = []
    n = 9
    extended_list = [" "] * n + list(l) + [" "] * n
    for i_start in range(len(extended_list) - n):
        tokens = extended_list[i_start : i_start + n]
        # avoid things like "da doo da doo da doo" or similar
        if len(set(tokens)) >= n // 2:
            ret.append(" ".join(tokens).strip())
    return ret


df_sl = (
    df_sl.with_columns(
        [
            pl.col("normalized_text")
            .str.to_lowercase()
            .str.split(by=" ")
            .apply(to_ngrams)
            .alias("tokens")
        ]
    )
    .explode("tokens")
    .filter(pl.col("tokens").is_not_null())
)
# df_sl.write_parquet("simpson_tokens.parquet")

characters_activity = (
    df_sl.groupby("character_id").count().sort("count", descending=True)
)
MOST_ACTIVE_THRESHOLD = 50
thresh = characters_activity[MOST_ACTIVE_THRESHOLD, 1]
print(
    f"Characters with less than {thresh} sentences will be ignored"
    f" because they are not in the {MOST_ACTIVE_THRESHOLD} most active"
)
most_active = characters_activity.filter(pl.col("count") >= thresh)
print("shape before: ", df_sl.shape)
df_sl = df_sl.join(most_active, on="character_id")
print("shape after: ", df_sl.shape)

# count token frequency + laplacian smooth
SMOOTHING_FACTOR = 1
ngram_totals = df_sl.groupby(["tokens"]).count()
ngram_totals = ngram_totals.with_columns(
    [
        (pl.col("count") + MOST_ACTIVE_THRESHOLD * SMOOTHING_FACTOR).alias(
            "total_count"
        ),
        pl.col("tokens").alias("ngram"),
    ]
).drop(["tokens", "count"])

characters_sentences = (
    df_sl.groupby(["character_id", "tokens"])
    .count()
    .with_columns(
        [
            (pl.col("count") + SMOOTHING_FACTOR).alias("character_count"),
            pl.col("tokens").alias("ngram"),
        ]
    )
    .drop(["tokens", "count"])
)

most_polarized = (
    characters_sentences.join(ngram_totals, on="ngram")
    .with_columns((pl.col("character_count") / pl.col("total_count")).alias("polarity"))
    .sort("polarity", descending=True)[:500]
)
most_characteristic = (
    most_polarized.join(df_c, left_on="character_id", right_on="id")
    .select([pl.col("name"), pl.col("ngram"), pl.col("polarity")])
    .sort("polarity", descending=True)
)

most_characteristic.write_ndjson("character_tokens.jsonl")
