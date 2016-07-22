#!/usr/bin/env python3

import os
import os.path
import nose.tools as nt
import delete_instuck_progress
import datetime
import time
import tempfile as tf


# note: ~ folder is not your home folder, but a sub folder of the one this code runs into


def create_test_files(abs_folder='~/tmp', filename='in-progress'):
    full_path = os.path.join(abs_folder, filename)
    if not os.path.exists(full_path):
        if not os.path.isdir(abs_folder):
            os.makedirs(abs_folder)
        with open(full_path, 'a'):
            today_full = datetime.date.today()
            t = datetime.datetime(today_full.year, today_full.month, today_full.day - 1, 0, 0)
            am_time = time.mktime(t.timetuple())
            os.utime(full_path, (am_time, am_time))


def test_drop_outdated_inprogress_file(filename='in-progress'):
    with tf.TemporaryDirectory() as tmp_dir:
        create_test_files(tmp_dir, filename)
        res = delete_instuck_progress.drop_outdated_inprogress_file(tmp_dir, filename)
        nt.assert_equal(True, res and not os.path.exists(os.path.join(tmp_dir, filename)))