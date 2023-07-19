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
# Add a bidder's bid
#------------------------------------------------------------
def place_bid(bidder, auction, amount):
    tmpl = '''
        INSERT INTO bids(bidder_id, auction_id, bid_price) 
        VALUES (%s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl, ([bidder, auction, amount]))
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
        print("User Story #2")
        print('Pat\'s bid on auction 2002 of $35 should be added to the bid table.')
        print('Calling add bid for pat120, bidder 1, for auction "2002"')
        place_bid(1, 2002,35)
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))