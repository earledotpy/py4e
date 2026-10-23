fname = input("Enter the file name: ")
cnt = 0
ttl = 0
try:
    fh = open(fname)
except: 
    print('File cannot be opened:', fname)
    exit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence: "):
        continue
    cnt = cnt + 1
    cpos = line.find(':')
    conf = line[cpos+1:].strip()
    try:
        val = float(conf)
    except:
        continue
    ttl = ttl + val

else:
    ##print(cnt)
    print('Average spam confidence:', ttl / cnt)
