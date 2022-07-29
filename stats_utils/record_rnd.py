import numpy as np
from datetime import datetime
import pathlib

def record_by_time(func_name, first_arg, output):
    hour = datetime.now().hour
    minute = datetime.now().minute

    record_path = f'./record/{func_name}'

    pathlib.Path(f'{record_path}').mkdir(parents=True, exist_ok=True)
    np.savetxt(f'{record_path}/{first_arg}_{hour}_{minute}.txt', X=output)
 
