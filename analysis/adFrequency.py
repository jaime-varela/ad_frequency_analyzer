# Script to parse data dump and extract counts based on information from itemMetadata.json
import json
import pandas as pd
from textExtractor import extractTextBetweenRegexConditions
from fileUtils import listDirs, listFiles
import os

def main():
    # read in JSON
    item_metadata_dict = json.load(open("itemMetadata.json", "r"))

    # init table
    ad_count_table = []

    DATA_DIR = "/home/jvarela/dataScienceData/adListener/data"
    subDirs = listDirs(DATA_DIR)
    for subDir in subDirs:

        extractedSponsorAdList = extractTextBetweenRegexConditions(os.path.join(DATA_DIR, subDir, "total_text.txt"))
        extractedSidePane = open(os.path.join(DATA_DIR, subDir, "sidePane_img.txt"), "rb").read().decode(errors='replace').replace("\r", "")
        extractedSponsorAdList = extractedSponsorAdList + [extractedSidePane]

        for adString in extractedSponsorAdList:

            adStringLowered = adString.replace("\n","").replace("\r", "").lower()
            for itemKey in item_metadata_dict.keys():
                relatedWords = item_metadata_dict[itemKey]['relatedWords']
                relatedWords = relatedWords + [itemKey]
                relatedWords = [ word.lower() for word in relatedWords]
                for relatedWord in relatedWords:
                    if adStringLowered.find(relatedWord) != -1:
                        person, dateDiscovered = subDir.split(" ")[0].split("_")
                        ad_count_table.append([itemKey, dateDiscovered, person, adString.replace("\n","").replace("\r", "")])

    # save table
    ad_count_table_df = pd.DataFrame(ad_count_table)
    ad_count_table_df.columns = ["itemKey", "dateDiscovered", "person", "adString"]
    ad_count_table_df.to_csv("itemMatch.tsv", sep="\t", index=False, quoting=1) # quoting=1 quote all


if __name__ == "__main__":
    main()

