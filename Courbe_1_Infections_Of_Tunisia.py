import csv
import matplotlib.pyplot as plt 



def ExtractFromCSV(PathFile):
    with open(PathFile, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data

def ExtractDataOfCountry(CountryName):
    DataResult = []
    for datalist in dataArray:
        DataCountry = datalist[0].split(';')
        if(DataCountry[1].lower() == CountryName.lower()):
            DataResult.append(DataCountry)
    return DataResult


# Function For Separate The Data of List Array
def ExtractSeparatedData(liste):
    DataSeparated = []

    # Extract dates Data
    dates = []
    for i in liste:
        dates.append(i[0][0:5])
    dates = dates[::-1] #reversing using list slicing
    DataSeparated.append(dates)
    # End Of Extraction

    # Extract infections Data
    infections = []
    for i in liste:
        infections.append(i[2])
    infections = infections[::-1] #reversing using list slicing
    DataSeparated.append(infections)
    # End Of Extraction

    # Extract deaths Data
    deaths = []
    for i in liste:
        deaths.append(i[3])
    deaths = deaths[::-1] #reversing using list slicing
    DataSeparated.append(deaths)
    # End Of Extraction

    # Extract healings Data
    healings = []
    for i in liste:
        healings.append(i[4])
    healings = healings[::-1] #reversing using list slicing
    DataSeparated.append(healings)
    # End Of Extraction

    # Extract rates deaths Data
    ratesdeaths = []
    for i in liste:
        ratesdeaths.append(i[5])
    ratesdeaths = ratesdeaths[::-1] #reversing using list slicing
    DataSeparated.append(ratesdeaths)
    # End Of Extraction

    # Extract rates healings Data
    rateshealings = []
    for i in liste:
        rateshealings.append(i[5])
    rateshealings = rateshealings[::-1] #reversing using list slicing
    DataSeparated.append(rateshealings)
    # End Of Extraction

    # Extract rates infections Data
    ratesinfections = []
    for i in liste:
        ratesinfections.append(i[5])
    ratesinfections = ratesinfections[::-1] #reversing using list slicing
    DataSeparated.append(ratesinfections)
    # End Of Extraction



    return DataSeparated


global dataArray
dataArray = ExtractFromCSV('coronaviruschiffres.csv') # Extract the Data of COVID-19 From csv file


# Tunisia Infections (Mars / Avril) ------------------------------------------------------------------

# line 1 points 
x1 = ExtractSeparatedData(ExtractDataOfCountry('tunisie'))[0][0:28] 
y1 = ExtractSeparatedData(ExtractDataOfCountry('tunisie'))[1][0:28] 
# plotting the line 1 points  
plt.plot(x1, y1, color='green', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='red', markersize=5,label = "March 2020" )
  
# line 2 points 
x2 = ExtractSeparatedData(ExtractDataOfCountry('tunisie'))[0][29:-1]  
y2 = ExtractSeparatedData(ExtractDataOfCountry('tunisie'))[1][29:-1]
# plotting the line 2 points  

plt.xticks(rotation=35)
plt.plot(x2, y2, color='orange', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='red', markersize=5,label = "April 2020" )
plt.subplots_adjust(left=0.04, bottom=0.09, right=1, top=0.97)

# naming the x axis 
plt.xlabel('Days - axis') 
# naming the y axis 
plt.ylabel('Infections - axis') 
# giving a title to my graph 
plt.title('the evolution of new cases of infection in Tunisia for the months March and April. ( Alt + F4 to Exit )') 
  
# show a legend on the plot 
plt.legend() 

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
# function to show the plot 
plt.show() 

#------------------------------------------------------------------------------------------------------