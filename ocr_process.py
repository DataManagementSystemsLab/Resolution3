import os
import shutil
import json
import ocrmypdf
import common as c


def ocr2(input, output, ocring):
    if (ocring):
            try:
                print("OCR "+ input)
                ocrmypdf.ocr(input, output, deskew=True)
            except:
                return False, ""    
    if (os.path.exists(output)):
            txt=c.convert(output)
            txt=txt.strip()
            if len(txt)==0:
                    print ("File "+input+ " is empty")
                    return False, ""
    else:
        return False,  ""                
    return True, txt                     

# Load the list of filenames from empty.json
def ocr(json_file):
    with open(json_file) as f:
            filenames = json.load(f)
            empty2=[]
            # Set the source and destination directories
            src_dir = 'files'
            dst_dir = 'files1'

            # Iterate through the list of filenames
            for filename in filenames:
                        # Construct the full path to the file in the source directory
                        base, extension = os.path.splitext(filename)
                        print("========="+ base +"=======")
                        src_path = os.path.join(src_dir, filename)
                        # Construct the full path to the destination location
                        dst_path = os.path.join(dst_dir, filename)
                        # Create the destination directory if it doesn't exist
                        f,txt=ocr2(src_path,dst_path,False)
                        txtfilename="txts/"+base+".txt"
                        if f==False:
                            f,txt=ocr2(src_path,dst_path,True)
                            if f:
                                with open(txtfilename, 'w') as tmpf:
                                    tmpf.write(txt)
                            else:    
                                empty2.append(filename)
                        else: 
                            with open(txtfilename, 'w') as tmpf:
                                tmpf.write(txt)

            print(empty2)
            # Open a file for writing
            with open('empty22.json', 'w') as f2:
                # Write the list to the file in JSON format
                json.dump(empty2, f2)
            print('Finished OCR files!')
