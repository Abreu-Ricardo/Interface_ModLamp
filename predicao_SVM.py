# from modlamp.ml import train_best_model, score_testset, predict
# from sklearn.model_selection import train_test_split
# from modlamp.datasets import load_ACPvsRandom, load_AMPvsUniProt
# from modlamp import descriptors

# #data = load_ACPvsRandom()
# data = load_AMPvsUniProt()

# desc = descriptors.PeptideDescriptor(data.sequences, scalename='pepcats')
# desc.calculate_autocorr(7)

# X_train, X_test, y_train, y_test = train_test_split(desc.descriptor, data.target, test_size = 0.33)

# best_svm_model = train_best_model('svm', X_train,y_train)
# print(score_testset(best_svm_model, X_test, y_test))

# print(modlamp.ml.predict())


from modlamp.ml import train_best_model, predict
from modlamp.datasets import load_ACPvsRandom, load_AMPvsUniProt
from modlamp.descriptors import PeptideDescriptor
from modlamp.sequences import Helices

#data = load_ACPvsRandom()
data = load_AMPvsUniProt()


desc = PeptideDescriptor(data.sequences, scalename='pepcats')
desc.calculate_autocorr(7)

best_svm_model = train_best_model('svm', desc.descriptor, data.target)

# Soh gera seq aleatorias
# H = Helices(seqnum=10, lenmin=7, lenmax=30)
# H.generate_sequences()

Seq = ['KVWKSIYTRCYRILNC', 'KKMGKKWQRIARRLYCLL', 'KVWKSYITRYCRIL', 'KWKYITRYCRIL']

descH = PeptideDescriptor(Seq, scalename='pepcats')
print(descH.calculate_autocorr(7))

df = predict(best_svm_model, x=descH.descriptor, seqs=descH.sequences)
print(df.head(4))  # all three shown sequences are predicted active (class 1)