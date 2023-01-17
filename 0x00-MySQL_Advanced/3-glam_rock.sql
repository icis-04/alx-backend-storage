-- Script used to check for life span of a band


SELECT band_name, (IFNULL(split, 2023) - formed)  AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
