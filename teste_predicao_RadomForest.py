import pandas as pd
from modlamp.datasets import load_AMPvsUniProt, load_ACPvsTM
from modlamp.descriptors import PeptideDescriptor
from modlamp.ml import train_best_model, score_cv
from modlamp.descriptors import PeptideDescriptor

### IN THE FOLLOWING LIST, ADD YOUR SEQUENCES TO BE PREDICTED ###
#to_predict = ['GLLDSLLALLFEWASQ', 'KLLKLLKLLKLLKLLKKKLKLKL', 'GLFDDSKALLKKDFWWW']
#to_predict = ['KVWKSIYTRCYRILNC', 'KKMGKKWQRIARRLYCLL', 'KVWKSYITRYCRIL', 'KWKYITRYCRIL']
to_predict = ['KCQGITRRCYCL']

########### IMPORTANTE
# This module incorporates functions to load different peptide datasets used for classification.
# Function Data load_AMPvsTM() Antimicrobial peptides versus trans-membrane sequences
# load_AMPvsUniProt() AMPs from the APD3 versus other peptides from the UniProt database
# load_ACPvsTM() Anticancer peptides (CancerPPD) versus helical transmembrane sequences
# load_ACPvsRandom() Anticancer peptides (CancerPPD) versus random scrambled AMP sequences
# load_custom() A custom data set provided in modlamp/data as a .csv file

# load training sequences
data = load_AMPvsUniProt()

# describe sequences with PepCATS descriptor
descr = PeptideDescriptor(data.sequences, 'pepcats')
descr.calculate_crosscorr(7)

# train a Random Forest classifier with given parameters based on the PEPCATS data
best_RF = train_best_model('RF', descr.descriptor, data.target, cv=2,
                            param_grid={'clf__bootstrap': [True], 'clf__criterion': ['gini'], 'clf__max_features':
                            ['sqrt'], 'clf__n_estimators': [500]})

# evaluate performance of the model in 5-fold cross validation
score_cv(best_RF, descr.descriptor, data.target, cv=5)

# describe sequences to be predicted with PEPCATS descriptor
lib_desc = PeptideDescriptor(to_predict, 'pepcats')
lib_desc.calculate_crosscorr(7)

# predict class probabilities for the desired sequences
proba = best_RF.predict_proba(lib_desc.descriptor)

# create ordered dictionary with sequences and prediction values and order it according to AMP predictions
d = pd.DataFrame({'sequence': to_predict, 'prediction': proba[:, 1]})
d = d.sort_values('prediction', ascending=False)
print(d)  # print the final predictions (sorted according to decreasing probabilities)

