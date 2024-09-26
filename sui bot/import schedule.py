import schedule
import time

def track_wallets():
    # Add logic to check Sui API
    pass

schedule.every(30).seconds.do(track_wallets)

while True:
    schedule.run_pending()
    time.sleep(1)
