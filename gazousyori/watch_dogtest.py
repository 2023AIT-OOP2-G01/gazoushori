from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
import os
import time

if __name__ == "__main__":

    # 対象ディレクトリ
    DIR_WATCH = './input'
    # 対象ファイル名のパターン
    # .jpg .jpeg .png .gif .psd .tif
    PATTERNS = ['*.jpg']

    def on_modified(event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('これが画像処理のコードを実行するタイミング')

    event_handler = PatternMatchingEventHandler(PATTERNS)
    event_handler.on_modified = on_modified

    observer = Observer()
    observer.schedule(event_handler, DIR_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
