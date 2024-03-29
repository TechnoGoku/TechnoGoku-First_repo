from datetime import datetime

today_time = datetime.today()


def get_days_from_today(date) -> int:
    try:
        your_date_object = datetime.strptime(your_date, "%Y-%m-%d")
        difference = today_time.toordinal() - your_date_object.toordinal()
        print(f"Ваша дата у форматі РРРР-ММ-ДД: {your_date} ")
        print(f"Ваша дата у форматі РРРР-ММ-ДД об'єкту datetime: {your_date_object}")
        print(f"Різниця дорівнює: {difference} днів")
        
        return difference
    except ValueError:
        print("Ви ввели дату невірного формату, потрібно ввести дату формату РРРР-ММ-ДД с дефісом '-', враховуючи 12 місяців та 31 день у місяці, та 29 днів у 02 місяці!")


    

your_date = input("Введіть вашу дату у форматі РРРР-ММ-ДД: ")
get_days_from_today(your_date)

