# copar_pdf_scraper.py
# Downloads every PDF from the specified CoPAR page and saves to a local directory.

import requests, os, bs4

url = 'http://copar.org/par/'    # starting url
os.makedirs('coparPar', exist_ok=True)   # store in local directory ./coparPar
while True:
    # Get the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text) #Creates BeautifulSoup object from text of downloaded page

    # Find the a elements.
    aElem = soup.select('a') #all a elements with
    #if aElem == []:
        #print('Could not find link.')
    #else:
    for i in range(len(aElem) + 1):
        pdfUrl = url + aElem[i].get('href')
        # Download the pdf.
        print('Downloading pdf %s...' % (pdfUrl))
        res = requests.get(pdfUrl)
        res.raise_for_status()

    # Save the pdf locally to ./coparPar.
        pdfFile = open(os.path.join('coparPar', os.path.basename(pdfUrl)), 'wb') #basename returns just the last part of the URL
        for chunk in res.iter_content(100000):
            pdfFile.write(chunk)
        pdfFile.close()

    print('Done.')
    break
