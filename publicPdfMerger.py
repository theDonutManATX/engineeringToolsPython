# we are going to merge a bunch of part PDFs to make a packet of parts automatically just by clicking on the python file
# I (Duncan McEwan) am doing this so that rev control is easier 11/29/2023

from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os
import re

# need to define paths to look for PDFs
# taking part 23052-3031 as an example, its path is:
# "C:\Users\UserID\Box\Internal\Projects\2023\ARC_23052_ULS\PDF\23052-3031_02.pdf"

# One thing I have to take into account is I won't know the rev control number at the end of the file path

pathStr = "C:/Users/UserID/Box/Internal/Projects/2023/ARC_23052_ULS/PDF/"

# Recommended to source part list from BOM for total completeness

#2003
PartList2003 = ["2003-", "3003", "3004", "3005", "3006", "3007", "3032", "3033", "3034", "3035", "3036", "3037", "3038", "3043", "3044", "3045"]

#2008
PartList2008 = ["2008.pdf", "2008-", "2008_", "2005", "2006", "2007", "2009", "2004", "23052-3001", "23052-3002", "23052-3008", "23052-3010", "23052-3011", "23052-3012", "23052-3013", "23052-3014", "23052-3015", "23052-3016",
"23052-3017", "23052-3018", "23052-3019", "23052-3020", "23052-3021", "23052-3022", "23052-3023", "23052-3024", "23052-3025", "23052-3026", "23052-3027",
"23052-3028", "23052-3029", "23052-3030", "23052-3039", "23052-3040", "23052-3041", "23052-3042", "23052-3046"]

#2010
PartList2010 = ["2010.pdf", "2010-", "2010_", "2011", "2012", "2013", "3038", "3045", "23052-3047", "23052-3048", "23052-3049", "23052-3050", "23052-3051", "23052-3052", "23052-3053", "23052-3054", "23052-3055", "3056",
"3057", "3058", "23052-3059", "23052-3060", "23052-3061", "23052-3116"]

#2014
PartList2014 = ["2014.pdf", "2014-", "2014_", "2015", "2016", "2018", "2019", "2020",  "23052-3062", "23052-3063", "23052-3064","23052-3065", "23052-3066", "23052-3067", "23052-3068", "23052-3069", "23052-3070", "23052-3071",
"23052-3072", "23052-3073", "23052-3074", "23052-3075", "23052-3076", "23052-3077", "23052-3078", "23052-3079", "23052-3080", "23052-3081", "23052-3084",
"23052-3085", "23052-3086", "23052-3087", "23052-3088", "23052-3114", "23052-3115"]

#2022
PartList2022 = ["23052-3093", "23052-3094", "23052-3095", "23052-3096", "23052-3097", "23052-3098", "23052-3099"]

#2024
PartList2024 = ["23052-3100", "23052-3101", "23052-3102", "23052-3104", "23052-3105", "23052-3106", "23052-3107", "23052-3108", "23052-3109", "23052-3110", "23052-3111", "23052-3112"]

# Active list declarations
activePartList = []
activePathList = []

pdf_files = [pdf for pdf in os.listdir("C:/Users/UserID/Box/Internal/Projects/2023/ARC_23052_ULS/PDF/") if '.pdf' in pdf]

#------------------------------#
# CHANGE BETWEEN SUB-ASSEMBLIES HERE #
activePartList = PartList2024
#------------------------------#

for i in range(len(activePartList)):
    for j in range(len(pdf_files)):
        if(activePartList[i] in pdf_files[j]):
            currentPathString = pathStr + pdf_files[j]
            activePathList.append(currentPathString)

# output file path (must be found due to unknown rev control number)
for j in range(len(pdf_files)):
    if("2022 COMBINED" in pdf_files[j]):
        combinedOutputPath = pathStr + pdf_files[j]

        # extract the rev control number to keep it consistent with what is already there, personally, I don't see the need for
        # a rev number on the COMBINED packages since they are the most prone to changes
        extractedFileName = pdf_files[j]
        endOfFileName = extractedFileName[-7:]
        if(re.search("[0-9]",endOfFileName)):
            revNumber = endOfFileName[-6:-4]
        else:
            revNumber = ""

merger = PdfMerger()

for pdf in activePathList:
    merger.append(pdf)

if(revNumber == ""):
    newPDFName = "23052-2024 COMBINED" + revNumber + ".pdf"
else:
    newPDFName = "23052-2024 COMBINED_" + revNumber + ".pdf"

merger.write(newPDFName)
merger.close()

os.remove("C:/Users/UserID/Box/Internal/Projects/2023/ARC_23052_ULS/PDF/" + newPDFName)
os.rename(newPDFName, "C:/Users/UserID/Box/Internal/Projects/2023/ARC_23052_ULS/PDF/" + newPDFName)
print(newPDFName + " Generated. Have a nice day.")