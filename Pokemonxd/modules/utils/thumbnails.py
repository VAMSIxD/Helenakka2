# Powered By @Pokemonxd

import os
import re
import textwrap

import aiofiles
import aiohttp
import numpy as np
import random

from PIL import Image, ImageChops, ImageOps, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

from Pokemonxd.utilities.config import YOUTUBE_IMG_URL
from Pokemonxd.resource import thumbs, colors



def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def add_corners(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)


async def gen_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open("cache/thumbx.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("cache/thumbx.png")
    image2 = Image.open(f"Pokemonxd/resource/amala.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image3.convert("RGBA")
    background = image5.filter(filter=ImageFilter.BoxBlur(30))
    enhancer = ImageEnhance.Brightness(background)
    background = enhancer.enhance(0.6)
    background.save("cache/blur_image.png")

    Xcenter = image3.width / 2
    Ycenter = image3.height / 2
    x1 = Xcenter - 250
    y1 = Ycenter - 250
    x2 = Xcenter + 250
    y2 = Ycenter + 250

    logo = image3.crop((x1, y1, x2, y2))
    logo.thumbnail((520, 520), Image.ANTIALIAS)
    logo.save(f"cache/temp.png")
    if not os.path.isfile(f"cache/circle.png"):
        im = Image.open(f"cache/temp.png").convert("RGBA")
        add_corners(im)
        im.save(f"cache/circle.png")

    image7 = Image.open(f"cache/circle.png")
    image8 = image7.convert("RGBA")
    image8.thumbnail((365, 365), Image.ANTIALIAS)
    width = int((1280 - 365) / 2)
    background = Image.open("cache/blur_image.png")
    background.paste(image8, (width + 2, 138), mask=image8)
    background.paste(image4, (0, 0), mask=image4)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Pokemonxd/resource/font2.ttf", 45)
    ImageFont.truetype("Pokemonxd/resource/font2.ttf", 70)
    arial = ImageFont.truetype("Pokemonxd/resource/font2.ttf", 30)
    ImageFont.truetype("resource/font.ttf", 30)

    para = textwrap.wrap(title, width=32)
    try:
        draw.text(
            (450, 35),
            f"STARTED PLAYING",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        if para[0]:
            text_w, text_h = draw.textsize(f"{para[0]}", font=font)
            draw.text(
                ((1280 - text_w) / 2, 560),
                f"{para[0]}",
                fill="white",
                stroke_width=1,
                stroke_fill="white",
                font=font,
            )
        if para[1]:
            text_w, text_h = draw.textsize(f"{para[1]}", font=font)
            draw.text(
                ((1280 - text_w) / 2, 610),
                f"{para[1]}",
                fill="white",
                stroke_width=1,
                stroke_fill="white",
                font=font,
            )
    except:
        pass
    text_w, text_h = draw.textsize(f"Duration: {duration} Mins", font=arial)
    draw.text(
        ((1280 - text_w) / 2, 665),
        f"Duration: {duration} Mins",
        fill="white",
        font=arial,
    )
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        img.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL

