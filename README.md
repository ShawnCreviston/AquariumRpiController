# AquariumRpiController
Aquarium Eco System Raspberry Pi based controller

This python program uses the rpi's main gpio pins to control 120v AC power relays to toggle on/off LED lights banks over an aquarium. In addition each light module setup can also have intensity controlled through PWM which is managed by a Arduino device connected to the USB of the rpi. It supports actinic and main lights on separate banks, of which I have my actinic light shifted to turn on slightly before the main lights. It runs a full moonlight, sunrise, and sunset cycle, with light banks on the left side of my tank turning on slightly before the right side to simulate the sun rising in the east and setting in the west.

This controller calculates the sunrise/sunset times and intensities based on the time of year. It can be configured to offset the daylight hours based on winter/summer cycles which will blend into the day cycles affecting sunrise/sunset and maximum daytime intensity. It also calculates the moon cycles, the main aquarium lights can be used as moon light or separate relays can be used for dedicated moon lights.

Though I am not currently using the tide feature on my tank I also wrote in a piece to calculate tide cycles as I'd like to implement something for it in the future.

The formulas used are basically modified Sin and Cosine waves, they start and end at the start of the year. So moon cycles are not a perfect match to real world but close enough for me.
