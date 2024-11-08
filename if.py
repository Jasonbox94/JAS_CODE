import os
rain = input('is it raining day today?')
try: 

    if str(rain) == 'Y' :
        print('yes')

except Exception as e:
    print(f"Unexpected error: {e}")
    