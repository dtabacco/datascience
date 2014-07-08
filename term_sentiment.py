import sys
import json


def computeSentiment(afinnfile, tweetfile):
    scores = {} # initialize an empty dictionary
    
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    
    #tweetfile = open("output.txt")
    #NumberofLines = (len)(tf.readlines())
    #print NumberofLines

    #Iterate through each line in the tweet file
    for i in tweetfile:
      #print 'starting New Line' 
      #print 'checking Sentiment File against this line:  i is the line number'
      tweetJSON = json.loads(i)	  # tweeetJSON is the whole tweet
     
      # Initialize Score to 0
      score = 0      
     # learned = 0   # For Debugging - Keeps track of number of new terms learned

      newterms = {} # initialize an empty dictionary for unknown terms

      # Iterate through all the keys in a given line, we only care about the "text' key
      for key, val in tweetJSON.items():

        #print key, 'corresponds to', val
        #print key  #word key is each key in
	#mystr = tweetJSON.get(key)
	#print key, ' corresponds to', tweetJSON[key]
	#encoded_string = mystr.encode('utf-8')

        # Check to make sure there it's the text key, otherwise its not the tweet
	if key == 'text':
	
	   #print 'Found a Text key'
	   # Split up the tweet sentence into words
           for valword in val.split(" "):      
              
              # removes spaces and newlines and other things causing formatting errors
	      valword = valword.rstrip()
              valword = valword.strip()  
	      valword = valword.lstrip() 
             # print 'term', valword.encode('utf-8')   
	      		 
  
	      if len(valword) != 0:
		# print 'word not empty...proceeding'
		
	      	 if scores.has_key(valword):
                    score = score + scores.get(valword)
            	
   	         else:
		    #print 'Did not find Term in dictionary', valword.encode('utf-8')
		    # d['mynewkey'] = 'mynewvalue'
		    
		       #print 'term', valword.encode('utf-8'), 'is', len(valword) 
   	               newterms[valword] = 0   # Add new term to the dictionary with no value yet
		#       learned = learned + 1
            #  else:
		 # print 'Looks like we found an empty word'     

      # Print the score of the Tweet (line)
      #print score
      #print 'learned ', learned, ' new terms in this tweet'

      # If score is high, give stored terms a high score too...same for low
       
      #print 'printing all new terms'
      	
     

      if score > 3:
	 for term in newterms:
	    newterms[term] = 3
	    print term.encode('utf-8'), newterms.get(term)
	  

      if score == 3:
	 for term in newterms:
	    newterms[term] = 3
	    print term.encode('utf-8'), newterms.get(term)
 
      if score == 2:
	 for term in newterms:
	    newterms[term] = 2
	    print term.encode('utf-8'), newterms.get(term)
 
      if score == 1:
	 for term in newterms:
	    newterms[term] = 1
	    print term.encode('utf-8'), newterms.get(term) 
        
      if score == 0:
	 for term in newterms:
	    newterms[term] = 0
	    print term.encode('utf-8'), newterms.get(term)

      if score == -1:
	 for term in newterms:
	    newterms[term] = -1
	    print term.encode('utf-8'), newterms.get(term)
      
      if score == -2:
	 for term in newterms:
	    newterms[term] = -2
	    print term.encode('utf-8'), newterms.get(term)

      if score == -3:
	 for term in newterms:
	    newterms[term] = -3
	    print term.encode('utf-8'), newterms.get(term)

      if score < -3:
	 for term in newterms:
	    newterms[term] = -3
	    #print 'wow this must have been a BAD tweet', 'score=', score
	    print term.encode('utf-8'), newterms.get(term)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    computeSentiment(sent_file, tweet_file)

if __name__ == '__main__':
    main()
