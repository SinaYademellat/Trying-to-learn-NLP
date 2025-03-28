import MyWebScraping



if __name__ == '__main__':

    A = MyWebScraping.MyWebScraping()
    list_of_name = [
        'mojassameh','badhaye-vahshi','khaneye-sorkh','Sarzamine-Bartar','Bandbaze-Mast','Khab-Dar-Khab','Morse','Docharkheh','Enghelabe-Rangha','Ghatel-Ya-Maghtool',
        'Gole-Sorkh','Charkheshe-Rangha','Enfejare-Ranghaa','Saeghe','Raghase-Maghroogh','Ki-Ba-Ma-Zooze-Mikeshe','Mikeshan-Ist','Toghyan','Mikhoonim-Vase-Taghiaa','Shabe-Sarde-Kalanshahr'
                    ]

    for number_,name in enumerate(list_of_name):
        URL_is = f"https://genius.com/Ali-sorena-{name}-lyrics"
        path_for_save = f'mojassameh/{number_}_{name}.txt'
        A.run_it(
                main_url    = URL_is ,
                all_div_need =["SongPage__LyricsWrapper-sc-d1392e2e-2 kxuJAg","Lyrics__Container-sc-926d9e10-1 fEHzCI"],
                paht_is= path_for_save
                )