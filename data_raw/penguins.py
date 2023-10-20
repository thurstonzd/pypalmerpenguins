import re

import pandas as pd
from skimpy import clean_columns

uri_adelie = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.219.3&entityid=002f3893385f710df69eeebe893144ff"
uri_gentoo = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.220.3&entityid=e03b43c924f226486f2f0ab6709d2381"
uri_chinstrap = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.221.2&entityid=fe853aa8f7a59aa84cdd3197619ef462"

uris = [uri_chinstrap, uri_adelie, uri_gentoo]
data_frames = []

for uri in uris:
    df = pd.read_csv(uri, keep_default_na=False, na_values=["", "NA", "."])
    data_frames.append(df)

def species_short(obs):
    return re.sub(r'\s.*', '', obs.species)

df = clean_columns(pd.concat(data_frames))
penguins = (df
    .assign(species=species_short)
)