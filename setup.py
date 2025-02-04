try:
    from overlays import builder
    builder.compile()
    builder.copy()
except:
    pass

import distribute_setup
import sys
import platform
distribute_setup.use_setuptools()
from setuptools import setup, Extension, find_packages

kernel = platform.release()

if kernel >= '4.1.0':
    kernel41 = [('BBBVERSION41', None)]
else:
    kernel41 = None

CFLAGS = ['-Wall', '-Werror', '-Wextra', '-Wno-missing-field-initializers', '-Wno-cast-function-type', '-Wno-format-truncation' ]

classifiers = ['Development Status :: 3 - Alpha',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware']

setup(name             = 'Adafruit_BBIO_ATRA',
      version          = '1.0.1',
      author           = 'Justin Cooper',
      author_email     = 'justin@adafruit.com',
      description      = 'A module to control BeagleBone IO channels',
      long_description = open('README.rst', encoding='utf-8').read() + open('CHANGELOG.rst', encoding='utf-8').read(),
      license          = 'MIT',
      keywords         = 'Adafruit BeagleBone IO GPIO PWM ADC',
      url              = 'https://github.com/adafruit/adafruit-beaglebone-io-python/',
      classifiers      = classifiers,
      packages         = find_packages(),
      py_modules       = ['Adafruit_I2C'],
      ext_modules      = [Extension('Adafruit_BBIO_ATRA.GPIO', ['source/py_gpio.c', 'source/event_gpio.c', 'source/c_pinmux.c', 'source/constants.c', 'source/common.c'], extra_compile_args=CFLAGS, define_macros=kernel41),
                          Extension('Adafruit_BBIO_ATRA.PWM', ['source/py_pwm.c', 'source/c_pwm.c', 'source/c_pinmux.c', 'source/constants.c', 'source/common.c'], extra_compile_args=CFLAGS, define_macros=kernel41),
                          Extension('Adafruit_BBIO_ATRA.ADC', ['source/py_adc.c', 'source/c_adc.c', 'source/constants.c', 'source/common.c'], extra_compile_args=CFLAGS, define_macros=kernel41),
                          Extension('Adafruit_BBIO_ATRA.SPI', ['source/spimodule.c', 'source/constants.c', 'source/common.c'], extra_compile_args=CFLAGS, define_macros=kernel41),
                          Extension('Adafruit_BBIO_ATRA.UART', ['source/py_uart.c', 'source/c_uart.c', 'source/constants.c', 'source/common.c'], extra_compile_args=CFLAGS, define_macros=kernel41)] )
