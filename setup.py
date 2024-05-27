from setuptools import setup
with open('README.md', 'r') as fp:
    readme = fp.read()

setup(
    name='image_collect',
    version='0.0.4',
    py_modules=['image_collect'],
    install_requires=["BeautifulSoup4","deep_translator"],
    url='https://github.com/ohS0eek4/image-collect',
    long_description=readme,
    long_description_content_type='text/markdown'
)