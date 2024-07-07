
def draw_number(pixoo, number, start_x, start_y):
    if number == 0:
        draw_number_0(pixoo, start_x, start_y)
    elif number == 1:
        draw_number_1(pixoo, start_x, start_y)
    elif number == 2:
        draw_number_2(pixoo, start_x, start_y)
    elif number == 3:
        draw_number_3(pixoo, start_x, start_y)
    elif number == 5:
        draw_number_5(pixoo, start_x, start_y)
    elif number == 4:
        draw_number_4(pixoo, start_x, start_y)
    elif number == 6:
        draw_number_6(pixoo, start_x, start_y)
    elif number == 7:
        draw_number_7(pixoo, start_x, start_y)
    elif number == 8:
        draw_number_8(pixoo, start_x, start_y)
    elif number == 9:
        draw_number_9(pixoo, start_x, start_y)


def draw_number_5(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo

    # Desenha a linha horizontal superior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y), color)
        pixoo.draw_pixel((start_x + x, start_y + 1), color)

    # Desenha a linha vertical esquerda superior de 4 pixels
    for y in range(1, 5):
        pixoo.draw_pixel((start_x, start_y + y), color)
        pixoo.draw_pixel((start_x +1, start_y + y), color)

    # Desenha a linha horizontal do meio de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 5), color)
        pixoo.draw_pixel((start_x + x, start_y + 6), color)

    # Desenha a linha vertical direita inferior de 4 pixels
    for y in range(5, 10):
        pixoo.draw_pixel((start_x + 5, start_y + y), color)
        pixoo.draw_pixel((start_x + 6, start_y + y), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 10), color)
        pixoo.draw_pixel((start_x + x, start_y + 11), color)

def draw_number_2(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo
    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y), color)
        pixoo.draw_pixel((start_x + x, start_y+1), color)

    # Desenha a linha vertical direita de 4 pixels
    for y in range(1, 5):
        pixoo.draw_pixel((start_x + 6, start_y + y), color)
        pixoo.draw_pixel((start_x + 5, start_y + y), color)

    # Desenha a linha horizontal do meio de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 5), color)
        pixoo.draw_pixel((start_x + x , start_y + 6), color)

    # Desenha a linha vertical esquerda de 4 pixels
    for y in range(6, 10):
        pixoo.draw_pixel((start_x, start_y + y), color)
        pixoo.draw_pixel((start_x + 1, start_y + y), color)

    # Desenha a última linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 10), color)
        pixoo.draw_pixel((start_x + x, start_y + 11), color)


def draw_number_0(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo

    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y), color)
        pixoo.draw_pixel((start_x + x, start_y+1), color)

    # Desenha a linha vertical direita superior de 8 pixels
    for y in range(1, 10):
        pixoo.draw_pixel((start_x + 5, start_y + y), color)
        pixoo.draw_pixel((start_x + 6, start_y + y), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 10), color)
        pixoo.draw_pixel((start_x + x, start_y + 11), color)

    # Desenha a linha vertical esquerda inferior de 8 pixels
    for y in range(1, 10):
        pixoo.draw_pixel((start_x, start_y + y), color)
        pixoo.draw_pixel((start_x + 1, start_y + y), color)


def draw_number_3(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo

    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y), color)
        pixoo.draw_pixel((start_x + x, start_y+1), color)

    # Desenha a linha vertical direita superior de 8 pixels
    for y in range(1, 10):
        pixoo.draw_pixel((start_x + 5, start_y + y), color)
        pixoo.draw_pixel((start_x + 6, start_y + y), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 10), color)
        pixoo.draw_pixel((start_x + x, start_y + 11), color)

    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 5), color)
        pixoo.draw_pixel((start_x + x, start_y + 6 ), color)


def draw_number_9(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo

    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y), color)
        pixoo.draw_pixel((start_x + x, start_y+1), color)

    # Desenha a linha vertical direita superior de 8 pixels
    for y in range(1, 10):
        pixoo.draw_pixel((start_x + 5, start_y + y), color)
        pixoo.draw_pixel((start_x + 6, start_y + y), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 10), color)
        pixoo.draw_pixel((start_x + x, start_y + 11), color)

    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 5), color)
        pixoo.draw_pixel((start_x + x, start_y + 6 ), color)

    # Desenha a linha vertical esquerda inferior de 8 pixels
    for y in range(1, 6):
        pixoo.draw_pixel((start_x, start_y + y), color)
        pixoo.draw_pixel((start_x + 1, start_y + y), color)


def draw_number_4(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo


    # Desenha a linha vertical direita superior de 8 pixels
    for y in range(0, 12):
        pixoo.draw_pixel((start_x + 5, start_y + y), color)
        pixoo.draw_pixel((start_x + 6, start_y + y), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 5), color)
        pixoo.draw_pixel((start_x + x, start_y + 6), color)


    # Desenha a linha vertical esquerda inferior de 8 pixels
    for y in range(0, 5):
        pixoo.draw_pixel((start_x, start_y + y), color)
        pixoo.draw_pixel((start_x + 1, start_y + y), color)


def draw_number_8(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo

    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y), color)
        pixoo.draw_pixel((start_x + x, start_y+1), color)

    # Desenha a linha vertical direita superior de 8 pixels
    for y in range(1, 10):
        pixoo.draw_pixel((start_x + 5, start_y + y), color)
        pixoo.draw_pixel((start_x + 6, start_y + y), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 5), color)
        pixoo.draw_pixel((start_x + x, start_y + 6), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 10), color)
        pixoo.draw_pixel((start_x + x, start_y + 11), color)

    # Desenha a linha vertical esquerda inferior de 8 pixels
    for y in range(1, 10):
        pixoo.draw_pixel((start_x, start_y + y), color)
        pixoo.draw_pixel((start_x + 1, start_y + y), color)


def draw_number_6(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo

    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y), color)
        pixoo.draw_pixel((start_x + x, start_y+1), color)

    # Desenha a linha vertical direita superior de 8 pixels
    for y in range(1, 6):
        pixoo.draw_pixel((start_x + 5, start_y + y+5), color)
        pixoo.draw_pixel((start_x + 6, start_y + y+6), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 5), color)
        pixoo.draw_pixel((start_x + x, start_y + 6), color)

    # Desenha a linha horizontal inferior de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y + 10), color)
        pixoo.draw_pixel((start_x + x, start_y + 11), color)

    # Desenha a linha vertical esquerda inferior de 8 pixels
    for y in range(1, 10):
        pixoo.draw_pixel((start_x, start_y + y), color)
        pixoo.draw_pixel((start_x + 1, start_y + y), color)


def draw_number_7(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo

    # Desenha a primeira linha horizontal de 7 pixels
    for x in range(7):
        pixoo.draw_pixel((start_x + x, start_y), color)
        pixoo.draw_pixel((start_x + x, start_y+1), color)

    # Desenha a linha vertical central de 10 pixels
    for y in range(12):
        pixoo.draw_pixel((start_x + 5, start_y + y), color)
        pixoo.draw_pixel((start_x + 6, start_y + y), color)

def draw_number_1(pixoo, start_x, start_y):
    color = (255, 255, 255)  # Cor branca, por exemplo

    # Desenha a linha vertical central de 10 pixels
    for y in range(12):
        pixoo.draw_pixel((start_x + 2, start_y + y), color)
        pixoo.draw_pixel((start_x + 3, start_y + y), color)
        pixoo.draw_pixel((start_x + 4, start_y + y), color)