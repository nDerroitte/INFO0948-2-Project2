from argparse import ArgumentParser, ArgumentTypeError
from ChannelCoding import *
from SourceCoding import *


if __name__ == "__main__":

    usage = """
    USAGE:      python3 run.py <options>
    EXAMPLES:   (1) python run.py
                    - Launch the P1 of the project
    """

    # Using argparse to select the different setting for the run
    parser = ArgumentParser(usage)

    # part : corresponds to part of the project one wants to run
    parser.add_argument(
        '--part',
        help="""Define the part of the project the user one to run. Can be {1,
        2, 3, 0}. 0 is for all.
        """,
        type=int,
        default=1
    )
    args = parser.parse_args()
    part = args.part

    if(part == 1 or part == 0):
        sourceCoding()
    if(part == 2 or part == 0):
        channelCoding()
    if(part == 3 or part == 0):
        imageCompression()
