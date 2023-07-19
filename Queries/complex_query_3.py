#-----------------------------------------------------------------
# complex--user-story
#-----------------------------------------------------------------

import psycopg2
import sys

def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')    

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    for row in rows:
        print(row)

#------------------------------------------------------------
# Update the number of items when I add something to my cart
#------------------------------------------------------------

def add_fn(cart,item,quantity):
    tmpl = '''
    CREATE OR REPLACE FUNCTION add_items() 
    RETURNS trigger 
    LANGUAGE plpgsql AS 
    $$
    BEGIN
        UPDATE Carts
            SET num_items = num_items + %s
            WHERE cart_id = %s;
        return null;
    END
    $$;

    DROP TRIGGER IF EXISTS tr_add ON subscribing; 

    CREATE TRIGGER tr_add
        AFTER INSERT or UPDATE ON Contains
        FOR EACH ROW
        EXECUTE FUNCTION add_items(cart,item,quantity);

    INSERT INTO Contains(cart_id, item_id, quantity) 
        VALUES (%s, %s, %s);

    '''
    cmd = cur.mogrify(tmpl, [quantity,cart,cart,item,quantity])
    print_cmd(cmd)
    cur.execute(cmd)


if __name__ == '__main__':
    try:
        db, user = 'abcdebay', 'isdb'
        if len(sys.argv) >= 2:
            db = sys.argv[1]
        if len(sys.argv) >= 3:
            user = sys.argv[2]
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        print("--------------------------------------------------------------")
        print("User Story #8")
        print("A trigger that update the number of items in cart when add item to cart")
        print("Testing by inserting 1 of item 3 into cart 10006")
        print("The cart originally have 2 in num_items column and now should be 3")
        add_fn(10006, 3, 1)
        print("--------------------------------------------------------------")

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))