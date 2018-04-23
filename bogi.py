import sys
import os
import keyboard

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# LED script to highlight keys after pressing them
##################################################

from logipy import logi_led
from logipy.logi_led import Color
import time
import ctypes

def print_pressed_keys(e):
  logi_led.logi_led_set_lighting_for_key_with_key_name(e.scan_code, *effect_color.rgb_percent())
  time.sleep(0.2)
  logi_led.logi_led_set_lighting_for_key_with_key_name(e.scan_code, 0, 0, 0)

print ('Having a nice thing here')
logi_led.logi_led_init()
time.sleep(1)

effect_enabled = logi_led.logi_led_get_config_option_bool('effect/enabled', True) # Use a default value if not found
effect_color = logi_led.logi_led_get_config_option_color('effect/color', Color(0, 255, 0))

logi_led.logi_led_set_config_option_label('effect', 'Effect Settings')
logi_led.logi_led_set_config_option_label('effect/enabled', 'Enabled')
logi_led.logi_led_set_config_option_label('effect/color', 'Color')

if effect_enabled:
    keyboard.hook(print_pressed_keys)


input('Press enter to shutdown SDK...')
logi_led.logi_led_shutdown()
