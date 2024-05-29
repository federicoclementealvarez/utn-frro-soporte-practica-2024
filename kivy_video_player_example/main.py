import threading
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
import cv2
import numpy as np

class VideoThread(threading.Thread):
        def __init__(self, parent_widget):
                threading.Thread.__init__(self)
                self.parent_widget = parent_widget

        def run(self):
                global cap
                cap = cv2.VideoCapture(0)
                if (cap.isOpened()== False):
                        print("Error opening video stream or file")

                while(cap.isOpened()):
                        # Capture frame-by-frame
                        ret, frame = cap.read()
                        if ret == True:
                                # Convert the frame to a Kivy Image
                                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                                image = kivy.garden.opencv.cv2_to_kivy_image(image)

                                # Update the image in the Kivy widget
                                self.parent_widget.image = image

                                # Press Q on keyboard to  exit
                                if cv2.waitKey(25) & 0xFF == ord('q'):
                                        break

                        # Break the loop
                        else:
                                break

class VideoApp(App):
        def build(self):
                self.video_widget = VideoWidget()
                self.video_thread = VideoThread(self.video_widget)
                self.video_thread.start()
                return self.video_widget

class VideoWidget(Widget):
        image = ObjectProperty()

        def on_touch_down(self, touch):
                if self.collide_point(*touch.pos):
                        self.video_thread.daemon = True

if __name__ == "__main__":
        App().run()
        print("gola manolo")
