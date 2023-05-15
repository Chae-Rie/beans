cmake_minimum_required(VERSION 3.26)
set(This ExampleTests)


set(Sources
    ExampleTests.cpp                    # Was soll drin sein
)

add_executable(${This} ${Sources})      # Aus dem Test wird eine .exe werden
target_link_libraries(${This} PUBLIC    # Und wir linken verschiedene files ein
    gtest_main                          # gtest_main ist wichtig für die eigene main-loop
    gmock                               # gmock im Nachgang hinzugefügen als zu linkende Datei
    BeanStock	                        # Den Inhalt unserer Lib
)

add_test(
    NAME ${This}                        
    COMMAND ${This}
)