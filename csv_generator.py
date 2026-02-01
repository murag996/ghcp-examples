from faker import Faker
import csv
from datetime import datetime

fake = Faker('it_IT')

fields = [
    "id_cliente", "nome", "cognome", "codice_fiscale", "data_nascita",
    "indirizzo", "cap", "citta", "provincia", "telefono", "email",
    "azienda", "partita_iva", "iban", "swift_bic",
    "saldo_euro", "data_apertura"
]

def genera_codice_fiscale(fake):
    # Semplice fake CF (usa librerie come faker-codicefiscale per realismo)
    return fake.ssn().replace('/', '').upper()[:16]

with open("conti_bancari_fake.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for i in range(1, 101):
        writer.writerow({
            "id_cliente": i,
            "nome": fake.first_name(),
            "cognome": fake.last_name(),
            "codice_fiscale": genera_codice_fiscale(fake),
            "data_nascita": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),
            "indirizzo": fake.street_address(),
            "cap": fake.postcode(),
            "citta": fake.city(),
            "provincia": fake.administrative_unit(),
            "telefono": fake.phone_number(),
            "email": fake.email(),
            "azienda": fake.company(),
            "partita_iva": fake.company_vat(),
            "iban": fake.iban(),
            "swift_bic": fake.swift(),
            "saldo_euro": fake.pricetag(),
            "data_apertura": fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
        })
