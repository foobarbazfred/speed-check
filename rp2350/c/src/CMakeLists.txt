cmake_minimum_required(VERSION 3.13)
include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)

project(blink C CXX ASM)
set(CMAKE_C_STANDARD 11)
pico_sdk_init()

add_executable(myblink blink.c)
target_link_libraries(myblink pico_stdlib hardware_clocks)
pico_add_extra_outputs(myblink)
