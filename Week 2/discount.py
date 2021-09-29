from datetime import datetime

current_date_and_time = datetime.now()

weekday = current_date_and_time.isoweekday()

subtotal = float(input("What was the subtotal of your order?"))