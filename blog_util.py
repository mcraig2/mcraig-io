""" Util functions for displaying blog posts dynamically """
import glob


def get_blog_names():
    for fname in glob.glob('templates/blog/*.md'):
        with open(fname, 'r') as f:
            title = parse_comment(f.readline())
            # fname = '/'.join(fname.split('/')[1:])
            # yield title, fname
            yield title


def parse_comment(line):
    """ Given a markdown comment like: [//]: # (Some comment),
        parse out the comment

        :param line: the string containing the markdown comment

        :return: the subset of the string containing the info. """
    return line[9:-2]
