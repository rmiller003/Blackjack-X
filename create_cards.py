from PIL import Image, ImageDraw, ImageFont

def create_card_image(value, suit, is_back=False):
    card_width = 100
    card_height = 150
    image = Image.new('RGB', (card_width, card_height), 'white')
    draw = ImageDraw.Draw(image)

    if is_back:
        draw.rectangle((0, 0, card_width, card_height), fill='blue')
        image.save('cards/back.png')
        return

    font = ImageFont.load_default()
    suit_font = ImageFont.load_default()

    color = 'red' if suit in '♥♦' else 'black'

    draw.text((10, 10), value, font=font, fill=color)
    draw.text((card_width - 30, card_height - 40), value, font=font, fill=color, anchor="ms")
    draw.text((card_width/2, card_height/2), suit, font=suit_font, fill=color, anchor="mm")

    suit_char = suit
    if suit == '♥':
        suit_char = 'H'
    elif suit == '♦':
        suit_char = 'D'
    elif suit == '♣':
        suit_char = 'C'
    elif suit == '♠':
        suit_char = 'S'


    image.save(f'cards/{value}{suit_char}.png')

if __name__ == '__main__':
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = '♥♦♣♠'

    for suit in suits:
        for value in values:
            create_card_image(value, suit)

    create_card_image('', '', is_back=True)
