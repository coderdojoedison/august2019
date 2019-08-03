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
