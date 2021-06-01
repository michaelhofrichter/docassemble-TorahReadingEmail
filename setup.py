import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.TorahReadingEmail',
      version='0.0.4',
      description=('A docassemble extension.'),
      long_description='Uses the [Hebcal Triennial reading list](https://www.hebcal.com/sedrot/) and a separate Google Sheet with readers names to populate a way to easily send out an email about who is handling torah readings this week. \r\n\r\n## To Setup\r\nCopy the HebCal Triennial reading list for the current cycle into your own Google Drive and share it with your Docassemble Service account (see [Docassemble\'s Google Sheets example](https://docassemble.org/docs/functions.html#google%20sheets%20example)). Currently 5780-5782 is hardcoded into the package and you\'ll have to add a new code line for a different year.\r\n\r\n```\r\ncode: | \r\n  torahlist = read_sheet("Triennial-####-####", 0) \r\n```\r\n\r\nCreate a Google Sheet with the name `Torah Readers`. The columns should be: `First Name`, `Last Name`, `Email`, `Always Email`. Capitalization and spacing matters on these columns. `Always Email` should be configured with Data Validation for checkboxes only. Fill this in with any regular members of your Torah reading team. Add anyone else who needs to get these emails with the checkbox `Always Email` set to True. Delete any blank rows of the document. \r\n\r\nWhen completed, emails will be sent to any individuals named for a role and anyone who was listed with the `Always Email` attribute set to True in the Google Sheet. \r\n\r\n## Changelog:\r\n* 0.0.1 - MVP\r\n* 0.0.2 - Added link for Hebcal Licsense and expanded Readme.md\r\n* 0.0.3 - Added emailing support.\r\n* 0.0.4 - Fixed emailrecipients in function\r\n\r\n## Future Improvements:\r\n* increased recognition of the data from Hebcal including license clarification.\r\n* ability to pick the date of the next event (currently defaults to any within 7 days). ',
      long_description_content_type='text/markdown',
      author='Michael Hofrichter',
      author_email='michael.hofrichter@gmail.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/TorahReadingEmail/', package='docassemble.TorahReadingEmail'),
     )

