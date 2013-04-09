
from setuptools import setup

install_requires = [
    'requests==1.2.0',
    'python-dateutil==2.1'
]

setup(name="moz-kickoff-stats",
      version="0.1",
      description="Mozilla Project Kickoff Stats",
      url="https://github.com/st3fan/moz-kickoff-stats",
      author="Mozilla",
      author_email="sarentz@mozilla.com",
      install_requires = install_requires,
      scripts=['scripts/moz-kickoff-stats'])
