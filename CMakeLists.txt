cmake_minimum_required(VERSION 3.25)

project(BeanStock)

set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_CXX_FLAGS "-Wall")
# Set the MFC use case
add_definitions(-D_AFXDLL)

# Find MFC libraries
find_package(MFC REQUIRED)

# Find the resource compiler
find_program(RC_COMPILER NAMES rc.exe)


# für die verschiedenen directories

set (SOURCES
	beans/BeanStock.h
	beans/BeanStock.h
	beans/Messagecodes.h
	beans/QueryInterface.h
	beans/framework.h
	beans/BeanStockDlg.h
	beans/PostgresDB.h           
	beans/pch.h 
	beans/DatabaseInterface.h  
	beans/PostgresQuery.h  
	beans/Resource.h        
	beans/targetver.h

    BeanStock.rc           
	PostgresDB.cpp      
	BeanStockDlg.cpp       
	PostgresQuery.cpp   
	pch.cpp
	BeanStock.cpp  
	DatabaseInterface.cpp  
	QueryInterface.cpp


# Define the source files and resources



# Add the executable
add_executable(BeanStock ${SOURCES})

# Woher kommen die Dateien denn?

target_include_directories ( BeanStock PUBLIC include)

target_include_directories ( BeanStock PUBLIC src)

target_include_directories ( BeanStock PUBLIC tests)

target_include_directories ( BeanStock PUBLIC thirdparty)

# Link MFC libraries
target_link_libraries(BeanStock PRIVATE ${MFC_LIBRARIES})

# Set the resource compiler for the project
set(CMAKE_RC_COMPILER ${RC_COMPILER})
