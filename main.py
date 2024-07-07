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
    "frame_1.png",
    "frame_2.png",
    "frame_3.png",
    "frame_4.png",
    "frame_5.png",
    "frame_6.png",
    "frame_7.png",
    "frame_8.png",
    "frame_9.png",
    "frame_10.png"
]


def get_boi_gordo_price():
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

    return float(cotacao_ultimo_dia.text.replace(',', '.')), float(variacao.text.replace('%', '').replace(',', '.'))


def set_day_of_week(pixoo):
    actual_date = date.today()
    day_of_week_index = actual_date.weekday()
    pixoo.draw_text(day_of_week[day_of_week_index], (3, 2), color_day_of_week)


def set_hour_and_minutes(pixoo):
    hour = datetime.now().hour
    minute = datetime.now().minute

    if hour < 9:
        hour = "0" + str(hour)

    if minute < 9:
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


def set_background_gray(pixoo):
    for x in range(0, 64):
        for y in range(0, 64):
            pixoo.draw_pixel((x, y), color_gray)


def main():
    print('[.] Booting..')

    price, variation = get_boi_gordo_price()

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

        # Determine the color and symbol
        if variation >= 0:
            color = green
            symbol = '+'
        else:
            color = red
            symbol = '-'

        # Draw the change percentage

        for i in cow_images:
            set_background_gray(pixoo)
            # Place the background again first, no need to clear since it's screen sized
            pixoo.draw_image(f"cow-images/{i}", (0, -4))

            set_day_of_week(pixoo)
            set_calendar_date(pixoo)
            set_spacer(pixoo)
            set_hour_and_minutes(pixoo)

            pixoo.draw_text('Boi', (5, 50), (255, 255, 255))
            pixoo.draw_text('Gordo', (5, 57), (255, 255, 255))

            # Draw current price
            pixoo.draw_text(f'R${price:.2f}', (29, 50), color)
            pixoo.draw_text(f'{symbol}{variation:.1f}%', (35, 57), color)

            # Push to the display
            time.sleep(0.2)
            pixoo.push()


if __name__ == '__main__':
    main()
