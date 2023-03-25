import JSON
import time

if __name__=="__main__":
    fr=open('op_hash_ps.txt')
    text=fr.readlines()
    fr.close()
    for line in text:
        JSON.func(line)
        time.sleep(0.25)