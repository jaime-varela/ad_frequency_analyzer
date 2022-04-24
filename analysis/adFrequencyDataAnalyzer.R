library(ggplot2)
library(dplyr)
library(jsonlite)

setwd("~/Dropbox/software/adProject/ad_frequency_analyzer/analysis/")

item_matches <- read.table("itemMatch.tsv", sep="\t", header=T)
item_matches <- item_matches %>%
  dplyr::group_by(itemKey, dateDiscovered, person) %>%
  dplyr::summarise(n_times=n(),
                   adString=first(adString))

item_metadata_dict <- jsonlite::read_json("itemMetadata.json")
item_metadata_df <- as.data.frame(cbind("itemKey"=names(item_metadata_dict)))
item_metadata_df$dateDiscussed <- sapply(as.character(item_metadata_df$itemKey), function(item) {
  item_metadata_dict[[item]][["date"]]
})
item_metadata_df$discussionType <- sapply(as.character(item_metadata_df$itemKey), function(item) {
  item_metadata_dict[[item]][["discussionType"]]
})


item_data <- merge(item_metadata_df,
                   item_matches,
                   by = "itemKey",
                   all.x = T, all.y = T)

# relative date column
# for (min_date, max_date): get n_times total per item
# will plot in such a way that the 'day discussed' will be the x-axis origin