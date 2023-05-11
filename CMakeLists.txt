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
set(src)
add_subdirectory("docs")
add_subdirectory("include")
add_subdirectory("src")


# Define the source files and resources



# Add the executable
add_executable(BeanStock WIN32 ${src})

# Link MFC libraries
target_link_libraries(BeanStock PRIVATE ${MFC_LIBRARIES})

# Set the resource compiler for the project
set(CMAKE_RC_COMPILER ${RC_COMPILER})
