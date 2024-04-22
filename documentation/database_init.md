### Database Loading
All loading of initial database entries is managed by ```/birds/management/commands/load_all_bird_data.py``` and is called by the install script. It depends on the csv and python files described below.

The order of model dependency:
1. AgeAnnual -> AgeWRP -> GroupWRP
2. Band -> Taxon
3. BandAllocation

#### Annual Ages
The csv provided in has been generated from the BBL bander portal. It was made by logging into the bander portal and navigating to....

```/data/AgeAnnuals.csv```
CSV headers:
1. "number"
2. "alpha"
3. "description"
4. "explanation"

#### WRP Ages
```/data/AgeWRPs.csv```
CSV headers 
1. "code"
2. "sequence"
3. "description"
4. "status"
5. "annuals"

#### WRP Groups
```/data/GroupWRPs.csv```
CSV headers 
1. "number"
2. "explanation"
3. "ages"

#### Band Sizes
```/data/Bands.csv```
CSV headers
1. "size"
2. "comment"

#### Taxon
```/data/TaxonBBL.csv```
CSV headers
1. "number"
2. "alpha"
3. "common"
4. "scientific"
5. "taxonomic_order"

#### Band Allocations for each taxon
```/data/BandAllocations.csv```
CSV headers 
1. "number"
2. "alpha"
3. "common"
4. "band_size"
4. "scientific"

### Taxon field population
Currently using the python dictionary in the maps directory. Will need to update a more mature approach.

```/maps/maps_reference_data.py SPECIES``` 

Uses the species dictionary to update the Taxon
1. wing chord ranges
2. sex related wing chord ranges
3. sexing criteria
4. page number in the second edition of pyle
5. M2M relationship with Taxon and GroupWRP   