# empty list which will 
# contain all trending news articles' titles
titles=[]

# empty list which will 
# contain all trending news articles' descriptions
descriptions = [] 

for ar in article: 
	titles.append(ar["title"]) 
	
for ar in article: 
	descriptions.append(ar["description"]) 
