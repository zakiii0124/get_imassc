import tweepy
import config
from time import sleep
import os
import urllib.error
import urllib.request
import re
import sys


class GetContents():
    SSR_TEXT = '登場時の動画'
    EVENT_TEXT = 'イベントの予告動画'
    REPRINT_TEXT = '復刻'
    BIRTH_TEXT = '誕生日ミニコミュ'
    COMIC_TEXT = 'web4コマ漫画更新！'
    CARD_TEXT = 'アイドルをご紹介'
    USER = '@imassc_official'

    def __init__(self):
        self.arg = sys.argv[1]

    def get_serch(self):
        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        api = tweepy.API(auth)

        # 検索
        return tweepy.Cursor(api.user_timeline,
							id=self.USER,
							include_entities=True,
							tweet_mode='extended',
							lang='ja').items(self.num)

    def get_file_name(self, str, full_text):
        card_name = re.findall(str, full_text)
        return card_name[0]

    def download_file(self, url, dst_path):
        try:
            with urllib.request.urlopen(url) as web_file:
                data = web_file.read()
                with open(dst_path, mode='wb') as local_file:
                    local_file.write(data)
        except urllib.error.URLError as e:
            print(e)

    def make_directory(self):
        if not os.path.exists('ssr'):
            os.mkdir('ssr')

        if not os.path.exists('event'):
            os.mkdir('event')

        if not os.path.exists('birth'):
            os.mkdir('birth')

        if not os.path.exists('comic'):
            os.mkdir('comic')

        if not os.path.exists('card'):
            os.mkdir('card')

    def get_file(self):
        if self.arg.isdigit():
            self.num = int(self.arg)
            self.make_directory()
        else:
            print(sys.argv[1])
            print('数値を入力してください')
            return

        for result in self.get_serch():
            try:
                media = result.extended_entities['media']
                for m in media:
                    if m['type'] == 'video':
                        origin = [variant['url'] for variant in m['video_info']
                            ['variants'] if variant['content_type'] == 'video/mp4'][0]
                        if self.SSR_TEXT in result.full_text:
                            file_name = self.get_file_name("アイドル(\【.+?)さん登場時の",
                                                            result.full_text)
                            dst_path = 'ssr/{}.mp4'.format(file_name)
                        elif self.EVENT_TEXT in result.full_text:
                            if self.REPRINT_TEXT in result.full_text:
                                continue
                            file_name = self.get_file_name(
                                'シナリオイベント\「(.+?)\」が始まり', result.full_text)
                            dst_path = 'event/{}.mp4'.format(file_name)
                        elif self.BIRTH_TEXT in result.full_text:
                            file_name = self.get_file_name(
                                'メンバー\「(.+?)\」さん', result.full_text)
                            dst_path = 'birth/{}.mp4'.format(
                                file_name + str(result.created_at))
                        else:
                            continue
                        print(file_name)
                        self.download_file(origin, dst_path)
                    elif m['type'] == 'photo':
                        img_url = result.extended_entities['media'][0]['media_url']
                        if self.COMIC_TEXT in result.full_text:
                            file_name = self.get_file_name(
                                '(第.+?\』)', result.full_text)
                            dst_path = 'comic/{}.png'.format(file_name)
                        elif self.CARD_TEXT in result.full_text:
                            full_text = ''.join(result.full_text.splitlines())
                            file_name = self.get_file_name(
                                'アイドル(\【.+?)\#シャニマス', full_text)
                            dst_path = 'card/{}.png'.format(file_name)
                        else:
                            continue
                        print(file_name)
                        self.download_file(img_url, dst_path)
                    else:
                        continue
                sleep(1)
            except:
                pass


get_contents = GetContents()
get_contents.get_file()