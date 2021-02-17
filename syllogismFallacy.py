# Syllogism fallacies,
# Checks for fallacies within a syllogism
# and displays the result.
#
# If no fallacies are displayed,
# No fallacies were found and the argument is unconditionally valid.

"""
v1.1
TO DO:

make it look prrty
Accept a wider range of inputs
"""

# Rename this function
def statement(form):
    formInfo = []
    if form == 'A':
        formInfo = [
            'A',
            'positive',
            'universal',
            'subject term']
        return formInfo

    if form == 'E':
        formInfo = [
            'E',
            'negative',
            'universal',
            'subject and predicate terms']
        return formInfo

    elif form == 'I':
        formInfo = [
            'I',
            'positive',
            'particular',
            'none']
        return formInfo

    elif form == 'O':
        formInfo = [
            'O',
            'negative',
            'particular',
            'predicate term']
        return formInfo

def distributeTerms(majorPremise, minorPremise, conclusion, syllogismNumber):
    distributedTerms = []
    if syllogismNumber == '1':
        if 'subject' in majorPremise[3]:
            distributedTerms.append('Major premise - Middle term')
        if 'predicate' in majorPremise[3]:
            distributedTerms.append('Major premise - Major term')

        if 'subject' in minorPremise[3]:
            distributedTerms.append('Minor premise - Minor term')
        if 'predicate' in minorPremise[3]:
            distributedTerms.append('Minor premise - Middle term')

    elif syllogismNumber == '2':
        if 'subject' in majorPremise[3]:
            distributedTerms.append('Major premise - Major term')
        if 'predicate' in majorPremise[3]:
            distributedTerms.append('Major premise - Middle term')

        if 'subject' in minorPremise[3]:
            distributedTerms.append('Minor premise - Minor term')
        if 'predicate' in minorPremise[3]:
            distributedTerms.append('Minor premise - Middle term')


    elif syllogismNumber == '3':
        if 'subject' in majorPremise[3]:
            distributedTerms.append('Major premise - Middle term')
        if 'predicate' in majorPremise[3]:
            distributedTerms.append('Major premise - Major term')

        if 'subject' in minorPremise[3]:
            distributedTerms.append('Minor premise - Middle term')
        if 'predicate' in minorPremise[3]:
            distributedTerms.append('Minor premise - Minor term')

    elif syllogismNumber == '4':
        if 'subject' in majorPremise[3]:
            distributedTerms.append('Major premise - Major term')
        if 'predicate' in majorPremise[3]:
            distributedTerms.append('Major premise - Middle term')

        if 'subject' in minorPremise[3]:
            distributedTerms.append('Minor premise - Middle term')
        if 'predicate' in minorPremise[3]:
            distributedTerms.append('Minor premise - Minor term')

    
    if 'subject' in conclusion[3]:
        distributedTerms.append('Conclusion - Minor term')
    if 'predicate' in conclusion[3]:
        distributedTerms.append('Conclusion - Major term')
    return distributedTerms

def undistributedMiddleFallacy(distributedTerms):
    for item in distributedTerms:
        if 'Middle term' in item:
            return False
    return True

def illicitMajorFallacy(distributedTerms):
    if len(distributedTerms) == 1:
        if 'Major term' in distributedTerms[0]:
            return True
        else: return False

    elif len(distributedTerms) > 1:
        if 'Conclusion' in distributedTerms[-1] and 'Major term' in distributedTerms[-1]:
            for index in range(len(distributedTerms)-1):
                if 'Major term' in distributedTerms[index]:
                    return False
            return True
        else:
            return False
    else: return False

def illicitMinorFallacy(distributedTerms):
    if len(distributedTerms) == 1:
        if 'Minor term' in distributedTerms[0]:
            return True
        else: return False
    
    elif len(distributedTerms) > 1:
        if 'Conclusion' in distributedTerms[-1] and 'Minor term' in distributedTerms[-1]:
            for index in range(len(distributedTerms)-1):
                if 'Minor term' in distributedTerms[index]:
                    return False
            return True

        elif 'Conclusion' in distributedTerms[-2] and 'Minor term' in distributedTerms[-2]:
            for index in range(len(distributedTerms)-2):
                if 'Minor term' in distributedTerms[index]:
                    return False
            return True
        else: return False

    else: return False

def one_for_oneFallacy(form1, form2, form3):
    if form1[1] == form2[1] == 'negative':
        return True
    elif form1[1] == 'negative' and form3[1] != 'negative':
        return True
    elif form2[1] == 'negative' and form3[1] != 'negative':
        return True
    elif form3[1] == 'negative' and form1[1] != 'negative' and form2[1] != 'negative':
        return True
    else: return False

def existentialFallacy(form1, form2, form3):
    if form1[2] == 'universal' and form2[2] == 'universal':
        if form3[2] == 'universal':
            return False
        else: return True
    return False

def getForm(syllogism):
    disp = 'Please enter the form of the ' + str(syllogism) + ': '
    while True:
        retrievedForm = str(input(disp))
        if retrievedForm != 'A' and retrievedForm != 'E' and retrievedForm != 'I' and retrievedForm != 'O':
            print('Please enter a single, capital letter.')
        else: return retrievedForm

def getINT1234():
    while True:
        retrievedForm = str(input('Please enter the syllogism type number: '))
        if retrievedForm != '1' and retrievedForm != '2' and retrievedForm != '3' and retrievedForm != '4':
            print('Please enter a number between 1 and 4.')
        else: return retrievedForm

def main():
    form1 = getForm('major premise')
    form2 = getForm('minor premise')
    form3 = getForm('conclusion')
    number = getINT1234()
    print("Entered argument form. \n   ", form1, form2, form3,"-", number, "\n")
    test = distributeTerms(statement(form1),statement(form2),statement(form3),number)
    
    validity = True
    
    gogo = undistributedMiddleFallacy(test)
    if gogo == True:
        validity = False
        print("undistributed middle fallacy")

    gogo = illicitMajorFallacy(test)
    if gogo == True:
        validity = False
        print("illicit major fallacy")

    gogo = illicitMinorFallacy(test)
    if gogo == True:
        validity = False
        print("illicit minor fallacy")

    gogo = one_for_oneFallacy(statement(form1),statement(form2),statement(form3))
    if gogo == True:
        validity = False
        print("one-for-one fallacy")

    gogo = existentialFallacy(statement(form1),statement(form2),statement(form3))
    if gogo == True:
        validity = False
        print("existential fallacy")

    if validity == True:
        print('No fallacies detected. \nValid argument.')
    if validity == False:
        print("Invalid argument.")

def yesNO(string):
    yes = ["y", "yeah", "yes", "yep", "of course", "yeet", "please", "for sure", "true"]
    no = ["no", "nope", "not a chance", "no way", "negative", "false", "n"]
    while True:
        userInput = input(string + ': ')
        if userInput.lower() in yes: return True
        elif userInput.lower() in no: return False
        else: print("please type 'yes' or 'no' ")

checkContinue = True
while checkContinue == True:
    main()
    checkContinue = yesNO("Try another?")
    
"""
FORMATTING
solve this afterwards.
"""

