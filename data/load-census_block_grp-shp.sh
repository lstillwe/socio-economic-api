shp2pgsql -s 4269 /projects/datatrans/ACS_Data/USBlockGroups2011/USBlockGroups2011.shp public.census_block_grps_2011 | psql -d socio_econ -U datatrans
shp2pgsql -s 4269 /projects/datatrans/ACS_Data/USBlockGroups2016/USBlockGroups2016.shp public.census_block_grps_2016 | psql -d socio_econ -U datatrans
