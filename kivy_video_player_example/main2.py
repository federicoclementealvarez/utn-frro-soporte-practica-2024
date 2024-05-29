import threading
import kivy
import kivy.garden
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
import cv2
import numpy as np
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture


class MyApp(App):

  def build(self):
    self.img1 = Image()
    layout = BoxLayout()
    layout.add_widget(self.img1)
    return layout
  
  def update_image_source(self, frame):
    buf1 = cv2.flip(frame, 0)
    buf = buf1.tobytes()
    image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    self.img1.source = 'rosario_0.jpg'


def function1():
  MyApp().run()

def function2():
  cap = cv2.VideoCapture(0)
  if (cap.isOpened()== False):
    print("Error opening video stream or file")

  while(cap.isOpened()): 
    ret, frame = cap.read()
    if ret == True:

      # Update the image in the Kivy widget
      MyApp().update_image_source(frame)

      # Press Q on keyboard to  exit
      if cv2.waitKey(25) & 0xFF == ord('q'):
              break

    # Break the loop
    else:
            break


#Create thread objects
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

#Start the threads
thread1.start()
thread2.start()

#Wait for both threads to finish
thread1.join()
thread2.join()