import pandas as pd
import re
import string
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer 
nltk.download('stopwords')

class dataPreProcessing:
    def __init__(self,path):
        self.data=pd.read_csv(path,delimiter = ",",encoding='ISO-8859–1')
        self.data.columns = ((self.data.columns.str).replace("^ ","")).str.replace(" $","")   #removing cloumns spaces
        self.data["Article"].fillna("To be added", inplace = True)
        self.data["Headline"].fillna("To be added", inplace = True)       #replacing NaN values with some text
        self.data["Label"].fillna("To be added", inplace = True)
        self.data["Publisher"].fillna("To be added", inplace = True)
    def read_data(self):
        return self.data
    def clean_article(self,article):
        article=article.lower()
        article = re.sub('\[.*?\]', '', article)
        article = re.sub('[%s]' % re.escape(string.punctuation), '', article)
        article = re.sub('\w*\d\w*', '', article)
        return article
    def clean_dataset(self):
        for i in range(len(self.data)):
            self.data['Article'][i]=self.clean_article(self.data['Article'][i])
            self.data['Headline'][i]=self.clean_article(self.data['Headline'][i])
            self.data['Label'][i]=self.data['Label'][i].lower()
        return self.data
    def tokenize(self):
        pass
    def remove_stopwords(self):
        pass
        
data = dataPreProcessing('data/mohil.csv')                   #change will be here 
#data.read_data().shape           # for comparison of articles
#print(data.read_data().head()

def remove_stop_words(tokens):
    stopwordsInArticle=[]
    stopwordsNotInArticle=[]
    for i in tokens:
        if i not in stopwords.words('english'):
            stopwordsNotInArticle.append(i)
        else:
            stopwordsInArticle.append(i)
    return stopwordsInArticle,stopwordsNotInArticle

def lemmatise(tokens):
    lemmatizer = WordNetLemmatizer()
    for i in range(len(tokens)):
        tokens[i]=lemmatizer.lemmatize(tokens[i],"v")
    return tokens


#feature function  

def strongSubjectivtiy(string):

    file=open("data/bias-lexicon/subjandpolar.txt","r")

    for line in file:
        words=line.split()
        for word in words:
            if word == string:
                #print("found")
                #print(words[0] , words[2])
                if(words[0]=='type=strongsubj'):
                    return True
    return False
    file.close()

def strongSubjectivityContext(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(strongSubjectivtiy(article[index+1])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(strongSubjectivtiy(article[index+1])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index+2])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(strongSubjectivtiy(article[index-1])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(strongSubjectivtiy(article[index-1])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index-2])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(strongSubjectivtiy(article[index-2])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index-1])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index+1])):
            flag=True
            return flag
        if(strongSubjectivtiy(article[index+2])):
            flag=True
            return flag
    return flag


def weakSubjectivtiy(string):

    file=open("data/bias-lexicon/subjandpolar.txt","r")

    for line in file:
        words=line.split()
        for word in words:
            if word == string:
                #print("found")
                #print(words[0] , words[2])
                if(words[0]=='type=weaksubj'):
                    return True
    return False
    file.close()

def weakSubjectivityContext(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(weakSubjectivtiy(article[index+1])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(weakSubjectivtiy(article[index+1])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index+2])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(weakSubjectivtiy(article[index-1])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(weakSubjectivtiy(article[index-1])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index-2])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(weakSubjectivtiy(article[index-2])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index-1])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index+1])):
            flag=True
            return flag
        if(weakSubjectivtiy(article[index+2])):
            flag=True
            return flag
    return flag

def biasLexion(string):

    file=open("data/bias-lexicon/bias-lexicon.txt","r")

    for line in file:
        words=line.split()
        for word in words:
            if word == string:
                #print(word)
                #print(words[0] , words[2])
                return True
    return False
    file.close()

def positivewords(string):
    
    file=open("data/bias-lexicon/positive-words.txt","r")
    for line in file:
        words=line.split()
        positive = False
        if words[0] == string:
            positive = True
            return positive
        
    return positive
    file.close()


def positiveWordContext(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(positivewords(article[index+1])):
            flag=True
            return flag
        if(positivewords(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(positivewords(article[index+1])):
            flag=True
            return flag
        if(positivewords(article[index+2])):
            flag=True
            return flag
        if(positivewords(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(positivewords(article[index-1])):
            flag=True
            return flag
        if(positivewords(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(positivewords(article[index-1])):
            flag=True
            return flag
        if(positivewords(article[index-2])):
            flag=True
            return flag
        if(positivewords(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(positivewords(article[index-2])):
            flag=True
            return flag
        if(positivewords(article[index-1])):
            flag=True
            return flag
        if(positivewords(article[index+1])):
            flag=True
            return flag
        if(positivewords(article[index+2])):
            flag=True
            return flag
    return flag

def negativewords(string):
    
    file=open("data/bias-lexicon/negative-words.txt","r")
    for line in file:
        words=line.split()
        negative = False
        if words[0] == string:
            negative = True
            return negative
        
    return negative
    file.close()

def negativeWordContext(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(negativewords(article[index+1])):
            flag=True
            return flag
        if(negativewords(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(negativewords(article[index+1])):
            flag=True
            return flag
        if(negativewords(article[index+2])):
            flag=True
            return flag
        if(negativewords(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(negativewords(article[index-1])):
            flag=True
            return flag
        if(negativewords(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(negativewords(article[index-1])):
            flag=True
            return flag
        if(negativewords(article[index-2])):
            flag=True
            return flag
        if(negativewords(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(negativewords(article[index-2])):
            flag=True
            return flag
        if(negativewords(article[index-1])):
            flag=True
            return flag
        if(negativewords(article[index+1])):
            flag=True
            return flag
        if(negativewords(article[index+2])):
            flag=True
            return flag
    return flag

def factives_hooper(string):
    
    file=open("data/bias-lexicon/factives_hooper1975.txt","r")
    for line in file:
        words=line.split()
        factives = False
        if words[0] == string:
            factives = True
            return factives
        
    return factives
    file.close()

def factives_hooper_context(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(factives_hooper(article[index+1])):
            flag=True
            return flag
        if(factives_hooper(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(factives_hooper(article[index+1])):
            flag=True
            return flag
        if(factives_hooper(article[index+2])):
            flag=True
            return flag
        if(factives_hooper(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(factives_hooper(article[index-1])):
            flag=True
            return flag
        if(factives_hooper(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(factives_hooper(article[index-1])):
            flag=True
            return flag
        if(factives_hooper(article[index-2])):
            flag=True
            return flag
        if(factives_hooper(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(factives_hooper(article[index-2])):
            flag=True
            return flag
        if(factives_hooper(article[index-1])):
            flag=True
            return flag
        if(factives_hooper(article[index+1])):
            flag=True
            return flag
        if(factives_hooper(article[index+2])):
            flag=True
            return flag
    return flag

def hedges(string):
    file=open("data/bias-lexicon/hedges_hyland2005.txt","r")
    for line in file:
        words=line.split()
        hedge = False
        if words[0] == string:
            hedge = True
            return hedge
    return hedge
    file.close()

def hedges_context(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(hedges(article[index+1])):
            flag=True
            return flag
        if(hedges(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(hedges(article[index+1])):
            flag=True
            return flag
        if(hedges(article[index+2])):
            flag=True
            return flag
        if(hedges(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(hedges(article[index-1])):
            flag=True
            return flag
        if(hedges(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(hedges(article[index-1])):
            flag=True
            return flag
        if(hedges(article[index-2])):
            flag=True
            return flag
        if(hedges(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(hedges(article[index-2])):
            flag=True
            return flag
        if(hedges(article[index-1])):
            flag=True
            return flag
        if(hedges(article[index+1])):
            flag=True
            return flag
        if(hedges(article[index+2])):
            flag=True
            return flag
    return flag

def assertive_hooper(string):
    file=open("data/bias-lexicon/assertives_hooper1975.txt","r")
    for line in file:
        words=line.split()
        assertives = False
        if words[0] == string:
            assertives = True
            return assertives
    return assertives
    file.close()

def assertive_context(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(assertive_hooper(article[index+1])):
            flag=True
            return flag
        if(assertive_hooper(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(assertive_hooper(article[index+1])):
            flag=True
            return flag
        if(assertive_hooper(article[index+2])):
            flag=True
            return flag
        if(assertive_hooper(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(assertive_hooper(article[index-1])):
            flag=True
            return flag
        if(assertive_hooper(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(assertive_hooper(article[index-1])):
            flag=True
            return flag
        if(assertive_hooper(article[index-2])):
            flag=True
            return flag
        if(assertive_hooper(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(assertive_hooper(article[index-2])):
            flag=True
            return flag
        if(assertive_hooper(article[index-1])):
            flag=True
            return flag
        if(assertive_hooper(article[index+1])):
            flag=True
            return flag
        if(assertive_hooper(article[index+2])):
            flag=True
            return flag
    return flag

def report_verb(string):
    file=open("data/bias-lexicon/report_verbs.txt","r")
    for line in file:
        words=line.split()
        report = False
        if words[0] == string:
            report = True
            return report
    return report
    file.close()

def report_verb_context(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(report_verb(article[index+1])):
            flag=True
            return flag
        if(report_verb(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(report_verb(article[index+1])):
            flag=True
            return flag
        if(report_verb(article[index+2])):
            flag=True
            return flag
        if(report_verb(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(report_verb(article[index-1])):
            flag=True
            return flag
        if(report_verb(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(report_verb(article[index-1])):
            flag=True
            return flag
        if(report_verb(article[index-2])):
            flag=True
            return flag
        if(report_verb(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(report_verb(article[index-2])):
            flag=True
            return flag
        if(report_verb(article[index-1])):
            flag=True
            return flag
        if(report_verb(article[index+1])):
            flag=True
            return flag
        if(report_verb(article[index+2])):
            flag=True
            return flag
    return flag


def implicative_verb(string):
    file=open("data/bias-lexicon/implicatives_karttunen1971.txt","r")
    for line in file:
        words=line.split()
        implicative = False
        if words[0] == string:
            implicative = True
            return implicative
    return implicative
    file.close()

def implicative_verb_context(article,word,index):
    length=len(article)-1
    flag=False
    if index==0:
        if(implicative_verb(article[index+1])):
            flag=True
            return flag
        if(implicative_verb(article[index+2])):
            flag=True
            return flag
    if index==1:
        if(implicative_verb(article[index+1])):
            flag=True
            return flag
        if(implicative_verb(article[index+2])):
            flag=True
            return flag
        if(implicative_verb(article[index-1])):
            flag=True
            return flag
    if index==length:
        if(implicative_verb(article[index-1])):
            flag=True
            return flag
        if(implicative_verb(article[index-2])):
            flag=True
            return flag
    if index==length-1:
        if(implicative_verb(article[index-1])):
            flag=True
            return flag
        if(implicative_verb(article[index-2])):
            flag=True
            return flag
        if(implicative_verb(article[index+1])):
            flag=True
            return flag
    if index>1 and index<length-1:
        if(implicative_verb(article[index-2])):
            flag=True
            return flag
        if(implicative_verb(article[index-1])):
            flag=True
            return flag
        if(implicative_verb(article[index+1])):
            flag=True
            return flag
        if(implicative_verb(article[index+2])):
            flag=True
            return flag
    return flag

def pos(string):
    tagged = nltk.pos_tag([string])
    #print(tagged[0][1])
    return tagged[0][1]
    
def posNeg1(article,index):
    if index==0:
        return 'none'
    else:
        string=article[index-1]
        tagged = nltk.pos_tag([string])
        return tagged[0][1]
    
def posNeg2(article,index):
    if index==0 or index==1:
        return 'none'
    else:
        string=article[index-2]
        tagged = nltk.pos_tag([string])
        return tagged[0][1]
def pos1(article,index):
    length=len(article)-1
    if index==length:
        return 'none'
    else:
        string=article[index+1]
        tagged = nltk.pos_tag([string])
        return tagged[0][1]
def pos2(article,index):
    length=len(article)-1
    if index==length or index==length-1:
        return 'none'
    else:
        string=article[index+1]
        tagged = nltk.pos_tag([string])
        return tagged[0][1]



result={
        'Hedge':[],
        'HedgeContext':[],
        'FativeVerb':[],
        'FactiveVerbContext':[],
        'AssertiveVerb':[],
        'AssertiveVerbContext':[],
        'ImplicativeVerb':[],
        'ImplicativeVerbContext':[],
        'ReportVerb':[],
        'ReportVerbContext':[],
        'StrongSub':[],
        'StrongSubContext':[],
        'WeakSub':[],
        'WeakSubContext':[],
        'PositiveWord':[],
        'PositiveWordContext':[],
        'NegativeWord':[],
        'NegativeWordContext':[],
        'BiasLexicon':[]
}
size=data.read_data().shape[0]
for j in range(size):
    #data.clean_dataset()['Article'][i]
    article=data.clean_dataset()['Article'][j]
    tokens=word_tokenize(article)
    stopwordsInArticle,stopwordsNotInArticle=remove_stop_words(tokens)
    stopwordsNotInArticle=lemmatise(stopwordsNotInArticle)
    features = {
            'word':[],
            'POS':[],
            'POSNeg1':[],
            'POSNeg2':[],
            'POS1':[],
            'POS2':[],
            'Hedge':[],
            'HedgeContext':[],
            'FativeVerb':[],
            'FactiveVerbContext':[],
            'AssertiveVerb':[],
            'AssertiveVerbContext':[],
            'ImplicativeVerb':[],
            'ImplicativeVerbContext':[],
            'ReportVerb':[],
            'ReportVerbContext':[],
            'StrongSub':[],
            'StrongSubContext':[],
            'WeakSub':[],
            'WeakSubContext':[],
            'PositiveWord':[],
            'PositiveWordContext':[],
            'NegativeWord':[],
            'NegativeWordContext':[],
            'BiasLexicon':[]
    }

    for i in range(len(stopwordsNotInArticle)):
        features['word'].append(stopwordsNotInArticle[i])
        features['POS'].append(pos(stopwordsNotInArticle[i]))
        features['POSNeg1'].append(posNeg1(stopwordsNotInArticle,i))
        features['POSNeg2'].append(posNeg2(stopwordsNotInArticle,i))
        features['POS1'].append(pos1(stopwordsNotInArticle,i))
        features['POS2'].append(pos2(stopwordsNotInArticle,i))
        features['Hedge'].append(hedges(stopwordsNotInArticle[i]))
        features['HedgeContext'].append(hedges_context(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['FativeVerb'].append(factives_hooper(stopwordsNotInArticle[i]))
        features['FactiveVerbContext'].append(factives_hooper_context(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['AssertiveVerb'].append(assertive_hooper(stopwordsNotInArticle[i]))
        features['AssertiveVerbContext'].append(assertive_context(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['ImplicativeVerb'].append(implicative_verb(stopwordsNotInArticle[i]))
        features['ImplicativeVerbContext'].append(implicative_verb_context(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['ReportVerb'].append(report_verb(stopwordsNotInArticle[i]))
        features['ReportVerbContext'].append(report_verb_context(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['StrongSub'].append(strongSubjectivtiy(stopwordsNotInArticle[i]))
        features['StrongSubContext'].append(strongSubjectivityContext(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['WeakSub'].append(weakSubjectivtiy(stopwordsNotInArticle[i]))
        features['WeakSubContext'].append(weakSubjectivityContext(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['PositiveWord'].append(positivewords(stopwordsNotInArticle[i]))
        features['PositiveWordContext'].append(positiveWordContext(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['NegativeWord'].append(negativewords(stopwordsNotInArticle[i]))
        features['NegativeWordContext'].append(negativeWordContext(stopwordsNotInArticle,stopwordsNotInArticle[i],i))
        features['BiasLexicon'].append(biasLexion(stopwordsNotInArticle[i]))

    #features
    df = pd.DataFrame(features, columns = [
            'word',
            'POS',
            'POSNeg1',
            'POSNeg2',
            'POS1',
            'POS2',
            'Hedge',
            'HedgeContext',
            'FativeVerb',
            'FactiveVerbContext',
            'AssertiveVerb',
            'AssertiveVerbContext',
            'ImplicativeVerb',
            'ImplicativeVerbContext',
            'ReportVerb',
            'ReportVerbContext',
            'StrongSub',
            'StrongSubContext',
            'WeakSub',
            'WeakSubContext',
            'PositiveWord',
            'PositiveWordContext',
            'NegativeWord',
            'NegativeWordContext',
            'BiasLexicon']
            )

    for col in df.columns:
        if col!='word' and col!='POS' and col!='POSNeg1' and col!='POSNeg2' and col!='POS1' and col!='POS2':
            df[col]=df[col]*1
    r,c = df.shape

    for col in df.columns:
        if col!='word' and col!='POS' and col!='POSNeg1' and col!='POSNeg2' and col!='POS1' and col!='POS2':
            result[col].append((df[col].sum()/r)*100)
            

df_result = pd.DataFrame(result, columns = [
        'Hedge',
        'HedgeContext',
        'FativeVerb',
        'FactiveVerbContext',
        'AssertiveVerb',
        'AssertiveVerbContext',
        'ImplicativeVerb',
        'ImplicativeVerbContext',
        'ReportVerb',
        'ReportVerbContext',
        'StrongSub',
        'StrongSubContext',
        'WeakSub',
        'WeakSubContext',
        'PositiveWord',
        'PositiveWordContext',
        'NegativeWord',
        'NegativeWordContext',
        'BiasLexicon']
        )
print(df_result)
df_result.to_csv('mohil_result.csv')
