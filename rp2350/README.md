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
10000274 <main>:
10000274:       b500            push    {lr}
10000276:       b085            sub     sp, #20
10000278:       480f            ldr     r0, [pc, #60]   @ (100002b8 <main+0x44>)
1000027a:       ab03            add     r3, sp, #12
1000027c:       aa02            add     r2, sp, #8
1000027e:       a901            add     r1, sp, #4
10000280:       f000 fda4       bl      10000dcc <check_sys_clock_khz>
10000284:       b918            cbnz    r0, 1000028e <main+0x1a>
10000286:       490c            ldr     r1, [pc, #48]   @ (100002b8 <main+0x44>)
10000288:       480c            ldr     r0, [pc, #48]   @ (100002bc <main+0x48>)
1000028a:       f000 f83d       bl      10000308 <panic>
1000028e:       9801            ldr     r0, [sp, #4]
10000290:       e9dd 1202       ldrd    r1, r2, [sp, #8]
10000294:       f000 fcd8       bl      10000c48 <set_sys_clock_pll>
10000298:       2001            movs    r0, #1
1000029a:       f000 f811       bl      100002c0 <gpio_init>
1000029e:       2301            movs    r3, #1
100002a0:       ec43 3044       mcrr    0, 4, r3, r3, cr4
100002a4:       f04f 0100       mov.w   r1, #0
100002a8:       f04f 0201       mov.w   r2, #1
100002ac:       ec42 3040       mcrr    0, 4, r3, r2, cr0
100002b0:       ec41 3040       mcrr    0, 4, r3, r1, cr0
100002b4:       e7f8            b.n     100002a8 <main+0x34>
100002b6:       bf00            nop
100002b8:       000249f0        .word   0x000249f0
100002bc:       100017d0        .word   0x100017d0

100002c0 <gpio_init>:
100002c0:       b430            push    {r4, r5}
100002c2:       f04f 0300       mov.w   r3, #0
100002c6:       ec43 0044       mcrr    0, 4, r0, r3, cr4
100002ca:       ec43 0040       mcrr    0, 4, r0, r3, cr0
100002ce:       2505            movs    r5, #5
100002d0:       f44f 7480       mov.w   r4, #256        @ 0x100
100002d4:       4b0b            ldr     r3, [pc, #44]   @ (10000304 <gpio_init+0x44>)
100002d6:       00c2            lsls    r2, r0, #3
100002d8:       f853 1020       ldr.w   r1, [r3, r0, lsl #2]
100002dc:       eb03 0080       add.w   r0, r3, r0, lsl #2
100002e0:       f081 0140       eor.w   r1, r1, #64     @ 0x40
100002e4:       f102 4380       add.w   r3, r2, #1073741824     @ 0x40000000
100002e8:       f503 3320       add.w   r3, r3, #163840 @ 0x28000
100002ec:       f001 02c0       and.w   r2, r1, #192    @ 0xc0
100002f0:       f500 5180       add.w   r1, r0, #4096   @ 0x1000
```
(we can check asm code by ,,,    arm-none-eabi-objdump -d myblink.elf | grep -A 20 main)
loop part
```
100002a8:       f04f 0201       mov.w   r2, #1
100002ac:       ec42 3040       mcrr    0, 4, r3, r2, cr0
100002b0:       ec41 3040       mcrr    0, 4, r3, r1, cr0
100002b4:       e7f8            b.n     100002a8 <main+0x34>
```
### generated pulse
- 34.40ns
- 29.07MHz
