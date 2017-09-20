from conans import ConanFile, tools, os

class BoostType_TraitsConan(ConanFile):
    name = "Boost.Type_Traits"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-type_traits"
    description = "For a description of this library, please visit http://boost.org/type_traits "
    license = "www.boost.org/users/license.html"
    lib_short_names = ["type_traits"]
    requires = "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Core/1.65.1@bincrafters/testing", \
                      "Boost.Static_Assert/1.65.1@bincrafters/testing"

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()