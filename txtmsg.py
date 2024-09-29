from pyp2p.net import Net
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

def p2p_listener(callback):
    net = Net(passive_bind="0.0.0.0", passive_port=44444, node_type="passive")
    net.start()

    while True:
        net.receive_from_any()
        for con in net:
            for reply in con.get_data():
                callback(reply)

def display_text(message, font_size=10):
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    matrix = RGBMatrix(options=options)

    # Set up font
    font = graphics.Font()
    font.LoadFont("path_to_font.bdf")  # You will need a suitable font file

    # Set color for the text
    text_color = graphics.Color(255, 255, 255)
    pos = matrix.width

    while True:
        matrix.Clear()
        len = graphics.DrawText(matrix, font, pos, 10, text_color, message)
        pos -= 1  # Move text left
        if pos + len < 0:
            pos = matrix.width  # Reset position once it scrolls off screen
        time.sleep(0.05)  # Adjust scrolling speed


def on_message_received(message):
    display_text(message)

if __name__ == "__main__":
    p2p_listener(on_message_received)
