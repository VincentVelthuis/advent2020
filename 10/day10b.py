import sys,fileinput

def diff_to_previous(l):
    ans = []
    for i in range(1,len(l)):
        ans += [l[i]-l[i-1]]
    return ans

def count_seguence_of_1s(l):
    cur_seq = 0
    seq_dict = {}
    for n in l:
        if n == 1:
            cur_seq += 1
        else: #if item != 1, sequence has ended
            if cur_seq > 1: 
                seq_dict.setdefault(cur_seq,0)
                seq_dict[cur_seq] += 1
            cur_seq = 0
    # for possible last sequence at EOL
    if cur_seq > 1:
        seq_dict.setdefault(cur_seq,0)
        seq_dict[cur_seq] += 1
    
    return seq_dict
    
def calc_ans_from_seq_dict(seq_dict):
    ans = 1
    mults_dict = {2:2,3:4,4:7}
    print("count sequences of 1's")
    for i in seq_dict:
        ans *= mults_dict[i]**seq_dict[i]
        print("-- {}: {} time(s) \t {}^{} = {}".format(i,seq_dict[i], \
            mults_dict[i],seq_dict[i],mults_dict[i]**seq_dict[i]))
    print("all answers multiplied = {}".format(ans))

### PROGRAM START
lines = [int(line.strip()) for line in \
    fileinput.input(files=sys.argv[1])]

# add min and max voltage
lines += [ 0, max(lines)+3 ]
# change to set to sort & change back to list to iterate
lines = list(set(lines))

calc_ans_from_seq_dict(count_seguence_of_1s(diff_to_previous(lines)))
