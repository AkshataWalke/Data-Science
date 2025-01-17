coding
***
created on Mon Apr 2 

@author: Deil
***

#SERIES IS USED TO MODEL ONE DIMENSIONAL DATA,
#SIMILAR TO A LIST OF PYTHON.
#The series object also has a few more bits.
#of data,including on #index on name.
 

import pandas as pd
songs2 = pd.Series([145,142,38,13],name='counts')
#it is a easy to inspect the index of a series(or data)
songs2.index
#The index can be string based as well.
#in which case pandas indicates.


songs3 = pd.Series([145,142,38,13],name='counts',
index=['Paut','Jhon''George','Ringo'])
songs3.index

#numeric column will become Nan
import pandas as pd
f1=pd.read_csv('age.csv')
f1
df=pd.read_excel("C:/1-pythpn/age.csv")
df

#None,NaN, nan and null are synonyms.
import numpy as np
numpy_ser = np.array([145,142,38,13])
songs[1]
#142
numpy_ser[1]
#they both have methods in common
songs3.mean()
numpy_ser.mean()

george=pd.Series(0,7,1,22)
index=('1968','1969','1970','1971')
george

george('1968')
george('1970')
for item in george;:
    print(item)