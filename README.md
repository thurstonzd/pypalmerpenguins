
<!-- README.md is generated from README.Rmd. Please edit that file -->

# palmerpenguins <a href='https://allisonhorst.github.io/palmerpenguins/'><img src='man/figures/logo.png' align="right" height="138.5" /></a>

pypalmerpenguins is an attempt to convert the original palmerpenguins to python using pandas et. al. For the original R repository, see 
allisonhorst/palmerpenguins.

<img src="man/figures/README-flipper-bill-1.png" width="75%" style="display: block; margin: auto;" />

## Installation

TODO

## About the data

Data were collected and made available by [Dr. Kristen
Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php)
and the [Palmer Station, Antarctica
LTER](https://pallter.marine.rutgers.edu/), a member of the [Long Term
Ecological Research Network](https://lternet.edu/).

The palmerpenguins package contains two datasets.

``` r
library(palmerpenguins)
data(package = 'palmerpenguins')
```

One is called `penguins`, and is a simplified version of the raw data;

``` python
penguins.head()
#>   species island bill_length_mm bill_depth_mm flipper_length_… body_mass_g sex  
#>   <fct>   <fct>           <dbl>         <dbl>            <int>       <int> <fct>
#> 1 Adelie  Torge…           39.1          18.7              181        3750 male 
#> 2 Adelie  Torge…           39.5          17.4              186        3800 fema…
#> 3 Adelie  Torge…           40.3          18                195        3250 fema…
#> 4 Adelie  Torge…           NA            NA                 NA          NA <NA> 
#> 5 Adelie  Torge…           36.7          19.3              193        3450 fema…
#> 6 Adelie  Torge…           39.3          20.6              190        3650 male 
#> # … with 1 more variable: year <int>
```

The second dataset is `penguins_raw`, and contains all the variables and
original names as downloaded;

``` python
penguins_raw.head()
#>   studyName `Sample Number` Species          Region Island Stage `Individual ID`
#>   <chr>               <dbl> <chr>            <chr>  <chr>  <chr> <chr>          
#> 1 PAL0708                 1 Adelie Penguin … Anvers Torge… Adul… N1A1           
#> 2 PAL0708                 2 Adelie Penguin … Anvers Torge… Adul… N1A2           
#> 3 PAL0708                 3 Adelie Penguin … Anvers Torge… Adul… N2A1           
#> 4 PAL0708                 4 Adelie Penguin … Anvers Torge… Adul… N2A2           
#> 5 PAL0708                 5 Adelie Penguin … Anvers Torge… Adul… N3A1           
#> 6 PAL0708                 6 Adelie Penguin … Anvers Torge… Adul… N3A2           
#> # … with 10 more variables: `Clutch Completion` <chr>, `Date Egg` <date>,
#> #   `Culmen Length (mm)` <dbl>, `Culmen Depth (mm)` <dbl>,
#> #   `Flipper Length (mm)` <dbl>, `Body Mass (g)` <dbl>, Sex <chr>,
#> #   `Delta 15 N (o/oo)` <dbl>, `Delta 13 C (o/oo)` <dbl>, Comments <chr>
```

Both datasets contain data for 344 penguins. There are 3 different
species of penguins in this dataset, collected from 3 islands in the
Palmer Archipelago, Antarctica.

We gratefully acknowledge Palmer Station LTER and the US LTER Network.
Special thanks to Marty Downs (Director, LTER Network Office) for help
regarding the data license & use.

## Examples

Penguins are fun to summarize! For example:

``` python
penguins.groupby("species").count()

species
Adelie    152
Chinstrap
Gentoo

penguins %>% 
  group_by(species) %>% 
  summarize(across(where(is.numeric), mean, na.rm = TRUE))
#> # A tibble: 3 × 6
#>   species   bill_length_mm bill_depth_mm flipper_length_mm body_mass_g  year
#>   <fct>              <dbl>         <dbl>             <dbl>       <dbl> <dbl>
#> 1 Adelie              38.8          18.3              190.       3701. 2008.
#> 2 Chinstrap           48.8          18.4              196.       3733. 2008.
#> 3 Gentoo              47.5          15.0              217.       5076. 2008.
```

Penguins are fun to visualize! For example:

<img src="man/figures/README-mass-flipper-1.png" width="75%" style="display: block; margin: auto;" />

<img src="man/figures/README-flipper-hist-1.png" width="75%" style="display: block; margin: auto;" />

## Artwork

You can download palmerpenguins art (useful for teaching with the data)
in `vignette("art")`. If you use this artwork, please cite with:
“Artwork by @allison_horst”.

### Meet the Palmer penguins

<img src="man/figures/lter_penguins.png" width="75%" style="display: block; margin: auto;" />

### Bill dimensions

The culmen is the upper ridge of a bird’s bill. In the simplified
`penguins` data, culmen length and depth are renamed as variables
`bill_length_mm` and `bill_depth_mm` to be more intuitive.

For this penguin data, the culmen (bill) length and depth are measured
as shown below (thanks Kristen Gorman for clarifying!):

<img src="man/figures/culmen_depth.png" width="75%" style="display: block; margin: auto;" />

## License

Data are available by
[CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/)
license in accordance with the [Palmer Station LTER Data
Policy](https://pallter.marine.rutgers.edu/data/) and the [LTER Data
Access Policy for Type I data](https://lternet.edu/data-access-policy/).

## Citation

To cite the palmerpenguins package, please use:

``` r
citation("palmerpenguins")
#> 
#> To cite palmerpenguins in publications use:
#> 
#>   Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer
#>   Archipelago (Antarctica) penguin data. R package version 0.1.0.
#>   https://allisonhorst.github.io/palmerpenguins/. doi:
#>   10.5281/zenodo.3960218.
#> 
#> A BibTeX entry for LaTeX users is
#> 
#>   @Manual{,
#>     title = {palmerpenguins: Palmer Archipelago (Antarctica) penguin data},
#>     author = {Allison Marie Horst and Alison Presmanes Hill and Kristen B Gorman},
#>     year = {2020},
#>     note = {R package version 0.1.0},
#>     doi = {10.5281/zenodo.3960218},
#>     url = {https://allisonhorst.github.io/palmerpenguins/},
#>   }
```

## Additional data use information

Anyone interested in publishing the data should contact [Dr. Kristen
Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php)
about analysis and working together on any final products. From Gorman
et al. (2014): “Individuals interested in using these data are expected
to follow the US LTER Network’s Data Access Policy, Requirements and Use
Agreement: <https://lternet.edu/data-access-policy/>.”

## References

**Data originally published in:**

-   Gorman KB, Williams TD, Fraser WR (2014). Ecological sexual
    dimorphism and environmental variability within a community of
    Antarctic penguins (genus *Pygoscelis*). PLoS ONE 9(3):e90081.
    <https://doi.org/10.1371/journal.pone.0090081>

**Data citations:**

Adélie penguins:

-   Palmer Station Antarctica LTER and K. Gorman, 2020. Structural size
    measurements and isotopic signatures of foraging among adult male
    and female Adélie penguins (*Pygoscelis adeliae*) nesting along the
    Palmer Archipelago near Palmer Station, 2007-2009 ver 5.
    Environmental Data Initiative.
    <https://doi.org/10.6073/pasta/98b16d7d563f265cb52372c8ca99e60f>
    (Accessed 2020-06-08).

Gentoo penguins:

-   Palmer Station Antarctica LTER and K. Gorman, 2020. Structural size
    measurements and isotopic signatures of foraging among adult male
    and female Gentoo penguin (*Pygoscelis papua*) nesting along the
    Palmer Archipelago near Palmer Station, 2007-2009 ver 5.
    Environmental Data Initiative.
    <https://doi.org/10.6073/pasta/7fca67fb28d56ee2ffa3d9370ebda689>
    (Accessed 2020-06-08).

Chinstrap penguins:

-   Palmer Station Antarctica LTER and K. Gorman, 2020. Structural size
    measurements and isotopic signatures of foraging among adult male
    and female Chinstrap penguin (*Pygoscelis antarcticus*) nesting
    along the Palmer Archipelago near Palmer Station, 2007-2009 ver 6.
    Environmental Data Initiative.
    <https://doi.org/10.6073/pasta/c14dfcfada8ea13a17536e73eb6fbe9e>
    (Accessed 2020-06-08).
