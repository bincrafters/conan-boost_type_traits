from conans import ConanFile, tools


class BoostType_TraitsConan(ConanFile):
    name = "Boost.Type_Traits"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost-type_traits"
    description = "For a description of this library, please visit http://boost.org/type_traits "
    license = "www.boost.org/users/license.html"

    requires = \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing"

    lib_short_names = ["type_traits"]
    is_header_only = True

    # BEGIN

    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    def package_id(self):
        if self.is_header_only:
            self.info.header_only()

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
