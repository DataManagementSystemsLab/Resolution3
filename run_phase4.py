import json

f_file = open("resolution.json", "r")
res = json.load(f_file)


f_file = open("files.json", "r")
files = json.load(f_file)


def sort_items(items):
    return sorted(items, key=lambda x: [s for s in x])

ar=[]
d={}
for r in res:
	v=res[r]
	ht={}
	ht["parent"]=v["parent"]
	ht["txt"]=v["txt"]
	try:
		val=v["key"]
		if val in files.keys():
			ht["url"]=files[val]["selfLink"]
		else:
			val=val.split('.')
			val=val[0]
			ht["url"]=files[val]["selfLink"]
	except:
		ht["url"]=""
		ar.append(v["key"])
	d[v["key"]]=ht



a_file = open("d.json", "w")
json.dump(d, a_file)
