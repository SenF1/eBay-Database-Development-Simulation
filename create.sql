-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-12-12 01:21:07.1

-- tables
-- Table: Auctions
CREATE TABLE Auctions (
    auction_id int  NOT NULL,
    length decimal(5,3)  NOT NULL,
    item_id int  NOT NULL,
    list_price int  NOT NULL,
    close_price money  NOT NULL,
    highest_bidder int  NOT NULL,
    CONSTRAINT Auctions_pk PRIMARY KEY (auction_id)
);

-- Table: Bidders
CREATE TABLE Bidders (
    bidder_id int  NOT NULL,
    username text  NOT NULL,
    CONSTRAINT Bidders_pk PRIMARY KEY (bidder_id)
);

-- Table: Bids
CREATE TABLE Bids (
    bid_id serial  NOT NULL,
    bidder_id int  NOT NULL,
    auction_id int  NOT NULL,
    bid_price money  NOT NULL,
    CONSTRAINT Bids_pk PRIMARY KEY (bid_id)
);

-- Table: Buyers
CREATE TABLE Buyers (
    buyer_id int  NOT NULL,
    username text  NOT NULL,
    CONSTRAINT Buyers_pk PRIMARY KEY (buyer_id)
);

-- Table: Carts
CREATE TABLE Carts (
    cart_id int  NOT NULL,
    buyer_id_1 int  NOT NULL,
    buyer_id_2 int  NULL,
    num_items int  NOT NULL,
    CONSTRAINT check_1 CHECK (buyer_id_2 IS NULL OR buyer_id_1 != buyer_id_2) NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT Carts_pk PRIMARY KEY (cart_id)
);

-- Table: Contains
CREATE TABLE Contains (
    cart_id int  NOT NULL,
    item_id int  NOT NULL,
    quantity int  NOT NULL,
    CONSTRAINT Contains_pk PRIMARY KEY (cart_id,item_id)
);

-- Table: Items
CREATE TABLE Items (
    item_id int  NOT NULL,
    item_name text  NOT NULL,
    details text  NOT NULL,
    category text  NOT NULL,
    seller_id int  NOT NULL,
    stock_count int  NOT NULL,
    sold_count int  NOT NULL,
    price_each money  NOT NULL,
    CONSTRAINT Items_pk PRIMARY KEY (item_id)
);

-- Table: Reviews
CREATE TABLE Reviews (
    review_id int  NOT NULL,
    from_username text  NOT NULL,
    to_username text  NOT NULL,
    date date  NOT NULL,
    comment text  NOT NULL,
    score int  NOT NULL,
    CONSTRAINT check_different_users CHECK (from_username != to_username ) NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT allowed_score CHECK (0 <= score AND score <= 100) NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT Reviews_pk PRIMARY KEY (review_id)
);

-- Table: Sales
CREATE TABLE Sales (
    sale_id int  NOT NULL,
    buyer_id int  NOT NULL,
    item_id int  NOT NULL,
    quantity int  NOT NULL,
    price_each_at_sold money  NOT NULL,
    total_price money  NOT NULL,
    date date  NOT NULL,
    CONSTRAINT Sales_pk PRIMARY KEY (sale_id)
);

-- Table: Sellers
CREATE TABLE Sellers (
    seller_id int  NOT NULL,
    username text  NOT NULL,
    CONSTRAINT Sellers_pk PRIMARY KEY (seller_id)
);

-- Table: Users
CREATE TABLE Users (
    username text  NOT NULL,
    name text  NOT NULL,
    gender char(1)  NOT NULL,
    email text  NOT NULL,
    phone varchar(15)  NOT NULL,
    address text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (username)
);

-- foreign keys
-- Reference: Auctions_Bidders (table: Auctions)
ALTER TABLE Auctions ADD CONSTRAINT Auctions_Bidders
    FOREIGN KEY (highest_bidder)
    REFERENCES Bidders (bidder_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Auctions_Items (table: Auctions)
ALTER TABLE Auctions ADD CONSTRAINT Auctions_Items
    FOREIGN KEY (item_id)
    REFERENCES Items (item_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Bids_Auctions (table: Bids)
ALTER TABLE Bids ADD CONSTRAINT Bids_Auctions
    FOREIGN KEY (auction_id)
    REFERENCES Auctions (auction_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Bids_Bidders (table: Bids)
ALTER TABLE Bids ADD CONSTRAINT Bids_Bidders
    FOREIGN KEY (bidder_id)
    REFERENCES Bidders (bidder_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Buyers_Users (table: Buyers)
ALTER TABLE Buyers ADD CONSTRAINT Buyers_Users
    FOREIGN KEY (username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Carts_Buyers_1 (table: Carts)
ALTER TABLE Carts ADD CONSTRAINT Carts_Buyers_1
    FOREIGN KEY (buyer_id_1)
    REFERENCES Buyers (buyer_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Carts_Buyers_2 (table: Carts)
ALTER TABLE Carts ADD CONSTRAINT Carts_Buyers_2
    FOREIGN KEY (buyer_id_2)
    REFERENCES Buyers (buyer_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Contains_Carts (table: Contains)
ALTER TABLE Contains ADD CONSTRAINT Contains_Carts
    FOREIGN KEY (cart_id)
    REFERENCES Carts (cart_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Contains_Items (table: Contains)
ALTER TABLE Contains ADD CONSTRAINT Contains_Items
    FOREIGN KEY (item_id)
    REFERENCES Items (item_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Users1 (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Reviews_Users1
    FOREIGN KEY (from_username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Users2 (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Reviews_Users2
    FOREIGN KEY (to_username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Sales_Buyers (table: Sales)
ALTER TABLE Sales ADD CONSTRAINT Sales_Buyers
    FOREIGN KEY (buyer_id)
    REFERENCES Buyers (buyer_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Sales_Items (table: Sales)
ALTER TABLE Sales ADD CONSTRAINT Sales_Items
    FOREIGN KEY (item_id)
    REFERENCES Items (item_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Sellers_Items (table: Items)
ALTER TABLE Items ADD CONSTRAINT Sellers_Items
    FOREIGN KEY (seller_id)
    REFERENCES Sellers (seller_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Sellers_Users (table: Sellers)
ALTER TABLE Sellers ADD CONSTRAINT Sellers_Users
    FOREIGN KEY (username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Bidders (table: Bidders)
ALTER TABLE Bidders ADD CONSTRAINT Users_Bidders
    FOREIGN KEY (username)
    REFERENCES Users (username)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

