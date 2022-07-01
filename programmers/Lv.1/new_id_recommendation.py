import re

def solution(new_id):
    new_id = new_id.lower() # stage 1 (O)
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id) # stage 2 
    new_id = re.sub(r"[.]+",".",new_id) # stage 3
    new_id = new_id.strip(".") # stage 4
    if len(new_id) == 0: new_id = "a"  # stage 5
    if len(new_id) > 15: new_id = new_id.replace(new_id[15:],"")
    if new_id[-1] == ".": new_id = new_id[:-1] # stage 6
    while len(new_id) < 3:
        new_id += new_id[-1] # stage 7
    answer = new_id
    return answer