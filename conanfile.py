from conans import ConanFile, CMake, tools


class CppTaskflowConan(ConanFile):
    name = "cpp-taskflow"
    version = "2.1.0"
    license = "MIT"
    url = "https://cpp-taskflow.github.io/"
    description = "Modern C++ Parallel Task Programming Library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/cpp-taskflow/cpp-taskflow.git", "master")
        git.checkout("v" + self.version)

    def build(self):
        tools.patch(patch_file="AppleClang.patch")
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.info.header_only()
