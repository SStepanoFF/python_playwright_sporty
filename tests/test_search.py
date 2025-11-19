def test_twitch_mobile_search(
        directory_page,
        search_result_page,
        streamer_page
):
    directory_page.open()
    directory_page.search("StarCraft II")

    search_result_page.scroll_down(2)
    search_result_page.select_first_streamer()
    streamer_page.welcome_chat_label.wait_for(state="visible")
    search_result_page.wait_and_screenshot("streamer_page.png")
