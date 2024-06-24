# AUTOGENERATED! DO NOT EDIT! File to edit: ../03a_pydantic.ipynb.

# %% auto 0
__all__ = ['DATA_DIR', 'DATA_FILE', 'original_data', 'min_year', 'max_year', 'ConstrainedInt', 'DataSelectorModel']

# %% ../03a_pydantic.ipynb 101
from typing import Annotated
from pydantic import model_validator, BaseModel, Field

# %% ../03a_pydantic.ipynb 129
from pathlib import Path
import pandas as pd

# %% ../03a_pydantic.ipynb 130
DATA_DIR = 'data'
DATA_FILE = 'land-ocean-temp-index.csv'

original_data = pd.read_csv(Path(DATA_DIR) / DATA_FILE, escapechar='#')
min_year = original_data['Year'].min()
max_year = original_data['Year'].max()

# %% ../03a_pydantic.ipynb 133
from typing_extensions import TypeAliasType

# %% ../03a_pydantic.ipynb 135
ConstrainedInt = TypeAliasType(
    "ConstrainedInt", 
    Annotated[
        int, 
        Field(ge=min_year, le=max_year)
    ]
)

# %% ../03a_pydantic.ipynb 138
class DataSelectorModel(BaseModel, validate_assignment=True):
    year_range: Annotated[
        # The key change is in the line below
        tuple[ConstrainedInt, ConstrainedInt],
        # With this change to the type we no longer need to tell ipyautoui
        # what kind of widget to use. Field contains just a brief description
        Field(description="Range of years to plot")
    ] = (1800, 2000)
    window_size: Annotated[int, Field(ge=2, le=100)] = 2
    polynomial_order: Annotated[int, Field(ge=1, le=10)] = 1

    # mode="after" means the validator runs after pydantic has checked that the individual
    # fields have values that are valid.
    @model_validator(mode="after")
    def limit_polynomial_order(self):
        
        if self.polynomial_order > self.window_size - 1:
            # Handle a bad polynomial order or window size
            raise ValueError("Polynomial order must be smaller than window size")
            
        # If we got this far the polynomial order is consistent with the window size
        # so return self. Failing to return self will end up causing an error.
        return self
