from gdeltdoc import GdeltDoc, Filters

f = Filters(
    keyword = "chatgpt",
    start_date = "2020-05-10",
    end_date = "2023-06-25"
)

gd = GdeltDoc()

# Search for articles matching the filters
articles = gd.article_search(f)

# Get a timeline of the number of articles matching the filters
timeline = gd.timeline_search("timelinevolraw", f)