from random import random
import re
import numpy as np
from lxml import etree


def generateRandomKey():
    return np.base_repr(int(np.floor(random() * 2 ** 24)), 32).lower()


def convert_html_to_draft(html):
    """

    :param html: string
    :return: data: dict
    """
    if html:
        if html.startswith('"'):
            html = str(html[1:-1])

        apiData = []
        entityMap = {}
        blocks = []

        parsed_html = etree.HTML(html)
        all_leaf_nodes = parsed_html.xpath('//*[not(*)]')

        for i, item in enumerate(all_leaf_nodes):

            if item.tag == 'p':
                p(apiData, blocks, item)
            elif item.tag == 'a':
                a(apiData, blocks, entityMap, i, item)

            elif item.tag == 'img':
                img(blocks, entityMap, i, item)

            elif item.tag == 'iframe':
                iframe(blocks, entityMap, i, item)

            elif item.tag == 'h1':
                h1(apiData, blocks, item)

            elif item.tag == 'h2':
                h2(apiData, blocks, item)

            elif item.tag == 'code':
                code(apiData, blocks, item)

            elif item.tag == 'blockquote':
                blockquote(apiData, blocks, item)

            elif item.tag == 'li':
                li(apiData, blocks, item)

            elif item.tag == 'br':
                pass
            else:
                continue

        data = {"draft": {"blocks": blocks, "entityMap": entityMap},
                "html": html,
                "apiData": apiData
                }
        return data

    else:
        print("No Image")
        pass


def img(blocks, entityMap, i, item):
    imgsrc = item.xpath('@src')[0]
    if imgsrc:
        # print(f"Image got: {imgsrc}")
        if imgsrc.startswith('/assets'):
            imgsrc = f"https://www.readr.tw{imgsrc}"
        else:
            entityMap.update({str(i): {
                "type": "EMBEDDEDCODE",
                "mutability": "IMMUTABLE",
                "data":
                    {"code": f'<img src={imgsrc}>',
                     "alignment": "center"}
            }})

            blocks.append(
                {
                    "key": generateRandomKey(),
                    "text": " ",
                    "type": "unstyled",
                    "depth": 0,
                    "inlineStyleRanges": [
                    ],
                    "entityRanges": [
                        {
                            "offset": 0,
                            "length": 1,
                            "key": i
                        }
                    ],
                    "data": {}
                }
            )
    else:
        raise ValueError(f"Image is missing, not found src {imgsrc}")


def iframe(blocks, entityMap, i, item):
    key = generateRandomKey()
    iframe_src = item.xpath('@src')[0]
    print(iframe_src)
    blocks.append(
        {
            "key": key,
            "text": " ",
            "type": "atomic",
            "depth": 0,
            "inlineStyleRanges": [
            ],
            "entityRanges": [
                {
                    "offset": 0,
                    "length": 1,
                    "key": i
                }
            ],
            "data": {}
        }
    )
    entityMap.update(
        {str(i): {
            "type": "EMBEDDEDCODE",
            "mutability": "IMMUTABLE",
            "data":
                {
                    "code": f'<iframe src={iframe_src} frameborder="0" scrolling="no" style="width:100%;height:600px;" allowfullscreen="allowfullscreen"></iframe>',
                    "alignment": "center"}
        }}
    )


def p(apiData, blocks, item):
    random_key = generateRandomKey()
    blocks.append({
        "key": random_key,
        "text": item.text,
        "type": "unstyled",
        "depth": 0,
        # "inlineStyleRanges": [{"offset": 0, "length": len(item.text)}],
        "inlineStyleRanges": [],
        "entityRanges": [
        ],
        "data": {}
    })
    apiData.append(
        {
            "id": random_key,
            "type": "unstyled",
            "alignment": "center",
            "content": [
                etree.tostring(item)
            ],
            "styles": {
            }
        }
    )


def a(apiData, blocks, entityMap, i, item):
    random_key = generateRandomKey()
    link = item.xpath('@href')[0]
    parent = item.getparent()
    text_list = [text for text in parent.itertext()]  # generator
    index_in_list = text_list.index(item.text)
    block = {
        "key": random_key,
        "text": ''.join(text_list),
        "type": "unstyled",
        "depth": 0,
        "inlineStyleRanges": [
        ],
        "entityRanges": [
            {
                "offset": len(''.join(text_list[:index_in_list])),
                "length": len(item.text),
                "key": i
            }
        ],
        "data": {"url": link}
    }
    entityMap.update({str(i): {
        "type": "LINK",
        "mutability": "MUTABLE",
        "data": {"url": link, "targetOption": "_self"}
    }})
    blocks.append(block)
    apiData.append(
        {
            "id": random_key,
            "type": "unstyled",
            "alignment": "center",
            "content": [
                etree.tostring(parent)
            ],
            "styles": {
            }
        }
    )


def h1(apiData, blocks, item):
    _type = "header-one"
    random_key = generateRandomKey()
    blocks.append({
        "key": random_key,
        "text": item.text,
        "type": _type,
        "depth": 0,
        "inlineStyleRanges": [
        ],
        "entityRanges": [
        ],
        "data": {}
    })
    apiData.append(
        {
            "id": random_key,
            "type": _type,
            "alignment": "center",
            "content": [
                etree.tostring(item)
            ],
            "styles": {
            }
        }
    )


def h2(apiData, blocks, item):
    _type = "header-two"
    random_key = generateRandomKey()
    blocks.append({
        "key": random_key,
        "text": item.text,
        "type": _type,
        "depth": 0,
        "inlineStyleRanges": [
        ],
        "entityRanges": [
        ],
        "data": {}
    })
    apiData.append(
        {
            "id": random_key,
            "type": _type,
            "alignment": "center",
            "content": [
                etree.tostring(item)
            ],
            "styles": {
            }
        }
    )


def code(apiData, blocks, item):
    random_key = generateRandomKey()
    blocks.append({
        "key": random_key,
        "text": item.text,
        "type": "code-block",
        "depth": 0,
        "inlineStyleRanges": [
        ],
        "entityRanges": [
        ],
        "data": {}
    })
    apiData.append(
        {
            "id": random_key,
            "type": "code-block",
            "alignment": "center",
            "content": [
                etree.tostring(item)
            ],
            "styles": {
            }
        }
    )


def blockquote(apiData, blocks, item):
    random_key = generateRandomKey()
    blocks.append({
        "key": random_key,
        "text": item.text,
        "type": "blockquote",
        "depth": 0,
        "inlineStyleRanges": [
        ],
        "entityRanges": [
        ],
        "data": {}
    })
    apiData.append(
        {
            "id": random_key,
            "type": "blockquote",
            "alignment": "center",
            "content": [
                etree.tostring(item)
            ],
            "styles": {
            }
        }
    )


def li(apiData, blocks, item):
    random_key = generateRandomKey()
    if item.getparent().tag == 'ol':
        blocks.append({
            "key": random_key,
            "text": item.text,
            "type": "ordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [
            ],
            "entityRanges": [
            ],
            "data": {}
        })

        apiData.append(
            {
                "id": random_key,
                "type": "ordered-list-item",
                "alignment": "center",
                "content": [
                    etree.tostring(item)
                ],
                "styles": {
                }
            }
        )
    elif item.getparent().tag == 'ul':
        blocks.append({
            "key": random_key,
            "text": item.text,
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        })
    apiData.append(
        {
            "id": random_key,
            "type": "unordered-list-item",
            "alignment": "center",
            "content": [
                etree.tostring(item)
            ],
            "styles": {
            }
        }
    )


def text_to_draft(text: str):
    pattern = "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    url_regex = re.compile(pattern)
    for url in re.findall(url_regex, text):
        text = text.replace(url[0], '<a href="%(url)s">%(url)s</a>' % {"url": url[0]})

    paragraphs = text.split('\n\n\n')
    text = ''.join("<p>" + paragraph + "</p>" for paragraph in paragraphs)

    draft = convert_html_to_draft(text)
    return draft
