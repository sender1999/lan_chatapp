from django.shortcuts import render
import json
import glob

def log(request, year, month, day):
    title = year+'_'+month+'_'+day
    path = 'log/'+title+'.log'
    with open(path) as f:
        logs = f.read()
    logs_list = []
    hoge = logs.split('\n')

    for s in hoge:
        if len(s) != 0:
            tmp = json.loads(s)
            logs_list.append(list(tmp.values()))

    context = {
            'logs_list':logs_list,
            'title':title,
        }
    
    return render(request, 'polls/log.html',context)


def index(request):
    files = glob.glob('log/*')
    files = list(map(lambda x:x[4:14], files))
    context = {
            'files':files
        }
    
    return render(request, 'polls/index.html',context)
