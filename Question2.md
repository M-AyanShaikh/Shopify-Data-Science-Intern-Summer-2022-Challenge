# Question 2

## Question 2.a

A total of 54 orders were shipped by Speedy Express.

```
SELECT
	COUNT(*)
FROM
	Orders
WHERE
	ShipperID=1
```


## Question 2.b

The last name of the employee with the most orders is "Peacock".

```
WITH TempTable AS (SELECT
	e.EmployeeID,
	LastName,
	COUNT(*) COUNTS
FROM
	Orders e
INNER JOIN Employees d ON d.EmployeeID = e.EmployeeID
GROUP BY
	e.EmployeeID)
SELECT LASTNAME, MAX(COUNTS) FROM TempTable
```
