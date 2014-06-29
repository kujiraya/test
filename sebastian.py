#!/usr/bin/evn python
from subprocess import check_call
import time

while True:
  check_call(["git", "pull", "origin", "master"])
  check_call(["ant", "clean", "release", ""])
  try:
    check_call(["php", "./sebastian/d.php"])
  except e:
    print "error"
  time.sleep(60)
