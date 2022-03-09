"""En este fichero tendrían que estar la mayoría de funciones para que el codigo fuera fácil de leer,
 pero por falta de tiempo no me ha dado tiempo de darle estructura al codigo y hacerlo mas amable """
 #########################################################################################################################
def coords_froms(s):
    list = s.replace('{','').replace('}','').replace('[','').replace(']','').split(':')
    a =[float(i) for i in list[2].replace("'",'').split(',')]
    return a

#########################################################################################################################