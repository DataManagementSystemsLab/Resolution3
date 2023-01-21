import json
import common as c


f_file = open("files.json", "r")
files = json.load(f_file)


pdfs=c.get_pdfs(files)
docs=c.get_docs(files)
folders=c.get_folders(files)
others=c.get_others(files)

resfiles,failed,empty=c.get_resolutions2(files, "/home/ubuntu/Resolution2/files/")

#resfiles,failed=c.get_resolutions2(files)
#txts=c.get_content_files(files)


# Convert the data to a JSON string
json_data = json.dumps(resfiles)

# Save the JSON string to a file
with open('resfiles.json', 'w') as f:
  f.write(json_data)

json_data = json.dumps(failed)

# Save the JSON string to a file
with open('failed.json', 'w') as f:
  f.write(json_data)  

json_data = json.dumps(empty)

# Save the JSON string to a file
with open('empty.json', 'w') as f:
  f.write(json_data)  


#c.get_contents("files", files, txts)
