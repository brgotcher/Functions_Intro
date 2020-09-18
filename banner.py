def banner_text(text: str = " ", width: int = 80) -> None:
    """
    Center the entered text and border with asterisks
    :param text: the string to be printed
    :param width: the width around the entered text
    :return: nothing is returned
    """
    screen_width = width
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("*", 60)
banner_text("Testing", 60)
banner_text("*", 60)
banner_text(width=60)
banner_text("looooooooooooooooooooooooong teeeeeeeeeeeeeeeext", 60)
banner_text("*", 60)
banner_text("BANNER TEXT FUNCTION", 60)
banner_text("*", 60)
banner_text("*", 60)
