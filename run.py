from booking.booking import Booking

try:
    with Booking(teardown=True) as bot:

        bot.landing_first_page()
        bot.accept_cookies()
        bot.change_currency(currency='USD')
        bot.bypass_registration_prompt()
        bot.insert_destination(destination_name=input("Travel destination...>"))
        bot.select_dates(check_in_date=input("Check in date. e.g (2023-11-22)...>"),
                         check_out_date=input("Check out date. e.g (2023-11-22)...>"))
        bot.select_adults(count=int(input("How many travellers?...>")))
        bot.click_search()
        bot.implicitly_wait(5)
        bot.change_language()
        bot.bypass_registration_prompt()
        bot.apply_filtration()
        bot.refresh() #a workaround to let the bot grab the correct data
        bot.return_results()
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

