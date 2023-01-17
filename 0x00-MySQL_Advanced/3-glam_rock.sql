-- Script used to check for life span of a band


SELECT band_name, formed - split AS lifespan
FROM metal_bands
WHERE style='Glam rock';
