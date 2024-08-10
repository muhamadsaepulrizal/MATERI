#di __init__ kita import module supaya bisa dipakai di main program 

#ini jika di main program di panggil import sains
from . import math #from(dari) titik(.) maksudnya si sains, import si module math yg terdapat banyak fungsi
from . import fisika

# from .math import kali #bisa juga seperti ini di main program tinggal panggil (sains.kali())


#ini jika di main di panggil from sains import *
#dan berikut adalah __all_ dengan list nama modulenya
# dan yang __all__ tidak disarankan
#__all__ = [
#    "math",
#    "fisika"
#]