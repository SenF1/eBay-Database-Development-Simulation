#-----------------------------------------------------------------
# complex-user-story
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
# Add item to cart
#------------------------------------------------------------
def add_item(cart, item, quantity):
    tmpl = '''
        INSERT INTO Contains(cart_id, item_id, quantity) 
        VALUES (%s, %s, %s)
    '''
    cmd = cur.mogrify(tmpl, [cart,item,quantity])
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
        print("User Story #1")
        print('Calling add item to add 5 of item 4 to dave937\'s cart')
        add_item(10004, 4, 5)
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))