from conans import ConanFile, tools, os

class BoostType_TraitsConan(ConanFile):
    name = "Boost.Type_Traits"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-type_traits"
    source_url = "https://github.com/boostorg/type_traits"
    description = "For a description of this library, please visit http://boost.org/type_traits "
    license = "www.boost.org/users/license.html"
    lib_short_name = "type_traits"

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.source_url))

    def package(self):
        include_dir = src=os.path.join(os.getcwd(), self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)
