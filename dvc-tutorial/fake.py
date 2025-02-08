import pandas as pd
import numpy as np

from pathlib import Path

if __name__ == '__main__':

    df = pd.DataFrame(
        data=np.random.random(size=(100, 5)),
        columns=list('ABCDE')
    )

    folder = Path('data')
    folder.mkdir(parents=True, exist_ok=True)

    i_lim, i = 10, 0

    base_name = 'dirty_data.csv'
    while Path(folder, base_name).exists() and i < i_lim:
        base_name = 'dirty_' + base_name
        i += 1
    
    if i >= i_lim:
        raise RuntimeWarning(
            'Parece que já existem arquivos de mais na sua pasta!'
        )

    dest = folder / base_name
    df.to_csv(dest, index=False)

    print(
        f"Dataset with size {df.size} saved at {dest.name}"
    )