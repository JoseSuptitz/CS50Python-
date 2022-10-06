from fpdf import FPDF

def main():
    name = input('Name: ')
    shirt(name)

def shirt(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=40)
    pdf.cell(50, 0, 'CS50 Shirtificate')
    pdf.image("shirtificate.png", x=0, y=60)
    pdf.text(x=50, y=140, txt=f"{name} took CS50")
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()