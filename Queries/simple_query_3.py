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
# Show the item of top most sold within a category
#------------------------------------------------------------
def show_top_sold(cate):
    tmpl = '''
        SELECT item_id, item_name, sold_count
          FROM items
         WHERE category LIKE %s
      ORDER BY sold_count DESC
         LIMIT 1;
    '''
    cmd = cur.mogrify(tmpl, [('%'+cate+'%')])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        item_id,item_name,sold_count = row
        print("%s. (%s) %s." % (item_id,item_name,sold_count))

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
        print("User Story #3")
        print("return the item of top most sold within a category")
        print("Testing Appliances category")
        print("Should return: Proctor Silex Plate sold 23")
        show_top_sold("Appliances")
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))