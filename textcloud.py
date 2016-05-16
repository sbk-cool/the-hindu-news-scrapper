from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random


class TextCloud:
    """Makes text cloud with document."""

#Initialises the text to be used for text cloud.
    def __init__(self,text):
        self.text=text

#Define the color function for the text cloud.
    def grey_color_func(self,word, font_size, position, orientation, random_state=None, **kwargs):
        return "hsl(0, 0%%, %d%%)" % 100

#Makes the word cloud using the text.
    def makeCloud(self):
        wordcloud = WordCloud().generate(self.text)
        plt.imshow(wordcloud.recolor(color_func=grey_color_func,random_state=3))
        plt.axis("off")
        plt.show()
