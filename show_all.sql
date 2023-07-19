\c abcdebay;


\echo "Table: users";
SELECT * FROM users;

\echo "Table: users identified as sellers";
SELECT * FROM sellers;

\echo "Table: users identified as buyers";
SELECT * FROM buyers;

\echo "Table: users identified as bidders";
SELECT * FROM bidders;

\echo "Table: all the bids on platform";
SELECT * FROM bids;

\echo "Table: all the auctions on platform";
SELECT * FROM auctions;

\echo "Table: all the carts hold by buyers";
SELECT * FROM carts;

\echo "Table: all the items containning in carts";
SELECT * FROM contains;

\echo "Table: all the reviews on users";
SELECT * FROM reviews;

\echo "Table: all the items to be bid or sell";
SELECT * FROM items;

\echo "Table: all the sell transations made";
SELECT * FROM sales;