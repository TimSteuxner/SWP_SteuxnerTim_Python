from flask import Flask, request
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect("help.db", check_same_thread=False)


cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS symbols(name varchar(20), count INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS statistic (winPlayer INT, winsComp INT, draws INT)")


@app.route('/datasql', methods=['POST'])
def handle_form():
    stats = request.json  # Angenommen, die Daten werden im JSON-Format gesendet
    sqlData(stats)
    return "Daten erfolgreich hinzugefügt"


def sqlData(stats):
    st = cursor.execute('SELECT * FROM statistic')
    sy = cursor.execute('SELECT * FROM symbols')
    if st is None and sy is None:
        cursor.execute("INSERT INTO statistic (wincPlayer, winsComp, draws) VALUES (?, ?, ?)",
                       (stats['playerwins'], stats['compwins'], stats['draws']))

        for symbol, count in stats['symbol_counts'].items():
            cursor.execute("INSERT INTO symbols (name, count) VALUES (?, ?)", (symbol, count))
    else:
        cursor.execute('UPDATE statistic SET winPlayer = ?, winsComp = ?, draws = ?',
                       (stats['playerwins'], stats['compwins'], stats['draws']))
        for symbol, count in stats['symbol_counts'].items():
            cursor.execute('UPDATE symbols SET count = ? WHERE name = ?', (count, symbol))

    st = cursor.execute('SELECT * FROM statistic')
    sy = cursor.execute('SELECT * FROM symbols')
    connection.commit()
    print(st + sy)

if __name__ == '__main__':
    app.run(debug=True)
