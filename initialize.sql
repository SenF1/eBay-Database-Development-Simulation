-- Setup the database for a very simple 'social network'.
-- Friends - Users - Messages 

\c postgres
DROP DATABASE IF EXISTS abcdebay;

CREATE database abcdebay;
\c abcdebay

\i create.sql


\copy users(username,name,gender,email,phone,address) FROM users.csv csv header;


\copy sellers(seller_id, username) FROM sellers.csv csv header;


\copy buyers(buyer_id, username) FROM buyers.csv csv header;


\copy bidders(bidder_id, username) FROM bidders.csv csv header;


\copy reviews(review_id, from_username, to_username, date, comment, score) FROM reviews.csv csv header;


\copy items(item_id, item_name, details, category, seller_id, stock_count, sold_count, price_each) FROM items.csv csv header;


\copy sales(sale_id, buyer_id, item_id, quantity, price_each_at_sold,total_price, date) FROM sales.csv csv header;


\copy auctions(auction_id,length,item_id,list_price,close_price,highest_bidder) FROM auctions.csv csv header;


\copy bids(bid_id, bidder_id, auction_id, bid_price) FROM bids.csv csv header;


\copy carts(cart_id,buyer_id_1,buyer_id_2,num_items) FROM carts.csv csv header NULL AS 'NULL';


\copy contains(cart_id, item_id, quantity) FROM contains.csv csv header;
