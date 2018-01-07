import turtle

UserInput = input("Enter letters and numbers to be converted to a 3of9 barcode. Maximum of 10 characters.")

window = turtle.Screen()
window.bgcolor("white")

rootwindow = window.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

def thin_bar(barcode):
    barcode.width(3)   
    barcode.color("black")
    barcode.right(90)
    barcode.forward(100)
    barcode.left(90)
    barcode.left(90)
    barcode.forward(100)
    barcode.right(90)
    barcode.color("white")
    barcode.width(1)
    barcode.forward(4)

def thick_bar(barcode):
    barcode.width(7)   
    barcode.color("black")
    barcode.right(90)
    barcode.forward(100)
    barcode.left(90)
    barcode.left(90)
    barcode.forward(100)
    barcode.right(90)
    barcode.color("white")
    barcode.width(2)
    barcode.forward(5)

def small_space(barcode):
    barcode.width(2)
    barcode.color("white")
    barcode.forward(4)

def large_space(barcode):
    barcode.width(2)
    barcode.color("white")
    barcode.forward(8)
    

def draw_star(barcode):
    thin_bar(barcode)
    large_space(barcode)
    thin_bar(barcode)
    small_space(barcode)
    thick_bar(barcode)
    small_space(barcode)
    thick_bar(barcode)
    small_space(barcode)
    thin_bar(barcode)
    small_space(barcode)
    

def finish_barcode(barcode):
    barcode.width(18)
    barcode.color("white")
    barcode.left(90)
    barcode.left(90)
    barcode.forward(950)
    barcode.left(90)
    barcode.forward(100)
    barcode.left(90)
    barcode.forward(950)
	
	
def draw(barcode, call):
	if call == "thin":
		thin_bar(barcode)
	elif call == "thick":
		thick_bar(barcode)
	elif call == "large":
		large_space(barcode)
	elif call == "small":
		small_space(barcode)
		

Word = {
	"A": ["thick", "small", "thin", "small", "thin", "large", "thin", "small", "thick", "small"],
	"B": ["thin", "small", "thick", "small", "thin", "large", "thin", "small", "thick", "small"],
	"C": ["thick", "small", "thick", "small", "thin", "large", "thin", "small", "thin", "small"],
        "D": ["thin", "small", "thin", "small", "thick", "large", "thin", "small", "thick", "small"],
        "E": ["thick", "small", "thin", "small", "thick", "large", "thin", "small", "thin", "small"],	
	"F": ["thin", "small", "thick", "small", "thick", "large", "thin", "small", "thin", "small"],	
        "G": ["thin", "small", "thin", "small", "thin", "large", "thick", "small", "thick", "small"],	
	"H": ["thick", "small", "thin", "small", "thin", "large", "thick", "small", "thin", "small"],	
        "I": ["thin", "small", "thick", "small", "thin", "large", "thick", "small", "thin", "small"],	
	"J": ["thin", "small", "thin", "small", "thick", "large", "thick", "small", "thin", "small"],	
        "K": ["thick", "small", "thin", "small", "thin", "small", "thin", "large", "thick", "small"],	
	"L": ["thin", "small", "thick", "small", "thin", "small", "thin", "large", "thick", "small"],	
        "M": ["thick", "small", "thick", "small", "thin", "small", "thin", "large", "thin", "small"],	
	"N": ["thin", "small", "thin", "small", "thick", "small", "thin", "large", "thick", "small"],	
        "O": ["thick", "small", "thin", "small", "thick", "small", "thin", "large", "thin", "small"],	
	"P": ["thin", "small", "thick", "small", "thick", "small", "thin", "large", "thin", "small"],	
        "Q": ["thin", "small", "thin", "small", "thin", "small", "thick", "large", "thick", "small"],	
	"R": ["thick", "small", "thin", "small", "thin", "small", "thick", "large", "thin", "small"],	
        "S": ["thin", "small", "thick", "small", "thin", "small", "thick", "large", "thin", "small"],	
	"T": ["thin", "small", "thin", "small", "thick", "small", "thick", "large", "thin", "small"],	
        "U": ["thick", "large", "thin", "small", "thin", "small", "thin", "small", "thick", "small"],	
	"V": ["thin", "large", "thick", "small", "thin", "small", "thin", "small", "thick", "small"],	
        "W": ["thick", "large", "thick", "small", "thin", "small", "thin", "small", "thin", "small"],	
	"X": ["thin", "large", "thin", "small", "thick", "small", "thin", "small", "thick", "small"],	
        "Y": ["thick", "large", "thin", "small", "thick", "small", "thin", "small", "thin", "small"],	
	"Z": ["thin", "large", "thick", "small", "thick", "small", "thin", "small", "thin", "small"],	
        "1": ["thick", "small", "thin", "large", "thin", "small", "thin", "small", "thick", "small"],	
	"2": ["thin", "small", "thick", "large", "thin", "small", "thin", "small", "thick", "small"],	
        "3": ["thick", "small", "thick", "large", "thin", "small", "thin", "small", "thin", "small"],	
	"4": ["thin", "small", "thin", "large", "thick", "small", "thin", "small", "thick", "small"],	
        "5": ["thick", "small", "thin", "large", "thick", "small", "thin", "small", "thin", "small"],	
	"6": ["space", "thin", "small", "thick", "large", "thick", "small", "thin", "small", "thin", "small"],	
        "7": ["thin", "small", "thin", "large", "thin", "small", "thick", "small", "thick", "small"],	
	"8": ["thick", "small", "thin", "large", "thin", "small", "thick", "small", "thin", "small"],	
        "9": ["thin", "small", "thick", "large", "thin", "small", "thick", "small", "thin", "small"],	
	"0": ["thin", "small", "thin", "large", "thick", "small", "thick", "small", "thin", "small"]
	}
    
barcode = turtle.Turtle()
barcode.color("white")
barcode.width(7)
barcode.speed(35)
barcode.left(90)
barcode.left(90)
barcode.forward(300)
barcode.right(90)
barcode.right(90)
barcode.color("black")


draw_star(barcode)

ListCount = 0
for i in UserInput:
    if ListCount < 10:
        NewString = i.upper()
        try:
            for j in Word[NewString]:
                    draw(barcode, j)
        except KeyError:
            print("Your input must be letters and/or whole numbers. Try again.")

    ListCount += 1

draw_star(barcode)
finish_barcode(barcode)


window.exitonclick()
