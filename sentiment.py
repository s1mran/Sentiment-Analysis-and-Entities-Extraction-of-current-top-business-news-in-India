import nltk
nltk.download('vader_lexicon')

#importing SentimentIntensityAnalyzer package for vader sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def result(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<22} {}".format("Snetiment Result", str(score)))
    print ("Sentiment Score: " + str(score['compound']) )	
    
for i in range(10): 
	# printing sentiment scores of each news:
        print(str(i+1)+" "+titles[i])
        # sentiment scores for this news is:
        result(descriptions[i])
        
        
        
	
				 
