import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('tracksamit.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
''')


fname = raw_input('Enter the file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'


def lookup(d, key):
    found = False
    for chu in d:
        if found : return chu.text
        if chu.tag == 'key' and chu.text == key :
            found = True
    return None

stuf = ET.parse(fname)
all = stuf.findall('dict/dict/dict')
print 'Dict count:', len(all)
for entr in all:
    if ( lookup(entr, 'Track ID') is None ) : continue

    name = lookup(entr, 'Name')
    artist = lookup(entr, 'Artist')
    album = lookup(entr, 'Album')
    count = lookup(entr, 'Play Count')
    rating = lookup(entr, 'Rating')
    length = lookup(entr, 'Total Time')
    genre = lookup(entr, 'Genre')

    if name is None or artist is None or album is None or genre is None :
        continue

    print name, artist, album, genre, count, rating, length

        
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES ( ?, ?, ?, ?, ?, ? )''', ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()