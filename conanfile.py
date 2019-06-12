from conans import ConanFile, CMake, tools


class CppTaskflowConan(ConanFile):
    name = "Cpp-Taskflow"
    version = "2.1.0"
    license = "MIT"
    homepage = "https://cpp-taskflow.github.io/"
    url = "https://github.com/torshind/conan-cpp-taskflow/"
    description = "Modern C++ Parallel Task Programming Library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        self.run("git clone --branch v"
                 + self.version
                 + " https://github.com/cpp-taskflow/cpp-taskflow.git")

    def build(self):
        tools.patch(base_path="cpp-taskflow", patch_file="AppleClang.patch")
        cmake = CMake(self)
        cmake.configure(source_folder="cpp-taskflow")
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.info.header_only()
