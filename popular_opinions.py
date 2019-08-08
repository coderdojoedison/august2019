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


def renderButterfliesBarChart():
    butterflies = pygal.Bar()
    butterflies.title = 'Butterfly Count'

    file = open('/home/pi/Downloads/butterflies.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(': ')
        butterflies.add(label, int(value))
    file.close()

    fileName = "butterflies"
    createAndRender( butterflies, fileName )

def renderpn():
    pn = pygal.Bar()
    pn.title = 'Pirates vs Ninjas'

    file = open('/home/pi/Downloads/piratesninjas.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        pn.add(label, int(value))
    file.close()


    fileName = "PiratesVsNinja"
    createAndRender( pn, fileName )

def rendersports():
    sports = pygal.Bar()
    sports.title = 'Favorite Sports'

    file = open('/home/pi/Downloads/sports.txt' , 'r')

    for line in file.read().splitlines():
        if line:
            label, value = line.split(' ')
            sports.add(label, int(value))
    file.close()

    fileName = "Sports"
    createAndRender ( sports, fileName ) 
    


def getUserInput():
    userInput = input("Which chart do you want to draw? For example, (say Pets_Bar, Pets_Pie, Butterfly, Pirates, Sports): ")
    userInput = userInput.lower() 
    if (userInput == "pets_bar"):
        renderPetsBarChart()
    elif (userInput == "pets_pie"):
        renderPetsPieChart()
    elif (userInput == "sports"):
        rendersports()
    elif (userInput == "pn"):
        renderpn()
    elif (userInput == "butterfly"):
        renderButterfliesBarChart() 
    
#call each of the functions to render

getUserInput()



    
                           
