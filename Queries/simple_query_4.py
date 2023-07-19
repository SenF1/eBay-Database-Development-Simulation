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
# Show seller with best rating
#------------------------------------------------------------
def show_best_seller():
    tmpl = '''
        SELECT r.to_username, CAST(AVG(r.score) AS INT) as score
          FROM sellers as s
               LEFT JOIN users as u ON s.username = u.username
               JOIN reviews as r ON s.username = r.to_username
      GROUP BY r.to_username
      ORDER BY AVG(r.score) DESC
         LIMIT 1;
    '''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print_rows(rows)
    print()
    for row in rows:
        username,score = row
        print("%s. (%s)" % (username,score))

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
        print("User Story #4")
        print("return the seller with best rating")
        print("Should return: raja283 with 99")
        show_best_seller()
        print("--------------------------------------------------------------")
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))