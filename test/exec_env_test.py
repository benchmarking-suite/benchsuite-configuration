# Benchmarking Suite
# Copyright 2014-2017 Engineering Ingegneria Informatica S.p.A.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Developed in the ARTIST EU project (www.artist-project.eu) and in the
# CloudPerfect EU project (https://cloudperfect.eu/)
import logging
import os

from benchsuite.core.controller import BenchmarkingController
from benchsuite.stdlib.execution.vm_environment import VM, VMSetExecutionEnvironment
from benchsuite.stdlib.util.libcloud_helper import guess_platform

class Image:
    pass

if __name__ == '__main__':

   image = Image()
   image.name = 'ubuntu-1412server'
   #image.name = 'base_centos_7'

   print(guess_platform(image))





