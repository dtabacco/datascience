import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def computeSentiment(afinnfile, tweetfile):
    #afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    
    #tweetfile = open("output.txt")
    #NumberofLines = (len)(tf.readlines())
    #print NumberofLines
    for i in tweetfile:
      #print 'checking Sentiment File against this line:  i is the line number'
      tweetJSON = json.loads(i)	  # tweeetJSON is the whole tweet
     
      # Initialize Score to 0
      score = 0      

      #for key in tweetJSON:
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
   

      # Print the score of the Tweet (line)
      print score
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    computeSentiment(sent_file, tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
