import os
import time
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import date, datetime
from numbers_pixels import draw_number

from pixoo import Pixoo

# Load .env variables
load_dotenv()

color_gray = (36, 39, 43)
color_red = (188, 84, 75)
color_lightgray = (211, 211, 211)
color_black = (0, 0, 0)

color_calendar_date = color_red
color_day_of_week = color_red
color_spacer = color_lightgray

day_of_week = [
    "SEG",
    "TER",
    "QUA",
    "QUI",
    "SEX",
    "SAB",
    "DOM"
]

cow_images = [
    "frame_01.png",
    "frame_02.png",
    "frame_03.png",
    "frame_04.png",
    "frame_05.png",
    "frame_06.png",
    "frame_07.png",
    "frame_08.png",
    "frame_09.png",
    "frame_10.png"
]

coffee_bean_images = [
    "frame_01.png",
    "frame_02.png",
    "frame_03.png",
    "frame_04.png",
    "frame_05.png"
]


def get_cattle_price():
    url = "https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx"

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'id': 'imagenet-indicador1'})

    cotacao_ultimo_dia = "0"
    variacao = "0"

    if table:
        for row in table.find('tbody').find_all('tr'):
            cells = row.find_all('td')
            cotacao_ultimo_dia = cells[1]
            variacao = cells[2]
            break
    else:
        print("Tabela não encontrada.")

    return float(cotacao_ultimo_dia.text.replace('.', '').replace(',', '.')), float(variacao.text.replace('%', '').replace(',', '.'))

def get_coffee_price():
    url = "https://www.cepea.esalq.usp.br/br/indicador/cafe.aspx"

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'id': 'imagenet-indicador1'})

    cotacao_ultimo_dia = "0"
    variacao = "0"

    if table:
        for row in table.find('tbody').find_all('tr'):
            cells = row.find_all('td')
            cotacao_ultimo_dia = cells[1]
            variacao = cells[2]
            break
    else:
        print("Tabela não encontrada.")

    print(cotacao_ultimo_dia)

    return float(cotacao_ultimo_dia.text.replace('.', '').replace(',', '.')), float(variacao.text.replace('%', '').replace(',', '.'))


def set_day_of_week(pixoo):
    actual_date = date.today()
    day_of_week_index = actual_date.weekday()
    pixoo.draw_text(day_of_week[day_of_week_index], (3, 2), color_day_of_week)


def set_hour_and_minutes(pixoo):
    hour = datetime.now().hour
    minute = datetime.now().minute

    if hour <= 9:
        hour = "0" + str(hour)

    if minute <= 9:
        minute = "0" + str(minute)

    split_hour = list(str(hour))
    split_minute = list(str(minute))

    draw_number(pixoo, int(split_hour[0]), 29, 2)
    draw_number(pixoo, int(split_hour[1]), 37, 2)

    pixoo.draw_pixel((45, 4), color_red)
    pixoo.draw_pixel((45, 5), color_red)
    pixoo.draw_pixel((45, 10), color_red)
    pixoo.draw_pixel((45, 11), color_red)
    pixoo.draw_pixel((46, 4), color_red)
    pixoo.draw_pixel((46, 5), color_red)
    pixoo.draw_pixel((46, 10), color_red)
    pixoo.draw_pixel((46, 11), color_red)

    draw_number(pixoo, int(split_minute[0]), 48, 2)
    draw_number(pixoo, int(split_minute[1]), 56, 2)


def set_spacer(pixoo):
    for y in range(2, 14):
        pixoo.draw_pixel((27, y), color_spacer)


def set_calendar_date(pixoo):
    actual_date = date.today()

    day = actual_date.day
    month = actual_date.month

    if day < 9:
        day = "0" + str(day)

    if month < 9:
        month = "0" + str(month)

    pixoo.draw_text('{}'.format(day), (17, 2), color_calendar_date)
    pixoo.draw_text('{}'.format(month), (1, 9), color_calendar_date)
    pixoo.draw_pixel((9, 11), color_calendar_date)
    pixoo.draw_text('{}'.format(actual_date.year), (11, 9), color_calendar_date)


def set_background_black(pixoo):
    for x in range(0, 64):
        for y in range(0, 64):
            pixoo.draw_pixel((x, y), color_black)


def main():
    print('[.] Booting..')

    price_cattle, variation_cattle = get_cattle_price()
    price_coffee, variation_coffee = get_coffee_price()

    # Verify if the ip address is set, can't default this one
    ip_address = os.environ.get('PIXOO_IP_ADDRESS')
    if ip_address is None:
        print('[x] Please set the `PIXOO_IP_ADDRESS` value in the .env file')
        return

    # A pleasant green color. Like a yet-to-be-ripe banano
    green = (99, 199, 77)
    red = (255, 0, 68)

    # Retrieve some config
    timeout = 3600

    # Set up a connection and show the background
    pixoo = Pixoo(ip_address)

    print('[.] Starting update loop')
    while True:
        # Retrieve the current price and change percentage from the coingecko API



        # Draw the change percentage

        for repeat in range(3):
            if variation_cattle >= 0:
                color = green
                symbol = '+'
            else:
                color = red
                symbol = '-'

            for i in cow_images:
                set_background_black(pixoo)
                # Place the background again first, no need to clear since it's screen sized
                pixoo.draw_image(f"cow-images/{i}", (0, -4))

                set_day_of_week(pixoo)
                set_calendar_date(pixoo)
                set_spacer(pixoo)
                set_hour_and_minutes(pixoo)

                pixoo.draw_text('Boi', (5, 50), (255, 255, 255))
                pixoo.draw_text('Gordo', (5, 57), (255, 255, 255))

                # Draw current price
                pixoo.draw_text(f'R${price_cattle:.2f}', (29, 50), color)
                pixoo.draw_text(f'{symbol}{variation_cattle:.2f}%', (35, 57), color)

                # Push to the display
                time.sleep(0.2)
                pixoo.push()

        for repeat in range(6):
            if variation_coffee >= 0:
                color = green
                symbol = '+'
            else:
                color = red
                symbol = '-'

            for i in coffee_bean_images:
                set_background_black(pixoo)
                # Place the background again first, no need to clear since it's screen sized
                pixoo.draw_image(f"coffee-bean-images/{i}", (0, -1))

                set_day_of_week(pixoo)
                set_calendar_date(pixoo)
                set_spacer(pixoo)
                set_hour_and_minutes(pixoo)

                pixoo.draw_text('Saca', (5, 50), (255, 255, 255))
                pixoo.draw_text('Cafe', (5, 57), (255, 255, 255))

                # Draw current price
                pixoo.draw_text(f'R${price_coffee:.2f}', (29, 50), color)
                pixoo.draw_text(f'{symbol}{variation_coffee:.2f}%', (35, 57), color)

                # Push to the display
                time.sleep(0.2)
                pixoo.push()

if __name__ == '__main__':
    main()
