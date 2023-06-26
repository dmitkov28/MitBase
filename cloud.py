import matplotlib.pyplot as plt
from wordcloud import WordCloud


def create_wordcloud(headlines: list):
    wordcloud = WordCloud(background_color="white", max_words=40).generate(
        " ".join([item for item in headlines])
    )
    fig, _ = plt.subplots()
    plt.imshow(wordcloud)
    plt.axis("off")
    return fig


