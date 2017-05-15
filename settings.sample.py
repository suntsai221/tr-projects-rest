# MONGO DATABASE SETTINGS
DATA_FORMAT = "a, %d %b %Y %H:%M:%S GMT+8"
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'keystone-test'
ASSETS_URL = 'http://stage.mirrormedia.mg/'
GCS_URL = 'https://storage.googleapis.com/mirrormedia-dev/'
ENV = 'dev'

# ALLOW ACTIONS
DEBUG = False
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE'] if DEBUG else ['GET']

slug_schema = {
  'slug': {
    'type': 'string',
  },
  'isCampaign': {
    'type': 'boolean',
  },
}

listing_schema = {
  'name': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'style': {
    'type': 'string',
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'sections': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'sections',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroVideo': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'isAdvertised': {
    'type': 'boolean',
  },
  'publishedDate': {
    'type': 'datetime',
  },
  'isCampaign': {
    'type': 'boolean',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  }
}

meta_schema = {
  'name': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'style': {
    'type': 'string',
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'sections': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'sections',
      'field': '_id',
      'embeddable': True
    },
  },
  'topics': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'topics',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'writers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': 'name',
            'embeddable': True
        },
    },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroVideo': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'relateds': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'isAdvertised': {
    'type': 'boolean',
  },
  'publishedDate': {
    'type': 'datetime',
  },
  'og_description': {
    'type': 'string',
  },
  'isCampaign': {
    'type': 'boolean',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  }
}

contact_schema = {
  'name': {
    'type': 'string',
  },
  'email': {
    'type': 'string',
    'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  },
  'homepage': {
    'type': 'string',
  },
  'facebook': {
    'type': 'string',
  },
  'twitter': {
    'type': 'string',
  },
  'instantgram': {
    'type': 'string',
  },
  'bio': {
    'type': 'string',
  },
  'image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
}

event_schema = {
  'name': {
    'type': 'string',
  },
  'state': {
    'type': 'string',
  },
  'eventType': {
    'type': 'string',
  },
  'startDate': {
    'type': 'datetime',
  },
  'endDate': {
    'type': 'datetime',
  },
  'embed': {
    'type': 'string',
  },
  'video': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'sections': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'sections',
            'field': '_id',
            'embeddable': True
        },
    },
  },
}

node_schema = {
  'name': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'heroVideo': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroCaption': {
    'type': 'string',
  },
  'state': {
    'type': 'string',
  },
  'nodeDate': {
    'type': 'datetime',
  },
  'createTime': {
    'type': 'datetime',
  },
  'updatedAt': {
    'type': 'datetime',
  },
  'activity': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'activities',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'content': {
    'type': 'dict',
    'schema': {
       "html": {
          "type": "string",
       },
     },  
  },
  'og_title': {
    'type': 'string',
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'og_description': {
    'type': 'string',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
}

post_schema = {
  'name': {
    'type': 'string',
  },
  'slug': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'subtitle': {
    'type': 'string',
  },
  'heroVideo': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroCaption': {
    'type': 'string',
  },
  'state': {
    'type': 'string',
  },
  'sections': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'sections',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'writers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'photographers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'camera_man': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'designers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'engineers': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'contacts',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'publishedDate': {
    'type': 'datetime',
  },
  'createTime': {
    'type': 'datetime',
  },
  'updatedAt': {
    'type': 'datetime',
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'topics': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'topics',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'topics_ref': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': 'topics',
            'embeddable': True
         },
     },
  },
  'tags': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'tags',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'style': {
    'type': 'string',
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'content': {
    'type': 'dict',
    'schema': {
       "html": {
          "type": "string",
       },
     },  
  },
  'relateds': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
  'extend_byline': {
    'type': 'string',
  },
  'og_title': {
    'type': 'string',
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'isAdvertised': {
    'type': 'boolean',
  },
  'lockJS': {
    'type': 'boolean',
  },
  'og_description': {
    'type': 'string',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'device': {
    'type': 'string',
  },
  'isCampaign': {
    'type': 'boolean',
  },
}

sections_schema = {
    'title': {
      'type': 'string',
    },
    'name': {
      'type': 'string',
    },
    'type': {
      'type': 'string',
      'allowed': ['articles', 'file', 'link']
    },
    'description': {
      'type': 'string',
    },
    'isFeatured': {
      'type': 'boolean',
    },
    'image': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'images',
        'field': '_id',
        'embeddable': True
      },
    },
    'heroImage': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'images',
        'field': '_id',
        'embeddable': True
      },
    },
    'categories': {
      'type': 'list',
      'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
       },
    },
    'extend_cats': {
      'type': 'list',
      'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
       },
    },
    'topics': {
      'type': 'list',
      'schema': {
          'type': 'objectid',
          'data_relation': {
              'resource': 'topics',
              'field': '_id',
              'embeddable': True
           },
       }, 
    },
    'style': {
      'type': 'string',
    },
    'og_title': {
      'type': 'string',
    },
    'og_description': {
      'type': 'string',
    },
    'og_image': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'images',
        'field': '_id',
        'embeddable': True
      },
    },
    'css': {
      'type': 'string',
    },
    'javascript': {
      'type': 'string',
    },
    'twitter': {
      'type': 'string',
    },
    'sortOrder': {
      'typr': 'integer',
    }
}

videos_schema = {
  'title': {
    'type': 'string',
  },
  'description': {
    'type': 'string',
  },
  'sections': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'sections',
            'field': '_id',
            'embeddable': True
        },
    },
  },
  'feed': {
    'type': 'boolean',
  },
  'categories': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'postcategories',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'video': {
    'type': 'dict',
    'schema': {
        'filetype': {
          'type': 'string',
        },
        'filename': {
          'type': 'string',
        },
        'originalname': {
          'type': 'string',
        },
        'path': {
          'type': 'string',
        },
        'projectId': {
          'type': 'string',
        },
        'size': {
          'type': 'string',
        },
        'url': {
          'type': 'string',
        },
    },
  },  
  'createTime': {
    'type': 'datetime',
  },
  'relateds': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
  'updatedAt': {
    'type': 'datetime',
  },
  'publishedDate': {
    'type': 'datetime',
  },
  'state': {
    'type': 'string',
  },
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  },
}

activities_schema = {
  'name': {
    'type': 'string',
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'heroVideo': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroCaption': {
    'type': 'string',
  },
  'topics': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'topics',
        'field': '_id',
        'embeddable': True
      },
    }, 
  },
  'og_title': {
    'type': 'string',
  },
  'og_description': {
    'type': 'string',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
}

postcategories_schema = {
  'name': {
    'type': 'string',
  },
  'title': {
    'type': 'string',
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'brief': {
    'type': 'dict',
    'schema': {
      "html": {
        "type": "string",
      },
    },
  },
  'heroVideo': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroCaption': {
    'type': 'string',
  },
  'og_title': {
    'type': 'string',
  },
  'og_description': {
    'type': 'string',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'isCampaign': {
    'type': 'boolean',
  },
  'style': {
    'type': 'string',
  },
  'css': {
    'type': 'string',
  },
  'javascript': {
    'type': 'string',
  }
}

audios_schema = {
  'title': {
    'type': 'string',
  },
  'description': {
    'type': 'string',
  },
  'audio': {
    'type': 'dict',
    'schema': {
        'filetype': {
          'type': 'string',
        },
        'filename': {
          'type': 'string',
        },
        'originalname': {
          'type': 'string',
        },
        'path': {
          'type': 'string',
        },
        'projectId': {
          'type': 'string',
        },
        'size': {
          'type': 'string',
        },
        'url': {
          'type': 'string',
        },
    },
  },  
  'coverPhoto': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  },
}

tags_schema = {
  'name': {
    'type': 'string',
  },
  'leading': {
    'type': 'string',
  },
  'heroVideo': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'og_title': {
    'type': 'string',
  },
  'og_description': {
    'type': 'string',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'style': {
    'type': 'string',
  },
  'css': {
    'type': 'string',
  },
  'javascript': {
    'type': 'string',
  },
  'sortOrder': {
    'typr': 'integer',
  },
  'sections': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'sections',
            'field': '_id',
            'embeddable': True
        },
    },
  },  
}

topics_schema = {
  'name': {
    'type': 'string',
  },
  'leading': {
    'type': 'string',
  },
  'type': {
    'type': 'string',
  },
  'source': {
    'type': 'string',
  },
  'state': {
    'type': 'string',
  },
  'sort': {
    'type': 'string',
  },
  'heroVideo': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'videos',
      'field': '_id',
      'embeddable': True
    },
  },
  'sections': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'sections',
            'field': '_id',
            'embeddable': True
        },
    },
  },  
  'heroImage': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'isFeatured': {
    'type': 'boolean',
  },
  'og_title': {
    'type': 'string',
  },
  'og_description': {
    'type': 'string',
  },
  'og_image': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'images',
      'field': '_id',
      'embeddable': True
    },
  },
  'style': {
    'type': 'string',
  },
  'javascript': {
    'type': 'string',
  },
  'dfp': {
    'type': 'string',
  },
  'mobile_dfp': {
    'type': 'string',
  },
  'sortOrder': {
    'typr': 'integer',
  }
}

choices_schema = {
  'pickDate': {
    'type': 'string',
  },
  'isPublished': {
    'type': 'boolean',
  },
  'choices': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'meta',
            'field': '_id',
            'embeddable': True
         },
     }, 
  },
}

image_schema = {
  'photographer': {
    'type': 'objectid',
    'data_relation': {
      'resource': 'contacts',
      'field': '_id',
      'embeddable': True
    },
  },
  'description': {
    'type': 'string',
  },
  'sale': {
    'type': 'Boolean',
  },
  'topics': {
    'type': 'list',
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'topics',
            'field': '_id',
            'embeddable': True
         },
     },
  },
  'tags': {
    'type': 'list',
    'schema': {
      'type': 'objectid',
      'data_relation': {
        'resource': 'tags',
        'field': '_id',
        'embeddable': True
      },
    },
  },
  'image': {
    'type': 'dict',
    'schema': {
      'artist': {
        'type': 'string',
      },
      'description': {
        'type': 'string',
      },
      'filename': {
        'type': 'string',
      },
      'filetype': {
        'type': 'string',
      },
      'height': {
        'type': 'number',
      },
      'width': {
        'type': 'number',
      },
      'size': {
        'type': 'number',
      },
      'url': {
        'type': 'string',
      }
    },
  },
  'createTime': {
    'type': 'datetime',
  },
}

posts = {
    'item_title': 'post',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'default_sort': [('publishedDate', -1)],
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': { '$or': [ { 'state': 'published' }, { 'state': 'invisible' } ] },
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['writers','photographers','camera_man','designers','engineers','heroImage', 'heroVideo', 'topics', 'sections', 'categories', 'tags', 'og_image', 'relateds'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': post_schema
}

nodes = {
    'item_title': 'node',
    'datasource': {
        'source': 'nodes',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['heroImage', 'heroVideo', 'activity', 'og_image'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': node_schema
}

slug = {
    'item_title': 'slug',
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': slug_schema
}

event = {
    'item_title': 'event',
    'datasource': {
        'source': 'events',
        'filter': {'state': 'published'},
        'default_sort': [('startDate', -1)],
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['image','sections', 'video'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': event_schema
}

listing = {
    'item_title': 'listing',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'default_sort': [('publishedDate', -1)],
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['heroImage', 'sections', 'writers', 'og_image', 'heroVideo','categories'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': listing_schema
}

meta = {
    'item_title': 'meta',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'default_sort': [('publishedDate', -1)],
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'published'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['heroImage','writers', 'topics','sections', 'categories','og_image', 'heroVideo', 'relateds'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': meta_schema
}

drafts = {
    'item_title': 'draft',
    'additional_lookup': {
        'url': 'regex("[\w-]+")',
        'default_sort': [('publishedDate', -1)],
        'field': 'slug'
    },
    'datasource': {
        'source': 'posts',
        'filter': {'state': 'draft'},
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['writers','photographers','designers','engineers','heroImage', 'heroVideo', 'topics', 'sections', 'categories', 'tags', 'og_image'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': post_schema
}

choices = {
    'item_title': 'choice',
    'datasource': {
        'source': 'choices',
        'filter': {'isPublished': True},
    },
    'embedded_fields': ['choices'],
    'resource_methods': ['GET'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': choices_schema
}

topics = {
    'item_title': 'topic',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'datasource': {
        'source': 'topics',
        'filter': {'state': 'published'},
        'default_sort': [('sortOrder', 1)],
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['heroImage', 'heroVideo', 'og_image'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': topics_schema
}

tags = {
    'item_title': 'tag',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['heroImage', 'heroVideo', 'og_image', 'sections'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': tags_schema
}

contacts = {
  'item_title': 'contact',
  'additional_lookup': {
    'url': 'regex(".+")',
    'field': 'name'
  },
  'resource_methods': ['GET'],
  'cache_control': 'max-age=1500,must-revalidate',
  'cache_expires': 1500,
  'allow_unknown': False,
  'embedded_fields': ['image'],
  'schema': contact_schema
}

postcategories = {
    'item_title': 'postcategory',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': postcategories_schema,
}

activities = {
    'item_title': 'activity',
    'resource_methods': ['GET'],
    'embedded_fields': ['heroImage', 'heroVideo', 'topics'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': activities_schema,
}

sections = {
    'item_title': 'section',
    'additional_lookup': {
        'url': 'regex(".+")',
        'field': 'name'
    },
    'resource_methods': ['GET'],
    'embedded_fields': ['categories', 'heroImage', 'image', 'extend_cats', 'topics'],
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'allow_unknown': False,
    'schema': sections_schema,
}

images = {
    'resource_methods': ['GET'],
    'datasource': {'default_sort': [('createTime', -1)]},
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'schema': image_schema,
}

audios = {
    'resource_methods': ['GET'],
    'cache_control': 'max-age=1500,must-revalidate',
    'embedded_fields': ['coverPhoto'],
    'cache_expires': 1500,
    'schema': audios_schema,
}

videos = {
    'resource_methods': ['GET'],
    'datasource': {
        'source': 'videos',
        'filter': {'state': 'published'},
    },
    'cache_control': 'max-age=1500,must-revalidate',
    'cache_expires': 1500,
    'embedded_fields': ['categories', 'sections', 'tags', 'relateds'],
    'schema': videos_schema,
}

DOMAIN = {
    'posts': posts,
    'drafts': drafts,
    'meta': meta,
    'listing': listing,
    'slug': slug,
    'tags': tags,
    'choices': choices,
    'contacts': contacts,
    'topics': topics,
    'nodes': nodes,
    'postcategories': postcategories,
    'activities': activities,
    'images': images,
    'audios': audios,
    'videos': videos,
    'event': event,
    'sections': sections,
    }

XML = False
IF_MATCH = False
X_DOMAINS = '*'
X_HEADERS = ['Content-Type']
PAGINATION_DEFAULT = 10
