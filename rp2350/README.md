# Speed test by C language


### build uf2 file
```
mkdir build
cd build
cmake .. -DPICO_BOARD=pico2_w -DPICOTOOL_FETCH_FROM_GIT=OFF
make myblink
```

### source code
simple only L/H of GPIO
```
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

```

Generated machine code
```
```
