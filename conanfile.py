#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostTypeTraitsConan(base.BoostBaseConan):
    name = "boost_type_traits"
    url = "https://github.com/bincrafters/conan-boost_type_traits"
    lib_short_names = ["type_traits"]
    header_only_libs = ["type_traits"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_static_assert"
    ]
