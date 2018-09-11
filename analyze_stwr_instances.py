import os.path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import re
import ast

inputfile = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\stwr_instances\stwr_instances.xlsx"
outputdir = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\stwr_instances"
data = pd.read_excel(inputfile)
data_fict = data[data["fictional"]=="yes"]
data_nonfict = data[data["fictional"]=="no"]
#%%

# len of stwr types
#ax = data.boxplot(column=["len"], by="type", figsize=(20, 10))

#%%
# direct_len = list(data[data["type"]=="direct"]["len"].sort_values(ascending=False))
# plt.plot(direct_len)
#
# indirect_len = list(data[data["type"]=="indirect"]["len"].sort_values(ascending=False))
# plt.plot(indirect_len)
#
# reported_len = list(data[data["type"]=="reported"]["len"].sort_values(ascending=False))
# plt.plot(reported_len)

#%%
data_ind = data[data["type"]=="indirect"]
form = []
count_zu = 0
count_dass = 0
count_wwort = 0
for index, row in data_ind.iterrows():
    surf = row["anno"]
    merkmale = []
    if (re.search("\A\s*[dD]ass", surf)):
        merkmale.append("dass")
        count_dass += 1
    if (re.search("\A\s*[dD]aß", surf)):
        merkmale.append("dass")
        count_dass += 1
    if (re.search("\A\s*[Ww]", surf)):
        merkmale.append("w-wort")
        count_wwort += 1
    if (re.search(" zu ", surf)):
        merkmale.append("zu")
        count_zu += 1
    form.append(merkmale)
#data_ind.loc["form"] = form
print(len(data_ind))
print(form)

#%%
data_rep = data[data["type"]=="reported"]
print("DATA rep: {}".format(len(data_rep)))
verbs = data_rep["verbs"].sort_values(ascending=True)
verbs_lit = [ast.literal_eval(x) for x in list(verbs)]
verbs_flat = [item for sublist in verbs_lit for item in sublist]

v_dict = {}
for elem in verbs_flat:
    if elem in v_dict.keys():
        v_dict[elem] += 1
    else:
        v_dict[elem] = 1
print(v_dict)
import operator
sorted_x = sorted(v_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_freq = [str(elem) for elem in sorted_x]
with open(os.path.join(outputdir, "rep_verbs.txt"), "w") as f:
    f.write("\n".join(sorted_freq))




