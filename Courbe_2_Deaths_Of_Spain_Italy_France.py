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


# France / Italy / Spain Deaths (Marsh / April) ------------------------------------------------------------------



figure, axis_italie = plt.subplots()
axis_espagne = axis_italie.twinx()
axis_france = axis_italie.twinx()
axis_france.spines["right"].set_position(("axes", 1.05))
axis_france.spines["right"].set_visible(True)


# line 1 points 
x1 = ExtractSeparatedData(ExtractDataOfCountry('france'))[0][37:-1] 
y1 = ExtractSeparatedData(ExtractDataOfCountry('france'))[2][38:] 
# line 2 points 
x2 = ExtractSeparatedData(ExtractDataOfCountry('italie'))[0][30:]   
y2 = ExtractSeparatedData(ExtractDataOfCountry('italie'))[2][30:]
# line 3 points 
x3 = ExtractSeparatedData(ExtractDataOfCountry('italie'))[0][30:]   
y3 = ExtractSeparatedData(ExtractDataOfCountry('espagne'))[2][29:]



# plotting the lines   
axis_espagne.tick_params(axis='y' , labelsize=5)
axis_italie.tick_params(axis='y' , labelsize=5)
axis_france.tick_params(axis='y', labelsize=5)
axis_france.plot(x1, y1,color="blue", linestyle='dashed', linewidth = 1.5)
axis_espagne.plot(x3, y3,color="red", linestyle='dashed', linewidth = 1.5) 
axis_italie.plot(x2, y2,color="green", linestyle='dashed', linewidth = 1.5)



#Settings for the window
plt.subplots_adjust(left=0.04, bottom=0.09, right=0.92, top=0.97)

# naming the axis 
axis_italie.set_xlabel('Days - axis') 
axis_italie.set_xticklabels(labels = x2, rotation=45)
axis_italie.set_ylabel('Italy Deaths - axis') 
axis_espagne.set_ylabel('Spain Deaths - axis')
axis_france.set_ylabel('France Deaths - axis')

# giving a title to my graph 
plt.title('the evolution of new cases of Deaths in france / italy / spain for the months March and April. ( Alt + F4 to Exit )') 
  
# show a legend on the plot 
custom_lines = [Line2D([0], [0], color="blue", lw=2),
                Line2D([0], [0], color="green", lw=2),
                Line2D([0], [0], color="red", lw=2)]

plt.legend(custom_lines, ['France', 'Italy', 'Spain'])


# Zooming the window Auto
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
# function to show the plot 

plt.show() 

#------------------------------------------------------------------------------------------------------