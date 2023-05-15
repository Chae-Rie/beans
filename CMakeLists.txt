#cmake_minimum_required(VERSION 3.25)
#
#set(This BeanStock)
#
#project(${This})
#
#set(CMAKE_C_STANDARD 99)
#set(CMAKE_CXX_STANDARD 17)
#set(CMAKE_POSITION_INDEPENDENT_CODE ON)
#set(CMAKE_CXX_FLAGS "-Wall")
## Set the MFC use case
#add_definitions(-D_AFXDLL)
#
## Find MFC libraries
#find_package(MFC REQUIRED)
#
## Find the resource compiler
#find_program(RC_COMPILER NAMES rc.exe)
#
#
#enable_testing() # Wir wollen testen
#
## Add the executable
##add_executable(BeanStock ${SOURCES}) 
## Wir wollen eig nur die .exe im Test erstellen und den MainCode als STATIC lib adden
#
#
#add_subdirectory(thirdparty/googletest)
#
#
## für die verschiedenen directories
#
#set (SOURCES
#	include/BeanStock.h
#	include/BeanStock.h
#	include/Messagecodes.h
#	include/QueryInterface.h
#	include/framework.h
#	include/BeanStockDlg.h
#	include/PostgresDB.h           
#	include/pch.h 
#	include/DatabaseInterface.h  
#	include/PostgresQuery.h  
#	include/Resource.h        
#	include/targetver.h
#
#    src/BeanStock.rc           
#	src/PostgresDB.cpp      
#	src/BeanStockDlg.cpp       
#	src/PostgresQuery.cpp   
#	src/pch.cpp
#	src/BeanStock.cpp  
#	src/DatabaseInterface.cpp  
#	src/QueryInterface.cpp
#)
#
#add_library(${This} STATIC ${SOURCES})
#
## Woher kommen die Dateien denn?
#
#target_include_directories ( BeanStock PUBLIC include)
#
#target_include_directories ( BeanStock PUBLIC src)
#
#target_include_directories ( BeanStock PUBLIC mytests)
#
#target_include_directories ( BeanStock PUBLIC thirdparty/libpq)
#
#target_include_directories ( BeanStock PUBLIC thirdparty/googletest)
#
## Link MFC libraries
#target_link_libraries(BeanStock PRIVATE ${MFC_LIBRARIES})
#
## Set the resource compiler for the project
#set(CMAKE_RC_COMPILER ${RC_COMPILER})


cmake_minimum_required(VERSION 3.5)

project(BeanStock)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_MFC_FLAG 2)

# Find MFC and set some flags
find_package(MFC REQUIRED)
set(CMAKE_MFC_FLAG ${MFC_USE_STATIC_LIBS})

# Add include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Add source files
file(GLOB_RECURSE SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")

# Add resource files
file(GLOB_RECURSE RESOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.rc")

# Add third-party libraries
add_subdirectory(thirdparty/googletest)
add_subdirectory(thirdparty/libpq)

# Add the main executable
add_executable(BeanStock WIN32 ${SOURCES} ${RESOURCES})

# Link with MFC and other libraries
target_link_libraries(BeanStock PRIVATE ${MFC_LIBRARIES} libpq)

# Add the tests
add_subdirectory(mytests)
