# Pi-Hue

Pi-Hue is a quick Flask app to throw on a Raspberry Pi that lets you interface with Philips Hue's API. Let's start quick-n-dirty and refine as we go.

## Why am I bothering with the Raspberry Pi?

It lets everybody on your network mess with your lights.

## Why else though?

Because I'd like to leverage my Pi's camera to get the outside color temperature, and adjust the lights accordingly.

## Anything else you'd like to tell us?

This is my first foray into the IoT. This is a tech space that I really enjoy and would love to do more in. If you'd like to contribute, or have any ideas, please feel free to suggest something.

## Setup

To make this work, you really just need a sqlite DB, a Raspberry Pi, and a Pi Camera. I called mine 'light.db', so you'll see that referenced in the code. It currently needs two tables, one called light_intensity and light_groups. You can infer the columns for now, will update once everything is a bit more polished :)

I have a pi-hue.ini file in /etc/pi-hue where I store my Hue API settings (ip_address and username).

## More explanations

Chose Flask for a web framework because having to write scripts and crons, it will be nice to be able to do everything in Python. Also just another excuse to write some more python.

The next step is hardcoding some lookups for the 'ct' value of the hue to the brightness value we get from the image. Once that's complete, this will be fully functional (and a little quirky). Once that's complete and the web app receives a little attention (want to set a toggle for this functionality, plus an optional brightness setting in addition to color temp), will have to do some math to make the values correspond a little more elegantly.
