import os

LICENSE = """# Copyright 2024 University College London
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

"""

FILES = [
    "./tests/test_package_generation.py",
    "./tests/test_git_init.py",
    "./tests/data/test_package_generation/tests/test_dummy.py",
    "./{{cookiecutter.project_slug}}/tests/test_dummy.py",
]

for filepath in FILES:
    if os.path.exists(filepath):
        with open(filepath) as f:
            content = f.read()
        if "University College London" not in content:
            with open(filepath, "w") as f:
                f.write(LICENSE + content)
            print(f"✅ Added license to {filepath}")
        else:
            print(f"ℹ️ License already exists in {filepath}")
    else:
        print(f"❌ File not found: {filepath}")
