from tkinter import *
root = Tk()
root.minsize(670, 450)
root.maxsize(690, 500)
root.title("Data Calculator from Marks")

mainf = Frame(root)  # Main Frame
mainf.grid(padx="10")

# Functions


def main():

    # Creating the New Window
    # Getting the values
    global ass
    global ssd
    global ams
    ass = assr1.get()
    ssd = ssdr1.get()
    ams = amsr1.get()

    # Destroying the Labels
    assf.destroy()
    ssdf.destroy()
    amsf.destroy()
    Submit1.destroy()
    submit.destroy()

    # Frames for Second Page
    namef = Frame(mainf)
    namef.pack(anchor="w")
    rollf = Frame(mainf)
    rollf.pack(anchor="w")
    submit2f = Frame(mainf)
    submit2f.pack(anchor="w")

    # Getting the Name of the Student
    namew1 = StringVar()
    namel = Label(namef, text="Enter the Name of the Student",
                  fg="red", font="weight:bold")
    namel.grid(row="1", column="0",)
    namew2 = Entry(namef, textvariable=namew1, fg="red")
    namew2.grid(row="1", column="2", padx=62, pady=5)

    # Getting the Roll Number of the Student
    rollnow1 = IntVar()
    rollnol = Label(rollf, text="Enter the Roll Number of the Student",
                    fg="red", font="weight:bold")
    rollnol.grid(row="3", column="0")
    rollnow2 = Entry(rollf, textvariable=rollnow1, fg="red")
    rollnow2.grid(row="3", column="3", padx=20)



    def submit2():
        # Getting the Values
        global name
        global rollno
        global ctf
        name = namew1.get()
        rollno = rollnow2.get()

        # Destroying Variables
        namef.destroy()
        rollf.destroy()
        submit2f.destroy()

        if(ass == "Yes"):

            if(ams == "Yes"):
                # Creating Frames
                headf = Frame(mainf)
                headf.pack(anchor="w")
                phyf = Frame(mainf)
                phyf.pack(anchor="w")
                chemf = Frame(mainf)
                chemf.pack(anchor="w")
                biof = Frame(mainf)
                biof.pack(anchor="w")
                mathf = Frame(mainf)
                mathf.pack(anchor="w")

                if(ssd == "Yes"):
                    hisf = Frame(mainf)
                    hisf.pack(anchor="w")
                    geof = Frame(mainf)
                    geof.pack(anchor="w")
                    civf = Frame(mainf)
                    civf.pack(anchor="w")

                if (ssd == "No"):
                    ssf = Frame(mainf)
                    ssf.pack(anchor="w")

                firstlf = Frame(mainf)
                firstlf.pack(anchor="w")
                secondlf = Frame(mainf)
                secondlf.pack(anchor="w")

                failpf = Frame(mainf)
                failpf.pack(anchor="w", pady=10)
                totalf = Frame(mainf)
                totalf.pack(anchor="w")

                submit3f = Frame(mainf)
                submit3f.pack(anchor="w")

                # Creating Labels
                headl = Label(
                    headf, text=f"Enter the Marks Scored by the {name} in:", font="weight:bold 22")
                headl.grid()
                phyl = Label(phyf, text="Physics", font=" 12", fg="red")
                phyl.grid(row="1", column="0")
                cheml = Label(chemf, text="Chemistry", font=" 12", fg="red")
                cheml.grid(row="3", column="0")
                biol = Label(biof, text="Biology", font=" 12", fg="red")
                biol.grid(row="5", column="0")

                mathl = Label(mathf, text="Mathematics", font=" 12", fg="red")
                mathl.grid(row="7", column="0")

                if (ssd == "Yes"):
                    hisl = Label(hisf, text="History", font=" 12", fg="red")
                    hisl.grid(row="9", column="0")
                    geol = Label(geof, text="Geography", font=" 12", fg="red")
                    geol.grid(row="11", column="0")
                    civil = Label(civf, text="Civics", font=" 12", fg="red")
                    civil.grid(row="13", column="0")

                    firstll = Label(
                        firstlf, text="First Language", font=" 12", fg="red")
                    firstll.grid(row="15", column="0")

                    secondll = Label(
                        secondlf, text="Second Language", font=" 12", fg="red")
                    secondll.grid(row="17", column="0")

                    failpl = Label(
                        failpf, text="Enter the Failing Percentage", font=" 15", fg="red")
                    failpl.grid(row="19", column="0")
                    totall = Label(
                        totalf, text="Enter the Total Marks the Exams Were Conducted", font=" 15", fg="red")
                    totall.grid(row="20", column="0")

                if (ssd == "No"):
                    ssdl = Label(ssf, text="Social Science",
                                 font=" 12", fg="red")
                    ssdl.grid(row="9", column="0")

                    firstll = Label(
                        firstlf, text="First Language", font=" 12", fg="red")
                    firstll.grid(row="11", column="0")
                    secondll = Label(
                        secondlf, text="Second Language", font=" 12", fg="red")
                    secondll.grid(row="13", column="0")

                    failpl = Label(
                        failpf, text="Enter the Failing Percentage", font=" 15", fg="red")
                    failpl.grid(row="15", column="0")
                    totall = Label(
                        totalf, text="Enter the Total Marks the Exams Were Conducted", font=" 15", fg="red")
                    totall.grid(row="17", column="0")

                # Creating Variables
                phyv = IntVar()
                chemv = IntVar()
                biov = IntVar()
                mathv = IntVar()
                if (ssd == "Yes"):
                    hisv = IntVar()
                    geov = IntVar()
                    civv = IntVar()

                if (ssd == "No"):
                    ssv = IntVar()

                firstlv = IntVar()
                secondlv = IntVar()
                failpv = IntVar()
                totalv = IntVar()

                # Creating Widgets
                phyw = Entry(phyf, textvariable=phyv)
                phyw.grid(row="1", column="3", padx="100")

                chemw = Entry(chemf, textvariable=chemv)
                chemw.grid(row="3", column="3", padx=85)

                biow = Entry(biof, textvariable=biov)
                biow.grid(row="5", column="3", padx=103)

                mathw = Entry(mathf, textvariable=mathv)
                mathw.grid(row="7", column="3", padx=67)

                if (ssd == "Yes"):
                    hisw = Entry(hisf, textvariable=hisv)
                    hisw.grid(row="9", column="3", padx=108)

                    geow = Entry(geof, textvariable=geov)
                    geow.grid(row="11", column="3", padx=78)

                    civw = Entry(civf, textvariable=civv)
                    civw.grid(row="13", column="3", padx=113)

                    firstlw = Entry(firstlf, textvariable=firstlv)
                    firstlw.grid(row="15", column="3", padx=52)

                    secondlw = Entry(secondlf, textvariable=secondlv)
                    secondlw.grid(row="17", column="3", padx=30)

                    failpw = Entry(failpf, textvariable=failpv)
                    failpw.grid(row="19", column="3", padx="10")

                    totalw = Entry(totalf, textvariable=totalv)
                    totalw.grid(row="20", column="3", padx="10")

                if (ssd == "No"):
                    ssw = Entry(ssf, textvariable=ssv)
                    ssw.grid(row="9", column="3", padx=50)

                    firstlw = Entry(firstlf, textvariable=firstlv)
                    firstlw.grid(row="11", column="3", padx=50)

                    secondlw = Entry(secondlf, textvariable=secondlv)
                    secondlw.grid(row="13", column="3", padx=27)

                    failpw = Entry(failpf, textvariable=failpv)
                    failpw.grid(row="15", column="3", padx="10")

                    totalw = Entry(totalf, textvariable=totalv)
                    totalw.grid(row="17", column="3", padx="10")

                # Submit Function

                def submit3():
                    # Creating Global Variables for the Values
                    global phym
                    global chemm
                    global biom
                    global mathm
                    if (ssd == "Yes"):
                        global hism
                        global geom
                        global civm
                    if (ssd == "No"):
                        global ssm

                    global firstlm
                    global secondlm

                    global failp
                    global totalm

                    # Getting the Values
                    phym = phyv.get()
                    chemm = chemv.get()
                    biom = biov.get()
                    mathm = mathv.get()

                    if (ssd == "Yes"):
                        hism = hisv.get()
                        geom = geov.get()
                        civm = civv.get()

                    if (ssd == "No"):
                        ssm = ssv.get()

                    firstlm = firstlv.get()
                    secondlm = secondlv.get()
                    failp = failpv.get()
                    totalm = totalv.get()



                    # Destroying Frames

                    headf.destroy()
                    phyf.destroy()
                    chemf.destroy()
                    biof.destroy()
                    mathf.destroy()
                    firstlf.destroy()
                    secondlf.destroy()

                    if (ssd == "Yes"):
                        hisf.destroy()
                        geof.destroy()
                        civf.destroy()

                    if (ssd == "No"):
                        ssf.destroy()

                    failpf.destroy()
                    totalf.destroy()
                    submit3f.destroy()

                    a = totalm
                    global phytm,chemtm,biotm,mathtm,firstltm,secondltm
                    phytm = a
                    chemtm = a
                    biotm = a
                    mathtm = a
                    if (ssd == "Yes"):
                        global histm, geotm, civtm
                        histm = a
                        geotm = a
                        civtm = a
                    if (ssd == "No"):
                        global sstm
                        sstm = a
                    firstltm = a
                    secondltm = a

                    # Calculation
                    calculate()


                submit3 = Button(submit3f, text="Submit", command=submit3)
                submit3.pack(anchor="w", pady="10")

            if (ams == "No"):

                # Creating Frames for Input of Total Marks
                headamnf = Frame(mainf)
                headamnf.pack()

                phyamnf = Frame(mainf)
                phyamnf.pack(anchor="w")

                # Chemistry Frame
                chemamnf = Frame(mainf)
                chemamnf.pack(anchor="w")
                bioamnf = Frame(mainf)
                bioamnf.pack(anchor="w")
                mathmnf = Frame(mainf)
                mathmnf.pack(anchor="w")

                if (ssd == "Yes"):
                    histamnf = Frame(mainf)
                    histamnf.pack(anchor="w")
                    geoamnf = Frame(mainf)
                    geoamnf.pack(anchor="w")
                    civamnf = Frame(mainf)
                    civamnf.pack(anchor="w")

                if (ssd == "No"):
                    ssamnf = Frame(mainf)
                    ssamnf.pack(anchor="w")

                firstlamnf = Frame(mainf)
                firstlamnf.pack(anchor="w")
                secondlamnf = Frame(mainf)
                secondlamnf.pack(anchor="w")

                failpamnf = Frame(mainf)
                failpamnf.pack(anchor="w", pady=10)

                Submit4f = Frame(mainf)
                Submit4f.pack(anchor="w")

                # Creating Labels

                headamnl = Label(headamnf, text=f"Enter the Marks Scored by {name} in the Following Subjects\n and Languages in First Box and Total Marks the Exam were \nConducted in the Second Box", font="weight:bold 18")
                headamnl.grid()

                phyamnl = Label(phyamnf, text="Physics", font=" 12", fg="red")
                phyamnl.grid(row="1", column="0")

                chemamnl = Label(chemamnf, text="Chemistry",
                                 font=" 12", fg="red")
                chemamnl.grid(row="3", column="0")

                bioamnl = Label(bioamnf, text="Biology", font=" 12", fg="red")
                bioamnl.grid(row="5", column="0")

                mathamnl = Label(mathmnf, text="Mathematics",
                                 font=" 12", fg="red")
                mathamnl.grid(row="7", column="0")

                if (ssd == "Yes"):
                    hisamnl = Label(histamnf, text="History",
                                    font=" 12", fg="red")
                    hisamnl.grid(row="9", column="0")

                    geoamnl = Label(geoamnf, text="Geography",
                                    font=" 12", fg="red")
                    geoamnl.grid(row="11", column="0")

                    civiamnl = Label(civamnf, text="Civics",
                                     font=" 12", fg="red")
                    civiamnl.grid(row="13", column="0")

                    firstlamnl = Label(
                        firstlamnf, text="First Language", font=" 12", fg="red")
                    firstlamnl.grid(row="15", column="0")

                    secondlamnl = Label(
                        secondlamnf, text="Second Language", font=" 12", fg="red")
                    secondlamnl.grid(row="17", column="0")

                    failpamnl = Label(
                        failpamnf, text="Enter the Failing Percentage", font=" 15", fg="red")
                    failpamnl.grid(row="19", column="0")

                if (ssd == "No"):
                    ssdamnl = Label(
                        ssamnf, text="Social Science", font=" 12", fg="red")
                    ssdamnl.grid(row="9", column="0")

                    firstlamnl = Label(
                        firstlamnf, text="First Language", font=" 12", fg="red")
                    firstlamnl.grid(row="11", column="0")

                    secondlamnl = Label(
                        secondlamnf, text="Second Language", font=" 12", fg="red")
                    secondlamnl.grid(row="13", column="0")

                    failpamnl = Label(
                        failpamnf, text="Enter the Failing Percentage", font=" 15", fg="red")
                    failpamnl.grid(row="15", column="0")

                # Creating Variables for Marks
                phyamnv = IntVar()
                chemamnv = IntVar()
                bioamnv = IntVar()
                mathamnv = IntVar()

                if (ssd == "Yes"):
                    hisamnv = IntVar()
                    geoamnv = IntVar()
                    civamnv = IntVar()

                if (ssd == "No"):
                    ssamnv = IntVar()

                firstlamnv = IntVar()
                secondlamnv = IntVar()
                failpamnv = IntVar()

                # Creating Variables for Total Marks

                phyamntmv = IntVar()
                chemamntmv = IntVar()
                bioamntmv = IntVar()
                mathamntmv = IntVar()

                if (ssd == "Yes"):
                    hisamntmv = IntVar()
                    geoamntmv = IntVar()
                    civamntmv = IntVar()

                if (ssd == "No"):
                    ssamntmv = IntVar()

                firstlamntmv = IntVar()
                secondlamntmv = IntVar()

                # Creating Widgets for Marks
                phyamnw = Entry(phyamnf, textvariable=phyamnv)
                phyamnw.grid(row="1", column="3", padx="100")

                chemamnw = Entry(chemamnf, textvariable=chemamnv)
                chemamnw.grid(row="3", column="3", padx=85)

                bioamnw = Entry(bioamnf, textvariable=bioamnv)
                bioamnw.grid(row="5", column="3", padx=103)

                mathamnw = Entry(mathmnf, textvariable=mathamnv)
                mathamnw.grid(row="7", column="3", padx=67)

                if (ssd == "Yes"):
                    hisamnw = Entry(histamnf, textvariable=hisamnv)
                    hisamnw.grid(row="9", column="3", padx=108)

                    geoamnw = Entry(geoamnf, textvariable=geoamnv)
                    geoamnw.grid(row="11", column="3", padx=78)

                    civamnw = Entry(civamnf, textvariable=civamnv)
                    civamnw.grid(row="13", column="3", padx=113)

                    firstlamnw = Entry(firstlamnf, textvariable=firstlamnv)
                    firstlamnw.grid(row="15", column="3", padx=50)

                    secondamnlw = Entry(secondlamnf, textvariable=secondlamnv)
                    secondamnlw.grid(row="17", column="3", padx=27)

                    failpamnw = Entry(failpamnf, textvariable=failpamnv)
                    failpamnw.grid(row="19", column="3", padx="10")

                if (ssd == "No"):
                    ssamnw = Entry(ssamnf, textvariable=ssamnv)
                    ssamnw.grid(row="9", column="3", padx=50)

                    firstlamnw = Entry(firstlamnf, textvariable=firstlamnv)
                    firstlamnw.grid(row="11", column="3", padx=50)

                    secondamnlw = Entry(secondlamnf, textvariable=secondlamnv)
                    secondamnlw.grid(row="13", column="3", padx=27)

                    failpamnw = Entry(failpamnf, textvariable=failpamnv)
                    failpamnw.grid(row="15", column="3", padx="10")

                #     Creating Widgets for Total Marks

                phyamntmw = Entry(phyamnf, textvariable=phyamntmv)
                phyamntmw.grid(row="1", column="5", padx="13")

                chemamntmw = Entry(chemamnf, textvariable=chemamntmv)
                chemamntmw.grid(row="3", column="5", padx=30)

                bioamntmw = Entry(bioamnf, textvariable=bioamntmv)
                bioamntmw.grid(row="5", column="5", padx=12)

                mathamntmw = Entry(mathmnf, textvariable=mathamntmv)
                mathamntmw.grid(row="7", column="5", padx=48)

                if (ssd == "Yes"):
                    hisamntmw = Entry(histamnf, textvariable=hisamntmv)
                    hisamntmw.grid(row="9", column="5", padx=6)

                    geoamntmw = Entry(geoamnf, textvariable=geoamntmv)
                    geoamntmw.grid(row="11", column="5", padx=36)

                    civamntmw = Entry(civamnf, textvariable=civamntmv)
                    civamntmw.grid(row="13", column="5", padx=1)

                    firstlamntmw = Entry(firstlamnf, textvariable=firstlamntmv)
                    firstlamntmw.grid(row="15", column="5", padx=65)

                    secondamnltmw = Entry(
                        secondlamnf, textvariable=secondlamntmv)
                    secondamnltmw.grid(row="17", column="5", padx=90)

                if (ssd == "No"):
                    ssamntmw = Entry(ssamnf, textvariable=ssamntmv)
                    ssamntmw.grid(row="9", column="5", padx=65)

                    firstlamntmw = Entry(firstlamnf, textvariable=firstlamntmv)
                    firstlamntmw.grid(row="11", column="5", padx=65)

                    secondamnltmw = Entry(
                        secondlamnf, textvariable=secondlamntmv)
                    secondamnltmw.grid(row="13", column="5", padx=86)

                # Submit Function

                def submit4():

                    # Creating Variables for the Marks
                    global phym
                    global chemm
                    global biom
                    global mathm

                    if (ssd == "Yes"):
                        global hism
                        global geom
                        global civm

                    if (ssd == "No"):
                        global ssm

                    global firstlm
                    global secondlm

                    global failp

                    # Assigning the Values to the Variables
                    phym = phyamnv.get()
                    chemm = chemamnv.get()
                    biom = bioamnv.get()
                    mathm = mathamnv.get()

                    if (ssd == "Yes"):
                        hism = hisamnv.get()
                        geom = geoamnv.get()
                        civm = civamnv.get()

                    if (ssd == "No"):
                        ssm = ssamnv.get()

                    firstlm = firstlamnv.get()
                    secondlm = secondlamnv.get()

                    failp = failpamnv.get()  # Failing Percentage

                    # Creatin Total Marks Global Variable
                    global phytm
                    global chemtm
                    global biotm
                    global mathtm
                    global firstltm
                    global secondltm
                    if (ssd == "Yes"):
                        global histm
                        global geotm
                        global civtm
                    if (ssd == "No"):
                        global sstm

                    # Getting the Total Marks
                    phytm = phyamntmv.get()
                    chemtm = chemamntmv.get()
                    biotm = bioamntmv.get()
                    mathtm = mathamntmv.get()

                    if (ssd == "Yes"):
                        histm = hisamntmv.get()
                        geotm = geoamntmv.get()
                        civtm = civamntmv.get()

                    if (ssd == "No"):
                        sstm = ssamntmv.get()

                    firstltm = firstlamntmv.get()
                    secondltm = secondlamntmv.get()

                    # Getting the Total Marks
                    phytm = phyamntmv.get()
                    chemm = chemamntmv.get()
                    biotm = bioamntmv.get()
                    mathm = mathamntmv.get()
                    if (ssd == "Yes"):
                        histm = hisamntmv.get()
                        geotm = geoamntmv.get()
                        civtm = civamntmv.get()
                    if (ssd == "No"):
                        sstm = ssamntmv.get()
                    firstltm = firstlamntmv.get()
                    secondltm = secondlamntmv.get()

                    # Destroying Frames

                    headamnf.destroy()
                    phyamnf.destroy()
                    chemamnf.destroy()
                    bioamnf.destroy()
                    mathmnf.destroy()
                    firstlamnf.destroy()
                    secondlamnf.destroy()
                    failpamnf.destroy()

                    if (ssd == "Yes"):
                        histamnf.destroy()
                        geoamnf.destroy()
                        civamnf.destroy()

                    if (ssd == "No"):
                        ssamnf.destroy()

                    Submit4f.destroy()

                    # Calculation
                    calculate()

                submit4 = Button(Submit4f, text="Submit", command=submit4)
                submit4.pack(anchor="w", pady="10")

        if (ass == "No"):

            if (ams == "Yes"):
                # Creating Frames
                headf = Frame(mainf)
                headf.pack(anchor="w")

                scif = Frame(mainf)
                scif.pack(anchor="w")
                mathf = Frame(mainf)
                mathf.pack(anchor="w")

                if (ssd == "Yes"):
                    hisf = Frame(mainf)
                    hisf.pack(anchor="w")
                    geof = Frame(mainf)
                    geof.pack(anchor="w")
                    civf = Frame(mainf)
                    civf.pack(anchor="w")

                if (ssd == "No"):
                    ssf = Frame(mainf)
                    ssf.pack(anchor="w")

                firstlf = Frame(mainf)
                firstlf.pack(anchor="w")
                secondlf = Frame(mainf)
                secondlf.pack(anchor="w")

                failpf = Frame(mainf)
                failpf.pack(anchor="w", pady=10)
                totalf = Frame(mainf)
                totalf.pack(anchor="w")

                submit5f = Frame(mainf)
                submit5f.pack(anchor="w")

                # Creating Labels
                headl = Label(
                    headf, text=f"Enter the Marks Scored by the {name} in:", font="weight:bold 22")
                headl.grid(row="0")

                scil = Label(scif, text="Science", font=" 12", fg="red")
                scil.grid(row="2", column="0")
                mathl = Label(mathf, text="Mathematics", font=" 12", fg="red")
                mathl.grid(row="4", column="0")

                if (ssd == "Yes"):
                    hisl = Label(hisf, text="History", font=" 12", fg="red")
                    hisl.grid(row="6", column="0")
                    geol = Label(geof, text="Geography", font=" 12", fg="red")
                    geol.grid(row="8", column="0")
                    civil = Label(civf, text="Civics", font=" 12", fg="red")
                    civil.grid(row="10", column="0")

                    firstll = Label(
                        firstlf, text="First Language", font=" 12", fg="red")
                    firstll.grid(row="12", column="0")

                    secondll = Label(
                        secondlf, text="Second Language", font=" 12", fg="red")
                    secondll.grid(row="14", column="0")

                    failpl = Label(
                        failpf, text="Enter the Failing Percentage", font=" 15", fg="red")
                    failpl.grid(row="16", column="0")
                    totall = Label(totalf, text="Enter the Total Marks the Exams Were Conducted", font=" 15", fg="red")
                    totall.grid(row="18", column="0")

                if (ssd == "No"):
                    ssdl = Label(ssf, text="Social Science",
                                 font=" 12", fg="red")
                    ssdl.grid(row="6", column="0")

                    firstll = Label(
                        firstlf, text="First Language", font=" 12", fg="red")
                    firstll.grid(row="8", column="0")
                    secondll = Label(
                        secondlf, text="Second Language", font=" 12", fg="red")
                    secondll.grid(row="10", column="0")

                    failpl = Label(
                        failpf, text="Enter the Failing Percentage", font=" 15", fg="red")
                    failpl.grid(row="12", column="0")
                    totall = Label(
                        totalf, text="Enter the Total Marks the Exams Were Conducted", font=" 15", fg="red")
                    totall.grid(row="14", column="0")

                # Creating Variables
                sciv = IntVar()
                mathv = IntVar()
                if (ssd == "Yes"):
                    hisv = IntVar()
                    geov = IntVar()
                    civv = IntVar()

                if (ssd == "No"):
                    ssv = IntVar()

                firstlv = IntVar()
                secondlv = IntVar()
                failpv = IntVar()
                totalv = IntVar()

                # Creating Widgets
                sciw = Entry(scif, textvariable=sciv)
                sciw.grid(row="2", column="3", padx="99")

                mathw = Entry(mathf, textvariable=mathv)
                mathw.grid(row="4", column="3", padx=67)

                if (ssd == "Yes"):
                    hisw = Entry(hisf, textvariable=hisv)
                    hisw.grid(row="6", column="3", padx=108)

                    geow = Entry(geof, textvariable=geov)
                    geow.grid(row="8", column="3", padx=78)

                    civw = Entry(civf, textvariable=civv)
                    civw.grid(row="10", column="3", padx=113)

                    firstlw = Entry(firstlf, textvariable=firstlv)
                    firstlw.grid(row="12", column="3", padx=52)

                    secondlw = Entry(secondlf, textvariable=secondlv)
                    secondlw.grid(row="14", column="3", padx=30)

                    failpw = Entry(failpf, textvariable=failpv)
                    failpw.grid(row="16", column="3", padx="10")

                    totalw = Entry(totalf, textvariable=totalv)
                    totalw.grid(row="18", column="3", padx="10")

                if (ssd == "No"):
                    ssw = Entry(ssf, textvariable=ssv)
                    ssw.grid(row="6", column="3", padx=50)

                    firstlw = Entry(firstlf, textvariable=firstlv)
                    firstlw.grid(row="8", column="3", padx=50)

                    secondlw = Entry(secondlf, textvariable=secondlv)
                    secondlw.grid(row="10", column="3", padx=27)

                    failpw = Entry(failpf, textvariable=failpv)
                    failpw.grid(row="12", column="3", padx="10")

                    totalw = Entry(totalf, textvariable=totalv)
                    totalw.grid(row="14", column="3", padx="10")

                    # Submit Function

                def submit5():

                    # Creating Global Variables
                    global scim
                    global mathm

                    if (ssd == "Yes"):
                        global hism
                        global geom
                        global civm

                    if (ssd == "No"):
                        global ssm

                    global firstlm
                    global secondlm

                    global failp
                    global totalm

                    # Getting the Values
                    scim = sciv.get()
                    mathm = mathv.get()

                    if (ssd == "Yes"):
                        hism = hisv.get()
                        geom = geov.get()
                        civm = civv.get()

                    if (ssd == "No"):
                        ssm = ssv.get()
                    firstlm = firstlv.get()
                    secondlm = secondlv.get()
                    failp = failpv.get()
                    totalm = totalv.get()

                    # Destroying Frames
                    headf.destroy()
                    scif.destroy()
                    mathf.destroy()
                    firstlf.destroy()
                    secondlf.destroy()
                    if (ssd == "Yes"):
                        hisf.destroy()
                        geof.destroy()
                        civf.destroy()
                    if (ssd == "No"):
                        ssf.destroy()
                    failpf.destroy()
                    totalf.destroy()
                    submit5f.destroy()

                    a = totalm
                    global scitm
                    global mathtm

                    scitm = a 
                    mathtm = a
                    if (ssd == "Yes"):
                        global histm
                        global geotm
                        global civtm
                        histm = a
                        geotm = a
                        civtm = a
                    if (ssd == "No"):
                        global sstm
                        sstm = a
                    global firstltm
                    global secondltm
                    firstltm = a
                    secondltm = a

                    # Calculation
                    calculate()

                Submit5 = Button(submit5f, text="Submit", command=submit5)
                Submit5.pack(anchor="w", pady="10")

            if (ams == "No"):
                # Creating Frames for Input of Total Marks
                headamnf = Frame(mainf)
                headamnf.pack()

                sciamnf = Frame(mainf)
                sciamnf.pack(anchor="w")
                mathmnf = Frame(mainf)
                mathmnf.pack(anchor="w")

                if (ssd == "Yes"):
                    histamnf = Frame(mainf)
                    histamnf.pack(anchor="w")
                    geoamnf = Frame(mainf)
                    geoamnf.pack(anchor="w")
                    civamnf = Frame(mainf)
                    civamnf.pack(anchor="w")

                if (ssd == "No"):
                    ssamnf = Frame(mainf)
                    ssamnf.pack(anchor="w")

                firstlamnf = Frame(mainf)
                firstlamnf.pack(anchor="w")
                secondlamnf = Frame(mainf)
                secondlamnf.pack(anchor="w")

                failpamnf = Frame(mainf)
                failpamnf.pack(anchor="w", pady=10)

                Submit6f = Frame(mainf)
                Submit6f.pack(anchor="w")

                # Creating Labels

                headamnl = Label(headamnf, text=f"Enter the Marks Scored by {name} in the Following Subjects\n and Languages in First Box and Total Marks the Exam were \nConducted in the Second Box", font="weight:bold 18")
                headamnl.grid(row="1", column="0")

                sciamnl = Label(sciamnf, text="Science", font=" 12", fg="red")
                sciamnl.grid(row="2", column="0")

                mathamnl = Label(mathmnf, text="Mathematics",
                                 font=" 12", fg="red")
                mathamnl.grid(row="4", column="0")

                if (ssd == "Yes"):
                    hisamnl = Label(histamnf, text="History",
                                    font=" 12", fg="red")
                    hisamnl.grid(row="6", column="0")

                    geoamnl = Label(geoamnf, text="Geography",
                                    font=" 12", fg="red")
                    geoamnl.grid(row="8", column="0")

                    civiamnl = Label(civamnf, text="Civics",
                                     font=" 12", fg="red")
                    civiamnl.grid(row="10", column="0")

                    firstlamnl = Label(firstlamnf, text="First Language", font=" 12", fg="red")
                    firstlamnl.grid(row="12", column="0")

                    secondlamnl = Label(secondlamnf, text="Second Language", font=" 12", fg="red")
                    secondlamnl.grid(row="14", column="0")

                    failpamnl = Label(failpamnf, text="Enter the Failing Percentage", font=" 15", fg="red")
                    failpamnl.grid(row="16", column="0")

                if (ssd == "No"):
                    ssdamnl = Label(ssamnf, text="Social Science", font=" 12", fg="red")
                    ssdamnl.grid(row="6", column="0")

                    firstlamnl = Label(firstlamnf, text="First Language", font=" 12", fg="red")
                    firstlamnl.grid(row="8", column="0")

                    secondlamnl = Label(secondlamnf, text="Second Language", font=" 12", fg="red")
                    secondlamnl.grid(row="10", column="0")

                    failpamnl = Label(failpamnf, text="Enter the Failing Percentage", font=" 15", fg="red")
                    failpamnl.grid(row="12", column="0")

                # Creating Variables for Marks and Failing Percentage.
                sciamnv = IntVar()
                mathamnv = IntVar()

                if (ssd == "Yes"):
                    hisamnv = IntVar()
                    geoamnv = IntVar()
                    civamnv = IntVar()

                if (ssd == "No"):
                    ssamnv = IntVar()

                firstlamnv = IntVar()
                secondlamnv = IntVar()
                failpamnv = IntVar()

                # Creating Variables for Total Marks

                sciamntmv = IntVar()
                mathamntmv = IntVar()

                if (ssd == "Yes"):
                    hisamntmv = IntVar()
                    geoamntmv = IntVar()
                    civamntmv = IntVar()

                if (ssd == "No"):
                    ssamntmv = IntVar()

                firstlamntmv = IntVar()
                secondlamntmv = IntVar()

                # Creating Widgets for Marks and Failing Percentage.
                sciamnw = Entry(sciamnf, textvariable=sciamnv)
                sciamnw.grid(row="2", column="3", padx=99)

                mathamnw = Entry(mathmnf, textvariable=mathamnv)
                mathamnw.grid(row="4", column="3", padx=67)

                if (ssd == "Yes"):
                    hisamnw = Entry(histamnf, textvariable=hisamnv)
                    hisamnw.grid(row="6", column="3", padx=108)

                    geoamnw = Entry(geoamnf, textvariable=geoamnv)
                    geoamnw.grid(row="8", column="3", padx=78)

                    civamnw = Entry(civamnf, textvariable=civamnv)
                    civamnw.grid(row="10", column="3", padx=113)

                    firstlamnw = Entry(firstlamnf, textvariable=firstlamnv)
                    firstlamnw.grid(row="12", column="3", padx=50)

                    secondamnlw = Entry(secondlamnf, textvariable=secondlamnv)
                    secondamnlw.grid(row="14", column="3", padx=27)

                    failpamnw = Entry(failpamnf, textvariable=failpamnv)
                    failpamnw.grid(row="16", column="3", padx="10")

                if (ssd == "No"):
                    ssamnw = Entry(ssamnf, textvariable=ssamnv)
                    ssamnw.grid(row="6", column="3", padx=50)

                    firstlamnw = Entry(firstlamnf, textvariable=firstlamnv)
                    firstlamnw.grid(row="8", column="3", padx=50)

                    secondamnlw = Entry(secondlamnf, textvariable=secondlamnv)
                    secondamnlw.grid(row="10", column="3", padx=27)

                    failpamnw = Entry(failpamnf, textvariable=failpamnv)
                    failpamnw.grid(row="12", column="3", padx="10")

                    # Creating Widgets for Total Marks.

                sciamntmw = Entry(sciamnf, textvariable=sciamntmv)
                sciamntmw.grid(row="2", column="5", padx=14)

                mathamntmw = Entry(mathmnf, textvariable=mathamntmv)
                mathamntmw.grid(row="4", column="5", padx=48)

                if (ssd == "Yes"):
                    hisamntmw = Entry(histamnf, textvariable=hisamntmv)
                    hisamntmw.grid(row="6", column="5", padx=6)

                    geoamntmw = Entry(geoamnf, textvariable=geoamntmv)
                    geoamntmw.grid(row="8", column="5", padx=36)

                    civamntmw = Entry(civamnf, textvariable=civamntmv)
                    civamntmw.grid(row="10", column="5", padx=1)

                    firstlamntmw = Entry(firstlamnf, textvariable=firstlamntmv)
                    firstlamntmw.grid(row="12", column="5", padx=65)

                    secondamnltmw = Entry(
                        secondlamnf, textvariable=secondlamntmv)
                    secondamnltmw.grid(row="14", column="5", padx=90)

                if (ssd == "No"):
                    ssamntmw = Entry(ssamnf, textvariable=ssamntmv)
                    ssamntmw.grid(row="6", column="5", padx=65)

                    firstlamntmw = Entry(firstlamnf, textvariable=firstlamntmv)
                    firstlamntmw.grid(row="8", column="5", padx=65)

                    secondamnltmw = Entry(
                        secondlamnf, textvariable=secondlamntmv)
                    secondamnltmw.grid(row="10", column="5", padx=86)

                # Submit Function

                def submit6():
                    # Creating Global Variables
                    global scim
                    global mathm
                    if (ssd == "Yes"):
                        global hism
                        global geom
                        global civm
                    if (ssd == "No"):
                        global ssm

                    global firstlm
                    global secondlm

                    global failp

                    # Getting the Values
                    scim = sciamnv.get()
                    mathm = mathamnv.get()

                    if (ssd == "Yes"):
                        hism = hisamnv.get()
                        geom = geoamnv.get()
                        civm = civamnv.get()

                    if (ssd == "No"):
                        ssm = ssamnv.get()

                    firstlm = firstlamnv.get()
                    secondlm = secondlamnv.get()

                    failp = failpamnv.get()

                    # Making the Total Mark Variable Gloabl
                    global scitm
                    global mathtm

                    if (ssd == "Yes"):
                        global histm
                        global geotm
                        global civtm
                    if (ssd == "No"):
                        global sstm

                    global firstltm
                    global secondltm

                    # Geting the Total Marks
                    scitm = sciamntmv.get()
                    mathtm = mathamntmv.get()
                    if (ssd == "Yes"):
                        histm = hisamntmv.get()
                        geotm = geoamntmv.get()
                        civtm = civamntmv.get()
                    if (ssd == "No"):
                        sstm = ssamntmv.get()

                    firstltm = firstlamntmv.get()
                    secondltm = secondlamntmv.get()

                    # Destroying Frames

                    headamnf.destroy()
                    sciamnf.destroy()
                    mathmnf.destroy()
                    firstlamnf.destroy()
                    secondlamnf.destroy()
                    failpamnf.destroy()

                    if (ssd == "Yes"):
                        histamnf.destroy()
                        geoamnf.destroy()
                        civamnf.destroy()

                    if (ssd == "No"):
                        ssamnf.destroy()

                    Submit6f.destroy()
                    # Calculation of Percentage
                    calculate()

                submit6 = Button(Submit6f, text="Submit", command=submit6)
                submit6.pack(anchor="w", pady="10")

    Submit2 = Button(submit2f, text="Submit", command=submit2)
    Submit2.grid(row="10", pady=10, padx=5)


def calculate():
    if (ass == "Yes"):
        phyp = (phym * 100) / phytm
        chemp = (chemm * 100) / chemtm
        biop = (biom * 100) / biotm

    if (ass == "No"):
        scip = (scim * 100) / scitm

    # Social Calculation
    if (ssd == "Yes"):
        hisp = (hism * 100) / histm
        geop = (geom * 100) / geotm
        civp = (civm * 100) / civtm
    
    if (ssd == "No"):
        ssp = (ssm * 100) / sstm



    # Math and Language Calculation
    firstlp = (firstlm * 100) / firstltm
    secondlp = (secondlm * 100) / secondltm
    mathp = (mathm * 100) / mathtm

    # Calcualting Total Percentage
    # Calculating Printing the Total Data of the Student
    global totalp
    if(ass == "No" and ssd == "Yes"):
        totalp = (scip+mathp+hisp+geop+civp+firstlp+secondlp)/7
    
    if(ass == "No" and ssd == "No"):
        totalp = (scip+mathp+ssp+firstlp+secondlp)/5


    if (ass == "Yes" and ssd == "Yes"):
        totalp = (phyp+chemp+biop+mathp+hisp+geop+civp+firstlp+secondlp)/9
    
    if (ass == "Yes" and ssd == "No"):
        totalp = (phyp+chemp+biop+mathp+ssp+firstlp+secondlp)/7



    # Determining whether the student is a pass or fail
    if (totalp >= failp):
        passp = "Pass"
    else:
        passp = "Fail"

    if (ass == "Yes"):
        # Physcics
        if (phyp >= failp):
            phyns = "Passed"
        else:
            phyns = "Failed"
        # Chemistry
        if (chemp >= failp):
            chemns = "Passed"
        else:
            chemns = "Failed"
        # Biology
        if (biop >= failp):
            bions = "Passed"
        else:
            bions = "Failed"
    # Science
    if (ass == "No"):
        if (scip >= failp):
            scins = "Passed"
        else:
            scins = "Failed"
    # Math
    if (mathp >= failp):
        mathns = "Passed"
    else:
        mathns = "Failed"

    if (ssd == "Yes"):
        if (hisp >= failp):
            hisns = "Passed"
        else:
            hisns = "Failed"
        if (geop >= failp):
            geons = "Passed"
        else:
            geons = "Failed"
        if (civp >= failp):
            civns = "Passed"
        else:
            civns = "Failed"
        
    if (ssd == "No"):
        if (ssp >= failp):
            ssns = "Passed"
            
        else:
            ssns = "Failed"
    
    

    # First Language
    if (firstlp >= failp):
        firstlns = "Passed"
    else:
        firstlns = "Failed"
    # Second Language
    if (secondlp >= failp):
        secondlns = "Passed"
    else:
        secondlns = "Failed"


    # Creating Labels for Showing the Data
    headl1 = Label(mainf, text=f"The Marks and Percentage Scored by {name} in:", font=("Arial", 18, "bold"))
    headl1.pack(padx="10")

    if (ass == "Yes"):
        phyo = Label(mainf, text=f"Physics: Marks Scored is {phym}, Percentage is {phyp}%, The Student has {phyns} ", fg="red", font="13")
        phyo.pack(anchor="w",pady = "3")
        chemo = Label(mainf, text=f"Chemistry: Marks Scored is {chemm} Percentage is {chemp}%, The Student has {chemns}", fg="red", font="13")
        chemo.pack(anchor="w",pady = "3")
        bioo = Label(mainf, text=f"Biology: Marks Scored is {biom} Percentage is {biop}%, The Student has {bions}", fg="red", font="13")
        bioo.pack(anchor="w",pady = "3")
    if (ass == "No"):
        scio = Label(mainf, text=f"Science: Marks Scored is {scim} Percentage is {scip}%, The Student has {scins}", fg="red", font="13")
        scio.pack(anchor="w",pady = "3")

    matho = Label(mainf, text=f"Mathematics: Marks Scored is {mathm} Percentage is {mathp}%, The Student has {mathns}", fg="red", font="13")
    matho.pack(anchor="w",pady = "3")
    if (ssd == "Yes"):
        hiso = Label(mainf, text=f"History: Marks Scored is {hism} Percentage is {hisp}%, The Student has {hisns}", fg="red", font="13")
        hiso.pack(anchor="w",pady = "3")
        geoo = Label(
            mainf, text=f"Geography: Marks Scored is {geom} Percentage is {geop}%, The Student has {geons}", fg="red", font="13")
        geoo.pack(anchor="w",pady = "3")
        civo = Label(mainf, text=f"Civics: Marks Scored is {civm} Percentage is {civp}%, The Student has {civns}", fg="red", font="13")
        civo.pack(anchor="w",pady = "3")
    if (ssd == "No"):
        sso = Label(mainf, text=f"Social: Marks Scored is {ssm} Percentage is {ssp}%, The Student has {ssns}", fg="red", font="13")
        sso.pack(anchor="w",pady = "3")

    firstlo = Label(mainf, text=f"First Language: Marks Scored is {firstlm} Percentage is {firstlp}%, The Student has {firstlns}", fg="red", font="13")
    firstlo.pack(anchor="w",pady = "3")
    secondlo = Label(mainf, text=f"Second Language: Marks Scored is {secondlm} Percentage is {secondlp}%, The Student has {secondlns}", fg="red", font="13")
    secondlo.pack(anchor="w",pady = "3")

    totalpo = Label(mainf, text=f"The Total Percentage of the Student is {totalp}%", fg="red", font="15")
    totalpo.pack(anchor="w",pady = "3")

    fpo = Label(mainf, text=f"The Student as {passp} in Total ", fg="red", font="15")
    fpo.pack(anchor="w",pady = "3")

    def mains():
        headl1.destroy()
        if (ass == "Yes"):
            phyo.destroy()
            chemo.destroy()
            bioo.destroy()
        if (ass == "No"):
            scio.destroy()
        matho.destroy()
        if (ssd == "Yes"):
            hiso.destroy()
            geoo.destroy()
            civo.destroy()
        if (ssd == "No"):
            sso.destroy()
        firstlo.destroy()
        secondlo.destroy()
        totalpo.destroy()
        fpo.destroy()
        save.destroy()
        btn.destroy()
        main()

    if (ams=="No"):
        global mathtm1,firstltm1,secondltm1
        mathtm1 = mathtm
        firstltm1 = firstltm
        secondltm1 = secondltm
        if (ass == "Yes"):
            global phytm1,chemtm1,biomt1
            phytm1 = phytm
            chemtm1 = chemtm
            biomt1 = biotm
        if (ass == "No"):
            global scitm1
            scitm1 = scitm
        if (ssd == "Yes"):
            global histm1,geotm1,civtm1
            histm1 = histm
            geotm1 = geotm
            civtm1 = civtm
        if (ssd == "No"):
            global sstm1
            sstm1 = sstm
    

    # Function to Create TXT File
    def savefile():         
        if (ass == "Yes"):
            f = open(name + ".txt", "w")
            f.write(
                f"The Name of the Student is {name}\n"
                f"Roll Number is {rollno}\n"


                f"\nMarks and Percentage of the Student in Physics\n"
                f"The Marks scored by {name} in Physics is {phym} out of {phytm}\n"
                f"The Percentage of {name} in Physics is {phyp}\n"
                f"The Student has {phyns}\n"

                f"\nMarks and Percentage of the Student in Chemistry\n"
                f"The Marks scored by  {name} in Chemistry is {chemm} out of {chemtm}\n"
                f"The Percentage of {name} in Chemistry is {chemp}\n"
                f"The Student has {chemns}\n"

                f"\nMarks and Percentage of the Student in Biology\n"
                f"The Marks scored by {name} in Biology is {biom} out of {biotm}\n"
                f"The Percentage of {name} in Biology is {biop}\n"
                f"The Student has {bions}\n"
            )
            f.close()

        if (ass == "No"):
            f = open(name + ".txt", "w")
            f.write(
                f"The Name of the Student is {name}\n"
                f"Roll Number is {rollno}\n"

                f"\nMarks and Percentage of the {name} in Science\n"
                f"The Marks scored by {name} in Science is {scim} out of {scitm}\n"
                f"The Percentage of {name} in  Science {scip}\n"
                f"The Student has {scins}\n"
            )
            f.close()


        f = open(name + ".txt", "a")
        f.write(
            f"\nThe Marks and Percentage of {name} in Mathematics\n\n"
            f"The Marks scored by {name} in Mathematics is {mathm} out of {mathtm}\n"
            f"The Percentage of {name} in Mathematics is {mathp}\n"
            f"The Student has {mathns}\n"
            
            f"\nThe Marks and Percentage of {name} in First Language\n\n"
            f"The Marks scored by {name} in First Language is {firstlm} out of {firstltm}\n"
            f"The Percentage of {name} in First Language is {firstlp}\n"
            f"The Student has {firstlns}\n"
            
            f"\nThe Marks and Percentage of {name} in Second Language\n\n"
            f"The Marks scored by {name} in Second Language is {secondlm} out of {secondltm}\n"
            f"The Percentage of {name} in Second Language is {secondlp}\n"
            f"The Student has {secondlns}\n"
        )
        f.close()
        

        if (ssd == "No"):
            f = open(name + ".txt", "a")
            f.write(

                f"\nThe Marks and Percentage of {name} in Social Science\n\n"
                f"The Marks scored by {name} in Social Science is {ssm} out of {sstm}\n"
                f"The Percentage of {name} in Social Science is {ssp}\n"
                f"The Student has {ssns}\n"

                f"\n{name} Total Percentage is {totalp}"
                f"\n{name} as {passp} Overall"
            )
            f.close()

        if (ssd == "Yes"):
            f = open(name + ".txt", "a")
            f.write(
                f"\nMarks and Percentage of the {name} in History\n"
                f"The Marks scored by {name} in History is {hism} out of {histm}\n"
                f"The Percentage of {name} in History is {hisp}\n"
                f"The Student has {hisns}\n"

                f"\nMarks and Percentage of the {name} in Geography\n"
                f"The Marks scored by {name} in Geography is {geom} out of {geotm}\n"
                f"The Percentage of {name} in Geography is {geop}\n"
                f"The Student has {geons}\n"

                f"\nMarks and Percentage of the {name} in Civics\n"
                f"The Marks scored by {name} in Civics is {civm} out of {civtm}\n"
                f"The Percentage of {name} in Civics is {geop}\n"
                f"The Student has {civns}\n"

                f"\n{name} Total Percentage is {totalp}"
                f"\n{name} as {passp} Overall"
            )
            f.close()

    # Creating Buttons
    btn = Button(mainf, text="Calculate for Another Student", font=("Arial", 13, "bold"), width=27, height=1, command=mains)
    btn.pack(anchor = "w",pady = "20")
    save = Button(mainf, text="Save", font=("Arial", 13, "bold"), width=27, height=1, command=savefile)
    save.pack(anchor = "w",pady = "20")


# Outside the Main

# Creating Frames

assf = Frame(mainf, borderwidth=1)
assf.pack(anchor="w")

ssdf = Frame(mainf, borderwidth=1)
ssdf.pack(anchor="w")

amsf = Frame(mainf, borderwidth=1)
amsf.pack(anchor="w")


submit = Frame(root)
submit.grid()


# Creating Variables for Input
assr1 = StringVar()
ssdr1 = StringVar()
amsr1 = StringVar()


# Configuring the basic Inputs Texts and Radio Buttons
# Science -PCB
assl = Label(
    assf, text='''Is Science Divided into Physic,Chemistry,Biology if 'Yes' Click 'Y' else enter 'N':''', fg="red")
assl.grid(row="0")

assr2 = Radiobutton(assf, text="Yes", padx=48, variable=assr1, value="Yes")
assr2.grid(row="0", column="3")

assr2 = Radiobutton(assf, text="No", padx=59, variable=assr1, value="No")
assr2.grid(row="0", column="4")

# Social -HGC
ssdl = Label(ssdf, text='''Is Social Science Divided into History,Geography,Civics if 'Yes' enter 'Y' else enter 'N':''', fg="red")
ssdl.grid(row="1")

ssdr2 = Radiobutton(ssdf, text="Yes", padx=14, variable=ssdr1, value="Yes")
ssdr2.grid(row="1", column="3")

ssdr2 = Radiobutton(ssdf, text="No", padx=92, variable=ssdr1, value="No")
ssdr2.grid(row="1", column="4")


# Total Marks
amsl = Label(amsf, text='''Is the Total Marks Same for all Subject if 'Yes' Enter 'Y' else Enter 'N':''', fg="red")
amsl.grid(row="2")

amsr2 = Radiobutton(amsf, text="Yes", padx=104, variable=amsr1, value="Yes")
amsr2.grid(row="2", column="1")

amsr2 = Radiobutton(amsf, text="No", variable=amsr1, value="No")
amsr2.grid(row="2", column="2")

# First Submit Button
Submit1 = Button(submit, text="Submit", command=main)
Submit1.pack(anchor=CENTER, pady="8")


root.mainloop()