--  lists all the cities contained in the hbtn_0d_usa
SELECT ct.id, ct.name, st.name
FROM cities AS ct
INNER JOIN states AS st
ON ct.state_id = st.id
ORDER BY ct.id ASC;
