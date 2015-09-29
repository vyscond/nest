# nest

cli to help you quickly build your setup.py

# Install

- pip

```
pip install nest
```

- pip + github

```
pip install -e git+https://github.com/vyscond/nest.git#egg=nest
```

- git clone + pip

```
git clone https://github.com/vyscond/nest.git
cd nest
pip install .
```

- git clone + make

```
git clone https://github.com/vyscond/nest.git
cd nest
make install
```

## Usage

- creating new setup.json base

```
nest new
```

- generating the setup.py based on our setup.json

```
nest gen
```

### All the commands bellow will make modifications only on setup.json file to prevent any error before generating the real setup.py. To see the modifications run ```nest gen```

- upgrading versions (semver based)

```
nest upgrade <major|minor|patch>
```

- downgrading versions (semver based)

```
nest downrade <major|minor|patch>
```

- requirements

- add extras

```
nest extras add <package_name> <tag>
```

- update basic attributes (this will update the tag values over the setup.json.

```
nest update <tagname>
```

- console help

If you're in trouble using __nest__ just type ```nest help``` to get the general view of the program or ```nest help <command_name>``` for a more specific help.


# Contributions



# License

The MIT License (MIT)

Copyright (c) 2015 Vyscond

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
