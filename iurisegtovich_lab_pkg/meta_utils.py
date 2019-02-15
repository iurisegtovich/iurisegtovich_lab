def labdict(names,objlist):
    return dict(zip(names.replace(" ","").split(","),objlist))

'''x=1
y=2
z=3
print(labdict("x,y,z",
              [x,y,z]))'''

def ddicteval(ddict,keys):
    for key in keys:
        value=ddict[key]
        ddict=value
        pass
    return value

'''testddict={"C1":{"com":"value"}}
value=ddicteval(testddict,("C1","com",))
print(value)'''


def save_seqcalc_data(names_data:dict,filename='test.out'):
    '''saves a dict of name_of_variable:array_of_values to a file'''
    import numpy as np
    nline=len(list(names_data.values())[0])
    ncol=len((names_data.values()))
    i=np.arange(0,nline)
    
    headers="i"
    columns=[i,]
#     print(columns)
    for eachk, eachv in names_data.items():
        headers += ", "+eachk #string concatenate
        columns.append(eachv)      #list append
#         print(columns)
    np.savetxt(filename, np.asarray(columns).T, delimiter=', ',header=headers, fmt=['%d']+(ncol)*['%.18e'],comments="")
        
def load_seqcalc_data(filename='test.out'):
    '''returns a dict of name_of_variable:array_of_values loaded from a file'''
    import numpy as np
    headers = np.genfromtxt(filename,delimiter=', ',skip_header=0,comments=None,max_rows=1,dtype=str)
#     print(headers)
    cols = np.loadtxt(filename,skiprows=1,delimiter=', ',unpack=True)
    return dict(zip(headers,cols))

def test_this_bagassa():
    '''tests save_seqcalc_data and load_seqcalc_data'''
    x = np.linspace(0.0312,5.123120,10)
    y = np.linspace(-90.0312,5.123120,10)
    z = np.linspace(0.046e5,57.123120e9,10)
    
    save_seqcalc_data({'x':x,
                       'y':y,
                       'z':z})
    
    loaded_dict = load_seqcalc_data()
    print(loaded_dict)
    
def expand_ndarrayobj(singleitemdict):
    '''expands a array of array objects to a dictionary of arrays
    occARRAYofARRRAYS[k][0,0] and occARRAYofARRRAYS[k][0,1] are now occDICT['occ00'][k] and occDICT['occ00'][k]
    where k counts from 0 to npoints
    '''
    import numpy as np
    expanded_dict={}
    for singlekey, singlevalue in singleitemdict.items(): #should be one pass for the singleitemdict
        npoints=len(singlevalue) #number of k
        #nested loops according to object shape? restricted to 1 or 2
        if len(singlevalue[0].shape)==1:
            for i in range(len(singlevalue[0].shape[0])):
                expanded_dict[singlekey+str(i)]=np.asarray([singlevalue[k][i] for k in range(npoints)])
            
        elif len(singlevalue[0].shape)==2:
            for i in range((singlevalue[0].shape[0])):
                for j in range((singlevalue[0].shape[1])):
                    expanded_dict[singlekey+str(i)+str(j)]=np.asarray([singlevalue[k][i,j] for k in range(npoints)])                
    return expanded_dict
#usage
#EXPoccs = expand_ndarrayobj({'Occ':Occ})


def sci(number):
    return "{:.2E}".format(number)
