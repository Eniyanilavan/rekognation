import psycopg2
import json
conn = psycopg2.connect(database = "exort", user = "postgres", password = "eniyan007", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
with open('server.json','r') as fp:
    # cur.execute("SELECT * FROM public.attendance")
    # rows = cur.fetchall()
    # print(rows)
    # print ("Operation done successfully")
    # conn.close()
    data = fp.readline()
    data = json.loads(data)
    coll_id = data['collid']
    for date in data["attendance"]:
        for name in data["attendance"][date]:
            print(date)
            cmd = ("INSERT INTO public.attendance (name,date,coll_id,dept) VALUES ('"+name+"',"+date+",'"+coll_id+"', 'CSE')")
            cur.execute(cmd)
conn.commit()
conn.close()