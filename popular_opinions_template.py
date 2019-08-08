import pygal
import webbrowser


def createAndRender( chart, fileName ):

    svgFileName = fileName +".svg"
    chart.render_to_file( svgFileName)           
    htmlFileName = fileName + ".html"
                
    txt1 =  "<!DOCTYPE html><html><head></head><body><figure><embed type=\"image/svg+xml\" src= "
    txt2 = " </figure><body></html>"
    htmlSrc = txt1 +  svgFileName + txt2
    print("\n htmlsrc ")
    print( htmlSrc )
    print("\n htmlsrc ")
    with open(htmlFileName, "w") as htmlFile:
            htmlFile.write( htmlSrc)
    
    webbrowser.open(htmlFileName, new=2)

def renderPetsPieChart():
    petspie = pygal.Pie()
    petspie.title = 'Popular Pets'
    
    file = open('/home/pi/Downloads/pets.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        petspie.add(label, int(value))

    file.close()

    fileName = "petspie"
    createAndRender( petspie, fileName )

def renderPetsBarChart():
    petsbar = pygal.Bar()
    petsbar.title = 'Popular Pets'
    

    file = open('/home/pi/Downloads/pets.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        petsbar.add(label, int(value))
        
    file.close()
    fileName = "petsbar"
    createAndRender( petsbar, fileName )

def getUserInput():
    userInput = input("Which chart do you want to draw? For example, (say Pets_Bar, Pets_Pie, Butterfly, Pirates, Sports): ")
    userInput = userInput.lower() 
    if (userInput == "pets_bar"):
        renderPetsBarChart()
    elif (userInput == "pets_pie"):
        renderPetsPieChart()

getUserInput() 
