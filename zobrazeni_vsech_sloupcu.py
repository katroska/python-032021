import pandas as pd
import numpy as np

# když si chci zobrazit všechny sloupce:
desired_width = 1000
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)
