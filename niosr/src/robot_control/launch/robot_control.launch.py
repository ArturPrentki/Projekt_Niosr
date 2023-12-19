# Copyright 2023 stask
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def launch_setup(context, *args, **kwargs):
    param_path = LaunchConfiguration('robot_control_param_file').perform(context)
    if not param_path:
        param_path = PathJoinSubstitution(
            [FindPackageShare('robot_control'), 'config', 'robot_control.param.yaml']
        ).perform(context)

    robot_control_node = Node(
        package='robot_control',
        executable='robot_control_node.py',
        name='robot_control_node',
        parameters=[
            param_path
        ],
        output='screen',
        arguments=['--ros-args', '--log-level', 'info', '--enable-stdout-logs'],
        emulate_tty=True
    )

    camera_aruco_node = Node(
        package='robot_control',
        executable='camera_aruco_node.py',
        name='camera_aruco_node',
        parameters=[
            param_path
        ],
        output='screen',
        arguments=['--ros-args', '--log-level', 'info', '--enable-stdout-logs'],
        emulate_tty=True
    )

    return [
        robot_control_node,
        camera_aruco_node
    ]


def generate_launch_description():
    declared_arguments = []

    def add_launch_arg(name: str, default_value: str = None):
        declared_arguments.append(
            DeclareLaunchArgument(name, default_value=default_value)
        )

    add_launch_arg('robot_control_param_file', '')

    return LaunchDescription([
        *declared_arguments,
        OpaqueFunction(function=launch_setup)
    ])
