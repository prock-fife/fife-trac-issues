Trac to Github Issues migration
===============================
This script was used to migrate data of our trac installation (around 1'800 tickets) to Github Issues.
It writes json files as specified in APIv3.
Partially based on [github-trac-ticket-import](https://github.com/adamcik/github-trac-ticket-import) by @adamcik.

The basic assumptions made should be documented in `convert.py`.
You will definitely need to edit `data.py`, which we didn't bother converting to YAML.

Find below documentation for our specific migration needs and the MIT license.

Procedure to update comments.csv
================================

Execute `python2 dumpapi.py -u <trac_username> -p <trac_password>`.  When this is done (it will take some time to dump the tickets) you will have a `comments.csv` file (still a work in progres).

Next execute: `python2 convert.py`

If there is any output besides a list of tickets, check that malformed row in csv

Probably missed some sort of escaping or the replacement algorithm went really wild

When everything looks good:

`tar -czf fife.tar.gz fife/`

And bother a poor github admin once more!

License
=======
The MIT License (MIT)

Copyright (c) 2013 Wayne Prasek <wprasek@gmail.com>
based on work Copyright (c) 2012 Chris Oelmueller <chris.oelmueller@gmail.com>
based on work Copyright (c) 2010 Thomas Adamcik

Permission is hereby granted, free of charge,  to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction,  including without limitation the rights
to use,  copy, modify,  merge, publish,  distribute, sublicense,  and/or sell
copies of the Software,  and to permit persons  to whom  the Software is fur-
nished to do so, subject to the following conditions:

The above  copyright notice  and this permission notice  shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS  PROVIDED "AS IS",  WITHOUT WARRANTY OF ANY KIND,  EXPRESS OR
IMPLIED,  INCLUDING  BUT NOT  LIMITED TO  THE WARRANTIES  OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR  PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR  COPYRIGHT HOLDERS  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIA-
BILITY,  WHETHER IN AN ACTION OF CONTRACT,  TORT OR OTHERWISE,  ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
