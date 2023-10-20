import re
from datetime import datetime

import pandas as pd
from skimpy import clean_columns

uri_adelie = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.219.3&entityid=002f3893385f710df69eeebe893144ff"
uri_gentoo = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.220.3&entityid=e03b43c924f226486f2f0ab6709d2381"
uri_chinstrap = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.221.2&entityid=fe853aa8f7a59aa84cdd3197619ef462"

uris = [uri_chinstrap, uri_adelie, uri_gentoo]
data_frames = []

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')

for uri in uris:
    df = pd.read_csv(
        uri, 
        keep_default_na=False, 
        na_values=["", "NA", "."]
        )
    data_frames.append(df)

def species_short(s):
    return re.sub(r'\s.*', '', s)

penguins_raw = pd.concat(data_frames).fillna('')

penguins_raw.to_csv(r"D:\Documents\programming\pypalmerpenguins\penguins_raw.csv")

penguins = (
    clean_columns(penguins_raw).assign(
        species=lambda x: x.species.apply(species_short),
        sex=lambda x: x.sex.apply(str.lower),
        date_egg=lambda x: x.date_egg.apply(dateparse),
        flipper_length_mm = lambda x: pd.to_numeric(x.flipper_length_mm, errors='coerce'),
        body_mass_g=lambda x: pd.to_numeric(x.body_mass_g, errors='coerce')
    ).assign(
        year=lambda x: x.date_egg.apply(lambda a: a.year)
    ).rename(
        columns={
            "culmen_length_mm": "bill_length_mm",
            "culmen_depth_mm": "bill_depth_mm"
        }
    )
)[[
    'species', 
    'island', 
    'bill_length_mm', 
    'bill_depth_mm', 
    'flipper_length_mm', 
    'body_mass_g', 
    'sex', 
    'year']]