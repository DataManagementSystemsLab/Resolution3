f_file = open("res.json", "r")
res = json.load(f_file)


f_file = open("files.json", "r")
files = json.load(f_file)


def sort_items(items):
    return sorted(items, key=lambda x: [s for s in x])


d={}
for r in res:
	v=res[r]
	ht={}
	ht["parent"]=v["parent"]
	ht["txt"]=v["txt"]
	try:
		ht["url"]=files[v["key"]]["selfLink"]
	except:
		ht["url"]=""	
	d[v["key"]]=ht

a_file = open("d.json", "w")
json.dump(d, a_file)