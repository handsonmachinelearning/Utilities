from collections import Counter
import json

class Vocabulary:
    
    def __init__(self, vocabulary, wordFrequencyFilePath):
        self.vocabulary = vocabulary
        self.BAG_OF_WORDS_FILE_FULL_PATH = wordFrequencyFilePath
        self.input_word_index = {}
        self.reverse_input_word_index = {}
        
        self.input_word_index["START"] = 1
        self.input_word_index["UNKOWN"] = -1
        self.MaxSentenceLength = None
        
    def PrepareVocabulary(self,reviews):
        self._prepare_Bag_of_Words_File(reviews)
        self._create_Vocab_Indexes()
        
        self.MaxSentenceLength = max([len(txt.split(" ")) for txt in reviews])
      
    def Get_Top_Words(self, number_words = None):
        if number_words == None:
            number_words = self.vocabulary
        
        chars = json.loads(open(self.BAG_OF_WORDS_FILE_FULL_PATH).read())
        counter = Counter(chars)
        most_popular_words = {key for key, _value in counter.most_common(number_words)}
        return most_popular_words
    
    def _prepare_Bag_of_Words_File(self,reviews):
        counter = Counter()    
        for s in reviews:
            counter.update(s.split(" "))
            
        with open(self.BAG_OF_WORDS_FILE_FULL_PATH, 'w') as output_file:
            output_file.write(json.dumps(counter))
                 
    def _create_Vocab_Indexes(self):
        INPUT_WORDS = self.Get_Top_Words(self.vocabulary)

        #word to int
        #self.input_word_index = dict(
        #    [(word, i) for i, word in enumerate(INPUT_WORDS)])
        for i, word in enumerate(INPUT_WORDS):
            self.input_word_index[word] = i
        
        #int to word
        #self.reverse_input_word_index = dict(
        #    (i, word) for word, i in self.input_word_index.items())
        for word, i in self.input_word_index.items():
            self.reverse_input_word_index[i] = word

        #self.input_word_index = input_word_index
        #self.reverse_input_word_index = reverse_input_word_index
        #seralize.dump(config.DATA_FOLDER_PATH+"input_word_index.p",input_word_index)
        #seralize.dump(config.DATA_FOLDER_PATH+"reverse_input_word_index.p",reverse_input_word_index)
        
        
    def TransformSentencesToId(self, sentences):
        vectors = []
        for r in sentences:
            words = r.split(" ")
            vector = np.zeros(len(words))

            for t, word in enumerate(words):
                if word in self.input_word_index:
                    vector[t] = self.input_word_index[word]
                else:
                    pass
                    #vector[t] = 2 #unk
            vectors.append(vector)
            
        return vectors
    
    def ReverseTransformSentencesToId(self, sentences):
        vectors = []
        for r in sentences:
            words = r.split(" ")
            vector = np.zeros(len(words))

            for t, word in enumerate(words):
                if word in self.input_word_index:
                    vector[t] = self.input_word_index[word]
                else:
                    pass
                    #vector[t] = 2 #unk
            vectors.append(vector)
            
        return vectors
