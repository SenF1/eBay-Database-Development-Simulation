#-----------------------------------------------------------------
# first-user-story
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
# Show buyer that brought the most of a seller
#------------------------------------------------------------
def show_top_buyer(seller_username):
    tmpl = '''
        SELECT b.username, SUM(s.quantity) as total_brought
          FROM sales as s
               JOIN items as i ON i.item_id = s.item_id
               JOIN sellers as sel ON i.seller_id = sel.seller_id
               JOIN buyers as b ON s.buyer_id = b.buyer_id
         WHERE sel.username = %s
      GROUP BY b.username
      ORDER BY SUM(s.quantity) DESC
         LIMIT 1;
    '''
    cmd = cur.mogrify(tmpl, [seller_username])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        username,total_brought = row
        print("%s. (%s)" % (username,total_brought))

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
        print("User Story #6")
        print("return the buyer that brought most item from a particular seller")
        print("Testing Seller with username raja283")
        print("Should return: xiaoyint brought 11 items from raja283")
        show_top_buyer("raja283")
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))