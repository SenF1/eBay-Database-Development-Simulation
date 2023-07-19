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
# Share cart with another buyer
#------------------------------------------------------------
def share_cart(buyer_id_share_from, buyer_id_share_to):
    tmpl = '''
        UPDATE carts
           SET buyer_id_2 = %s
         WHERE buyer_id_1 = %s;
    '''
    cmd = cur.mogrify(tmpl, [buyer_id_share_to,buyer_id_share_from])
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
        print("User Story #10")
        print("Share cart with someone")
        print("Testing buyer_id 4 share with buyer_id 1")
        print("No return")
        share_cart(4,1)
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))