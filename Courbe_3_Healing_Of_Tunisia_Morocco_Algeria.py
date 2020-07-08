import csv
import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D


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



# Tunisia / Algeria / Morocco Healings (April) ------------------------------------------------------------------



figure, axis_algerie = plt.subplots()
axis_maroc = axis_algerie.twinx()
axis_tunisie = axis_algerie.twinx()
axis_tunisie.spines["right"].set_position(("axes", 1.05))
axis_tunisie.spines["right"].set_visible(True)


# line 1 points 
x1 = ExtractSeparatedData(ExtractDataOfCountry('tunisie'))[0][28:-1] 
y1 = ExtractSeparatedData(ExtractDataOfCountry('tunisie'))[3][28:-1] 
# line 2 points 
x2 = ExtractSeparatedData(ExtractDataOfCountry('AlgÃ©rie'))[0][36:]   
y2 = ExtractSeparatedData(ExtractDataOfCountry('AlgÃ©rie'))[3][36:]
# line 3 points 
x3 = ExtractSeparatedData(ExtractDataOfCountry('Maroc'))[0][30:]   
y3 = ExtractSeparatedData(ExtractDataOfCountry('Maroc'))[3][30:]



# plotting the lines  
 
axis_maroc.tick_params(axis='y', labelsize=5)
axis_algerie.tick_params(axis='y', labelsize=5)
axis_tunisie.tick_params(axis='y', labelsize=5)
axis_tunisie.plot(x1, y1,color="red")
axis_algerie.plot(x2, y2,color="green")
axis_maroc.plot(x3, y3, color="orange") 


#Settings for the window
plt.subplots_adjust(left=0.04, bottom=0.09, right=0.92, top=0.97)

# naming the axis 
axis_algerie.set_xlabel('Days - axis') 
axis_algerie.set_xticklabels(labels = x2, rotation=45)
axis_algerie.set_ylabel('Algeria Healings - axis') 
axis_maroc.set_ylabel('Morocco Healings - axis')
axis_tunisie.set_ylabel('Tunisia Healings - axis')

# giving a title to my graph 
plt.title('the evolution of new cases of Healings in Algeria / Morocco / Tunisia for the month April. ( Alt + F4 to Exit )') 
  
# show a legend on the plot 
custom_lines = [Line2D([0], [0], color="red", lw=2),
                Line2D([0], [0], color="green", lw=2),
                Line2D([0], [0], color="orange", lw=2)]

plt.legend(custom_lines, ['Tunisia', 'Algeria', 'Morocco'],loc='upper left')


# Zooming the window Auto
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
# function to show the plot 

plt.show() 

#------------------------------------------------------------------------------------------------------