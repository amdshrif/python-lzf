from setuptools import setup, Extension


VERSION = (0, 2, 4)

setup(
    name="python-lzf",
    description="C Extension for liblzf",
    version=".".join(filter(None, map(str, VERSION))),
    author="Travis Parker",
    author_email="travis.parker@gmail.com",
    url="http://github.com/teepark/python-lzf",
    license="BSD",
    ext_modules=[Extension(
        'lzf',
        ['lzf_module.c', 'lzf_c.c', 'lzf_d.c'],
        include_dirs=('.',),
        extra_compile_args=[
            '-Wall',
            # '-I/usr/include/python3.8/',
             ],
        # swig_opts=['-modern', '-I/usr/include/python3.8/']
        )],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: C",
        "Topic :: System :: Archiving :: Compression",
    ],
    package_data={
        "": [
                "data/lib.linux-x86_64-3.6/lzf.cpython-36m-x86_64-linux-gnu.so", 
                "data/lib.linux-x86_64-3.8/lzf.cpython-38-x86_64-linux-gnu.so"
            ],
    }
)
