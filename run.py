from booking.booking import Booking

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

