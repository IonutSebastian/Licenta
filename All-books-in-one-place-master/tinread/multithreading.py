import multiprocessing
from tinread.tinreadGetdata import tinread_get_data

def tinread():
    try:
        p1=multiprocessing.Process(target=tinread_get_data,args=('http://82.208.158.166/opac/bibliographic_view/', '1','15',))
        p2=multiprocessing.Process(target=tinread_get_data,args=('http://86.120.27.26:8080/opac/bibliographic_view/', '6','15',))
        p3=multiprocessing.Process(target=tinread_get_data,args=('http://bjarges.adisan.ro/opac/bibliographic_view/', '7','15',))
        p4=multiprocessing.Process(target=tinread_get_data,args=('http://188.27.227.136:8081/opac/bibliographic_view/', '8','15',))
        p5=multiprocessing.Process(target=tinread_get_data,args=('https://catalog.bibliobihor.ro/opac/bibliographic_view/', '9','15',))
        p6=multiprocessing.Process(target=tinread_get_data,args=('https://tinread.bjbn.ro/opac/bibliographic_view/', '10','15',))
        p7=multiprocessing.Process(target=tinread_get_data,args=('https://toread.bjbraila.ro/opac/bibliographic_view/', '11','15',))
        p8=multiprocessing.Process(target=tinread_get_data,args=('http://5.2.236.17:8080/opac/bibliographic_view/', '12','15',) )
        p9=multiprocessing.Process(target=tinread_get_data,args=('http://5.2.240.141/opac/bibliographic_view/', '13','15',) )
        p10=multiprocessing.Process(target=tinread_get_data,args=('http://193.231.136.4/opac/bibliographic_view/', '14','15',))
        p1.start()
        p2.start()
        p3.start()
        # p4.start()
        # p5.start()
        # p6.start()
        # p7.start()
        # p8.start()
        # p9.start()
        # p10.start()
    except:
        pass