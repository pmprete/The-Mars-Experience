from os.path import isfile, join
import os

#zoom lvl to merge 4,5...etc
download_zoom = 4

print("==[[SPACE MONKEYES!]]==")
print("Process starting...")

base_dir = "./"
tile_fromat = ".png"
if not os.path.exists(base_dir+"/Rows"):
    os.makedirs(base_dir+"/Rows")
base_dir = base_dir+"/"+str(download_zoom)
rows = [int(dir) for dir in os.listdir(base_dir) if not isfile(join(base_dir, dir)) and int(dir)]
rows.sort()
print("Merging columns...")
for r in rows:
    str_r = str(r)
    print("Row "+str_r+" >> ", end="")  
    cols = [f for f in os.listdir(base_dir+"/"+str_r) if isfile(join(base_dir+"/"+str_r, f)) and f.endswith(tile_fromat)]
    print("Merging {0} columns >> ".format(len(cols)), end="")    
    command = "convert -background none +append "+base_dir+"/"+str_r+"/*.png ./Rows/"+"{0:04d}".format(r)+tile_fromat
    os.system(command)
    print("OK!")
print("Finish merging columns!")

print("Merging rows (may take a while)...")
command = "convert -background none -append ./Rows/*"+tile_fromat+" ./merged_tiles"+tile_fromat
os.system(command) 
print("Finish merging rows!")

print("Process finished!")

print("==[[SPACE MONKEYES!]]==")