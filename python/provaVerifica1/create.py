import sqlite3

# Crea il database e le tabelle
connection = sqlite3.connect('file.db')
cursor = connection.cursor()

# Crea la tabella 'files'
cursor.execute('''
CREATE TABLE IF NOT EXISTS files (
    id_file INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    tot_frammenti INTEGER NOT NULL
)
''')

# Crea la tabella 'frammenti'
cursor.execute('''
CREATE TABLE IF NOT EXISTS frammenti (
    id_frammento INTEGER PRIMARY KEY AUTOINCREMENT,
    id_file INTEGER NOT NULL,
    n_frammento INTEGER NOT NULL,
    host TEXT NOT NULL,
    FOREIGN KEY (id_file) REFERENCES files(id_file)
)
''')

# Popola il database con dati di esempio
cursor.execute("INSERT INTO files (nome, tot_frammenti) VALUES ('file1', 3)")
cursor.execute("INSERT INTO frammenti (id_file, n_frammento, host) VALUES (1, 1, '192.168.1.10')")
cursor.execute("INSERT INTO frammenti (id_file, n_frammento, host) VALUES (1, 2, '192.168.1.11')")
cursor.execute("INSERT INTO frammenti (id_file, n_frammento, host) VALUES (1, 3, '192.168.1.12')")

# Salva e chiudi
connection.commit()
connection.close()
