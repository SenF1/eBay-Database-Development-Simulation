#-----------------------------------------------------------------
# simple-user-story
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
# Show sales from a certain seller
#------------------------------------------------------------
def show_sales(seller_username):
    tmpl = '''
        SELECT a.sale_id, a.date, a.buyer_id, a.item_id, a.quantity, a.price_each_at_sold, a.total_price
          FROM Sellers as s
            JOIN items as i ON i.seller_id = s.seller_id
            JOIN Sales as a ON i.item_id = a.item_id
         WHERE s.username = %s
      ORDER BY a.date DESC;
    '''
    cmd = cur.mogrify(tmpl, ([seller_username]))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    print(seller_username + "\'s SALE SUMMARY")
    for row in rows:
        sid,date,bid,aid,q,peach,total = row
        print("%s %s %s %s %s %s %s" % (sid,date,bid,aid,q,peach,total))

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
        print('Calling show sales for raja283')
        print('Should show details for raja283\'s three sales')
        show_sales('raja283')
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))