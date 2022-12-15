SELECT DISTINCT
	bin,
	CASE
		WHEN LENGTH(bin) = 4 THEN CONCAT(SUBSTRING(range_bin_low,1,LENGTH(bin)),'00000000')
		WHEN LENGTH(bin) = 5 THEN CONCAT(SUBSTRING(range_bin_low,1,LENGTH(bin)),'0000000')
		WHEN LENGTH(bin) = 6 THEN CONCAT(SUBSTRING(range_bin_low,1,LENGTH(bin)),'000000')
		WHEN LENGTH(bin) = 7 THEN CONCAT(SUBSTRING(range_bin_low,1,LENGTH(bin)),'00000')
   	END LOW,
	CASE
		WHEN LENGTH(bin) = 4 THEN CONCAT(SUBSTRING(range_bin_max,1,LENGTH(bin)),'99999999')
		WHEN LENGTH(bin) = 5 THEN CONCAT(SUBSTRING(range_bin_max,1,LENGTH(bin)),'9999999')
		WHEN LENGTH(bin) = 6 THEN CONCAT(SUBSTRING(range_bin_max,1,LENGTH(bin)),'999999')
		WHEN LENGTH(bin) = 7 THEN CONCAT(SUBSTRING(range_bin_max,1,LENGTH(bin)),'99999')
   	END HIGH,
	CASE
		WHEN bin.country in (null,'') THEN RANGES.country
		ELSE bin.country
	END COUNTRY
FROM `range` RANGES
	INNER JOIN bin
		ON bin = SUBSTRING(range_bin_low,1,LENGTH(bin));
