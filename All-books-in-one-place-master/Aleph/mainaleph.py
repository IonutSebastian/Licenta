from Aleph import getdataaleph
import multiprocessing


if __name__ == '__main__':
    try:
        p1=multiprocessing.Process(target=getdataaleph,args=('http://aleph.bcucluj.ro:8991/F/QM8XINTBQA3RQH5U93AM1TDXXMHVYLMPY3222AGPNA29RBFEF6-28465?func=find-c-0', '2',))
        p2=multiprocessing.Process(target=getdataaleph,args=('http://aleph23.biblacad.ro:8991/F/1HNYGMTVHXS9GJJQ9DAYTQ8DCA6PRSEIP2V24E3D1E9CEPIT9H-16273?func=find-c-0','15',))
        p3=multiprocessing.Process(target=getdataaleph,args=('http://81.180.222.245:8991/F/QV4LU1B44MFRH559UMUFR4VI7463B2S831L8I74TYDNINA85CS-02060?func=find-c-0', '16',))
        p4=multiprocessing.Process(target=getdataaleph,args=('http://exlibris.usv.ro:8991/F/5MV9R9IKKQX4N6BJ8GBSMMH3UNJP4H2E33RX1HT97UPLDA7I2G-04878?func=find-c-0', '17',))


        p1.start()
        p2.start()
        p4.start()



    except:
        pass