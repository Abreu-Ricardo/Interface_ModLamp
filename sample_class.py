

from modlamp.descriptors import GlobalDescriptor, PeptideDescriptor
from modlamp.plot import helical_wheel, plot_aa_distr


def TESTE(txt):
    print(txt)

def hidrofobicidade(seq):
    desc = GlobalDescriptor(seq)
    desc.hydrophobic_ratio()
    return desc.descriptor[0][0]

def carga(seq):
    desc = GlobalDescriptor(seq)
    desc.calculate_charge(ph=7.0)
    return desc.descriptor[0][0]

def ponto_isoeletrico(seq):
    desc = GlobalDescriptor(seq)
    desc.isoelectric_point()
    return desc.descriptor[0][0]

def peso_molecular(seq):
    desc = GlobalDescriptor(seq)
    desc.calculate_MW()
    return desc.descriptor[0][0]

def Bomam(seq):
    desc = GlobalDescriptor(seq)
    desc.boman_index()
    return desc.descriptor[0][0]



# if __name__ == '__main__':
#     seq1 = "KKMGKKWQRIARRLYCLL"
#     seq2 = "KVWKSIYTRCYRILNC"
#     seq3 = "KVWKSYITRYCRIL"
#     seq4 = "KWKYITRYCRIL" 

#     seq = ["KKMGKKWQRIARRLYCLL", "KVWKSIYTRCYRILNC", "KVWKSYITRYCRIL", "KWKYITRYCRIL"]

#     for i in range(0, len(seq)):
#         desc = GlobalDescriptor(seq[i])
#         print(f"{i+1} -> {seq[i]}")
#         print(f"Hidrofobicidade({i+1}):             {hidrofobicidade(desc):.3f}")
#         print(f"Valor da carga({i+1}):              {carga(desc)}")
#         print(f"Valor do ponto isoeletrico({i+1}):  {ponto_isoeletrico(desc):.3f}")
#         print(f"Valor do peso Molecular({i+1}):     {peso_molecular(desc):.3f}")
#         print(f"Valor de Bomam({i+1}):              {Bomam(desc):.3f}\n")

    