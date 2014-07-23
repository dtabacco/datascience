import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #person = record[0]
    key = record[1]

    #key = (person, friend)
    #symkey = (friend, person)
   
    # Emit (Key as Identifier, value)
    
    #print key, record


    mr.emit_intermediate(key ,record)
    

    
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    #for v in list_of_values:
    #  total += v
    #print key, len(list_of_values) - 1
    
     JoinList = [] #Custom List
    #a.insert(0, x)
    
    #if key == "32":
     
    #totalIterations = len(list_of_values) - 1
     index = 0
   
     for i in list_of_values:   #Iterate for each join
       #JoinList.insert(0, list_of_values[0] + list_of_values[1])
      
       if index != 0: 
	 JoinList.insert(index, list_of_values[0] + list_of_values[index])
       index = index + 1
     for p in JoinList: 
       mr.emit((p))

    #mr.emit((list_of_values))
 #   if key == "32": 
#      mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
