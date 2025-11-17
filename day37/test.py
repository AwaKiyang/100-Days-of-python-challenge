from datetime import datetime
today = datetime.now()
waar = str(today.date()).replace('-','')
print(type(waar))