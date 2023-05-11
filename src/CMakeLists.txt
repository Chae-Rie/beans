cmake_minimum_required(VERSION 3.25)

set(dir "${CMAKE_CURRENT_SOURCE_DIR}")

list (
    APPEND src
    "${dir}/BeanStock.cpp"
    "${dir}/BeanStockDlg.cpp"
    "${dir}/PostgresQuery.cpp"
    "${dir}/DatabaseInterface.cpp"
    "${dir}/QueryInterface.cpp"
    "${dir}/PostgresDB.cpp"
    "${dir}/pch.cpp"
    "${dir}/BeanStock.rc"
)

set(src "${src}" PARENT_SCOPE)