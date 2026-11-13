import pymupdf

doc = pymupdf.open("private_pdfs/MU_TMA_01-Q.pdf")

questions = []

for page in doc:
    text = page.get_text("blocks", sort = True)
    number = page.number

    for block in text:
        if block[6] == 0 and block[4]:

            words = block[4].split()

            if len(words) >= 2:
                if words[0] == "Question" and words[1].isdigit():

                    question = {
                            "number": int(words[1]) ,
                            "page": number 
                            }

                    questions.append(question)



print(questions)
