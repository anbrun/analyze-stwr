import os.path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib



def create_rel_cols(data):
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

    return data

def barplot_by_metadata(data, col, outfile):
    """
    expects data with rel columns
    generates a plot
    :param data:
    :return:
    """
    # matplotlib.rc('xtick', labelsize=20)
    # matplotlib.rc('ytick', labelsize=20)
    font = {'size': 20}
    matplotlib.rc('font', **font)
    # rename the rel columns
    rename_dict = {"rel_direct": "direkt", "rel_indirect": "indirekt", "rel_freeIndirect": "frei indirect", "rel_reported": "erzählt",
     "text_type": "Texttyp", "rel_indirect freeIndirect": "ind/frei ind"}
    renamed = data.rename(index=str, columns=rename_dict)

    print(data.columns.values)

    new_col = col
    if col in rename_dict:
        new_col = rename_dict[col]

    renamed_grouped = renamed.groupby(by=[new_col])[
        "direkt", "indirekt", "erzählt", "frei indirect", "ind/frei ind",].mean()

    ax2 = renamed_grouped.plot(kind="bar", rot=0, figsize=(20, 10))
    #plt.subplots_adjust(bottom=0.4)
    plt.savefig(outfile)

def boxplot_medium_by_metadata(data, col, outfile):
    medium_cols = ["rel_speech", "rel_thought", "rel_writing", "rel_speech thought", "rel_speech writing",
                   "rel_thought writing", "rel_speech thought writing"]
    medium_cols_mixed = ["rel_speech thought", "rel_speech writing",
                   "rel_thought writing", "rel_speech thought writing"]
    medium_cols_main = ["rel_speech", "rel_thought", "rel_writing"]

    ax = data.boxplot(column=medium_cols_main, by=col, figsize=(20, 10))
    plt.savefig(outfile)

def boxplot_rwtype_by_metadata(data, col, outfile):
    rename_dict = {"rel_direct": "direkt", "rel_indirect": "indirekt", "rel_freeIndirect": "frei indirect",
                   "rel_reported": "erzählt",
                   "text_type": "Texttyp", "rel_indirect freeIndirect": "ind/frei ind"}
    renamed = data.rename(index=str, columns=rename_dict)
    new_col = col
    if col in rename_dict:
        new_col = rename_dict[col]

    ax = renamed.boxplot(column=[
        "direkt", "indirekt", "erzählt", "frei indirect", "ind/frei ind"], by=new_col, figsize=(20, 10))
    plt.savefig(outfile)


inputfile = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\metadata.xlsx"
outputdir = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31"
data = pd.read_excel(inputfile)
data_fict = data[data["fictional"]=="yes"]
data_nonfict = data[data["fictional"]=="no"]

# calculate rel cols for the data
data = create_rel_cols(data)
print(data.columns.values)
# generate barplot

col = "decade"
barplot_by_metadata(data, col, os.path.join(outputdir, "barplot_"+ col + ".png"))
#boxplot_medium_by_metadata(data, col, os.path.join(outputdir, "boxplot_medium_"+ col + ".png"))


# #%%
# medium_cols = ["rel_speech", "rel_thought", "rel_writing", "rel_speech thought", "rel_speech writing",
#                "rel_thought writing", "rel_speech thought writing"]
# medium_cols_mixed = ["rel_speech thought", "rel_speech writing",
#                "rel_thought writing", "rel_speech thought writing"]
# medium_cols_main = ["rel_speech", "rel_thought", "rel_writing"]
#
# ax = data.boxplot(column=medium_cols_main, by="text_type")
# plt.show()
#
# #%%
#
# texttypes = set(data["text_type"])
# for tt in texttypes:
#     print("{}: {}".format(tt, len(data[data["text_type"]==tt])))
# # entferne die seltenen texttypes (Unsure: 6, Anzeige: 7, Biographie: 8)
# texttypes_main = [x for x in list(texttypes) if x not in ["Unsure", "Anzeige", "Biographie"]]
# print("\n")
# for tt in texttypes_main:
#     print("{}: {}".format(tt, len(data[data["text_type"]==tt])))
#
# data_main_texttypes = data[data.text_type.isin(texttypes_main)]
# ax = data_main_texttypes.boxplot(column=type_cols, by="text_type")
#
#
# #%%
# #grouped = data.groupby(by=['text_type'])["rel_direct"].mean()
# grouped = data.groupby(by=['text_type'])
# #matplotlib.rc('xtick', labelsize=20)
# #matplotlib.rc('ytick', labelsize=20)
# font = {'size'   : 22}
# matplotlib.rc('font', **font)
#
# ax = data_main_texttypes.boxplot(column=["rel_direct"], by="text_type", figsize=(20, 10))
# plt.savefig(os.path.join(outputdir, "boxplot_all_texttype_rel_direct.png"))
#
# #%%
#
# renamed = data_main_texttypes.rename(index=str, columns=
# {"rel_direct": "direkt", "rel_indirect": "indirekt", "rel_freeIndirect": "frei indirect", "rel_reported": "erzählt",
#  "text_type": "Texttyp", "rel_indirect freeIndirect": "ind/frei ind"})
#
# renamed_grouped = renamed.groupby(by=["Texttyp"])["direkt", "indirekt", "erzählt",  "frei indirect", "ind/frei ind",].mean()
#
# ax2 = renamed_grouped.plot(kind="bar", rot=0, figsize=(20, 10))
# plt.savefig(os.path.join(outputdir, "barplot_all_texttype_rel_direct.png"))