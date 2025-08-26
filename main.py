from collectors import informatica
from storage import db

def run():
    db.init_db()
    data = informatica.fetch_informatica_data()
    db.save_data(data)
    print("Data collected and saved!")

if __name__ == "__main__":
    run()