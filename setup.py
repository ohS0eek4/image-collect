from setuptools import setup

setup(
    name='image-collect',
    version='0.0.0',
    py_modules=['image-collect'],
    entry_points={
        'console_scripts': [
            'image-collect = image-collect:main',
        ],
    },
)