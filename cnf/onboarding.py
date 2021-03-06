#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0

import logging

import time
import zipfile
from io import BytesIO

import oyaml as yaml

from config import Config
from onapsdk.sdc.properties import Property

from onapsdk.sdc.vendor import Vendor
from onapsdk.sdc.vsp import Vsp
from onapsdk.sdc.vf import Vf
from onapsdk.sdc.service import Service, ServiceInstantiationType

import os

logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
fh = logging.StreamHandler()
fh_formatter = logging.Formatter('%(asctime)s %(levelname)s %(lineno)d:%(filename)s(%(process)d) - %(message)s')
fh.setFormatter(fh_formatter)
logger.addHandler(fh)

# Read SDNC MODEL NAME and VERSION from CBA.zip
logger.info("*******************************")
logger.info("Retrieving SDNC MODEL NAME and VERSION")
logger.info("*******************************")
with zipfile.ZipFile(Config.VSPFILE, 'r') as package:
    cba_io = BytesIO(package.read("CBA.zip"))
    with zipfile.ZipFile(cba_io) as cba:
        with cba.open('TOSCA-Metadata/TOSCA.meta') as meta_file:
            tosca_meta = yaml.load(meta_file, Loader=yaml.FullLoader)
            SDNC_MODEL_NAME = tosca_meta.get("Template-Name")
            SDNC_MODEL_VERSION = tosca_meta.get("Template-Version")

logger.info("*******************************")
logger.info("******** SERVICE DESIGN *******")
logger.info("*******************************")

logger.info("******** Onboard Vendor *******")
vendor = Vendor(name=Config.VENDOR)
vendor.onboard()

logger.info("******** Onboard VSP *******")
mypath = os.path.dirname(os.path.realpath(__file__))
myvspfile = os.path.join(mypath, Config.VSPFILE)
vsp = Vsp(name=Config.VSPNAME, vendor=vendor, package=open(myvspfile, 'rb'))
vsp.onboard()

logger.info("******** Onboard VF *******")
vf = Vf(name=Config.VFNAME, properties=[
    Property(name="sdnc_model_name", property_type="string", value=SDNC_MODEL_NAME),
    Property(name="sdnc_model_version", property_type="string", value=SDNC_MODEL_VERSION),
    Property(name="sdnc_artifact_name", property_type="string", value=Config.SDNC_ARTIFACT_NAME)
]
        )
vf.vsp = vsp
vf.onboard()

logger.info("******** Onboard Service *******")
svc = Service(name=Config.SERVICENAME, resources=[vf], instantiation_type=ServiceInstantiationType.MACRO)
svc.onboard()

logger.info("******** Check Service Distribution *******")
distribution_completed = False
nb_try = 0
nb_try_max = 10
while distribution_completed is False and nb_try < nb_try_max:
    distribution_completed = svc.distributed
    if distribution_completed is True:
        logger.info("Service Distribution for %s is successfully finished", svc.name)
        break
    logger.info("Service Distribution for %s ongoing, Wait for 60 s", svc.name)
    time.sleep(60)
    nb_try += 1

if distribution_completed is False:
    logger.error("Service Distribution for %s failed !!", svc.name)
    exit(1)

