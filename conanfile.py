from conans import ConanFile, tools, os

class BoostType_TraitsConan(ConanFile):
    name = "Boost.Type_Traits"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-type_traits"
    source_url = "https://github.com/boostorg/type_traits"
    description = "For a description of this library, please visit http://boost.org/type_traits "
    license = "www.boost.org/users/license.html"
    lib_short_names = ["type_traits"]
    requires = "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing"

    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()