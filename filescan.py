import os, hashlib, sys

scanpath = '.'
if sys.argv[1:]:
    scanpath = sys.argv[1:][0]
prev_scan = 'prev_scan.txt'
modified =  0
files = {}
prev_files = {}

if os.path.isfile(prev_scan):
    with open(prev_scan, 'r') as f:
        prev_files = eval(f.read())
else:
    with open('myfile.dat', 'w+') as f:
        f.write("%s" % {})
# r=root, d=directories, f = files
for r, d, f in os.walk(scanpath):
    # print(f)
    for file in f:
        # print(file)
        fileinfo = {os.path.join(r, file) : hashlib.md5(open(os.path.join(r, file),'rb').read()).hexdigest()} # hashlib.sha256(os.path.join(r, file).encode('utf-8')).hexdigest()}
        # print(fileinfo)
        files.update(fileinfo)

# print(files)
# check if any new files are added
addchange = set(files) - set(prev_files)
for i in addchange:
    modified += 1
    print('N {} {}'.format(i, os.path.getsize(i)))

# check if any files are deleted since last run
delchange = set(prev_files) - set(files)
for i in delchange:
    modified += 1
    print('D {}'.format(i))

if len(addchange) >= 1 and len(delchange) >= 1:
    for z in addchange:
        # print(z)
        # hashlib.md5(open(os.path.join(r, z),'rb').read()).hexdigest()
        # print(files)
        for file, filehash in prev_files.items():
            # print(file, filehash)
            # print(hashlib.md5(open(z,'rb').read()).hexdigest())
            if filehash == hashlib.md5(open(z,'rb').read()).hexdigest():
                print('M {} -> {}'.format(z, file))

# print(files)
with open('prev_scan.txt', 'w') as f:
    # for item in files:
        f.write("%s" % files)
print('Total files scanned: {}'.format(len(files)))
print('Total files modified: {}'.format(modified))
