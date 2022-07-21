import zipfile
import os.path

# Define zipped files for processing
# GitHub has 100MB file size limit so had to break them up
directory = 'data'

files = [
    '{}/VCardTransactions-NoName.csv.zip'.format(directory),
    '{}/VCardTransactions-NoName2.csv.zip'.format(directory)
]

def UnzipFiles():
    for file in files:
        csvFile = file.replace('.zip','')
    
        if(not os.path.exists(csvFile)):
            print('File DOES NOT exist {} - un-zipping'.format(csvFile))
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(directory)
        else:
            print('File exists {} - NOT un-zipping'.format(csvFile))
    
def CombineFiles():
    viewFile = '{}/vtrans.csv'.format(directory)
    os.makedirs(os.path.dirname(viewFile), exist_ok=True)
    if(not os.path.exists(viewFile)):
        print('File NOT exists {} - merging'.format(viewFile))
        with open(files[0].replace('.zip','')) as fp:
            data = fp.read()

        with open(files[1].replace('.zip','')) as fp:
            data2 = fp.read()

        data += "\n"
        data += data2

        with open (viewFile, 'w') as fp:
            fp.write(data)
    else:
        print('File exists {} - NOT merging'.format(viewFile))
    return viewFile

def LoadLotFacts():
    return '{}/lot_facts.csv'.format(directory)