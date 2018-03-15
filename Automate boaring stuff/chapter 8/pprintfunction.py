import pprint
cats = [{'name':'Zophie' , 'desc': 'chubby'},{'name':'pooka','desc':'fluffy'}]
print(pprint.pformat(cats))
fileobj=open('mycats.py','w')
fileobj.write('cats ='+pprint.pformat(cats)+'\n')
fileobj.close()
