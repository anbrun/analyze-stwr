import os.path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

inputfile = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\metadata.xlsx"
outputdir = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31"
data = pd.read_excel(inputfile)
data_fict = data[data["fictional"]=="yes"]
data_nonfict = data[data["fictional"]=="no"]

#%%
# calculate rel for all
# print(len(data))
# print(len(data_fict))
# print(len(data_nonfict))
#
# def get_rel_types(df):
#     res_df = {}
#     res_df["direkt"] = [round(sum(df["direct"]) / sum(df["cabtokens"]) * 100, 2)]
#     res_df["frei indirekt"] = [round(sum(df["freeIndirect"]) / sum(df["cabtokens"]) * 100, 2)]
#     res_df["indirekt/frei indirekt"] = [round(sum(df["indirect freeIndirect"]) / sum(df["cabtokens"]) * 100, 2)]
#     res_df["indirekt"] = [round(sum(df["indirect"]) / sum(df["cabtokens"]) * 100, 2)]
#     res_df["erzählt"] = [round(sum(df["reported"]) / sum(df["cabtokens"]) * 100, 2)]
#     return pd.DataFrame(res_df)
#
# all_types = get_rel_types(data)
# fict_types = get_rel_types(data_fict)
# nonfict_type = get_rel_types(data_nonfict)

#%%
# create relative columns (types)
data["rel_direct"] = data["direct"] / data["cabtokens"] * 100
data["rel_freeIndirect"] = data["freeIndirect"] / data["cabtokens"] * 100
data["rel_indirect freeIndirect"] = data["indirect freeIndirect"] / data["cabtokens"] * 100
data["rel_indirect"] = data["indirect"] / data["cabtokens"] * 100
data["rel_reported"] = data["reported"] / data["cabtokens"] * 100
data["rel_frame"] = data["frame"] / data["cabtokens"] * 100
type_cols = ["rel_direct", "rel_freeIndirect", "rel_indirect freeIndirect", "rel_indirect",
             "rel_reported"]
# create relative columns (medium)
data["rel_speech"] = data["direct"] / data["cabtokens"] * 100
data["rel_thought"] = data["thought"] / data["cabtokens"] * 100
data["rel_writing"] = data["writing"] / data["cabtokens"] * 100
data["rel_speech thought"] = data["speech thought"] / data["cabtokens"] * 100
data["rel_speech writing"] = data["speech writing"] / data["cabtokens"] * 100
data["rel_thought writing"] = data["thought writing"] / data["cabtokens"] * 100
data["rel_speech thought writing"] = data["speech thought writing"] / data["cabtokens"] * 100

#%%
medium_cols = ["rel_speech", "rel_thought", "rel_writing", "rel_speech thought", "rel_speech writing",
               "rel_thought writing", "rel_speech thought writing"]
medium_cols_mixed = ["rel_speech thought", "rel_speech writing",
               "rel_thought writing", "rel_speech thought writing"]
medium_cols_main = ["rel_speech", "rel_thought", "rel_writing"]

ax = data.boxplot(column=medium_cols_main, by="text_type")
plt.show()

#%%

texttypes = set(data["text_type"])
for tt in texttypes:
    print("{}: {}".format(tt, len(data[data["text_type"]==tt])))
# entferne die seltenen texttypes (Unsure: 6, Anzeige: 7, Biographie: 8)
texttypes_main = [x for x in list(texttypes) if x not in ["Unsure", "Anzeige", "Biographie"]]
print("\n")
for tt in texttypes_main:
    print("{}: {}".format(tt, len(data[data["text_type"]==tt])))

data_main_texttypes = data[data.text_type.isin(texttypes_main)]
ax = data_main_texttypes.boxplot(column=type_cols, by="text_type")


#%%
#grouped = data.groupby(by=['text_type'])["rel_direct"].mean()
grouped = data.groupby(by=['text_type'])
matplotlib.rc('xtick', labelsize=20)
matplotlib.rc('ytick', labelsize=20)
#font = {'size'   : 22}
#matplotlib.rc('font', **font)

ax = data_main_texttypes.boxplot(column=["rel_direct"], by="text_type", figsize=(20, 10))
plt.savefig(os.path.join(outputdir, "boxplot_texttype_rel_direct.png"))