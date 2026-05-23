-- Lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS count_of_records FROM second_table GROUP BY score ORDER BY count_of_records DESC;
