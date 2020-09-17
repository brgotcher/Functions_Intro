def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)

banner_text("*")
banner_text("*")
banner_text("Testing")
banner_text("*")
banner_text(" ")
banner_text("*")
banner_text("BANNER TEXT FUNCTION")
banner_text("*")
banner_text("*")