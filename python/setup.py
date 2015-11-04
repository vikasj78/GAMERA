from distutils.core import setup, Extension
extension_mod = Extension("_gamerapy", 
                          ["_gamerapy.cc", "../src/Radiation.C","../src/Particles.C","../src/Utils.C"],
                          extra_compile_args=['-std=c++11'],
                          libraries=['gsl','gslcblas'],
                          include_dirs=['../include'],
                          extra_link_args=['-I$(GSLCFLAGS)'])

setup(name = "gamerapy", ext_modules=[extension_mod])
