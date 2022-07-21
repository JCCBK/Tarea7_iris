import math

def GCcontent(dna, sig_figs):
    dna = dna.replace('N', '')
    length = len(dna)
    g_count = dna.upper().count('G')
    c_count = dna.upper().count('C')
    gc_content = 10*(g_count + c_count) / length
    return round(gc_content, sig_figs)
 
def ATcontent(dna, sig_figs):
    dna = dna.replace('N', '')
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = 10*(a_count + t_count) / length
    return round(at_content, sig_figs) 
           
def potencia (x, y):
    x = int(x)
    y = int(y)
    z = x**y
    return [x, y, z]