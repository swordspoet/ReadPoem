import subprocess


class Player(object):
    def play_voice_by(self, voice_file_path):
        '''- 调用 mac 系统播放器 afplay 播放 MP3 文件
           - linux 下安装 sudo apt install mplayer，调用方法为：subprocess(['mplayer', voice_file_path])
        '''
        subprocess.call(['mplayer', voice_file_path])
