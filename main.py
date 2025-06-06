from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import time

# === Config Chrome ===
service = Service('C:\\Users\\40754\\Documents\\ASE\\MASTER\\anul 2, sem 2\\Web mining și analiza datelor\\chrome-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# === Load IMDb page ===
url = 'https://www.imdb.com/title/tt2172954/reviews/'
driver.get(url)

# Scroll + click Load More
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    try:
        load_more_button = driver.find_element('class name', 'ipl-load-more__button')
        load_more_button.click()
        time.sleep(2)
    except:
        break

# === Extract entire body text
body_text = driver.find_element('tag name', 'body').text
driver.quit()

# === Extract candidate reviews (rudimentar)
lines = body_text.split('\n')
review_lines = []
for i in range(len(lines)):
    if lines[i].strip() and len(lines[i]) > 80:  # presupunem că review-ul are peste 80 caractere
        review_lines.append(lines[i].strip())

# === Sentiment analysis
analyzer = SentimentIntensityAnalyzer()
data = []
for text in review_lines:
    sentiment = analyzer.polarity_scores(text)
    data.append({
        'Review': text,
        'Positive': sentiment['pos'],
        'Neutral': sentiment['neu'],
        'Negative': sentiment['neg'],
        'Compound': sentiment['compound']
    })

# === Salvare și vizualizare
df = pd.DataFrame(data)
df.to_csv('whiplash_raw_reviews_sentiment.csv', index=False)
print("✅ Review-uri brute salvate în whiplash_raw_reviews_sentiment.csv")

if not df.empty:
    plt.figure(figsize=(10, 6))
    plt.hist(df['Compound'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribuția sentimentelor brute')
    plt.xlabel('Scor Compound')
    plt.ylabel('Număr recenzii')
    plt.grid(True)
    plt.tight_layout()
    plt.show()