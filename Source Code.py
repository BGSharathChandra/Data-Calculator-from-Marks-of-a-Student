def seprates():

    ht = int(input("\n\nHow Many Students Percentage do you Want to Calculate:"))
    i = 0

    for i in range(ht):

        i += 1
        name = input("\nEnter the name of the Student:")
        rollno = int(input("Enter the Roll Number of the Student:"))

        #Inputs of Physics
        phym = float(input(f"\nEnter the  Marks Scored by {name} in Physics:"))
        if (ams == "N"):
            phytm = int(input("Enter the Total Marks Physics Exam was Conducted for:"))
            phyp = (phym/phytm)*100

        #Inputs of Chemistry
        chemm = float(
            input(f"\nEnter the Marks scored by {name} in Chemistry:"))
        if (ams == "N"):
            chemtm = int(
                input("Enter the Total Marks Chemistry Exam was Conducted for:"))
            chemp = (chemm/chemtm)*100

        # Input of Bilogy
        biom = float(input(f"\nEnter the Marks Scored by {name} in Biology:"))
        if (ams == "N"):
            biotm = int(
                input("Enter the Total Marks Biology Exam was Conducted for:"))
            biop = (biom / biotm) * 100

        # Input in Mathematics
        mathm = float(input(f"\nEnter the Marks Scored by {name} in Mathematics:"))
        if (ams == "N"):
            mathtm = float(
                input("Enter the Total Marks  Mathematics Exam was Conducted for:"))
            mathp = (mathm / mathtm) * 100

        # Inputs in Social Science
        ssm = float(input(f"\nEnter the Marks Scored by {name} in Social Science:"))
        if (ams == "N"):
            sstm = float(
                input("Enter the Total Marks  Social Science Exam was Conducted for:"))
            ssp = (ssm / sstm) * 100

        # Inputs in First Language
        firstlm = float(
            input(f"\nEnter the Marks Scored by {name} in First Language:"))
        if (ams == "N"):
            firstltm = float(input("Enter the Total Marks  First Language Exam was Conducted for:"))
            firstlp = (firstlm / firstltm) * 100

        # Inputs in Second Language
        secondlm = float(input(f"\nEnter the Marks Scored by {name} in Second Language:"))
        if (ams == "N"):
            secondltm = float(
                input("Enter the Total Marks  Second Language Exam was Conducted for:"))
            secondlp = (secondlm / secondltm) * 100
        
        

        if (ams == "Y"):
            a = float(input("\nEnter the Total Marks all the Exam were Conducted for:"))
            phytm = a
            biotm = a
            chemtm = a
            sstm = a
            mathtm = a
            firstltm = a
            secondltm = a
            sstm  = a
            phyp = (phym / a) * 100
            chemp = (chemm / a) * 100
            biop = (biom / a) * 100
            mathp = (mathm / a) * 100
            ssp  = (ssm/a)*100
            firstlp = (firstlm / a) * 100
            secondlp = (secondlm / a) * 100

        failp = float(input("\nEnter how much percentage the Student must have Scored to Pass the Exam:"))

        # Printing the Outputs of Student in Physics
        print("Physics Output\n")
        print(f"The Student has Scored {phym} out of {phytm} in Physics")
        print(f"The Total Percentage the {name} has Scored in Physics is {phyp}")
        if (phyp > failp):
            print(f"The {name} has passed the Physics Exam\n")
        else:
            print(f"The {name} has Failed in Physics Exam\n")

        # Chemistry Output
        print("Chemistry Output\n")
        print(f"The {name} has Scored {chemm} out of {chemtm} in Chemistry")
        print(f"The Total Percentage the {name} has Scored in Chemistry is {chemp}")
        if (chemp > failp):
            print(f"The {name} has passed the Chemistry Exam\n")
        else:
            print(f"The {name} has Failed in Chemistry Exam\n")

        # Biology Output 
        print("Biology Output\n")
        print(f"The {name} has Scored {biom} out of {biotm} in Biology")
        print(f"The Total Percentage the {name} has Scored in Biology is {biop}")
        if (biop > failp):
            print(f"The {name} has passed the Physics Exam\n")
        else:
            print(f"The {name} has Failed in Biology Exam\n")

        # Printing the Outputs of the Student in Mathematics
        print("Mathematics Output\n")
        print(f"The {name} has Scored {mathm} out of {mathtm} in Mathematics ")
        print(f"The Total Percentage of the {name} in Mathematics is {mathp}")
        if (mathp > failp):
            print(f"The {name} has Passed in Mathematics\n")
            mns = "Passed"
        else:
            print(f"The {name} as Failed in Mathematics Exam\n")
            mns = "Failed"

        # Printing the Outputs of Student in Social Science
        print("Social Science Output\n")
        print(f"The {name} has Scored {ssm} out of {sstm} in Social Science ")
        print(f"The Total Percentage of the {name} in Social Science is {ssp}")
        if (ssp > failp):
            print(f"The {name} has Passed in Social Science\n")
            mns = "Passed"
        else:
            print(f"The {name} as Failed in Social Science Exam\n")
            mns = "Failed"

        # Printing the Outputs in First Language
        print("First Language Output\n")
        print(
            f"The {name} as Scored {firstlm} out of {firstltm} in First Language")
        print(
            f"The Total Percentage of the {name} in Mathematics is ", firstlp)
        if (firstlp > failp):
            print(f"The {name} as Passed in First language Exam\n")
            flns = "Passed"
        else:
            print("The {name} as Failed in First Language Exam\n")

        # Printing the Outputs of Second Language Exam
        print("Second Language Output\n")
        if (ams == "N"):
            print(f"The Student has Scored {secondlm} out of {secondltm}")
        else:
            print(f"The {name} as Scored {secondlm} out of {a} in Second Language ")
        print(f"The Percentage of the {name} in Second Language is ", secondlp)
        if (secondlp > failp):
            print(f"The {name} as Passed in Second Language Exam")
            slns = "Passed"
        else:
            print(f"The {name} as Failed in Second Language Exam")
            slns = "Failed"


         # Calculating Printing the Total Data of the Student
        if (ams == "Y"):
           totalp = (phyp+chemp+biop+mathp+ssp+firstlp+secondlp)/7

        elif(ams == "N"):
            totalp = (phyp+chemp+biop+mathp+ssp+firstlp+secondlp)/7

        print(f"\nThe Total Percentage of {name} is {totalp}")
        if totalp > failp:
            print(f"{name} has passed Overall")
            tlns = "Passed"
        else:
            print(f"{name} as Failed")
            tlns = "Failed"

        f = open(name + ".txt", "w")
        f.write("Marks\n\n\n"
                f"The Name of the Student is {name}\n"
                f"Roll Number is {rollno}\n"


                f"\nOutputs of the Student in Physics\n"
                f"The Marks scored by the {name} in Physics is {phym} out of {phytm}\n"
                f"The Percentage of the {name} in Physics is {phyp}\n"
                f"The Student has {mns}\n"

                f"\nOutputs of the Student in Chemistry\n"
                f"The Marks scored by the {name} in Chemistry is {chemm} out of {chemtm}\n"
                f"The Percentage of the {name} in Chemistry is {chemp}\n"

                f"\nOutputs of the Student in Biology\n"
                f"The Student has {mns}\n"
                f"The Marks scored by the {name} in Biology is {biom} out of {biotm}\n"
                f"The Percentage of the {name} in Biology is {biop}\n"
                f"The Student has {mns}\n"

                f"\nThe Outputs of the {name} in Mathematics\n\n"
                f"The Marks scored by the {name} in Mathematics is {mathm} out of {mathtm}\n"
                f"The Percentage of the {name} in Mathematics is {mathp}\n"
                f"The Student has {mns}\n"

                f"\nThe Outputs of the {name} in Social Science\n\n"
                f"The Marks scored by the {name} in Social Science is {ssm} out of {sstm}\n"
                f"The Percentage of the {name} in Social Science is {ssp}\n"
                f"The Student has {mns}\n"

                f"\nThe Outputs of the {name} in First Language\n\n"
                f"The Marks scored by the {name} in First Language is {firstlm} out of {firstltm}\n"
                f"The Percentage of the {name} in First Language is {firstlp}\n"
                f"The Student has {flns}\n"

                f"\nThe Outputs of the {name} in Second Language\n\n"
                f"The Marks scored by the {name} in Second Language is {secondlm} out of {secondltm}\n"
                f"The Percentage of the {name} in Second Language is {secondlp}\n"
                f"The Student has {slns}\n"

                f"\n{name} Total Percentage is {totalp}"
                f"\n{name} as {tlns} Overall"
                )
        f.close()


def nseprate():

    ht = int(input("How Many Students Percentage do you Want to Calculate:"))
    i = 0

    for i in range(ht):

        i += 1
        name = input("\nEnter the name of the Student:")
        rollno = int(input("Enter the Roll Number of the Student:"))

        #Inputs of Science
        scim = float(input(f"\nEnter the  Marks Scored by {name} in Science"))
        if (ams == "N"):
            scitm = int(
                input("Enter the Total Marks Science Exam was Conducted for:"))
            scip = (scim/scitm)*100

        # Input in Mathematics
        mathm = float(input("\nEnter the Marks Scored by Student in Mathematics:"))
        if (ams == "N"):
            mathtm = float(
                input("Enter the Total Marks which was there in the Mathematics Exam:"))
            mathp = (mathm / mathtm) * 100

        # Inputs in Social Science
        ssm = float(input(f"\nEnter the Marks Scored by {name} in Second Language:"))
        if (ams == "N"):
            sstm = float(input("Enter the Total Marks  Second Language Exam was Conducted for:"))
            ssp = (ssm / sstm) * 100

        # Inputs in First Language
        firstlm = float(
            input("\nEnter the Marks Scored by Student in First Language:"))
        if (ams == "N"):
            firstltm = float(
                input("Enter the Total Marks which was there in the First Language Exam:"))
            firstlp = (firstlm / firstltm) * 100

        # Inputs in Secod Language
        secondlm = float(
            input("\nEnter the Marks Scored by Student in Second Language:"))
        if (ams == "N"):
            secondltm = float(
                input("Enter the Total Marks which was there in the Second Language Exam:\n"))
            secondlp = (secondlm / secondltm) * 100

        if (ams == "Y"):
            a = float(input("Enter the Total Marks all the Exam were Conducted for:"))
            scitm = a
            mathtm = a
            firstltm = a
            secondltm = a
            sstm = a
            scip = (scim / a) * 100
            mathp = (mathm / a) * 100
            ssp = (ssm/a)*100
            firstlp = (firstlm / a) * 100
            secondlp = (secondlm / a) * 100

        failp = float(input("\nEnter how much percentage the Student must have Scored to Pass the Exam:"))

        # Printing the Outputs of Student in Science
        print("Physics Output\n\n")
        print(f"The Student has Scored {scim} out of {scitm} in Physics")
        print(f"The Total Percentage the Student has Scored in Physics is {scip}")
        if (scip > failp):
            print("The Student has passed the Physics Exam\n")
        else:
            print("The Student has Failed in Physics Exam\n")

        # Printing the Outputs of the Student in Mathematics
        print(f"The Student has Scored {mathm} out of {mathtm} in Mathematics ")
        print(f"The Total Percentage of the Student in Mathematics is {mathp}")
        if (mathp > failp):
            print("The Student has Passed in Mathematics\n")
            mns = "Passed"
        else:
            print("The Student as Failed in Mathematics Exam\n")
            mns = "Failed"

        # Printing the Outputs in Social Science
        print("Social Science Output\n")
        print(f"The {name} has Scored {ssm} out of {sstm} in Social Science ")
        print(f"The Total Percentage of the {name} in Social Science is {ssp}")
        if (ssp > failp):
            print(f"The {name} has Passed in Social Science\n")
            mns = "Passed"
        else:
            print(f"The {name} as Failed in Social Science Exam\n")
            mns = "Failed"

        # Printing the Outputs in First Language
        print(f"The Student as Scored {firstlm} out of {firstltm} in First Language")
        print("The Total Percentage of the Student in Mathematics is ", firstlp)
        if (firstlp > failp):
            print("The Student as Passed in First language Exam\n")
            flns = "Passed"
        else:
            print("The Student as Failed in First Language Exam\n")
            flns = "Failed"

        # Printing the Outputs of Second Language Exam
        print(f"The Student has Scored {secondlm} out of {secondltm}")
        print("The Percentage of the Student in Second Language is ", secondlp)
        if (secondlp > failp):
            print("The Student as Passed in Second Language Exam")
            slns = "Passed"
        else:
            print("The Student as Failed in Second Language Exam")
            slns = "Failed"

        # Calculating Printing the Total Data of the Student
        if (ams == "Y"):
            totalp = (scip+mathp+ssp+firstlp+secondlp)/5

        elif(ams == "N"):
            totalp = (scip+mathp+ssp+firstlp+secondlp)/5

        print(f"The Total Percentage of {name} is {totalp}")
        if totalp > failp:
            print(f"{name} has passed Overall")
            tlns = "Passed"
        else:
            print(f"{name} as Failed")
            tlns = "Failed"

        f = open(name + ".txt", "w")
        f.write("Marks\n\n\n"
                f"The Name of the Student is {name}\n"
                f"Roll Number is {rollno}\n"


                f"\nOutputs of the Student in Science\n"
                f"The Marks scored by the {name} in Science is {scim} out of {scitm}\n"
                f"The Percentage of the {name} in  Science {scip}\n"
                f"The Student has {mns}\n"

                f"\nThe Outputs of the {name} in Mathematics\n\n"
                f"The Marks scored by the {name} in Mathematics is {mathm} out of {mathtm}\n"
                f"The Percentage of the {name} in Mathematics is {mathp}\n"
                f"The Student has {mns}\n"

                f"\nThe Outputs of the {name} in Social Science\n\n"
                f"The Marks scored by the {name} in Social Science is {ssm} out of {sstm}\n"
                f"The Percentage of the {name} in Social Science is {ssp}\n"
                f"The Student has {mns}\n"

                f"\nThe Outputs of the {name} in First Language\n\n"
                f"The Marks scored by the {name} in First Language is {firstlm} out of {firstltm}\n"
                f"The Percentage of the {name} in First Language is {firstlp}\n"
                f"The Student has {flns}\n"

                f"\nThe Outputs of the {name} in Second Language\n\n"
                f"The Marks scored by the {name} in Second Language is {secondlm} out of {secondltm}\n"
                f"The Percentage of the {name} in Second Language is {secondlp}\n"
                f"The Student has {slns}\n"

                f"\n{name} Total Percentage is {totalp}"
                f"\n{name} as {tlns} Overall"
                )
        f.close()


ass = input(
    '''Is Science Divided into Physics Chemistry Biology if 'Yes' enter 'Y' else enter 'N'  ''')
ams = input(
    "Is the Total Marks Same for all Subject if 'Yes' Enter 'Y' else Enter 'N' ")

if (ass == "Y"):
    seprates()
else:
    nseprate()
