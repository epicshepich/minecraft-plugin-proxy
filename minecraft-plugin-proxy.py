'''
A proxy built on FastAPI to find the most recent version of a Minecraft plugin.
'''

import requests
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from xml.etree import ElementTree as ET

api = FastAPI()

@api.get('/viabackwards/velocity')
async def viabackwards_velocity():

    latest_release = requests.get(
        'https://hangar.papermc.io/api/v1/projects/ViaVersion/ViaBackwards/latestrelease'
    ).text.strip()
    return RedirectResponse(
        f'https://hangar.papermc.io/api/v1/projects/ViaVersion/ViaBackwards/versions/{latest_release}/Velocity/download'
    )

@api.get('/luckperms/{server_type}')
async def luckperms_velocity(server_type):
    
    luckperms_metadata = requests.get('https://metadata.luckperms.net/data/all').json()

    return RedirectResponse(
        luckperms_metadata['downloads'][server_type]
    )
    

@api.get('/tribufu-velocityrcon')
async def tribufu_velocityrcon():

    velocityrcon_metadata = requests.get('https://mvn.tribufu.com/releases/com/tribufu/Tribufu-VelocityRcon/maven-metadata.xml').text

    root = ET.fromstring(velocityrcon_metadata)
    version = root.find('.//versioning/latest').text

    return RedirectResponse(
        f'https://mvn.tribufu.com/releases/com/tribufu/Tribufu-VelocityRcon/{version}/Tribufu-VelocityRcon-{version}.jar'
    )