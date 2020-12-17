#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program loops colours


def main():
    # This function loops colours

    # process

    counter1 = 0
    counter2 = 0
    counter3 = 0

    for counter1 in range(2):
        for counter2 in range(255):
            for counter3 in range(255):
                print("RGB ({0},{1},{2})".format(
                        counter1, counter2, counter3))


if __name__ == "__main__":
    main()
