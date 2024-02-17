
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    database="postgres",
    host="database-1.cov4jvuitnep.us-east-1.rds.amazonaws.com",
    user="postgres",
    password="mhatre123",
    port="5432")


def getCur():
    return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


code = """def get_losscost_zip(pclass, zip):
    cursor = getCur()
    cursor.execute("SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.losscost_zip where protection_class=%s and zip=%s",
                   (pclass, zip))
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row"""
exec(code)
print(get_losscost_zip("01","01882"))