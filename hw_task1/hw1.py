from datetime import datetime

date = "2021-10-09"

today_time = datetime.today()


def get_days_from_today(date) -> int:
    your_date_object = datetime.strptime(your_date, "%Y-%m-%d")
    print(f"Ваша дата у форматі РРРР-ММ-ДД: ")
    print(your_date_object)

your_date = input("Введіть вашу дату у форматі РРРР-ММ-ДД: ")
get_days_from_today(your_date)
print(your_date)