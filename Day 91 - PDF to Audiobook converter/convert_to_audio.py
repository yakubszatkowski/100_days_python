from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from progressbar_widget import Ui_progress_widget
import fitz, pyttsx3, math, time

class ConversionThread(QThread):

    def __init__(self, parent, save_file_path, language, text):
        super().__init__(parent)
        self.save_file_path = save_file_path
        self.language = language
        self.text = text
        

    def run(self):
        save_path = f'{self.save_file_path}'

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        choosen_voice = None
        for voice in voices:
            if self.language in voice.name:
                choosen_voice = voice
        
        engine.setProperty('voice', choosen_voice.id)
        engine.setProperty('rate', 180)
        engine.setProperty('volume', 1.0)

        engine.save_to_file(self.text, save_path)
        engine.runAndWait()


class SplashScreen(QSplashScreen, Ui_progress_widget):

    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        

    def read_pdf(self, file_path):
        self.show()
        self.text = ''
        max_percent = 19

        self.progres_label.setText('Conversion from pdf to text')

        with fitz.open(file_path) as doc:
            page_count = doc.page_count
            current_page = 0

            for page in doc:
                self.text += chr(12) + page.get_text('text', flags=0)
                current_page += 1
                progress_percent = math.floor((current_page / page_count)*max_percent)
                self.progress_bar.setValue(progress_percent)
                QApplication.processEvents()


    def convert_to_mp3(self, language, save_file_path):
        text_length = len(self.text)
        est_char_per_sec = 3400
        est_conversion_time = math.ceil(text_length / est_char_per_sec)
        max_percent = 80

        self.conversion = ConversionThread(self, save_file_path, language, self.text)
        self.conversion.finished.connect(self.finalizing)
        self.conversion.start()

        self.progres_label.setText('Conversion from text to audio')

        for second in range(est_conversion_time+1):
            progress_percent = math.floor((second/est_conversion_time)*max_percent) - 1
            total_progress = progress_percent+20
            self.progress_bar.setValue(total_progress)
            
            print(total_progress, self.conversion.isFinished())
            time.sleep(1)
            QApplication.processEvents()
            if total_progress == 99:
                self.progres_label.setText('Almost done...')
                QApplication.processEvents()


    def finalizing(self):
        self.progres_label.setText('Finished')
        self.progress_bar.setValue(100)
        print('Is finished:', self.conversion.isFinished())
        QApplication.processEvents()
        message_box = QMessageBox()
        message_box.information(None, 'Finished', 'PDF to Speech conversion finished!')
        self.text = ''

