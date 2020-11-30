import pyflakes
import re
def find_variable_assignments(source, target_var_names):
    k=[]
    for i in target_var_names :
         test = re.search(r'(.*?{k}.*?)'.format(k=i), source)
         if test !="" :
             k.append(i)
    return k
    