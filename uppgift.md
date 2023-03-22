Programmera mera i Python, 7.5 hp
Provmoment:      Tentamen, 5 hp.

Ladokkod             A266TG

Datum och tid:                                                     
Onsdag 22/3 kl.13.00 till torsdag 23/3 kl. 12.59

Plats:                                           
Hemtentamen         

Poäng:      Maximal poäng är 60 p. För godkänt krävs 36 p (60%).

Allmänna anvisningar:
- All kod ska vara väl genomtänkt, lättläst och välkommenterad.
- Variabler ska ha meningsfulla namn.
- Du får inte lämna in kod som genererar felmeddelande. Då blir deluppgiften
  omedelbart underkänd (0 p).
- Du får inte lämna in bortkommenterad kod.
- Varje uppgift skall lämnas in som .py-filer med följande namn:
  Uppgift_1.py          (uppgift 1)
  Uppgift_2.py          (uppgift 2)
  Uppgift_3.py          (uppgift 3)
  Lämna INTE in dessa filer komprimerade till en zip-fil eller i något annat
  komprimeringsformat.

 

Tentamen ska genomföras enskilt, dvs. samarbete är inte tillåtet. Det är inte heller tillåtet att använda någon form av AI-hjälpmedel, typ ChatGPT eller liknande. Genom att lämna in tentamen intygar du på heder och samvete att du har löst uppgifterna självständigt utan hjälp av någon annan person och inte heller använt någon form av AI-hjälpmedel.

 

Ansvariga lärare:                     
Hoshang Heydari, 0763–090722                       (uppgift 1)
Hoshang Heydari, 0763–090722                       (uppgift 2)
Chandadevi Giri,   0790–984299                       (uppgift 3)

Lycka till!

Uppgift 1       (Totalt 20 p)
Ansvarig lärare: Hoshang Heydari

 

a) Skapa följande Numpy-array genom att använda funktionen f(x)=x+x**y och döp den till NP_A. Använd sedan NP_A för att lösa nedanstående deluppgifter. (4p)

[[      1       0       0       0       0       0       0       0]
[      2       2       2       2       2       2       2       2]
[      3       4       6      10      18      34      66     130]
[      4       6      12      30      84     246     732    2190]
[      5       8      20      68     260    1028    4100   16388]
[      6      10      30     130     630    3130   15630   78130]
[      7      12      42     222    1302    7782   46662  279942]
[      8      14      56     350    2408   16814  117656  823550]
[      9      16      72     520    4104   32776  262152 2097160]
[     10      18      90     738    6570   59058  531450 4782978]]
 


b) Extrahera

                [[   4   10   34]
                 [   8   68 1028]
                 [  12  222 7782]]
ur NP_A genom att använda metoden slicing och skriv ut resultatet. (2p)

c) Omvandla NP_A till en standard Python lista och skriv ut denna. Skriv därefter ut alla element i listan som är större än 10 men mindre än 100. (4p)


d) Skriv ut summan av maximum och minimum samt medelvärdet för
- varje rad
- och varje kolumn
i NP_A i uppgift a. (4p)

 

e) Skapa en kopia av NP_A i uppg a och tillämpa funktionen where() för att byta ut alla element i denna kopia som är större än 100 mot talet -1. Skriv därefter ut innehållet på skärmen. (2p)

 

f) Omvandla NP_A i uppgift a till en vektor (endimensionell NumPy-array) och döp den till NP_Arr och skriv ut resultatet på skärmen. (2p)

 

g) Importera modulen pyplot och rita en graf över 1+NP_Arr**3+1+3*NP_Arr**2 + 6*NP_Arr och 1+ 1+3*NP_Arr**2 + 6*NP_Arr och 1+NP_Arr**3+ 6*NP_Arr i samma diagram. NP_Arr är den endimensionella vektorn skapad från NP_A i uppgift f. (2p)

 

 

Uppgift 2       (Totalt 20 p)
Ansvarig lärare: Hoshang Heydari

a) I den här uppgiften ska du utveckla ett program som håller reda på vilka datorer som finns i ett (fiktivt) företag. Du ska lösa uppgiften genom att använda dina kunskaper i objektorienterad programmering som du fått i denna kurs. Skapa klassen Dator som ska hålla reda på datortillverkare och viss annan information om datorn (se nedan). Därefter ska du skriva ett huvudprogram med två egendefinierade funktioner lista() och visa_data ()   Funktionen lista() frågar först efter antal datorer som ska lagras av programmet och därefter matas informationen in enligt nedan. Anropar man funktionen visa_data() ska programmet skriva ut listan över datorer som skapats med funktionen lista() i en tabell på skärmen enligt nedan. (8p)

   Ange antal datorer som ska skrivas in:1
   Ange tillverkare: HP
   Ange modell: OptiPlex 7000
   Ange processortyp: Core i7
   Ange installerad RAM (GB): 16
   Ange inköpspris: 14990

Tillverkare    Modell         Processortyp   Installerat RAM          Pris[kr]
=============================================================================
HP             OptiPlex 7000  Core i7         16GB                   14990

 

b) Du ska nu vidareutveckla programmet i uppg 2a genom att skapa underklassen Laptop till klassen Dator och som sparar information om laptopdatorer. Skriv ett huvudprogram där man skapar en underklass Laptop till klassen Dator enligt följande syntaxexempel:
Laptop('ASUS', 'ExpertBook', 'Core i5','16', '7990','15.6') och därefter skriver ut informationen på skärmen: (6p)

   Tillverkare: ASUS
   Modell: ExpertBook
   Processortyp: Core i5
   Installerat RAM: 16 GB
   Pris: 7990.0 Kr
   Skärmstorlek: 15.6 tum
 

c)  I denna deluppgift ska du använda modulen Pickle och skriva ett program som sparar informationen om datorerna som du skapade i uppgift 2a och 2b i en fil med namnet dator.dat. Du kan till exempel använda dump() metoden i Pickle modulen för att konverterar en Python-objekthierarki till en byteström vilken kallas serilaisering som kan sparas i en fil. Du kan skapa datafilen dator.dat och skriva dina datordata i den. Programmets utskrift ska ha följande utseende: (3p)

   Ange datorns fabrikat: Lenovo
   Ange modell: ThinkCentre M70t Tower G3
   Ange processortyp: Core i7 
   Ange installerat RAM (GB): 16
   Ange pris (kr): 9995.0

   Vill du ange flera datorer? (ja/nej): nej
   Data är skriven i filen dator.dat.


d) Nu ska vi läsa data som du har sparat i filen dator.dat. Du kan göra det också med hjälp av Pickle modulen och load() metoden. Du ska skapa en funktion visa_data(dator) som skriver ut datafil innehållet som vi har sparat i uppgift 2c. Utskrift ska se ut enligt nedan: (3p)

   Tillverkare: Lenovo
   Modell: ThinkCentre M70t Tower G3
   Processortyp: Core i7 
   Installerad RAM: 16 GB
   Pris: 9995.0 Kr



Uppgift 3       (Totalt 20 p)
Ansvarig lärare: Chanda

The World Happiness Report (https://worldhappiness.report/Links to an external site.) is a landmark survey of the state of global happiness. The reports examine the current state of happiness in the world and demonstrate how the new happiness science explains both individual and national levels differences in happiness. Governments, organizations, and civil society are using happiness indicators to guide their policy decisions in an increasing number of countries, which has increased the report's visibility on a global scale.

The csv files contain the Happiness Score for countries along with the factors used to explain the score for the year 2015 and 2016.Happiness Rank are the ranks of the countries based on the Happiness score. Happiness Score is a national average of the responses to the main life evaluation question asked in the Gallup World Poll (GWP), which uses the Cantril Ladder. The following columns: GDP per Capita, Family, Life Expectancy, Freedom, Generosity, Trust Government Corruption describe the extent to which these factors contribute in evaluating the happiness in each country.

3. 
The objective of the task is to analyze the ‘world happiness data’ for the year 2015 and 2016 with the filenames 2015.csv and 2016.csv. Below tasks must be performed by using pandas (3.a - 3.c) and matplotlib (3.b - 3.c) modules.

3a:
Write the code that reads the contents from given csv-files (see below) using Pandas with separator semicolon (;) and store the data in DataFrame objects as df_world_happiness_2015 and df_world_happiness_2016. Then check the content by printing the first five lines of the DataFrames.        (3p)

Download 2015.csv here Download here.
Download 2016.csv here Download here.

3b:

Calculate the average (mean) of the columns ‘Freedom’, ‘Happiness score’ and ‘Trust’ for the year 2015 and 2016 by ‘Region’. Present the result in tabular form (Table 1 and 2). (2p)
     Note:
     -     Rename the column name ‘Happiness Score’ as ‘Happiness’
     -     Rename the column name ‘Trust (Government Corruption)’ as ‘Trust’


Calculate the relative change using the below formula for the columns Freedom, Happiness and Trust (see Table 3). (2p)
Formula.PNG

 Example: 

 The relative change of Freedom for the region Australia and New Zealand  in 2015 and 2016  
 can  be calculated as: ((0.645310   - 0.574920) /0. 574920) *100

  3. Create the bar plot for the calculated difference to visualize the changes (see Figure 1).
      The figure must have the Title, x and y axis label and legend as shown in the Figure 1. (2p)

      (Please note that the tables below are representing samples and the content is not necessary
       the correct numbers)


Tabell_till_PM-1.PNG


Figure 1:

Figur_1_tentamen.png

3c:

The task is here for analyzing the top 10 happiest countries in the year 2015 and 2016

Create the new DataFrames named as df_2015 and df_2016 which contains only columns ‘Country’, ‘Health (Life Expectancy)’, ’Happiness Rank’ from df_world_happiness_2015 and df_world_happiness_2016. (1p)
Rename the column names in df_2015 and df_2016 as below: (1p)
'Country', 'Health_Expectancy_2015', 'Rank_2015'
'Country', 'Health_Expectancy_2016', 'Rank_2016'
Sort the values for the both DataFrames by 'Health_Expectancy_<year>’, where <year> refer to 2015 and 2016. (2p)
Create the new DataFrames from df_2015 and df_2016 for the top 10 countries by Health_Expectancy and their corresponding Rank and print a table as shown in Table 4 and 5. (2p)
Plot the scatter plot with x axis as Health Expectancy and y axis as Rank for the top 10 countries in 2015 and 2016. Combine the scatterplots using the subplot function. The figure must have the title, x and y axis label, legend and text annotation with the country name as shown in Figure 2. (3p)
Plot the bar plots for the countries (Hongkong, Singapore, Japan, South Korea, Italy) with country as x axis and Health Expectancy and Rank as y axis for year 2015 and 2016. The figure must have the title, x and y axis label and legend as shown in the Figure 3 and 4. (2p)
(Please note that the tables below are representing samples and the content is not necessary the correct numbers)

Tabell_2_till_PM.PNG

Figure 2:

Figur_2_tentamen.png

Figure 3:

Figur_3_tentamen.png

Figure 4:

Figur_4_tentamen-1.png

