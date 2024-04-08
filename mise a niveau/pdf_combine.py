from PyPDF2 import PdfReader, PdfWriter

contenu_sortie =PdfWriter()
fichier_pdf_presentation = open("presentation.pdf","rb")
fichier_pdf_recap = open("recap.pdf","rb")

readear_presentation = PdfReader(fichier_pdf_presentation)
readear_recap = PdfReader(fichier_pdf_recap)

print("Nombre de pages du fichier recap:", len(readear_recap.pages))

contenu_sortie.add_page(readear_presentation.pages[0])
for page in readear_recap.pages:
    contenu_sortie.add_page(page)

fichier_de_sortie = open("fichier_de_sortie.pdf", "wb")
contenu_sortie.write(fichier_de_sortie)

fichier_de_sortie.close()
# # fichier_pdf_presentation.close()
# fichier_pdf_recap.close()

