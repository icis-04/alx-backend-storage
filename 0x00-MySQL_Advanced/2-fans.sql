-- calculates the sum of fans by country


SELECT origin, SUM(fans) as 'nb_fans'
GROUP BY origin
ORDER BY 'nb_fans';
