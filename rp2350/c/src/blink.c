#include "pico/stdlib.h"
#include "hardware/clocks.h"

#define OUT_PIN  1   // GPIO:1  for output

int main() {

    // set systemclock to 150MHz
    set_sys_clock_khz(150000, true);

    // setup GPIO for output
    gpio_init(OUT_PIN);
    gpio_set_dir(OUT_PIN, GPIO_OUT);

    while (true) {
       gpio_put(OUT_PIN, 1);   // H
       gpio_put(OUT_PIN, 0);   // L
    }
}
