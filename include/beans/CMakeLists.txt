cmake_minimum_required(VERSION 3.25)

set(dir "${CMAKE_CURRENT_SOURCE_DIR}")

list(
    APPEND src
    "${dir}/BeanStock.h"
    "${dir}/BeanStockDlg.h"
    "${dir}/PostgresQuery.h"
    "${dir}/DatabaseInterface.h"
    "${dir}/PostgresDB.h"
    "${dir}/Messagecodes.h"
    "${dir}/QueryInterface.h"
    "${dir}/Resource.h"
    "${dir}/targetver.h"
    "${dir}/framework.h"
    "${dir}/pch.h"
)

set(src "${src}" PARENT_SCOPE)