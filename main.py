from datetime import datetime
import cal
import pdf

path = 'CarteRDV_DEBROUCKER_Tommy.pdf'

def main() :
    #delete all event with 'Place O Permis'
    cal.delete_all_event_permis()
    #add event
    res = pdf.extract_good_text(pdf.read_pdf(path))
    for e in res : 
        split = e[0].split('/')
        m = int(split[1])
        if m in [9,10,11,12] :
            y = 2021
        else :
            y = 2022
        cal.add_event('Place O Permis | ' + e[2], datetime(day=int(split[0]), month=m, year=y, hour=int(e[1])))

main()