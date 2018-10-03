from setuptools import setup, find_packages


setup(
    name='bookish',
    version='1.0',
    description='Find books by ISBN',
    author='Víctor Muñoz',
    author_email='victorm@marshland.es',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=(
        'pillow',
        'pyramid',
        'pyramid_jinja2',
        'requests',
        'waitress',
    ),
    extras_require={
        'dev': (
            'flake8',
            'pylint',
            'pyramid_debugtoolbar',
            'pyramid_flamegraph',
            'pytest',
            'pytest-cov',
        )
    },
    python_requires='>=3.5',
    zip_safe=True,
    entry_points={
        'paste.app_factory': [
            'main = bookish:main',
        ],
    },
)
