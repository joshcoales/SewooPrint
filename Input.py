from PIL import Image
import math
from Printer import Printer
from Formatter import Formatter

class Input(object):
    '''
    Stores a bunch of different raw inputs to be used.
    '''

    TYPE_TEXT = "text"
    TYPE_ASCII = "ascii"
    TYPE_IMAGE = "image"
    TYPE_STREAM = "stream"

    mPrinter = None
    mFormatter = None

    def __init__(self):
        '''
        Start input choice.
        '''
        self.mPrinter = Printer()
        self.mFormatter = Formatter()
        inputType = self.chooseInputType()
        if(inputType is None):
            print("Invalid input type.")
            return
        if(inputType == self.TYPE_TEXT):
            print("Text input type selected.")
            #Handle text type input.
            self.chooseTextInput()
            return
        if(inputType == self.TYPE_ASCII):
            print("Ascii art input type selected.")
            #TODO: Handle ascii art type input.
            return
        if(inputType == self.TYPE_IMAGE):
            print("Image input type selected.")
            #TODO: Handle image type input.
            return
        if(inputType == self.TYPE_STREAM):
            print("Stream input type selected.")
            #TODO: Hande stream type input.
            return
        print("Unknown input type.")
        return


    def chooseInputType(self):
        '''
        Ask the user what type of input they want
        '''
        print("Please select an input type.")
        print("Available input types: text, ascii art, image, stream")
        userInput = input("Enter type: ")
        userInputClean = userInput.strip().lower()
        if(userInputClean in ['text']):
            return self.TYPE_TEXT
        if(userInputClean in ['ascii','ascii art','asciiart']):
            return self.TYPE_ASCII
        if(userInputClean in ['image','img','picture','pic']):
            return self.TYPE_IMAGE
        if(userInputClean in ['stream','feed','twitter']):
            return self.TYPE_STREAM
        return None

    def chooseTextInput(self):
        'chooses a text input'
        print("Available text inputs: tech support oath, raw.")
        userInput = input("Please select: ")
        userInputClean = userInput.lower().strip()
        if(userInputClean in ['tech support oath','techsupportoath','oath']):
            oathText = self.techSupportOath()
            printOutput = self.mFormatter.title("Tech support oath")
            printOutput += self.mFormatter.multiLine(oathText)
            self.mPrinter.printRaw(printOutput)

    def techSupportOath(self):
        '''
        Recites the tech support oath.
        Parody of the Night's Watch oath.
        '''
        output = "User issues gather, and now my watch begins. " 
        output += "It shall not end until my death. "
        output += "I shall take no wife (that I will ever see except on weekends), "
        output += "hold no lands (because I don't make nearly enough), "
        output += "father no children (because I will never be home anyway). "
        output += "I shall receive no thanks and win no glory. "
        output += "I shall live and die at my desk. "
        output += "I am the antivirus in the darkness. "
        output += "I am the coder on the walls. "
        output += "I am the password reset that guards the logins of men. "
        output += "I pledge my life and honor to the Help Desk's Watch, "
        output += "for this night and all the nights to come."
        return output
    
    @staticmethod
    def loadImageFile(fileName):
        fileName = 'Opening_bill_transparent.png'
        image = Image.open(fileName).convert('RGBA')
        width,height = image.size
        newwidth = 400
        scalefactor = width/newwidth
        newheight = height//scalefactor
        endwidth = math.ceil(newwidth/8)*8
        endheight = math.ceil(newheight/8)*8
        image = image.resize((endwidth,endheight),Image.ANTIALIAS)
        
        image_string = b'\x1d\x2a'
        image_string += bytes([endwidth//8,endheight//8])
        pixnum = 0
        pixval = 0
        for x in range(endwidth):
            for y in range(endheight):
                r,g,b,a = image.getpixel((x,y))
                if(r*g*b<100*100*100 and a>50):
                    pixval += 2**(7-pixnum)
                if(pixnum==7):
                    image_string += bytes([pixval])
                    pixnum = 0
                    pixval = 0
                else:
                    pixnum += 1
        return image_string + b'\x1d\x2f\x00'
    
    @staticmethod
    def loadImageSilhouetteFile(fileName):
        image = Image.open(fileName).convert('RGBA')
        width,height = image.size
        newwidth = 400
        scalefactor = width/newwidth
        newheight = height//scalefactor
        endwidth = math.ceil(newwidth/8)*8
        endheight = math.ceil(newheight/8)*8
        image = image.resize((endwidth,endheight),Image.ANTIALIAS)
        
        image_string = b'\x1d\x2a'
        image_string += bytes([endwidth//8,endheight//8])
        pixnum = 0
        pixval = 0
        for x in range(endwidth):
            for y in range(endheight):
                _,_,_,a = image.getpixel((x,y))
                if(a>10):
                    pixval += 2**(7-pixnum)
                if(pixnum==7):
                    image_string += bytes([pixval])
                    pixnum = 0
                    pixval = 0
                else:
                    pixnum += 1
        image_string += b'\x1d\x2f\x00'
        return image_string
        
if(__name__=="__main__"):
    Input()
