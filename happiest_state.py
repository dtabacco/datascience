import sys
import json




def computeHappiestState(afinnfile, tweetfile):

    scores = {} # initialize an empty dictionary for term:score
    states = {} # initialize an empty dictionary for state:score
    
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    
    for i in tweetfile:
      
      tweetJSON = json.loads(i)	  # tweeetJSON is the whole tweet
     
      # Initialize Score to 0
      score = 0      

      for key, val in tweetJSON.items():

        #print key, 'corresponds to', val
        #print key  #word key is each key in
	#mystr = tweetJSON.get(key)
	#print key, ' corresponds to', tweetJSON[key]
	#encoded_string = mystr.encode('utf-8')

	if key == 'text':
           #print val.encode('utf-8')
	
           for valword in val.split(" "):
              #print valword.encode('utf-8')
	      if scores.has_key(valword):
                 score = score + scores.get(valword)
	


	if key == 'place':    # place is complex object
	  # print 'place is ',val  # print the full place object
	 
	    if val:   # only print places that are not null.  
	        
		#print 'place is ',val  # print the full place dictionary object
	        
		if 'US' in val.values():    # we only want to analyze the ones in US
		   #print 'United States'


		   # iterate through place dictionary
  	       	   for mykey, myval in val.items():   
		   #print mykey
		
		     if mykey == 'full_name':
		        #print myval.encode('utf-8')	
			
			city, state  = myval.split(",")
			
			state = state.strip()
			#print state
			
			if states.has_key(state):
			    states[state] = states.get(state) + score

			else:
			    states[state] = score

	     
	
      # Print the score of the Tweet (line)
      # print score

    # Clean up and remove USA from state field...a common error	    
    states.pop("USA")	
   	

    #for statekey, stateval in states.items():
	#   print statekey, stateval
    print keywithmaxval(states)
    
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    computeHappiestState(sent_file, tweet_file)

if __name__ == '__main__':
    main()
