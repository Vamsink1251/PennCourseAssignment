def search(keyword) :

   # implement the function here
   
   for x in Thesaurus:
      if x.word == keyword:
         synonyms_list=x.synonyms
   
   synonyms_list.insert(0,keyword)
   result=[]
   for word in synonyms_list:
      count = 0
      for lst in Corpus:
         for j in lst:
            if j == word:
               count +=1
      result.append((word,count))
   return result # modify to return a list of tuples

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function

# output :[('happy', 16), ('glad', 2), ('pleased', 2), ('delighted', 2), ('joyous', 1)]
