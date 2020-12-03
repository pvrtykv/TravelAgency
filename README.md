# TravelAgency
This is a simple console application that allows user to perform operations on travel_agency database. TravelAgency is a continuation of databases course project. It was created with Python 3.8 and PyMySQL, sys modules.
## Description
TravelAgency allows you to access travel_agency database as a client or as an employee. Client and employee interfaces have different functionalities. Client can browse available offers, and view  and change their personal information. Employee can manage client and offers data (view, add, delete, change).

```python

```
### SQL queries implemented in app
Examples of SQL queries that were used in app.
1. Select all trip offers where trip price is less than 2000 and hotel standard is at least 3-star.
```sql
  SELECT o.name,  l.city_name AS city, c.name AS country,
  h.name as hotel, h.stars, o.trip_price FROM offer o 
  INNER JOIN location l ON o.location_id = l.id 
  INNER JOIN country ON l.country_id = c.id 
  INNER JOIN hotel h ON o.hotel_id = h.id
  WHERE o.trip_price < 2000 AND h.stars IN ("3","4","5");
 ```

![ERD](travel_agency_erd.png)
*travel_agency database*
