import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

    #[sequence id, nucleotides]
    seq_id = record[0]
    nucleotides = record[1]

    #print seq_id
    #trim_nucleotides = nucleotides[len(nucleotides) - 10]
    
    trim_nucleotides_factor = len(nucleotides) - 10
    
    # Substring - start at beginning and go to int 	
    trim_nucleotides = nucleotides[:trim_nucleotides_factor]
	
    #print seq_id, len(nucleotides), len(trim_nucleotides) 
    
    #mr.emit_intermediate(seq_id , trim_nucleotides)
    mr.emit_intermediate(trim_nucleotides, seq_id)
    

    
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    #for v in list_of_values:
    #  total += v
    
    #print key, len(list_of_values) 
    #if len(list_of_values) == 1: 
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
