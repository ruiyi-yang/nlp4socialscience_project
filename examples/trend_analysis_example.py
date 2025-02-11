# Trend Analysis Example

from nlp4socialscience.trend_analysis import term_frequency_over_time
import matplotlib.pyplot as plt

## example texts and dates
texts = [
    "The economy is growing.",
    "Politics affects everyone.",
    "The economy impacts politics.",
    "Sports and social media are intertwined."
]
dates = ["2022-01", "2022-02", "2022-03", "2022-04"]

## analyze frequency of the term 'economy' over time
term = "economy"
frequency = term_frequency_over_time(texts, dates, term)

## plot the trend
plt.plot(list(frequency.keys()), list(frequency.values()), marker='o')
plt.xlabel('Date')
plt.ylabel(f'Frequency of "{term}"')
plt.title('Term Frequency Over Time')
plt.show()