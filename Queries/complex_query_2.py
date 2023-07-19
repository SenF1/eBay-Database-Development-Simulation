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
# Show demographics of a seller's customers
#------------------------------------------------------------
def show_demographics(seller, gender):
    tmpl = '''
        SELECT COUNT(b.buyer_id)
          FROM Sales as s
               LEFT JOIN Items as i ON i.item_id = s.item_id
               LEFT JOIN buyers as b ON s.buyer_id = b.buyer_id
               LEFT JOIN sellers as sel ON sel.seller_id = i.seller_id
               LEFT JOIN Users as u ON sel.username = u.username
        WHERE u.username = %s AND u.gender = %s;
    '''
    cmd = cur.mogrify(tmpl, ([seller, gender]))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        count = row
        print("%s" % (count) , gender)

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
        print("User Story #7")
        print('Calling show demographics for ethan00')
        print('Gender distributions')
        print('Should show a count of 2 males and 0 female')
        show_demographics("ethan00", "M")
        show_demographics("ethan00", "F")
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))