def compress(data):
	encoder,entry = [],[]
	while len(data) != 0:
		temp = data[0]
		if temp in entry:
			while temp in entry and len(data) > 0:
				data = data[1:]
				temp += data[0]
			index = entry.index(temp[:len(temp)-1])
			encoder.append(str(index+1)+"."+temp[-1])
		else:encoder.append(str(0)+"."+temp)
		entry.append(temp)
		data = data[1:]
	return " ".join(encoder)

def decompress(data):
	data, entry = data.split(" "), []
	for x in data:
		y = x.split(".")
		if int(y[0]) == 0: entry.append(y[1])
		else: entry.append(entry[int(y[0])-1]+y[1])
	return "".join(entry)


d = "ABCDABCABCDAABCABCE"
d = "06e630440a27b380730a278078810dec41ea174877920a093b00dc95a7b1fc1a6e9744d557e23e8448ea16c1f3629713b803e723e001372facadb815449bf8b07fbd76213e2fd8f8c3d9b0aff645e9679163a075d9a8695d70d4063cd23ad811a6c7c1c606b4d932725782928d11c5cbdbf4220f1bef6f995633a22d85583590abcdefgh"
print(d == decompress(compress(d)))



# def old_decompress(data):
#
# 	entry = []
# 	while len(data) != 0:
# 		if int(data[0]) == 0:
# 			entry.append(data[1])
# 		else:
# 			pre = entry[int(data[0])-1]
# 			entry.append(pre+data[1])
# 		data = data[2:]
#
# 	return "".join(entry)
