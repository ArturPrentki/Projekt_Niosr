cmake_minimum_required(VERSION 3.14)
project(robot_control)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies(REQUIRED
  ${${PROJECT_NAME}_BUILD_DEPENDS}
  ${${PROJECT_NAME}_BUILDTOOL_DEPENDS}
)

ament_python_install_package(${PROJECT_NAME})

set(PY_ROBOT_CONTROL "robot_control_node.py")
install(PROGRAMS ${PROJECT_NAME}/${PY_ROBOT_CONTROL} DESTINATION lib/${PROJECT_NAME})

set(PY_CAMERA_ARUCO "camera_aruco_node.py")
install(PROGRAMS ${PROJECT_NAME}/${PY_CAMERA_ARUCO} DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  find_package(ament_cmake_pytest REQUIRED)
  set(_pytest_tests
    test/test_robot_control.py
  )
  foreach(_test_path ${_pytest_tests})
    get_filename_component(_test_name ${_test_path} NAME_WE)
    ament_add_pytest_test(${_test_name} ${_test_path}
      APPEND_ENV PYTHONPATH=${CMAKE_CURRENT_BINARY_DIR}
      TIMEOUT 60
      WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    )
  endforeach()
endif()

ament_auto_package(INSTALL_TO_SHARE
  launch
  config
)
