from datetime import datetime

date = "2021-10-09"

today_time = datetime.today()


def get_days_from_today(date) -> int:
    your_date_object = datetime.strptime(your_date, "%Y-%m-%d")
    difference = today_time.toordinal() - your_date_object.toordinal()
    print(f"Ваша дата у форматі РРРР-ММ-ДД об'єкту datetime: {your_date_object}")
    print(f"Різниця дорівнює: {difference}")
    return difference
   

your_date = input("Введіть вашу дату у форматі РРРР-ММ-ДД: ")
get_days_from_today(your_date)
print(f"Ваша дата у форматі РРРР-ММ-ДД: {your_date} ")
