cmake_minimum_required(VERSION 3.0.2)
project(inverted_pendulum_controller)



find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

# catkin_package(
# )

include_directories(
  ${catkin_INCLUDE_DIRS}
)


## Generate services in the 'srv' folder
# add_service_files(
#   FILES
# )

generate_messages(
  DEPENDENCIES
  std_msgs
)



catkin_install_python(PROGRAMS
  # src/inverted_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
