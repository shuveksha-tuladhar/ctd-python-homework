# Task 5: Extending a Class

from dataclasses import dataclass
import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        n = len(self)
        size = 10
        for start in range(0, n, size):
            end = start + size
            print(self.columns.to_list())            
            print(super().iloc[start:end])
            print()  # Blank line betwe
        
if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()