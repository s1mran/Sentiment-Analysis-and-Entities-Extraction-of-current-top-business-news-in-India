nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# function to find entities of interest in sent 
def EntitiesOfInterest(sent):
    grammar = r"""
    NBAR:
        # Nouns and Adjectives, terminated with Nouns
        {<NN.*>*<NN.*>}

    NP:
        {<NBAR>}
        # Above, connected with in/of/etc...
        {<NBAR><IN><NBAR>}
    """
    chunker = nltk.RegexpParser(grammar)
    res = []
    chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sent)))
    for tree in chunk.subtrees(filter=lambda t: t.label() == 'NP'):
        res.append(' '.join([child[0] for child in tree.leaves()]))
    s= "[ "
    j=res[len(res)-1]
    for i in res:
        s= s+ "'" + i +"'"
        if i!=j:
            s=s+", "
            
    s=s+" ]"
    print s	
    
for i in range(10): 
	# printing entities of each news:
        print(str(i+1)+" "+titles[i])
        # entities of interest
        print("Entities of interest: ")
        EntitiesOfInterest(descriptions[i])
        
        
	
				 
