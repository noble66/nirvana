#!/usr/bin/env python

# generates a dict of forms for each train/test set of conll data.
#test_form is: {record_no: [form1, form2, form3...]}

import querySubnet as qs
import pickle

def main():
    train = ['./data/Conll2000/data/train_sen.dict', './data/Conll2000/data/train_pos.dict']
    test =  ['./data/Conll2000/data/test_sen.dict', './data/Conll2000/data/test_pos.dict']
    fw=open('./data/Conll2000/data/test_forms.dict','w')       # <<<
    all_dict={}
    fpos=open(test[1],'r')  # <<<
    with open(test[0], 'r') as f:   # <<<
        sens = pickle.load(f)
        pos = pickle.load(fpos)
        counter=0
        for s1 in sens.keys():
            s=sens[s1]
            forms_collect=[]
            tempdict={}
            counter+=1
            print ''
            print 'Processing record: ', counter
            qforms={}
            #print s
            for i in range(0, len(s)):
                tempdict[s[i]]=pos[s1][i]
            for q in s:
                qforms[q] = qs.formTagger(tempdict[q])
                forms_collect.append(qforms[q])
            #for q in s:
            #    print q, ' === ', tempdict[q], ' === ', qforms[q]
            #print '--------'
            all_dict[counter]=forms_collect
            #if counter==4:
            #    break
    pickle.dump(all_dict, fw)
    print ' -- done -- '

if __name__ == '__main__':
    main()
