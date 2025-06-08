raw_data = [5, "22", None, 8.4, "", 0]  

# Clean data: remove non-ints, convert to int  
new_data = []
for x in raw_data:
    if x==0:
        new_data.append(x)
    elif not x:
        pass
    else:
        try:
            int(x)
            new_data.append(x)
        except TypeError:
            pass
    
for x in new_data:
    print(x)