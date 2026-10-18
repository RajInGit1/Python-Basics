import sqlite3

var = sqlite3.connect('demo.db')
conn = var.cursor()

conn.execute('''

        create table if not exists DemoStu(
        sid number(3) primary key,
        sname varchar(20),
        age number(2)
        );

''')

conn.execute('''


    insert into DemoStu values (101, 'rahul',13);

    
''')

var.commit()
var.close()