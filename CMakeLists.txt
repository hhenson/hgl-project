cmake_minimum_required(VERSION 3.25)
project(hgl_workspace LANGUAGES NONE)

# Expose member documents and future sources without imposing a target toolchain.
file(GLOB_RECURSE HGL_MEMBER_FILES CONFIGURE_DEPENDS
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_spec/*.md"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_core/*.md"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_core/*.hgl"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_core/*.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_core/*.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_core/*.rs"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_std/*.md"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_std/*.hgl"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_std/*.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_std/*.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/hgl_std/*.rs")
set(HGL_WORKSPACE_FILES
    README.md AGENTS.md FOUNDATION.md context/existing-work.md
    ${HGL_MEMBER_FILES})
add_custom_target(hgl_workspace_files SOURCES ${HGL_WORKSPACE_FILES})
source_group(TREE "${CMAKE_CURRENT_SOURCE_DIR}" FILES ${HGL_MEMBER_FILES})
