import os.path
import sys
import pandas as pd

lib_path = os.path.abspath(os.path.join("../pycas_rw"))
sys.path.append(lib_path)

import pycas_rw_core.pycas as pycas
import pycas_rw_core.cas_util as cas_util
import re

ts_path = os.path.abspath(os.path.join(r"../pycas_rw/pycas_rw_core/redeWiedergabeTypesystem_compare_tei_cab.xml"))
def get_embedding(inputdir):
    """
    count the embedded STWR forms for each STWR type
    provide absolute and relative counts
    :param inputdir:
    :return:
    """
    res_dict = {"file": [], "corpuspart": [], "fictional":[], "text_type":[], "decade":[],
                "type": [], "instances": [], "dir_emb": [], "indfi_emb": [], "ind_emb": [], "rep_emb": [], "fi_emb": [],
                "total_emb": []}
    files_in_dir = [f for f in os.listdir(inputdir) if os.path.isfile(os.path.join(inputdir, f)) and re.search("\.xmi", str(f))]

    for file in files_in_dir:
        cas_in = pycas.CAS(os.path.join(inputdir, file), ts_path)
        util_in = cas_util.CASUtil(cas_in)
        annotation_types = util_in.annotation_types
        # metadata entries
        metadata = cas_in.get_annotation_index(annotation_types.METADATA)[0]
        corpuspart = metadata.get("Corpuspart")
        text_type = metadata.get("TextType")
        fictional = metadata.get("Fictional")
        decade = metadata.get("Decade")

        stwr_list = cas_in.get_annotation_index(annotation_types.STWR)
        dir_list = [x for x in stwr_list if x.get("RType") == "direct"]
        ind_list = [x for x in stwr_list if x.get("RType") == "indirect"]
        rep_list = [x for x in stwr_list if x.get("RType") == "reported"]
        indfi_list = [x for x in stwr_list if x.get("RType") == "indirect freeIndirect"]
        fi_list = [x for x in stwr_list if x.get("RType") == "freeIndirect"]

        # add dir info
        res_dict["file"].append(file)
        res_dict["corpuspart"].append(corpuspart)
        res_dict["text_type"].append(text_type)
        res_dict["fictional"].append(fictional)
        res_dict["decade"].append(decade)
        res_dict["type"].append("direct")
        res_dict["instances"].append(len(dir_list))
        emb_dir, emb_fi, emb_indfi, emb_ind, emb_rep = emb_counts_of_type(dir_list, cas_in)
        res_dict["dir_emb"].append(emb_dir)
        res_dict["fi_emb"].append(emb_fi)
        res_dict["indfi_emb"].append(emb_indfi)
        res_dict["ind_emb"].append(emb_ind)
        res_dict["rep_emb"].append(emb_rep)
        res_dict["total_emb"].append(emb_dir+emb_fi+emb_indfi+emb_ind+emb_rep)
        # add fi info
        res_dict["file"].append(file)
        res_dict["corpuspart"].append(corpuspart)
        res_dict["text_type"].append(text_type)
        res_dict["fictional"].append(fictional)
        res_dict["decade"].append(decade)
        res_dict["type"].append("freeIndirect")
        res_dict["instances"].append(len(fi_list))
        emb_dir, emb_fi, emb_indfi, emb_ind, emb_rep = emb_counts_of_type(fi_list, cas_in)
        res_dict["dir_emb"].append(emb_dir)
        res_dict["fi_emb"].append(emb_fi)
        res_dict["indfi_emb"].append(emb_indfi)
        res_dict["ind_emb"].append(emb_ind)
        res_dict["rep_emb"].append(emb_rep)
        res_dict["total_emb"].append(emb_dir + emb_fi + emb_indfi + emb_ind + emb_rep)
        # add indfi info
        res_dict["file"].append(file)
        res_dict["corpuspart"].append(corpuspart)
        res_dict["text_type"].append(text_type)
        res_dict["fictional"].append(fictional)
        res_dict["decade"].append(decade)
        res_dict["type"].append("indirect freeIndirect")
        res_dict["instances"].append(len(indfi_list))
        emb_dir, emb_fi, emb_indfi, emb_ind, emb_rep = emb_counts_of_type(indfi_list, cas_in)
        res_dict["dir_emb"].append(emb_dir)
        res_dict["fi_emb"].append(emb_fi)
        res_dict["indfi_emb"].append(emb_indfi)
        res_dict["ind_emb"].append(emb_ind)
        res_dict["rep_emb"].append(emb_rep)
        res_dict["total_emb"].append(emb_dir + emb_fi + emb_indfi + emb_ind + emb_rep)
        # add ind info
        res_dict["file"].append(file)
        res_dict["corpuspart"].append(corpuspart)
        res_dict["text_type"].append(text_type)
        res_dict["fictional"].append(fictional)
        res_dict["decade"].append(decade)
        res_dict["type"].append("indirect")
        res_dict["instances"].append(len(ind_list))
        emb_dir, emb_fi, emb_indfi, emb_ind, emb_rep = emb_counts_of_type(ind_list, cas_in)
        res_dict["dir_emb"].append(emb_dir)
        res_dict["fi_emb"].append(emb_fi)
        res_dict["indfi_emb"].append(emb_indfi)
        res_dict["ind_emb"].append(emb_ind)
        res_dict["rep_emb"].append(emb_rep)
        res_dict["total_emb"].append(emb_dir + emb_fi + emb_indfi + emb_ind + emb_rep)
        # add rep info
        res_dict["file"].append(file)
        res_dict["corpuspart"].append(corpuspart)
        res_dict["text_type"].append(text_type)
        res_dict["fictional"].append(fictional)
        res_dict["decade"].append(decade)
        res_dict["type"].append("reported")
        res_dict["instances"].append(len(rep_list))
        emb_dir, emb_fi, emb_indfi, emb_ind, emb_rep = emb_counts_of_type(rep_list, cas_in)
        res_dict["dir_emb"].append(emb_dir)
        res_dict["fi_emb"].append(emb_fi)
        res_dict["ind_emb"].append(emb_ind)
        res_dict["indfi_emb"].append(emb_indfi)
        res_dict["rep_emb"].append(emb_rep)
        res_dict["total_emb"].append(emb_dir + emb_fi + emb_indfi + emb_ind + emb_rep)
    res_df = pd.DataFrame(res_dict)
    return res_df


def emb_counts_of_type(anno_list, cas_in):
    emb_dir = 0
    emb_ind = 0
    emb_rep = 0
    emb_fi = 0
    emb_indfi = 0
    util_in = cas_util.CASUtil(cas_in)
    annotation_types = util_in.annotation_types
    for anno in anno_list:
        covered_stwr_annos = util_in.get_covered(anno, annotation_types.STWR)
        for emb in covered_stwr_annos:
            if emb != anno:
                if emb.get("RType") == "direct":
                    emb_dir += 1
                    #print(util_in.get_covered_text(emb))
                elif emb.get("RType") == "indirect":
                    emb_ind += 1
                    #print(util_in.get_covered_text(emb))
                elif emb.get("RType") == "reported":
                    emb_rep += 1
                    #print(util_in.get_covered_text(emb))
                elif emb.get("RType") == "freeIndirect":
                    emb_fi += 1
                    #print(util_in.get_covered_text(emb))
                elif emb.get("RType") == "indirect freeIndirect":
                    emb_indfi += 1
    return (emb_dir, emb_fi, emb_indfi, emb_ind, emb_rep)

#%%

#inputdir = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-17\test"
inputdir = r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\consens_2_preproc"
res_df = get_embedding(inputdir)

# writer = pd.ExcelWriter(
#     r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\direct_emb.xlsx")
# df_direct.to_excel(writer)
# writer.save()


#%%
# add relative columns

res_df["dir_emb_rel"] = round(res_df["dir_emb"] / res_df["instances"] * 100, 2)
res_df["fi_emb_rel"] = round(res_df["fi_emb"] / res_df["instances"] * 100, 2)
res_df["ind_emb_rel"] = round(res_df["ind_emb"] / res_df["instances"] * 100, 2)
res_df["rep_emb_rel"] = round(res_df["rep_emb"] / res_df["instances"] * 100, 2)
res_df["indfi_emb_rel"] = round(res_df["indfi_emb"] / res_df["instances"] * 100, 2)

#%%
# sum over all instances
all_instances = sum(res_df["instances"])
all_dir_emb = sum(res_df["dir_emb"])
all_fi_emb = sum(res_df["fi_emb"])
all_ind_emb = sum(res_df["ind_emb"])
all_rep_emb = sum(res_df["rep_emb"])

all_dir_emb_rel = round(all_dir_emb/all_instances * 100, 2)
all_fi_emb_rel = round(all_fi_emb/all_instances * 100, 2)
all_ind_emb_rel = round(all_ind_emb/all_instances * 100, 2)
all_rep_emb_rel = round(all_rep_emb/all_instances * 100, 2)

#%%
#only certain type
cats = ["direct", "freeIndirect", "indirect freeIndirect", "indirect", "reported"]
emb_rel_dict = {"main_cat": [], "dir_emb": [],  "fi_emb": [], "indfi_emb": [], "ind_emb": [],
                "rep_emb": [], "tot_emb": []}

for cat in cats:
    df_cat = res_df[res_df["type"] == cat]

    all_instances = sum(df_cat["instances"])
    all_dir_emb = sum(df_cat["dir_emb"])
    all_fi_emb = sum(df_cat["fi_emb"])
    all_ind_emb = sum(df_cat["ind_emb"])
    all_indfi_emb = sum(df_cat["indfi_emb"])
    all_rep_emb = sum(df_cat["rep_emb"])
    all_tot_emb = all_dir_emb + all_fi_emb + all_indfi_emb + all_ind_emb + all_rep_emb
    print("{} {} {} {} {}".format(all_instances, all_dir_emb, all_fi_emb, all_indfi_emb,
                                  all_ind_emb, all_rep_emb))

    all_dir_emb_rel = round(all_dir_emb / all_instances * 100, 2)
    all_fi_emb_rel = round(all_fi_emb / all_instances * 100, 2)
    all_indfi_emb_rel = round(all_indfi_emb / all_instances * 100, 2)
    all_ind_emb_rel = round(all_ind_emb / all_instances * 100, 2)
    all_rep_emb_rel = round(all_rep_emb / all_instances * 100, 2)
    all_tot_emb_rel = round(all_tot_emb / all_instances * 100, 2)

    emb_rel_dict["main_cat"].append(cat)
    emb_rel_dict["dir_emb"].append(all_dir_emb_rel)
    emb_rel_dict["fi_emb"].append(all_fi_emb_rel)
    emb_rel_dict["indfi_emb"].append(all_indfi_emb_rel)
    emb_rel_dict["ind_emb"].append(all_ind_emb_rel)
    emb_rel_dict["rep_emb"].append(all_rep_emb_rel)
    emb_rel_dict["tot_emb"].append(all_tot_emb_rel)
df_emb = pd.DataFrame(emb_rel_dict)

writer = pd.ExcelWriter(
    r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\embedded_per_cat.xlsx")
df_emb.to_excel(writer)
writer.save()

writer = pd.ExcelWriter(
    r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\embedded.xlsx")
res_df.to_excel(writer)
writer.save()

#%%

#test_df = get_embedding(r"E:\Git_RW\myrepo\7_final\consens_corpus_2018-08-31\test")

dir_df = res_df[res_df["type"]=="direct"]

ax = dir_df.boxplot(column=["dir_emb_rel", "ind_emb_rel", "rep_emb_rel"], by="decade")

#%%
