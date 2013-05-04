#!/usr/bin/env python

# the program builds an outfile for the patterns recognized from queries of the MSR QAByQ dataset.

import pickle
import querySubnet as qs

def findWQFreq():
    # finds word to query freq in MSR data
    print 'Loading file...'
    f=open('./data/MSR/Microsoft Q-A corpus/query_collection/allQueries.dict','r')
    qd=pickle.load(f)
    wq={}
    print 'Processing: \n'
    for dno in qd.keys():
        qlist=qd[dno]
        for q in qlist:
            qwords=q.split(' ')
            qlen = len(qwords)
            #if qlen > 20:
            #    print qwords
            #    print 'Waiting...'
            #    time.sleep(15)
            if qlen in wq.keys():
                wq[qlen]+=1
            else:
                wq[qlen]=1
    return wq

if __name__ == '__main__':
    dno=raw_input('Enter dataset no.(1-10): ')
    path = './data/MSR/Microsoft Q-A corpus/'
    msr_dataset = 'QAByQ_qSet_'+dno+'.dict'
    print ''
    f=open(path+msr_dataset, 'r')
    qdict = pickle.load(f)
    f.close()
    outfile=msr_dataset.split('.')[0]
    fw=open(path+'results/'+outfile+'.txt','w')
    fw.write('========== Nirwana 1.0 Testing ===== <<<< ')
    fw.write('MSR Dataset: ')
    fw.write(msr_dataset)
    fw.write(' >>>> \n\n')
    progress=0
    qprocessed = []
    print 'Processing Query: ',
    for q in qdict.keys():
        progress+=1
        #test
        #if len(qprocessed)>200:
        #    break
        qid=qdict[q]['QuestionID']
        if qid in qprocessed:
            continue
        fw.write( '=====')
        qprocessed.append(qid)
        qtxt=qdict[q]['QuestionText']
        fw.write(qid)
        fw.write(' ======= ')
        fw.write(qtxt)
        fw.write(' =======')
        fw.write('\n')
        print '..',len(qprocessed),
        qs.qNet(qtxt, fw, 1)
        fw.write( '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n')

    proc_str=str(len(qprocessed))
    print ''
    print ''
    print 'Total queries processed: ', progress
    print 'Total unique queries processed: ', proc_str
    fw.write('\nTotal unique queries processed: ')
    fw.write(proc_str)
    fw.write('\n')
    fw.close()
    print ''
    print ''
    print '============  xxx Done xxx ==========='
