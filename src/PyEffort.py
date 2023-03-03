from juliacall import Main as jl
import numpy as np

jl.seval("using Effort")
jl.seval("using SimpleChains")
jl.seval("using BSON")
jl.seval("using Static")

effort_compute_Pl = jl.seval('Effort.get_Pℓ')
effort_compute_Xil = jl.seval('Effort.get_Xiℓ')
effort_compute_Xil = jl.seval('Effort.get_Xiℓ')
effort_compute_f_z = jl.seval('Effort._f_z')
load_emu_jl = jl.seval('BSON.load')

def compute_Pl(*args):
    my_list = [elem for elem in args]
    if len(my_list) == 3:
        for i in range(len(args)-1):
            my_list[i] = jl.collect(my_list[i])
    else:
         for i in range(len(args)-2):
            my_list[i] = jl.collect(my_list[i])
    Pl = effort_compute_Pl(*my_list)
    return np.array(Pl)

def compute_Xil(cosmo, bs, emu):
    Xil = effort_compute_Xil(jl.collect(cosmo), jl.collect(bs), emu)
    return np.array(Xil)

def compute_fz(z, Omm, w0, wa):
    return effort_compute_f_z(z, Omm, w0, wa)

def load_emu(path):
    loaded = load_emu_jl(path)
    emu = loaded["Pℓ"]
    return emu
