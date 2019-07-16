/*Ran query below to go from LinearReg2 to linearReg2 (2)*/
SELECT * FROM `linearReg2` yr1 left join linearReg2 yr2 on (yr1.User=yr2.User and yr1.status="new" and yr2.status="2nd_year") where yr1.status="new"


