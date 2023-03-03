from juliacall import Main as jl

jl.seval("using Effort")
jl.seval("using SimpleChains")
jl.seval("using BSON")
jl.seval("using Static")

effort_compute_Pl = jl.seval('Effort.get_Pℓ')
effort_compute_Xil = jl.seval('Effort.get_Xiℓ')
load_emu_jl = jl.seval('BSON.load')

def compute_Pl(cosmo, bs, emu):
    Pl = effort_compute_Pl(jl.collect(cosmo), jl.collect(bs), emu)
    return Pl

def compute_Xil(cosmo, bs, emu):
    Pl = effort_compute_Xil(jl.collect(cosmo), jl.collect(bs), emu)
    return Pl

def load_emu(path):
    loaded = load_emu_jl(path)
    emu = loaded["Pℓ"]
    return emu
