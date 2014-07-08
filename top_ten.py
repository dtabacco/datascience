import sys
import json


def computeTopTen(tweetfile):
    
    hashtags = {} # initialize an empty dictionary hashtag:frequency
    scores = {} 
    entitiesParser = {} 

    #Iterate through each line in the tweet file
    for i in tweetfile:
      tweetJSON = json.loads(i)	  # tweeetJSON is the whole tweet
     
     

     # newterms = {} # initialize an empty dictionary for unknown terms

      # Iterate through all the keys in a given line, we only care about the "text' key
      for key, val in tweetJSON.items():
        #print key

        if key == 'entities':
              
            # print val
	     
	     # iterate through User dictionary to get entities
  	     for mykey, myval in val.items():   
	        # print mykey
		
                 if mykey == 'hashtags':
		      
			if myval:
			   #print myval
			   
			   for hashdict in myval:    #iterate through the List       
			      #print hashdict
                             
                              for hashkey, hashval in hashdict.items():
            			 # print hashkey
				  
				  if hashkey == 'text':
				     hashval = hashval.strip()
				    # print hashval.encode('utf-8') 
				     
				     if hashtags.has_key(hashval):
					hashtags[hashval] = hashtags.get(hashval) + 1;
				     
				     else:
   	              			hashtags[hashval] = 1   # Add new hashtag to the dictionary for first time


        # Check to make sure there it's the text key, otherwise its not the tweet
	if key == 'text':

	   # Split up the tweet sentence into words
           for valword in val.split(" "):      
              
              # removes spaces and newlines and other things causing formatting errors
	      valword = valword.rstrip()
              valword = valword.strip()  
	      valword = valword.lstrip() 
             #print 'term', valword.encode('utf-8')   
	      		 
	      if len(valword) != 0:
		# print 'word not empty...proceeding'
		
	      	 if scores.has_key(valword):
                    #score = score + scores.get(valword)
		 #   print 'This word already appeared', scores.get(valword) 
		    scores[valword] = scores.get(valword) + 1;
		#    print 'This word has now appeared', scores.get(valword)  
            	
   	         else:
   	              scores[valword] = 1   # Add new term to the dictionary for first time
		    #  print 'This word has now appeared', scores.get(valword)  
            #  else:
		 # print 'Looks like we found an empty word'     

      # Print the score of the Tweet (line)
      
      #print 'printing all new terms'
      	
    #for hashterms, freq in hashtags.items():
       #print hashterms.encode('utf-8'), freq

    for tag, count in sorted(hashtags.iteritems(), key=lambda (k, v): (-v, k))[:10]:
        print tag.encode('utf-8'), count


def main():
    tweet_file = open(sys.argv[1])
    computeTopTen(tweet_file)

if __name__ == '__main__':
    main()
