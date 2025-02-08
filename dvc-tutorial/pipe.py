import pandas as pd
from pathlib import Path

if __name__ == '__main__':

    source = Path('data', 'dirty_data.csv')

    assert source.exists(), 'Parece que o arquivo de entrada não existe ainda!'

    df = pd.read_csv(source)

    dff = df.map(lambda v: round(v * 10, 0))

    df = df.join(dff, rsuffix='other_')

    dest = Path('data', 'normalized')
    
    dest.mkdir(parents=True, exist_ok=True)
    
    filepath = dest / 'clean_data.csv'

    df.to_csv(filepath, index=False)