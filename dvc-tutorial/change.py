import pandas as pd
from pathlib import Path

if __name__ == '__main__':

    source = Path('data', 'dirty_data.csv')

    assert source.exists(), 'Parece que o arquivo de entrada não existe ainda!'

    df = pd.read_csv(source)

    df = df.map(lambda v: round(v * 10, 0))

    df.to_csv(source, index=False)
