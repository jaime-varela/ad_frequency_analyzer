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
                   all.x = F, all.y = T)

anonPerson <- list()
anonPerson <- c("Person1", "Person2")
names(anonPerson) <- c(unique(as.character(item_data$person))[1],
                       unique(as.character(item_data$person))[2])

START_DATE = as.Date("2022-03-09")
END_DATE = as.Date("2022-04-22")
for(item in names(item_metadata_dict)){
  dateDiscussed = as.Date(item_metadata_dict[[item]][["date"]])
  discussionType = item_metadata_dict[[item]][["discussionType"]]
  
  specific_item_matches <- item_data[(item_data$itemKey==item),]
  specific_item_matches$dateDiscussed <- rep(dateDiscussed, nrow(specific_item_matches))
  specific_item_matches$discussionType <- rep(discussionType, nrow(specific_item_matches))
  specific_item_matches$dateDiscovered <- as.Date(specific_item_matches$dateDiscovered)
  specific_item_matches$n_times <- as.integer(specific_item_matches$n_times)
  specific_item_matches$person <- as.character(specific_item_matches$person)
  
  for(person in c("jaime", "maria")){
    specific_item_person_matches <- specific_item_matches[specific_item_matches$person==person,] %>%
      mutate(dateDiscovered = as.Date(dateDiscovered))
    specific_item_person_matches <- specific_item_person_matches[,c("dateDiscovered","n_times")]
    specific_item_person_matches <- specific_item_person_matches %>%
      complete(dateDiscovered = seq.Date(START_DATE, END_DATE, by="day"))
    specific_item_person_matches$n_times[is.na(specific_item_person_matches$n_times)] <- 0
    
    p <- ggplot(specific_item_person_matches,
                aes(x=dateDiscovered,y=n_times)) +
      geom_point() + 
      xlab("Days") + ylab("Item Count") +
      ggtitle(paste0(item, ", ", anonPerson[[person]])) +
      geom_vline(xintercept = dateDiscussed, color="red",linetype="dashed") +
      theme_classic() + theme(plot.title = element_text(hjust=0.5))
    print(p)
    output_filename = paste0("plots/", gsub(" ", "_", item), "_", anonPerson[[person]], ".pdf")
    ggsave(output_filename, width=5, height=4)
  }
}

