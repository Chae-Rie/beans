#cmake_minimum_required(VERSION 3.26)
#set(This ExampleTests)
#
#
#set(Sources
#    ExampleTests.cpp                    # Was soll drin sein
#)
#
#add_executable(${This} ${Sources})      # Aus dem Test wird eine .exe werden
#target_link_libraries(${This} PUBLIC    # Und wir linken verschiedene files ein
#    gtest_main                          # gtest_main ist wichtig für die eigene main-loop
#    gmock                               # gmock im Nachgang hinzugefügen als zu linkende Datei
#    BeanStock	                        # Den Inhalt unserer Lib
#)
#
#add_test(
#    NAME ${This}                        
#    COMMAND ${This}
#)

enable_testing()

# Add include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

# Add source files
file(GLOB_RECURSE TEST_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")

# Add the test executable
add_executable(BeanStockTests ${TEST_SOURCES})

# Link with GoogleTest and the main application
target_link_libraries(BeanStockTests PRIVATE gtest gtest_main BeanStock)

# Add the tests
add_test(NAME AllTests COMMAND BeanStockTests)