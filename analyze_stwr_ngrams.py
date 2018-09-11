import os.path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import re


inputfile = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\stwr_instances\stwr_ngrams_level1.xlsx"
outputdir = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\stwr_instances"
data = pd.read_excel(inputfile)

#%%

# mark all lines that are not transitions

data["trans"] = data["tag1"] != data ["tag2"]

#%%
# calculate following words

# for direct
data_grouped_pos1= data.groupby(by="tag1")["freq"].sum()
data_grouped_pos2= data.groupby(by="tag2")["freq"].sum()

#%%
def calc_pos1(cat):
    direct_pos1 = data[data["tag1"]==cat]
    dir_tot = direct_pos1["freq"].sum()
    direct_pos1["rel"] = round(direct_pos1["freq"] / dir_tot * 100, 2)
    return direct_pos1

direct_pos1 = calc_pos1("direct")
indirect_pos1 = calc_pos1("indirect")
reported_pos1 = calc_pos1("reported")
fi_pos1 = calc_pos1("freeIndirect")
indfi_pos1 = calc_pos1("indirect freeIndirect")
x_pos1 = calc_pos1("x")

writer = pd.ExcelWriter(os.path.join(outputdir, "tags_following_pos1.xlsx"))
direct_pos1.to_excel(writer, sheet_name="pos1=dir")
indirect_pos1.to_excel(writer, sheet_name="pos1=ind")
reported_pos1.to_excel(writer, sheet_name="pos1=rep")
fi_pos1.to_excel(writer, sheet_name="pos1=f1")
indfi_pos1.to_excel(writer, sheet_name="pos1=indfi")
x_pos1.to_excel(writer, sheet_name="pos1=x")
writer.save()

#%%
def calc_pos2(cat):
    direct_pos1 = data[data["tag2"]==cat]
    dir_tot = direct_pos1["freq"].sum()
    direct_pos1["rel"] = round(direct_pos1["freq"] / dir_tot * 100, 2)
    return direct_pos1

direct_pos2 = calc_pos1("direct")
indirect_pos2 = calc_pos1("indirect")
reported_pos2 = calc_pos1("reported")
fi_pos2 = calc_pos1("freeIndirect")
indfi_pos2 = calc_pos1("indirect freeIndirect")
x_pos2 = calc_pos1("x")

writer = pd.ExcelWriter(os.path.join(outputdir, "tags_preceeding_pos2.xlsx"))
direct_pos2.to_excel(writer, sheet_name="pos1=dir")
indirect_pos2.to_excel(writer, sheet_name="pos1=ind")
reported_pos2.to_excel(writer, sheet_name="pos1=rep")
fi_pos2.to_excel(writer, sheet_name="pos1=f1")
indfi_pos2.to_excel(writer, sheet_name="pos1=indfi")
x_pos2.to_excel(writer, sheet_name="pos1=x")
writer.save()
