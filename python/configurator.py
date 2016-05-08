# coding=utf-8
__author__ = 'jim'
import ConfigParser


def add_cgf():
    config = ConfigParser.RawConfigParser()

    # When adding sections or items, add them in the reverse order of
    # how you want them to be displayed in the actual file.
    # In addition, please note that using RawConfigParser's and the raw
    # mode of ConfigParser's respective set functions, you can assign
    # non-string values to keys internally, but will receive an error
    # when attempting to write to a file or when you get it in non-raw
    # mode. SafeConfigParser does not allow such assignments to take place.
    config.add_section('Section1')
    config.set('Section1', 'an_int', '15')
    config.set('Section1', 'a_bool', 'true')
    config.set('Section1', 'a_float', '3.1415')
    config.set('Section1', 'baz', 'fun')
    config.set('Section1', 'bar', 'Python')
    config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

    # Writing our configuration file to 'example.cfg'
    with open('example.ini', 'wb') as configfile:
        config.write(configfile)

def print_r_cfg():
    config = ConfigParser.RawConfigParser()
    config.read('example.cfg')

    # getfloat() raises an exception if the value is not a float
    # getint() and getboolean() also do this for their respective types
    a_float = config.getfloat('Section1', 'a_float')
    an_int = config.getint('Section1', 'an_int')
    print a_float + an_int

    # Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
    # This is because we are using a RawConfigParser().
    if config.getboolean('Section1', 'a_bool'):
        print config.get('Section1', 'foo')

def print_cfg():
    config = ConfigParser.ConfigParser()
    config.read('example.cfg')

    # Set the third, optional argument of get to 1 if you wish to use raw mode.
    print config.get('Section1', 'foo', 0) # -> "Python is fun!"
    print config.get('Section1', 'foo', 1) # -> "%(bar)s is %(baz)s!"

    # The optional fourth argument is a dict with members that will take
    # precedence in interpolation.
    print config.get('Section1', 'foo', 0, {'bar': 'Documentation',
                                            'baz': 'evil'})

def dft_cfg():
    # New instance with 'bar' and 'baz' defaulting to 'Life' and 'hard' each
    config = ConfigParser.SafeConfigParser({'bar': 'Life', 'baz': 'hard'})
    config.read('example.cfg')

    print config.get('Section1', 'foo') # -> "Python is fun!"
    config.remove_option('Section1', 'bar')
    config.remove_option('Section1', 'baz')
    print config.get('Section1', 'foo') # -> "Life is hard!"

def opt_move(config, section1, section2, option):
    try:
        config.set(section2, option, config.get(section1, option, 1))
    except ConfigParser.NoSectionError:
        # Create non-existent section
        config.add_section(section2)
        opt_move(config, section1, section2, option)
    else:
        config.remove_option(section1, option)

if __name__=='__main__':
    add_cgf()