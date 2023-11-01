from datetime import datetime

# Pytamy użytkownika o datę urodzenia
birthday_day = int(input("Podaj dzień urodzin (1-31): "))
birthday_month = int(input("Podaj miesiąc urodzin (1-12): "))
birthday_year = int(input("Podaj rok urodzin: "))

# Tworzymy obiekt daty urodzin
birthday = datetime(birthday_year, birthday_month, birthday_day)

# Pobieramy aktualną datę
current_date = datetime.now()

# Obliczamy różnicę w dniach między aktualną datą a datą urodzin w bieżącym roku
if current_date < birthday:
    # Jeśli urodziny w tym roku jeszcze nie nadeszły, obliczamy różnicę bez zmiany roku
    days_until_birthday = (birthday - current_date).days
else:
    # Jeśli urodziny w tym roku już minęły, obliczamy różnicę z przesunięciem na następny rok
    next_birthday = datetime(current_date.year + 1, birthday_month, birthday_day)
    days_until_birthday = (next_birthday - current_date).days

# Wyświetlamy wynik
print(f"Do Twoich następnych urodzin pozostało {days_until_birthday} dni.")
print(f"Następne urodziny będą miały miejsce {next_birthday.strftime('%d.%m.%Y')}.")