"""Getting Started with Videos.

tutorial: https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
video codecs: https://www.fourcc.org/codecs.php
"""
import pathlib
from typing import Tuple
from typing import Union

import cv2
import numpy as np


def live_cam(camera_index: int = 0) -> None:
    video = cv2.VideoCapture(camera_index)
    # cv2.namedWindow('image_name', cv2.WINDOW_AUTOSIZE) # fixed size
    cv2.namedWindow('image_name', cv2.WINDOW_NORMAL) # resizable size
    if not video.isOpened():
        raise RuntimeError(f"Camera {camera_index} not available.")
    while True:
        is_frame_received, frame = video.read()
        if not is_frame_received:
            raise RuntimeError("Frame was not received")

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('image_name', frame_gray)

        if cv2.waitKey(1) == ord('q'):
            break

    video.release()

def open_file(fpath: Union[str, pathlib.Path]) -> None:
    video = cv2.VideoCapture(str(fpath))
    is_frame_received, frame = video.read()
    while video.isOpened():
        is_frame_received, frame = video.read()
        # nothing to stream
        if not is_frame_received:
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("imgae_name", frame_gray)

        if cv2.waitKey(25) == ord('q'):
            break

    video.release()


def save_cam(
    camera_index: int,
    fpath: Union[str, pathlib.Path],
    codec_name: str,
    fps: float = 25,
) -> None:
    video_in = cv2.VideoCapture(camera_index)
    if not video_in.isOpened():
        raise RuntimeError(f"Camera {camera_index} not available.")

    is_frame_received, frame = video_in.read()
    if not is_frame_received:
        raise RuntimeError("Frame was not received")

    width, height, _ = frame.shape
    codec = cv2.VideoWriter_fourcc(*codec_name)  # name must be converted into a list
    video_out = cv2.VideoWriter(str(fpath), codec, fps, (width, height))
    while video_in.isOpened():
        is_frame_received, frame = video_in.read()
        if not is_frame_received:
            break
        frame_flipped = cv2.flip(frame, 1)
        video_out.write(frame_flipped)

        cv2.imshow("image_name", frame_flipped)
        if cv2.waitKey(1) == ord("q"):
            break

    video_in.release()
    video_out.release()


if __name__ == "__main__":
    mode = "save_cam"
    if mode == "live_cam":
        live_cam(camera_index=0)
    if mode == "play_video":
        basedir = pathlib.Path(__file__).parents[1].resolve() / "data"
        fpath = basedir / "video_saved.mkv"
        open_file(fpath=fpath)
    if mode == "save_cam":
        basedir = pathlib.Path(__file__).parents[1].resolve() / "data"
        fpath = basedir / "video_saved.mkv"
        save_cam(camera_index=0, fpath=fpath, codec_name="H264", fps=25)
