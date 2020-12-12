from tqdm import tqdm
import time
for i in (t:=tqdm(range(1000))):
   t.set_description(f'MEDITATING')
   time.sleep(1)
