from distutils import log
import urllib.request
import threading
import logging
import time
import sys
import os       

class Downloader:
    def __init__(self) -> None:
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        self._url = sys.argv[1]        
        pass
    
    def _download_fn(self,id):
        logging.info("Thread %s: starting", id)
        if not os.path.exists('temp'):
            os.makedirs('temp')
        res = urllib.request.urlretrieve(self._url, f'temp/temp{id}.mp4') 
        os.remove(f'temp/temp{id}.mp4')
        logging.info(f'downloaded {self._url}: {res}')
        logging.info("Thread %s: finishing", id)

    def download(self,id):        
        x = threading.Thread(target=self._download_fn,args=(id,), daemon=True)        
        x.start()
        return x

if __name__=="__main__":
    dl = Downloader()
    threads = list()
    for i in range(1,int(sys.argv[2])+1):
        threads.append(dl.download(f'req_{i}'))
    logging.info(f'{sys.argv[2]} started')
    for index, thread in enumerate(threads):
        # logging.info("Main    : before joining thread %d.", index)
        thread.join()        
        logging.info("Main    : thread %d done", index)   
    


