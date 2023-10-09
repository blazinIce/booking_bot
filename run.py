from booking.booking import Booking

try:
    with Booking(teardown=True) as bot:

        bot.landing_first_page()
        bot.accept_cookies()
        bot.change_currency(currency='USD')
        bot.bypass_registration_prompt()
        bot.insert_destination(destination_name='france')
        bot.select_dates("2023-10-16", "2023-10-22")
        bot.select_adults(count=10)
        bot.click_search()
        bot.change_language()
        bot.apply_filtration()
        bot.keep_browser_open()
except Exception as e:
    if 'in PATH' in str(e):
        print("You're trying to run the bot from the command line \n"
              "Please add to your Selenium drivers to PATH"
              "Windows \n"
              "     set PATH=%PATH%;C:path to your folder \n \n"
          "    Linux: \n"
              "     PATH=$PATH:/path/toyour/folder/ \n")
    else:
        raise

