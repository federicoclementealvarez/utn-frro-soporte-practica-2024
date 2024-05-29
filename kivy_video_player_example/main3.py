from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2

class CamApp(App):

  def build(self):
    layout = BoxLayout(orientation='vertical')
    self.img1=Image()
    layout.add_widget(self.img1)
    self.save_img_button= Button(
      text='Foto',
      pos_hint={'center_x': .5, 'center_y': .5},
      size_hint=(None, None))
    self.save_img_button.bind(on_press=self.take_picture)
    layout.add_widget(self.save_img_button)
    #opencv2 stuffs
    self.capture = cv2.VideoCapture(0)
    cv2.namedWindow("CV2 Image")
    Clock.schedule_interval(self.update, 1.0/60.0)
    return layout

  def update(self, dt):
    # display image from cam in opencv window
    ret, frame = self.capture.read()
    cv2.imshow("CV2 Image", frame)
    self.image_frame = frame
    # convert it to texture
    buf1 = cv2.flip(frame, 0)
    buf = buf1.tostring()
    texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
    #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
    texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    # display image from the texture
    self.img1.texture = texture1
      
  def take_picture(self, *args):
    # save image to file in opencv window
    image_name = 'picture'
    cv2.imwrite(image_name + '.jpg', self.image_frame)

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()