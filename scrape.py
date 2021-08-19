from bs4 import BeautifulSoup
import sys
import csv

inputfile = "ta201.html"
filename = 'lectures.csv'
base_url = "https://hello.iitk.ac.in/ta201a21/" 

def main():
    n = sys.argv
    try:
        x = int(n[1])
    except:
        x=0
        print("Input an integer value")
        return

    htmlfile = open(inputfile,'r',encoding='utf-8')
    path = htmlfile.read()
    htmlfile.close()
    soup = BeautifulSoup(path,'html.parser')

    all_lecs = []
    i = 1
    weeks = soup.find_all('div',class_='weekDetailsBox')
    for week in weeks:
        lecs = week.find_all('div',class_='lectureItem')
        weekno = i
        i=i+1
        for lec in lecs:
            name = (lec.find('div',class_='lectureInfoBoxText').text).strip()   #final
            find_a=lec.find('a',href=True)
            link = base_url + find_a['href']      
            list_entry = list((name, weekno, link))
            all_lecs.append(list_entry)

    with open(filename, 'w') as output_file:
        writer = csv.writer(output_file)
        if x > len(all_lecs):
            x = len(all_lecs)
            print("Lecture number less than input, printing all lectures")
        all_lecs = all_lecs[-x:]
        writer.writerow(["Lecture Name", "Week Number","Link"])
        writer.writerows(all_lecs)

if __name__ == "__main__":
    main()