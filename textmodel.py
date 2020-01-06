#
# finalproject.py  (Milestone)
#
# Cuckcoo's Calling book checker  
#

import math
def clean_text(txt):
    """returns a list containing the words in txt after it has been “cleaned”"""
    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('?', '')
    txt = txt.replace(':', '')
    txt = txt.replace(';', '')
    txt = txt.replace('!', '')
    txt = txt.replace('-', '')
    txt = txt.replace('(', '')
    txt = txt.replace(')', '')
    txt = txt.lower()
    txt = txt.split()
    return txt
def sample_file_write(filename):
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.
        
def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)


def sentencesplitter(txt):
    """returns a list containing sentences"""
    txt = txt.replace('Mr. ', '')
    txt = txt.replace('Mrs. ', '')
    txt = txt.replace('Dr. ', '')
    txt = txt.replace('A.', '')
    txt = txt.replace('B.', '')
    txt = txt.replace('C.', '')
    txt = txt.replace('D.', '')
    txt = txt.replace('J.', '')
    txt = txt.replace('K.', '')
    txt = txt.replace('R.', '')
    txt = txt.replace('G.', '')
    txt = txt.replace('  ',' ')
    txt = txt.lower()
    txt = txt.replace('!', '**').replace('?','**').replace('.','**').split('**')
    txt = txt[:-1]
    return txt

#def stem(s):
#    """return the stem of word"""
#    if len(s) <= 3:
#        s = s
#    elif s[-3:] == 'ing':
#        if len(s) <= 4:
#            s = s
#        elif s[-4] == s[-5]:
#            s = s[:-4]
#        else:
#            s = s[:-3]
#    elif s[-3:] == 'ers':
#        if len(s) >= 5:
#            if s[-4] == s[-5]:
#                s = s[:-4]
#            else:
#                s = s[:-3]
#    elif s[-2:] == 'er':
#        s = s[:-2]
#    elif s[-3:] == 'ies':
#        s = s[:-2]
#    elif s[-2:] == 'ed':
#        if len(s) <= 4:
#            s = s
#        elif s[-3] == s[-4]:
#            s = s[:-3]
#        else:
#            s = s[:-2]
#    elif s[-1] == 'e':
#        s = s[:-1]
#    elif s[-4:] == 'tion':
#        s = s[:3] + 'e'
#    elif s[-1] == 'y':
#        s = s[:-1] + 'i'
#    elif s[-1] == 's':
#        if s[-1] == s[-2]:
#            s = s
#        else:
#            s = s[:-1]
#    if len(s) <= 4:
#        s = s
#    elif s[:3] == 'auto':
#        s = s[3:]
#    elif s[:2] == 'dis':
#        s = s[2:]
#    elif s[1] == 'il':
#        s = s[1:]
#    return s
def stem(s):
    """return the stem of words"""
    if s[-3:] in ['ing', 'cal', 'ful', 'ary', 'ish']:
        if len(s) > 6:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
    elif s[-2:] == 'er':
        if len(s) > 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
    elif s[-1:] == 's':
        if len(s) > 4:
            if s[-3:] == 'ies':
                s = s[:-2]
            else:
                s = s[:-1]
    elif s[-3:] == 'est':
        if len(s) > 6:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
    elif s[-2:] == 'ed':
        if len(s) > 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
    elif s[-2:] == 'ly':
        if len(s) > 5:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
    elif s[-1:] == 'y':
        s = s[:-1] + 'i'
    elif s[-1:] == 'e':
        s = s[:-1]
    elif s[-4:] in ['tion', 'able', 'ment']:
        if len(s) > 5:
            s = s[:-4]
    return s

def adverb(s):
    """chooses all adverbs ending in ly"""
    if s[-2:] == 'ly':
        s = s
    else:
        s = None 
    return s

def compare_dictionaries(d1, d2):
    """compare dictionaries and gives similarity score"""
    score = 0
    total = 0
    for key in d1:
        total += d1[key]
    for key2 in d2:
        if key2 in d1:
            score += d2[key2] * math.log(d1[key2] / total)
        else:
            score += d2[key2] * math.log(0.5 / total)
    return score
           
    
class TextModel:
    def __init__(self, model_name):
        """contructs new TextModel object by accepting a string model_name"""
        self.name = str(model_name) #the name
        self.words = {} #all the types of words
        self.word_lengths = {} #lengths and top length count
        self.stems = {} #all the stems
        self.sentence_lengths = {} #sentence lengths and all their counts
        self.lyadverbs = {} # counts number of adverbs ending in ly
    def __repr__(self):
        """returns a string that includes the name of the model as well as the sizes of dictionaries"""
    
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += "  number of word lengths: " + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of ly_adverbs: ' + str(len(self.lyadverbs)) + '\n'
        return s
        
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!
        
        sentencesplit = sentencesplitter(s)
        for sentence in sentencesplit:
            count = len(sentence.split())
            if str(count) in self.sentence_lengths:
                self.sentence_lengths[count] += 1
            else:
                self.sentence_lengths[count] = 1
        word_list = clean_text(s)
    
        # Template for updating the words dictionary.
        for w in word_list:
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair.
            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1
            length = len(w)
            # Add code to update other feature dictionaries.
            if length in self.word_lengths:
                self.word_lengths[length] += 1
            else:
                self.word_lengths[length] = 1
            eachstem = stem(w)
            if eachstem in self.stems:
                self.stems[eachstem] += 1
            else:
                self.stems[eachstem] = 1
            sellectadverbs = adverb(w)
            if sellectadverbs in self.lyadverbs:
                self.lyadverbs[sellectadverbs] += 1
            else:
                self.lyadverbs[sellectadverbs] = 1 
            if None in self.lyadverbs:
                del self.lyadverbs[None]
    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model. It should not explicitly return a value."""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)
    def save_model(self):
        """writing its various feature dictionaries to files"""
        file1 = open((self.name + '_' + 'words'), 'w')
        f2 = open((self.name + '_' + 'word_lengths'), 'w')
        f3 = open((self.name + '_' + 'stems'), 'w')
        f4 = open((self.name + '_' + 'sentence_lengths'), 'w')
        f5 = open((self.name + '_' + 'lyadverbs'), 'w')

        file1.write(str(self.words))
        f2.write(str(self.word_lengths))
        f3.write(str(self.stems))
        f4.write(str(self.sentence_lengths))
        f5.write(str(self.lyadverbs))

        file1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
    def read_model(self):
        """reads stored dictionaries """
        file1 = open((self.name + '_' + 'words'), 'r')
        f2 = open((self.name + '_' + 'word_lengths'), 'r')
        f3 = open((self.name + '_' + 'stems'), 'r')
        f4 = open((self.name + '_' + 'sentence_lengths'), 'r')
        f5 = open((self.name + '_' + 'lyadverbs'), 'r')

        dict_str1 = file1.read()
        dict_str2 = f2.read()
        dict_str3 = f3.read()
        dict_str4 = f4.read()
        dict_str5 = f5.read()

        file1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
                
        self.words = eval(dict_str1)
        self.word_lengths = eval(dict_str2)
        self.stems = eval(dict_str3)
        self.sentence_lengths = eval(dict_str4)
        self.lyadverbs = eval(dict_str5)
    def similarity_scores(self, other):
        """returns a list of log similarity scores measuring the similarity of self and other """
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        ly_adverbs_score = compare_dictionaries(other.lyadverbs, self.lyadverbs)
        score_lst = [word_score, word_lengths_score, stems_score, sentence_lengths_score, ly_adverbs_score]
        
        return score_lst
    def classify(self, source1, source2):
        """compares the called TextModel object (self) to two other “source” TextModel objects (source1 and source2)
        and determines which of these other TextModels is the more likely source of the called TextModel"""
        score1 = self.similarity_scores(source1)
        score2 = self.similarity_scores(source2)
        print('scores for source1: ', score1)
        print('scores for source2: ', score2)
        similarityone = 0
        similaritytwo = 0
        if score1[0] > score2[0]:
            similarityone += 1
        else:
            similaritytwo += 1
        if score1[1] > score2[1]:
            similarityone += 1
        else:
            similaritytwo += 1
        if score1[2] > score2[2]:
            similarityone += 1
        else:
            similaritytwo += 1
        if score1[3] > score2[3]:
            similarityone += 1
        else:
            similaritytwo += 1
        if score1[4] > score2[4]:
            similarityone += 1
        else:
            similaritytwo += 1
        if similarityone > similaritytwo:
            print(self.name, 'is more likely to have come from', source1.name)
        else:
            print(self.name, 'is more likely to have come from', source2.name)
def run_tests():
    """ classifies different text"""
    source1 = TextModel('rowling')
    source1.add_file('rowling_source_text.txt')

    source2 = TextModel('shakespeare')
    source2.add_file('shakespeare_source_text.txt')

    new1 = TextModel('wr100')
    new1.add_file('wr100_source_text.txt')
    new1.classify(source1, source2)
    
    
    
    sourc1 = TextModel('HIMYM')
    sourc1.add_file('HIMYM.txt')

    sourc2 = TextModel('FRIENDS')
    sourc2.add_file('FRIENDS.txt')

    new2 = TextModel('wr101')
    new2.add_file('wr101_source_text.txt')
    new2.classify(sourc1, sourc2)
    
    
    
    sour1 = TextModel('rowling')
    sour1.add_file('rowling_source_text.txt')

    sour2 = TextModel('shakespeare')
    sour2.add_file('shakespeare_source_text.txt')

    new3 = TextModel('wr102')
    new3.add_file('wr102_source_text.txt')
    new3.classify(sour1, sour2)
    
    
    
    sou1 = TextModel('rowling')
    sou1.add_file('rowling_source_text.txt')

    sou2 = TextModel('shakespeare')
    sou2.add_file('shakespeare_source_text.txt')

    new4 = TextModel('wr103')
    new4.add_file('wr103_source_text.txt')
    new4.classify(sou1, sou2)
