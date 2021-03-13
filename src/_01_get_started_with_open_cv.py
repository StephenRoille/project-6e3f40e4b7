"""Getting Started with Images.

https://docs.opencv.org/master/db/deb/tutorial_display_image.html
"""
import pathlib
from typing import Union

import cv2
import numpy as np


def read(
    img_path: Union[str, pathlib.Path], mode: int = cv2.IMREAD_UNCHANGED
) -> np.ndarray:
    """Read image from file.

    Arguments
    ---------
    img_path : :class:`str`
        Description_wrap_at_72_characters

    Keyword Arguments
    -----------------
    mode : :class:`int`, default is ``cv2.IMREAD_UNCHANGED``
        read mode among:

        * ``cv2.IMREAD_GRAYSCALE``;
        * ``cv2.IMREAD_COLOR`` (ignore transparency);
        * ``cv2.IMREAD_UNCHANGED``.

    Returns
    -------
    :class:`numpy.ndarray`
        image
    """
    return cv2.imread(str(img_path), mode)


if __name__ == "__main__":
    basedir = pathlib.Path(__file__).parents[1].resolve() / "data"
    fpath = basedir / "pexels_02.jpg"
    img = read(fpath, mode=cv2.IMREAD_GRAYSCALE)
    # cv2.namedWindow('image_names', cv2.WINDOW_NORMAL) # resizable
    cv2.namedWindow('image_names', cv2.WINDOW_AUTOSIZE) # fixed size
    cv2.imshow("image_names", img)
    cv2.waitKey(0)  # time [ms] before closing the window (0 for unlimited)
    cv2.imwrite(str(basedir / 'pexels_02_grey.png'), img)
