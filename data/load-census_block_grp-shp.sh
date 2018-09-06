shp2pgsql -s 4269 /projects/datatrans/ACS_Data/USBlockGroups2017/USBlockGroups2017.shp public.census_block_grps | psql -d socio_econ -U datatrans
