import PyPDF2, requests
def main():
    tries = "yes"
    url = input("Please enter the URL of the PDF: ")
    while "y" in tries.lower(): #This keeps the program running as long as someone wants to use it.
        word = input("\n\nPlease enter the word you are trying to find: ")
        test(word, url)
        tries = input("Would you like to search for another word? ") #Do we need this for website???
def test(word, Q1):
    x, z = 0, 0
    transfer = requests.get(Q1)
    open("PDF.pdf", "wb").write(transfer.content)
    pdfReader = PyPDF2.PdfFileReader("PDF.pdf")
    pages = pdfReader.getNumPages()
    for x1 in range(pages): #While the number of pages searched is not equal to the number of pages in the PDF: keep searching.
        derp1 = pdfReader.getPage(x1)
        derp2 = derp1.extractText()
        derp2 = derp2.replace("\n", " ") #This takes out PDF formatting of random indents and replaces it with spaces.
        derp3 = derp2.replace(" ", "") #Taking out all spaces allows for a more accurate search because of PDF formatting.
        if word.lower() in derp3.lower():
            z = final(derp3, derp2, word, x, x1, z) #Z is returned from final and printed to show number of results.
        if not x1 > 0:
            z = final(derp3, derp2, word, x, x1, z)
    print(str(z) + " Results found.\n") #This is better than "word not found" because it displays the same information with less code.
def final(derp3, derp2, word, x, x1, z):
    nospace = derp3.lower().split(".")
    derp = derp2.lower().split(".")
    while x != len(nospace): #This fixes the 1 word per page problem, now it searches through the whole page and returns every instance of the word.
        if word.lower() in nospace[x]:
            z += 1 #This allows the variable Z to keep track of how many times a word is found successfully.
            finalprint = ('"' + derp[x] + '."  (Found on page: ' + str(x1 + 1) + ")\n\n")
            open("Testnotepad.txt", "a").write(finalprint)  #Add number of results.
        x += 1
    return z
main()
open("Testnotepad.txt", "wb").close()
