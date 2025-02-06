
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys







my_hash_table = HashTable()

my_hash_table.print_table()



# def one(mylist, key):
# 	total = 0
# 	for i in range(len(mylist)):
# 		for j in range(i+1,len(mylist)):
# 			if i != j:
# 				if mylist[i] + mylist[j] == key:
# 					total += 1
# 	return total

# def two(mylist, key):
# 	total = 0
# 	mylist.sort()
# 	i = 0
# 	j = len(mylist)-1
# 	while (i < j):
# 		if(mylist[i] + mylist[j] < key):
# 			i+=1
# 		elif(mylist[i] + mylist[j] > key):
# 			j-=1
# 		else:
# 			total += 1
# 			i+=1
# 			j-=1
# 	return total

# def three(mylist, key):
# 	items={}
# 	total = 0
# 	for number in mylist:
# 		items[number]=1
# 	for number in mylist:
# 		other = key-number
# 		if(other in items):
# 			total+=1
# 	return total//2
    

