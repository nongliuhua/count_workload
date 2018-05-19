#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml
import logging.config
import os
import sys
sys.path.append(".\log")

def setup_logging(default_path = "logging.yaml",default_level = logging.INFO,env_key = "LOG_CFG"):
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path,"r") as f:
            logging.config.dictConfig(yaml.load(f))
    else:
        print('could not fing logging.yaml')
        logging.basicConfig(level = default_level)

setup_logging(default_path=".\log\logging.yaml")
log = logging.getLogger("fileLogger")


# logger.info("aaaaaaaaaaa")
# logger.debug("debug debug .....")
# for i in range(10):
#     print (i)
#     logger.debug(i)