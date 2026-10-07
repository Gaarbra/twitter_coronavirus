# Coronavirus Twitter Analysis

I analyzed every geotagged tweet sent in 2020 to study how coronavirus-related hashtags were used across different languages and countries. I used a MapReduce workflow to process the large dataset in parallel.

## How It Works

- `src/map.py` processes tweets and counts hashtag usage by language and country.
- `run_maps.sh` runs the mapper across the 2020 dataset in parallel using `nohup` and `&`.
- `src/reduce.py` combines the daily results into overall language and country totals.
- `src/visualize.py` creates bar graphs showing the top 10 languages or countries for each hashtag.
- `src/alternative_reduce.py` creates a line graph showing hashtag usage throughout the year.

## Results

`#coronavirus` was used primarily in English and most frequently in tweets from the United States. The Korean hashtag `#코로나바이러스` was primarily associated with Korean-language tweets and South Korea.

### #coronavirus by Language

![Coronavirus by Language](plots/reduced.lang_coronavirus.png)

### #coronavirus by Country

![Coronavirus by Country](plots/reduced.country_coronavirus.png)

### #코로나바이러스 by Language

![Korean Coronavirus by Language](plots/reduced.lang_korean.png)

### #코로나바이러스 by Country

![Korean Coronavirus by Country](plots/reduced.country_korean.png)

![](plots/alternative_reduce.png)

