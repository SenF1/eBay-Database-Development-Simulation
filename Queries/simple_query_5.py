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
# show_bid_count
#------------------------------------------------------------
def show_bid_count(auction_id):
    tmpl = '''
        SELECT auction_id, COUNT(auction_id) as count
          FROM bids 
         WHERE auction_id = %s
      GROUP BY auction_id
      ORDER BY COUNT(auction_id) DESC;
    '''

    cmd = cur.mogrify(tmpl, ([auction_id]))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        aid,count = row
        print("%s. (%s)" % (aid,count))

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
        print("User Story #5")
        print("return number of people bidded on an item")
        print("Should return: 5 people bidded on auction 2002")
        show_bid_count(2002)
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))