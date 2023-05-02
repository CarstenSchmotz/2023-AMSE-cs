# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This projects analyzes the number of car registraitons with electric drive compare to the 
with the prize for electric energy.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis the correlation wheter electric cars are an significant factor to the energy crisis. 
Is the electric car raising the energy bills?
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: car registration for cars with alternative motors in germany
* Metadata URL: https://mobilithek.info/offers/573358160767496192
* Data URL: https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2022_09.xlsx?__blob=publicationFile&v=4 
* Data Type: xlsx

Short description.
New car registration in the year 2022 with electric, h2m and Hybrid drives. 
The car owner, the type of car and the modell are listed in segments of the germany 


### Datasource2: Engerie prize and Usage of household
* Metadata URL: https://www.govdata.de/web/guest/suchen/-/details/strompreise-fur-haushalte-deutschland-jahrejahresverbrauchsklassen-preisbestandteile
* Data URL:  https://www-genesis.destatis.de/genesis/downloads/00/tables/61243-0002_00.csv 
* Data Type: CSV

Short description.
Electricity prices for households: Germany, years,annual consumption classes, price components


## Work Packages
<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

[i1]: https://github.com/jvalue/2023-amse-template/issues/1
1. Automated data pipeline [#1][i1]
2. Automated test  [#2][i2]
3. Continous integration [#3][i3]
4. Project deployment on Github [#4][i4]
5. Filter relevant cars and energy prizes [#5][i5]
6. Group cars registration and energy prizes by location [#6][i6] 
7. Destinguish heat points with strong prize raises and minimal change [#7][i7]
8. Link prize raise with car buys  [#8][i8]
9. Display the locations [#9][i9]
 

[i1]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/1
[i2]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/2
[i3]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/3
[i4]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/4
[i5]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/5
[i6]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/6
[i7]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/7
[i8]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/8
[i9]: https://github.com/CarstenSchmotz/2023-AMSE-cs/issues/9