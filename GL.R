setwd("")  # Set this to the directory of this file

# install.packages("ggplot2")
# install.packages("reshape")
library(ggplot2)
library(reshape)
library(graphics)

tracker <- c()
Native_means <- c()
Web_means <- c()
avg_values_all <- c()
diff_all <- c()
web_Econsumption <- c()
naive_Econsumption <- c()

#Function to extract all values from N files from a datapath to folder(repetitions has to be numbered starting from 1)
exctract_data_from_folder <- function(data_path,N) {
  Values <-c()
  for (i in 1:N) {
    data<-read.csv(paste(data_path, paste(as.character(i), ".csv",sep=""),sep = "") ,skip = 3, header=TRUE, stringsAsFactors=FALSE)
    #always fetch power from (lenth of file - 18 position, col 4)
    avg_power = as.integer(data[nrow(data)-18,4])
    #always fetch power from (lenth of file - 26 position, col 1)
    time = as.integer(data[nrow(data)-26,1])
    #transform into standard values
    avg_power = avg_power/1000000
    time = time/1000
    
    #Energy Consumption
    Joule = avg_power * time
    
    Values <- c(Values,Joule)
    
    print(paste("Path: ",paste(paste(" ", data_path,sep=""), paste(as.character(i), ".csv",sep=""),sep = "")))
    print(paste("This is joule for filenr : ", as.character(i)))
    print(Joule)
  }
return(Values)
} 

#---------------------------------------------------------------Plotting-----------------------------------------------

# Plotting Google Maps--------------------------------------------1
type1 = c(rep("GM", 15))
type2 = c(rep("GM", 15))

Values = exctract_data_from_folder("Google_Maps_native_15/",15)
Values2 = exctract_data_from_folder("Google_Maps_web_15/",15)

avg1 = mean(Values)
avg2 = mean(Values2)
diff = c(avg1 - avg2)
diff_all = c(diff_all,diff )

Native_means = c(Native_means,avg1)
Web_means <- c(Web_means,avg2)

std1 = sd(Values)
variance1 = std1**2
n1 = 15

std2 = sd(Values2)
variance2 = std2**2
n2 = 15

t_value = (avg2 - avg1) / sqrt(std1/n1 + std2/n2)

avg_values = c(avg1,avg2)
avg_values_all = c(avg_values_all,avg_values)

Nvalues = c(Values)
Wvalues = c(Values2)
tracker <- c(tracker,Values)
types=c(type1,type2)
naive_Econsumption <- c(naive_Econsumption,Values2)
Joule=c(Values,Values2)
TotalJoule=c(Values,Values2)
dataf <- data.frame(types,Joule)
Tt_n2 = c(rep("Native", 15))
Tt_w2 = c(rep("Web", 15))
treatment=c(Tt_n2,Tt_w2)


p <- ggplot(dataf, aes(types, Joule)) 
plot1 = p + geom_boxplot() 
plot1

#How similar are the distributions? 
qqplot(Values,Values2)

# Plotting Youtube-------------------------------------------------2
type1 = c(rep("YT", 15))
type2 = c(rep("YT", 15))

Values = exctract_data_from_folder("Youtube_N_15/",15)
Values2 = exctract_data_from_folder("Youtube_W_15/",15)
Nvalues = c(Nvalues,Values)
Wvalues = c(Wvalues,Values2)
tracker <- c(tracker,Values)
naive_Econsumption <- c(naive_Econsumption,Values2)
Joule=c(Values,Values2)
TotalJoule=c(TotalJoule,Joule)
types=c(type1,type2)
Tt_n = c(rep("Native", 15))
Tt_w = c(rep("Web", 15))
treatment2=c(Tt_n,Tt_w)
treatment=c(treatment,treatment2)
dataf2 <- data.frame(types,Joule)

avg1 = mean(Values)
avg2 = mean(Values2)
diff = c(avg1 - avg2)
diff_all = c(diff_all,diff )
avg_values = c(avg1,avg2)
avg_values_all = c(avg_values_all,avg_values)
Native_means = c(Native_means,avg1)
Web_means <- c(Web_means,avg2)

p <- ggplot(dataf2, aes(types, Joule)) 
plot2 = p + geom_boxplot() 
plot2

# Plotting Facebook-------------------------------------------------3
type1 = c(rep("FB", 15))
type2 = c(rep("FB", 15))

Values = exctract_data_from_folder("Facebook_native_15/",15)
Values2 = exctract_data_from_folder("Facebook_web_15/",15)
Nvalues = c(Nvalues,Values)
Wvalues = c(Wvalues,Values2)
tracker <- c(tracker,Values)
naive_Econsumption <- c(naive_Econsumption,Values2)
Joule=c(Values,Values2)
TotalJoule=c(TotalJoule,Joule)
types=c(type1,type2)
treatment=c(treatment,treatment2)
dataf3 <- data.frame(types,Joule)

avg1 = mean(Values)
avg2 = mean(Values2)
avg_values = c(avg1,avg2)
avg_values_all = c(avg_values_all,avg_values)
diff = c(avg2 - avg1)
diff_all = c(diff_all,diff )
Native_means = c(Native_means,avg1)
Web_means <- c(Web_means,avg2)

p <- ggplot(dataf3, aes(types, Joule)) 
plot2 = p + geom_boxplot() 
plot2

# Plotting Instagram-------------------------------------------------4
type1 = c(rep("IG", 15))
type2 = c(rep("IG", 15))

Values = exctract_data_from_folder("Instagram_native_15/",15)
Values2 = exctract_data_from_folder("Instagram_web_15/",15)
Nvalues = c(Nvalues,Values)
Wvalues = c(Wvalues,Values2)
tracker <- c(tracker,Values)
naive_Econsumption <- c(naive_Econsumption,Values2)
Joule=c(Values,Values2)
TotalJoule=c(TotalJoule,Joule)
types=c(type1,type2)
treatment=c(treatment,treatment2)
dataf4 <- data.frame(types,Joule)

avg1 = mean(Values)
avg2 = mean(Values2)
avg_values = c(avg1,avg2)
avg_values_all = c(avg_values_all,avg_values)
diff = c(avg2 - avg1)
diff_all = c(diff_all,diff )
Native_means = c(Native_means,avg1)
Web_means <- c(Web_means,avg2)

p <- ggplot(dataf4, aes(types, Joule)) 
plot2 = p + geom_boxplot() 
plot2

# Plotting Twitter-------------------------------------------------5
type1 = c(rep("T", 15))
type2 = c(rep("T", 15))
tracker <- c(tracker,Values)
naive_Econsumption <- c(naive_Econsumption,Values2)
Values = exctract_data_from_folder("Twitter_native_15/",15)
Values2 = exctract_data_from_folder("Twitter_web_15/",15)
Nvalues = c(Nvalues,Values)
Wvalues = c(Wvalues,Values2)
Joule=c(Values,Values2)
TotalJoule=c(TotalJoule,Joule)
types=c(type1,type2)
treatment=c(treatment,treatment2)
dataf5 <- data.frame(types,Joule)

avg1 = mean(Values)
avg2 = mean(Values2)
avg_values = c(avg1,avg2)
avg_values_all = c(avg_values_all,avg_values)
diff = c(avg2 - avg1)
diff_all = c(diff_all,diff )
Native_means = c(Native_means,avg1)
Web_means <- c(Web_means,avg2)

p <- ggplot(dataf5, aes(types, Joule)) 
plot2 = p + geom_boxplot() 
plot2

#------------------------------------------------------Plotting all------------------------------------------------------
#Add all dataframes from all applications

complete_dataframe = rbind(dataf,dataf2,dataf3,dataf4,dataf5)

bp <- ggplot(complete_dataframe, aes(types, Joule,fill=treatment, title("test"))) 
bp +  geom_boxplot() + ggtitle("Energyconsumption of treatments") +
  scale_fill_manual(values=c('#FF5151','#333E7C'))+theme(
  plot.title = element_text(color="black", size=14, face="bold.italic"),
  axis.title.x = element_text(color="black", size=14, face="bold"),
  axis.title.y = element_text(color="black", size=14, face="bold"))

qqplot(tracker,naive_Econsumption)

t.test(TotalJoule~treatment)

qqnorm(TotalJoule, main= "Energy Consumption QQ plot")
qqline(TotalJoule, col="red")

qqnorm(Wvalues, main= "Web energy consumption QQ plot")
qqline(Wvalues, col="red")

qqnorm(Nvalues, main= "Native energy consumption QQ plot")
qqline(Nvalues, col="red")

shapiro.test(Wvalues)
shapiro.test(Nvalues)

differences = Native_means - Web_means
qqnorm(differences, main="Differences in energy consumption per app QQ plot")

wilcox.test(Native_means, Web_means, paired = TRUE, alternative = "two.sided")

groups <- c("N","W","N","W","N","W","N","W","N","W")

t.test(avg_values_all~groups)

bars<-data.frame(treatment=rep(c("Native","Web"),each=5),
                 apps=rep(c("GM","YT","FB", "IG","T"),2),
                 means=c(Native_means, Web_means))


barplot <- ggplot(data=bars, aes(x=apps, y=means, fill=treatment)) + geom_bar(stat="identity", position=position_dodge())+ggtitle("Mean energy consumption for native vs web apps")+
  xlab("Application") + ylab("Average energy consumption (J)") + labs(fill="Legend") + scale_x_discrete(limits=c("GM","YT","FB","IG","T"))+
  scale_fill_manual(values=c('#FF5151','#333E7C')) +
  theme(
    plot.title = element_text(color="black", size=14, face="bold.italic"),
    axis.title.x = element_text(color="black", size=14, face="bold"),
    axis.title.y = element_text(color="black", size=14, face="bold")) 

barplot

# LOGPLOT

log_diff = sort(log(diff_all))


log_diff = c(-0.8230163,  1.5122412,  4.3350934,  2.8368953,0.2061938  )

barplot(log_diff,y=, main="Logarithmic difference distibution", 
        xlab="Applications",ylab="Log (avg energy consumption)")

mydata <- matrix(log_diff, ncol = 1, byrow = TRUE,
                 dimnames = list(c("T", "IG", "GM", 
                                   "FB", "YT")))

mydata


barplot(t(mydata), beside = TRUE,  
        ylim = c(0, 5), axes = TRUE,
        xlab="Applications",
        ylab="Log (avg energy consumption)",
        main = "Logarithmic difference distibution",
        col = "grey")

