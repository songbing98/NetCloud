#!/usr/bin/env python3
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@site: http://www.github.com/Lyrichu
@file: NetCloudCrawlerTest.py
@time: 2019/01/06 00:18
@description:
test for NetCloudCrawler
"""
from main.crawler import NetCloudCrawler
from main.util import Helper


class NetCloudCrawlerTest:
    def __init__(self):
        self.logger = Helper.get_logger()
        self.song_name = "敢爱"
        self.song_id = 186888
        self.singer_name = "张国荣"
        self.singer_id = 6457
        self.singer_url = 'http://music.163.com/artist?id={singer_id}'.format(singer_id = self.singer_id)
        self.crawler = NetCloudCrawler.NetCloudCrawl(self.song_name,self.song_id,self.singer_name,self.song_id)

    def test_save_singer_all_hot_comments_to_file(self):
        self.crawler.save_singer_all_hot_comments_to_file()

    def test_get_singer_hot_songs_ids(self):
        self.logger.info(self.crawler.get_singer_hot_songs_ids(self.singer_url))

    def test_save_all_comments_to_file(self):
        self.crawler.save_all_comments_to_file()

    def test_threading_save_all_comments_to_file(self):
        self.crawler.save_all_comments_to_file_by_multi_threading()

    def test_get_lyrics(self):
        lyrics = self.crawler.get_lyrics_format_json()
        self.logger.info(lyrics)

    def test_save_lyrics_to_file(self):
        self.crawler.save_lyrics_to_file()

    def test_generate_all_necessary_files(self):
        self.crawler.generate_all_necessary_files()

    def test_all(self):
        '''
        运行全部test
        '''
        # self.test_get_singer_hot_songs_ids()
        # self.test_save_all_comments_to_file()
        # self.test_save_singer_all_hot_comments_to_file()
        # self.test_threading_save_all_comments_to_file()
        self.test_generate_all_necessary_files()


if __name__ == '__main__':
    test = NetCloudCrawlerTest()
    test.test_all()
