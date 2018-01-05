import turtle

window = turtle.Screen()
window.bgcolor("white")

def thin_bar(barcode):
    barcode.width(5)   
    barcode.color("black")
    barcode.right(90)
    barcode.forward(100)
    barcode.left(90)
    barcode.left(90)
    barcode.forward(100)
    barcode.right(90)
    barcode.color("white")
    barcode.width(1)
    barcode.forward(5)

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
    barcode.forward(5)

def large_space(barcode):
    barcode.width(2)
    barcode.color("white")
    barcode.forward(12)
    

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
    barcode.forward(360)
    barcode.left(90)
    barcode.forward(100)
    barcode.left(90)
    barcode.forward(360)
	
	
def draw(barcode, call):
	if call == "thin":
		thin_bar(barcode)
	else if call == "thick":
		thick_bar(barcode)
	else if call == "large":
		large_space(barcode)
	else if call == "small":
		small_space(barcode)
		

Word = {
	"A": ["thick", "small", "thin", "small", "thin", "large", "thin", "small", "thick", "small"],
	"B": ["thin", "small", "thick", "small", "thin", "large", "thin", "small", "thick", "small"],
	"C": ["thick", "small", "thick", "small", "thin", "large", "thin", "small", "thin", "small"]
	}

    
barcode = turtle.Turtle()
barcode.color("black")
barcode.width(7)
barcode.speed(17)

draw_star(barcode)

for i in Word["A"]:
	draw(barcode, i)
for i in Word["B"]:
	draw(barcode, i)
for i in Word["C"]:
	draw(barcode, i)

draw_star(barcode)
finish_barcode(barcode)


window.exitonclick()
