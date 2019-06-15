import MySQLdb
import cv2
import numpy as np
import lz4.frame
from time import sleep

frames = []
entires = []

video = cv2.VideoCapture(0)

video.set(3, 640)
video.set(4, 480)

ret, frame = video.read()

#cv2.imshow("frame", frame)

#cv2.waitKey(0)

frame = frame.flatten()
frame = frame.tostring()
frame = lz4.frame.compress(frame)

host = "cardb.ccwooq5jrcka.eu-west-2.rds.amazonaws.com"
user = "carrysl"
password = "Monkey12"
dbName = "carinfo"

host = "dbrysl.ccwooq5jrcka.eu-west-2.rds.amazonaws.com"
user = "rysl"
password = "HomeOfBaseData19"
dbName = "rysl_general_db"

db = MySQLdb.connect(host = host,
                        user = user,
                        passwd = password,
                        db = dbName)

cur = db.cursor()

#cur.execute("CREATE TABLE Drives (carID int PRIMARY KEY, runTime int, lastDistance int, lastSpeed int, frame mediumblob, fail bool)")
#cur.execute("INSERT INTO Drives (carID, runTime, lastDistance, lastSpeed, fail) VALUES (2, 30, 30, 50, 1)")
#cur.execute("SHOW TABLES")
#cur.execute("TRUNCATE TABLE Drives")
"""
try:
    cur.execute("INSERT INTO Drives VALUES (1, 68, 72, 34, %s, 0)", frame)
    db.commit()
except:
    db.rollback()"""


"""print(cur.execute("SELECT * FROM Drives"))



for (x) in cur:
    frames.append(x[4])

for x in range(len(frames)):
    frames[x] = lz4.frame.decompress(frames[x])
    frames[x] = np.fromstring(frames[x], dtype = "uint8")
    frames[x] = frames[x].reshape((240, 320, 3))
    cv2.imshow("frame", frames[x])
    cv2.waitKey(1)
"""
cur.execute("TRUNCATE TABLE Drives")

db.close()
