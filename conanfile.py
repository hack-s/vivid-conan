import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get, copy, rmdir, replace_in_file
from collections import namedtuple

class vividRecipe(ConanFile):
    name = "vivid"
    version = "3.0.1"
    package_type = "library"

    # Optional metadata
    license = "MIT"
    author = ""
    url = "https://github.com/conan-io/conan-center-index/tree/master/recipes/vivid"
    description = ""
    topics = ("color")
    exports_sources = "src/*", "dependencies/*", "cmake/*", "CMakeLists.txt"

    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def source(self):
        get(
            self,
            **self.conan_data["sources"][self.version],
            strip_root=True
        )
        replace_in_file(self, os.path.join(self.source_folder, "CMakeLists.txt"), "add_subdirectory( tests )", "")

    def requirements(self):
        deps = self.conan_data["dependencies"][self.version]

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        #self.cpp_info.set_property("cmake_target_name", f"vivid::vivid")
        self.cpp_info.libs = ["vivid"] #[ "vivid" + ("_d" if self.settings.build_type == "Debug" else "") ]
