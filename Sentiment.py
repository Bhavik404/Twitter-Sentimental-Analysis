import pickle
import numpy as np
# from sklearn.feature_extraction.text import TfidfVectorizer
model = pickle.load(open('LogisticRegressionModel.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))

tweet = ["We all welcome Tesla Motors with open arms in India","You are a good guy","I have bad meeting tommorow"]
output=[]
for i in tweet: 
    tweet = vectorizer.transform([i])
    output.append(model.predict(tweet))
# tweet = vectorizer.transform(tweet)
# output = model.predict(tweet)
print(output)
results= np.concatenate(output)
print(results)
