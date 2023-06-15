import psutil

def make_graph(values, heigth, col_width) -> str:
	ratio=100//heigth
	out=""

	print("ratio ",ratio)
	
	for i in range(0, len(values)):
		
		print("orig ", values[i],end="")
		print(" mod ", values[i]%ratio,end="")
		if(values[i]%ratio//2>=ratio//2):
			values[i]+=ratio-values[i]%ratio
		else:
			values[i]-=values[i]%ratio
		print(" val ",values[i])

	for i in range(heigth-1,-1,-1):
		print(i*ratio)
		for j in range(0,len(values)):
			if values[j]==i*ratio or (values[j]//ratio>=heigth and i==heigth-1):
				out+="#"*col_width  
			else: 
				out +="⠀"*col_width
		out+="\n"

	print(values)	


	return out        

#val=[60,40,20,0,100,23]

#print(make_graph(values=val,heigth=50,col_width=5))
