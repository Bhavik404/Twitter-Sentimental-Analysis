from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import tweepy
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))

app = Flask(__name__)

model = pickle.load(open('SVC_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))

# Keys to access twitter
consumer_key = "Mm5exG8k9KgtnHko1hcmyK0Uv"
consumer_secret = "8xDF6oojJGEN77Mb5dBSrxaoMBpT8UDURrwALCOKg4jtdsf07h"
access_key = "1101137928409952258-BeZlmZyeT4haQJQZRJogLP96vQcKiK"
access_secret = "4emlzcwEzGZngeWghYJdLo7OEKyKcsvFfrzTNkh0tljtR"

# Fetching tweets
# Getting tweets from user
def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    tmp = []
    hour = []
    months = []
    day = []
    for tweet in tweepy.Cursor(api.user_timeline, id=username,result_type="recent", include_entities=True, exclude_replies=True, exclude_retweets=True, lang="en", tweet_mode='extended').items(150):
        tmp.append(tweet.full_text)
        time = tweet.created_at
        hour.append(time.strftime("%I %p"))
        months.append(time.strftime("%B %y"))
        day.append(time.strftime("%d"))
    return tmp, hour, months, day
# Getting tweets through hashtags
def get_hashtag(keyword):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    t = []
    hour = []
    months = []
    day = []
    date_since = '2021/01/01'
    for tweet in tweepy.Cursor(api.search, q=keyword, lang="en",since=date_since, tweet_mode='extended').items(50):
        t.append(tweet.full_text)
        time = tweet.created_at
        hour.append(time.strftime("%I%p"))
        months.append(time.strftime("%B"))
        day.append(time.strftime("%d"))
    return t, hour, months, day

# Preprocessing tweets
# Preprocessing just to get clean tweets
def clean_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    tweet = tweet.translate(str.maketrans("","",string.punctuation))
    tweet = re.sub(r"\@\w+|\#","",tweet)
    return tweet
# Preprocessing for futher analysis
# def preprocess_tweet_text(tweet):
#     tweet = tweet.lower()
#     tweet = re.sub(r"http\s+|www\s+|https\S+","",tweet,flags=re.MULTILINE)
#     tweet = tweet.translate(str.maketrans("","",string.punctuation))
#     tweet = re.sub(r"\@\w+|\#","",tweet)
#     tweet_tokens = word_tokenize(tweet)
#     filtered_words = [word for word in tweet_tokens if word not in stop_words]
#     ps = PorterStemmer()
#     stemmed_words = [ps.stem(w) for w in filtered_words]
#     lemmatizer = WordNetLemmatizer()
#     lemma_words = [lemmatizer.lemmatize(w,pos = "a") for w in stemmed_words]
#     return " ".join(lemma_words)
#END of Preprocessing

@app.route('/')
def indexpage():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def check_sentiment():
    if request.method == 'POST':
        tweet = request.form['text']
        raw_tweet = vectorizer.transform([tweet])
        prediction = model.predict(raw_tweet)
        result = (prediction[0]).upper()
        print(result)
    return render_template('index.html', text=tweet, results=result)


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        data = request.form['user_hashtag']
        if data[0] == '#':
            tweets, hours, months, day = get_hashtag(data)
        else:
            tweets, hours, months, day = get_tweets(data)
        # print(tweets)
        # print(hours)
        # print(months)
        cleaned_tweets = []
        # preprocessed_tweets = []
        prediction = []
        #Making tweets ready to display on Dashboards Table
        for tweet in tweets:
            cleaned_tweets.append(clean_tweet(tweet))
        #Preprocessing all fetched tweets for further analysis
        # for tweet in tweets:
        #     preprocessed_tweets.append(preprocess_tweet_text(tweet))
        # print(preprocessed_tweets)
        #Predicting the tweets fetched after preprocessing it
        for tweet in cleaned_tweets:
            tweet = vectorizer.transform([tweet])
            result = model.predict(tweet)
            result = result[0]
            result = result.upper()
            prediction.append(result)
        # print(prediction)

        #CODE FOR DATA OF PIE CHART
        pie_data = []
        pos_cnt = prediction.count('POSITIVE')
        neg_cnt = prediction.count('NEGATIVE')
        neu_cnt = prediction.count('NEUTRAL')
        pie_data.append(pos_cnt)
        pie_data.append(neu_cnt)
        pie_data.append(neg_cnt)
        # print(pie_data)
        #PIE CHART DONE

        #LINE CHART DATA CODE
        new_lst = []
        unique_months = []
        Positive_linechart = []
        Neutral_linechart = []
        Negative_linechart = []
        for i in months:
            if i not in unique_months:
                unique_months.append(i)
        for x in range(len(unique_months)):
            for i in range(len(months)):
                if months[i] == unique_months[x]:
                    new_lst.append(prediction[i])
            Positive_linechart.append(new_lst.count("POSITIVE"))
            Neutral_linechart.append(new_lst.count("NEUTRAL"))
            Negative_linechart.append(new_lst.count("NEGATIVE"))
            new_lst = []

        Positive_linechart = Positive_linechart[::-1]
        # if len(Positive_linechart)<6:
        #     while(len(Positive_linechart)!=6):
        #         Positive_linechart.insert(0,0)
        # if len(Positive_linechart)>6:
        #     while(len(Positive_linechart)!=6):
        #         Positive_linechart.remove(Positive_linechart[0])
        # print(Positive_linechart)

        Neutral_linechart = Neutral_linechart[::-1]
        # if len(Neutral_linechart)<6:
        #     while(len(Neutral_linechart)!=6):
        #         Neutral_linechart.insert(0,0)
        # if len(Neutral_linechart)>6:
        #     while(len(Neutral_linechart)!=6):
        #         Neutral_linechart.remove(Neutral_linechart[0])
        # print(Neutral_linechart)

        Negative_linechart = Negative_linechart[::-1]
        # if len(Negative_linechart)<6:
        #     while(len(Negative_linechart)!=6):
        #         Negative_linechart.insert(0,0)
        # if len(Negative_linechart)>6:
        #     while(len(Negative_linechart)!=6):
        #         Negative_linechart.remove(Negative_linechart[0])
        # print(Negative_linechart)

        unique_months = unique_months[::-1]
        # print(unique_months)

        # CODE FOR BAR CHART DATA
        lst = []
        march_days = []
        first_week = []
        second_week = []
        third_week = []
        forth_week = []
        positive_barchart = []
        neutral_barchart = []
        negative_barchart = []
        # print(day)
        # print(prediction)
        for i in range(len(months)):
            if months[i] == "March 21":
                lst.append(prediction[i])
                march_days.append(day[i])
        # print(lst)
        # print(march_days)
        march_days = list(map(int, march_days))
        for i in range(len(march_days)):
            if march_days[i] in range(1,8):
                first_week.append(lst[i])
            elif march_days[i] in range(8,15):
                second_week.append(lst[i])
            elif march_days[i] in range(15,22):
                third_week.append(lst[i])
            elif march_days[i] in range(22,32):
                forth_week.append(lst[i])
        # print(first_week)
        # print(second_week)
        # print(third_week)
        # print(forth_week)
        positive_barchart.append(first_week.count("POSITIVE"))
        positive_barchart.append(second_week.count("POSITIVE"))
        positive_barchart.append(third_week.count("POSITIVE"))
        positive_barchart.append(forth_week.count("POSITIVE"))
        print(positive_barchart)
        neutral_barchart.append(first_week.count("NEUTRAL"))
        neutral_barchart.append(second_week.count("NEUTRAL"))
        neutral_barchart.append(third_week.count("NEUTRAL"))
        neutral_barchart.append(forth_week.count("NEUTRAL"))
        print(neutral_barchart)
        negative_barchart.append(first_week.count("NEGATIVE"))
        negative_barchart.append(second_week.count("NEGATIVE"))
        negative_barchart.append(third_week.count("NEGATIVE"))
        negative_barchart.append(forth_week.count("NEGATIVE"))
        print(negative_barchart)
        # END BAR CHART DATA


        #CODE FOR WORDCLOUD DATA
        #JS CODE
        cloud = ''.join(cleaned_tweets)
        text_tokens = word_tokenize(cloud)
        tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
        cloud_data = ' '.join(tokens_without_sw)
        cloud_data = cloud_data.replace('amp', '')
        cloud_data = re.sub(r'[0-9]+', '', cloud_data)
        regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
        cloud_data = regrex_pattern.sub(r'',cloud_data)
        #JS CODE END
        #WORD CLOUD END

        #TOP 10 WORDS USED CHART DATA
        all_sentences = []
        for word in tweets:
            all_sentences.append(word)
        lines = list()
        for line in all_sentences:    
            words = line.split()
            for w in words: 
                lines.append(w)
        #Removing Punctuation
        lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]
        lines = [re.sub(r"http\S+|www\S+|https\S+", '', x, flags=re.MULTILINE) for x in lines]
        lines2 = []
        for word in lines:
            if word != '':
                lines2.append(word)
        #This is stemming the words to their root
        from nltk.stem.snowball import SnowballStemmer
        # The Snowball Stemmer requires that you pass a language parameter
        s_stemmer = SnowballStemmer(language='english')
        stem = []
        for word in lines2:
            stem.append(s_stemmer.stem(word))  
        # print(stem)
        stem2 = []
        for word in stem:
            if word not in stop_words:
                stem2.append(word)
        df = pd.DataFrame(stem2)
        df = df[0].value_counts()
        #This will give frequencies of our words
        from nltk.probability import FreqDist
        freqdoctor = FreqDist()
        for words in df:
            freqdoctor[words] += 1 
        # print(df)
        df = df[df.index != 'amp']
        df = df[df.index != 'rt']
        df = df[:10,]
        index = df.index
        top10words_count = df.values
        top10words_count = top10words_count.tolist()
        top10words = index.to_numpy(dtype='str')
        top10words = top10words.tolist()
        #END OF TOP 10 WORDS CHART

        #TOP 7 ORGANIZATIONS MENTIONED CHART DATA
        def show_ents(doc):
            if doc.ents:
                for ent in doc.ents:
                    print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
        str1 = " " 
        stem2 = str1.join(lines2)
        stem2 = nlp(stem2)
        label = [(X.text, X.label_) for X in stem2.ents]
        df6 = pd.DataFrame(label, columns = ['Word','Entity'])
        df7 = df6.where(df6['Entity'] == 'ORG')
        df7 = df7['Word'].value_counts()
        df7 = df7[df7.index != 'RT']
        df7 = df7[:8,]
        index = df7.index
        orgs_count = df7.values
        orgs_count = orgs_count.tolist()
        orgs = index.to_numpy(dtype='str')
        orgs = orgs.tolist()
        #END TOP 7 ORG DATA
        

    return render_template('dashboard.html',
                            tweets = tweets, 
                            predictions = prediction, 
                            pie_data = pie_data,
                            Positive_linechart = Positive_linechart,
                            Neutral_linechart = Neutral_linechart,
                            Negative_linechart = Negative_linechart,
                            months = unique_months,
                            cloud = cloud_data,
                            top10words = top10words,
                            top10words_count = top10words_count,
                            orgs = orgs,
                            orgs_count = orgs_count,
                            positive_barchart = positive_barchart,
                            neutral_barchart = neutral_barchart,
                            negative_barchart = negative_barchart)

if __name__ == "__main__":
    app.run(debug=True)
