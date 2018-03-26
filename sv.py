
from svmutil import *
from svm import *
import re
featureList=['construction','helmet','site','building','safety','work']
tweets=[(['doing', 'construction', 'people', 'kept', 'joking', 'inadequate', 'helmet', 'protecting', 'serious'],'positive'),
        (['brother', 'claims', 'safety', 'policies', 'construction', 'liberal', 'bureaucracy', 'wearing', 'helmet', 'head'],'positive'),
        (['norm', 'nowadays', 'wear', 'helmet', 'ride', 'bike', 'building', 'construction', 'site', 'common', 'sense'],'positive'),
        (['construction', 'site', 'required', 'wear', 'helmet', 'bettersafethansorry', 'safetyatwork'],'positive'),
        (['construction', 'site', 'required', 'wear', 'helmet', 'bettersafethansorry', 'safetyatwork'],'positive'),
        (['cathedral', 'construction', 'safety', 'helmet', 'sooner'],'positive'),
        (['fun'],'negative'),
        (['sniping', 'beta', 'fun'],'negative'),
        (['date', 'fun'],'negative'),
        (['wow', 'fun'],'negative'),
        (['fun', 'ago', 'dbacks', 'fastest', 'team', 'reach', 'world', 'series', 'dbacksmemories'],'negative')]
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end
def getSVMFeatureVectorAndLabels(tweets, featureList):
    sortedFeatures = sorted(featureList)
    map = {}
    feature_vector = []
    labels = []
    for t in tweets:
        label = 0
        map = {}
        #Initialize empty map
        for w in sortedFeatures:
            map[w] = 0

        tweet_words = t[0]
        tweet_opinion = t[1]
        #Fill the map
        for word in tweet_words:
            #process the word (remove repetitions and punctuations)
            word = replaceTwoOrMore(word)
            word = word.strip('\'"?,.')
            #set map[word] to 1 if word exists
            if word in map:
                map[word] = 1
        #end for loop
        values = map.values()
        feature_vector.append(values)
        if(tweet_opinion == 'positive'):
            label = 0
        elif(tweet_opinion == 'negative'):
            label = 1
        labels.append(label)
        #return the list of feature_vector and labels
    return {'feature_vector' : feature_vector, 'labels': labels}
#end

def getSVMFeatureVector(tweets, featureList):
    sortedFeatures = sorted(featureList)
    map = {}
    feature_vector = []
    labels = []
    for t in tweets:
        label = 0
        map = {}
        #Initialize empty map
        for w in sortedFeatures:
            map[w] = 0

        tweet_words = t[0]
        tweet_opinion = t[1]
        #Fill the map
        for word in tweet_words:
            #process the word (remove repetitions and punctuations)
            word = replaceTwoOrMore(word)
            word = word.strip('\'"?,.')
            #set map[word] to 1 if word exists
            if word in map:
                map[word] = 1
        #end for loop
        values = map.values()
        feature_vector.append(values)
        if(tweet_opinion == 'positive'):
            label = 0
        elif(tweet_opinion == 'negative'):
            label = 1
        labels.append(label)
    #return the list of feature_vector and labels
    return feature_vector
#end

#Train the classifier
result = getSVMFeatureVectorAndLabels(tweets, featureList)
problem = svm_problem(result['labels'], result['feature_vector'])
#'-q' option suppress console output
param = svm_parameter('-t 0 -c 7 -b 1')
# -t 0 --> Linear 1-->RBF 2-->sigmoid 3-->polynomial
# c--> cost
#g --> gamma

classifier = svm_train(problem, param)
svm_save_model('classifierDumpFile.model', classifier)

#Test the classifier
test_feature_vector = getSVMFeatureVector(tweets, featureList)
test_feature_labels = getSVMFeatureVectorAndLabels(tweets, featureList)
print test_feature_vector
#p_labels contains the final labeling result
p_labels, p_accs, p_vals = svm_predict([0] * len(test_feature_vector),test_feature_vector, classifier,'-b 1')
print p_labels
#print test_feature_labels
#ACC, MSE, SCC = evaluations(y, p_labels)