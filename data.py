import pprint

response = {
    "data": {
        "threaded_conversation_with_injections_v2": {
            "instructions": [
                {
                    "type": "TimelineAddEntries",
                    "entries": [
                        {
                            "entryId": "tweet-1838791842361430148",
                            "sortIndex": "7384580194493345659",
                            "content": {
                                "entryType": "TimelineTimelineItem",
                                "__typename": "TimelineTimelineItem",
                                "itemContent": {
                                    "itemType": "TimelineTweet",
                                    "__typename": "TimelineTweet",
                                    "tweet_results": {
                                        "result": {
                                            "__typename": "Tweet",
                                            "rest_id": "1838791842361430148",
                                            "has_birdwatch_notes": False,
                                            "core": {
                                                "user_results": {
                                                    "result": {
                                                        "__typename": "User",
                                                        "id": "VXNlcjo3NzE5NzA0MTQxNTUxODIwODE=",
                                                        "rest_id": "771970414155182081",
                                                        "affiliates_highlighted_label": {},
                                                        "has_graduated_access": True,
                                                        "is_blue_verified": True,
                                                        "profile_image_shape": "Circle",
                                                        "legacy": {
                                                            "following": False,
                                                            "can_dm": True,
                                                            "can_media_tag": True,
                                                            "created_at": "Sat Sep 03 07:17:44 +0000 2016",
                                                            "default_profile": True,
                                                            "default_profile_image": False,
                                                            "description": "President @comma_ai. Founder @__tinygrad__",
                                                            "entities": {
                                                                "description": {
                                                                    "urls": []
                                                                },
                                                                "url": {
                                                                    "urls": [
                                                                        {
                                                                            "display_url": "1m2019.com",
                                                                            "expanded_url": "http://1m2019.com/",
                                                                            "url": "https://t.co/jjCk5yFUcy",
                                                                            "indices": [
                                                                                0,
                                                                                23,
                                                                            ],
                                                                        }
                                                                    ]
                                                                },
                                                            },
                                                            "fast_followers_count": 0,
                                                            "favourites_count": 25,
                                                            "followers_count": 268843,
                                                            "friends_count": 189,
                                                            "has_custom_timelines": True,
                                                            "is_translator": False,
                                                            "listed_count": 1804,
                                                            "location": "San Diego, CA",
                                                            "media_count": 18,
                                                            "name": "George Hotz 🌑",
                                                            "normal_followers_count": 268843,
                                                            "pinned_tweet_ids_str": [],
                                                            "possibly_sensitive": False,
                                                            "profile_banner_url": "https://pbs.twimg.com/profile_banners/771970414155182081/1472975904",
                                                            "profile_image_url_https": "https://pbs.twimg.com/profile_images/772342671721455616/FE79-7Ev_normal.jpg",
                                                            "profile_interstitial_type": "",
                                                            "screen_name": "realGeorgeHotz",
                                                            "statuses_count": 159,
                                                            "translator_type": "none",
                                                            "url": "https://t.co/jjCk5yFUcy",
                                                            "verified": False,
                                                            "want_retweets": False,
                                                            "withheld_in_countries": [],
                                                        },
                                                        "professional": {
                                                            "rest_id": "1593098633032843264",
                                                            "professional_type": "Creator",
                                                            "category": [],
                                                        },
                                                        "tipjar_settings": {},
                                                        "verified_phone_status": False,
                                                    }
                                                }
                                            },
                                            "unmention_data": {},
                                            "edit_control": {
                                                "edit_tweet_ids": [
                                                    "1838791842361430148"
                                                ],
                                                "editable_until_msecs": "1727240712000",
                                                "is_edit_eligible": True,
                                                "edits_remaining": "5",
                                            },
                                            "is_translatable": False,
                                            "views": {
                                                "count": "110760",
                                                "state": "EnabledWithCount",
                                            },
                                            "source": '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
                                            "quoted_status_result": {
                                                "result": {
                                                    "__typename": "Tweet",
                                                    "rest_id": "1836929941654417861",
                                                    "has_birdwatch_notes": False,
                                                    "core": {
                                                        "user_results": {
                                                            "result": {
                                                                "__typename": "User",
                                                                "id": "VXNlcjoyMzkxMzIwODUy",
                                                                "rest_id": "2391320852",
                                                                "affiliates_highlighted_label": {},
                                                                "has_graduated_access": True,
                                                                "is_blue_verified": False,
                                                                "profile_image_shape": "Circle",
                                                                "legacy": {
                                                                    "following": False,
                                                                    "can_dm": False,
                                                                    "can_media_tag": True,
                                                                    "created_at": "Sat Mar 15 16:47:24 +0000 2014",
                                                                    "default_profile": True,
                                                                    "default_profile_image": False,
                                                                    "description": "AI researcher ||\nIIT Tirupati || Toshiba R & D",
                                                                    "entities": {
                                                                        "description": {
                                                                            "urls": []
                                                                        }
                                                                    },
                                                                    "fast_followers_count": 0,
                                                                    "favourites_count": 10074,
                                                                    "followers_count": 55,
                                                                    "friends_count": 310,
                                                                    "has_custom_timelines": True,
                                                                    "is_translator": False,
                                                                    "listed_count": 1,
                                                                    "location": "",
                                                                    "media_count": 43,
                                                                    "name": "Bhasker Sri Harsha",
                                                                    "normal_followers_count": 55,
                                                                    "pinned_tweet_ids_str": [],
                                                                    "possibly_sensitive": False,
                                                                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/2391320852/1637149209",
                                                                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1460935280995680258/dwuEmiVT_normal.jpg",
                                                                    "profile_interstitial_type": "",
                                                                    "screen_name": "BhaskerSriHarsh",
                                                                    "statuses_count": 575,
                                                                    "translator_type": "none",
                                                                    "verified": False,
                                                                    "want_retweets": False,
                                                                    "withheld_in_countries": [],
                                                                },
                                                                "tipjar_settings": {},
                                                                "verified_phone_status": False,
                                                            }
                                                        }
                                                    },
                                                    "unmention_data": {},
                                                    "edit_control": {
                                                        "edit_tweet_ids": [
                                                            "1836929941654417861"
                                                        ],
                                                        "editable_until_msecs": "1726796801000",
                                                        "is_edit_eligible": True,
                                                        "edits_remaining": "5",
                                                    },
                                                    "is_translatable": False,
                                                    "views": {
                                                        "count": "121516",
                                                        "state": "EnabledWithCount",
                                                    },
                                                    "source": '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
                                                    "legacy": {
                                                        "bookmark_count": 23,
                                                        "bookmarked": False,
                                                        "created_at": "Fri Sep 20 00:46:41 +0000 2024",
                                                        "conversation_id_str": "1836929941654417861",
                                                        "display_text_range": [0, 231],
                                                        "entities": {
                                                            "hashtags": [],
                                                            "media": [
                                                                {
                                                                    "display_url": "pic.x.com/o1zaaxed3p",
                                                                    "expanded_url": "https://twitter.com/BhaskerSriHarsh/status/1836929941654417861/photo/1",
                                                                    "id_str": "1836929928563941377",
                                                                    "indices": [
                                                                        232,
                                                                        255,
                                                                    ],
                                                                    "media_key": "3_1836929928563941377",
                                                                    "media_url_https": "https://pbs.twimg.com/media/GX4WCZ1WYAEvlKw.jpg",
                                                                    "type": "photo",
                                                                    "url": "https://t.co/o1zAAXed3P",
                                                                    "ext_media_availability": {
                                                                        "status": "Available"
                                                                    },
                                                                    "features": {
                                                                        "large": {
                                                                            "faces": []
                                                                        },
                                                                        "medium": {
                                                                            "faces": []
                                                                        },
                                                                        "small": {
                                                                            "faces": []
                                                                        },
                                                                        "orig": {
                                                                            "faces": []
                                                                        },
                                                                    },
                                                                    "sizes": {
                                                                        "large": {
                                                                            "h": 2048,
                                                                            "w": 922,
                                                                            "resize": "fit",
                                                                        },
                                                                        "medium": {
                                                                            "h": 1200,
                                                                            "w": 540,
                                                                            "resize": "fit",
                                                                        },
                                                                        "small": {
                                                                            "h": 680,
                                                                            "w": 306,
                                                                            "resize": "fit",
                                                                        },
                                                                        "thumb": {
                                                                            "h": 150,
                                                                            "w": 150,
                                                                            "resize": "crop",
                                                                        },
                                                                    },
                                                                    "original_info": {
                                                                        "height": 2048,
                                                                        "width": 922,
                                                                        "focus_rects": [
                                                                            {
                                                                                "x": 0,
                                                                                "y": 202,
                                                                                "w": 922,
                                                                                "h": 516,
                                                                            },
                                                                            {
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 922,
                                                                                "h": 922,
                                                                            },
                                                                            {
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 922,
                                                                                "h": 1051,
                                                                            },
                                                                            {
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 922,
                                                                                "h": 1844,
                                                                            },
                                                                            {
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 922,
                                                                                "h": 2048,
                                                                            },
                                                                        ],
                                                                    },
                                                                    "media_results": {
                                                                        "result": {
                                                                            "media_key": "3_1836929928563941377"
                                                                        }
                                                                    },
                                                                }
                                                            ],
                                                            "symbols": [],
                                                            "timestamps": [],
                                                            "urls": [],
                                                            "user_mentions": [
                                                                {
                                                                    "id_str": "1674187388825006082",
                                                                    "name": "the tiny corp",
                                                                    "screen_name": "__tinygrad__",
                                                                    "indices": [21, 34],
                                                                },
                                                                {
                                                                    "id_str": "771970414155182081",
                                                                    "name": "George Hotz 🌑",
                                                                    "screen_name": "realGeorgeHotz",
                                                                    "indices": [
                                                                        142,
                                                                        157,
                                                                    ],
                                                                },
                                                            ],
                                                        },
                                                        "extended_entities": {
                                                            "media": [
                                                                {
                                                                    "display_url": "pic.x.com/o1zaaxed3p",
                                                                    "expanded_url": "https://twitter.com/BhaskerSriHarsh/status/1836929941654417861/photo/1",
                                                                    "id_str": "1836929928563941377",
                                                                    "indices": [
                                                                        232,
                                                                        255,
                                                                    ],
                                                                    "media_key": "3_1836929928563941377",
                                                                    "media_url_https": "https://pbs.twimg.com/media/GX4WCZ1WYAEvlKw.jpg",
                                                                    "type": "photo",
                                                                    "url": "https://t.co/o1zAAXed3P",
                                                                    "ext_media_availability": {
                                                                        "status": "Available"
                                                                    },
                                                                    "features": {
                                                                        "large": {
                                                                            "faces": []
                                                                        },
                                                                        "medium": {
                                                                            "faces": []
                                                                        },
                                                                        "small": {
                                                                            "faces": []
                                                                        },
                                                                        "orig": {
                                                                            "faces": []
                                                                        },
                                                                    },
                                                                    "sizes": {
                                                                        "large": {
                                                                            "h": 2048,
                                                                            "w": 922,
                                                                            "resize": "fit",
                                                                        },
                                                                        "medium": {
                                                                            "h": 1200,
                                                                            "w": 540,
                                                                            "resize": "fit",
                                                                        },
                                                                        "small": {
                                                                            "h": 680,
                                                                            "w": 306,
                                                                            "resize": "fit",
                                                                        },
                                                                        "thumb": {
                                                                            "h": 150,
                                                                            "w": 150,
                                                                            "resize": "crop",
                                                                        },
                                                                    },
                                                                    "original_info": {
                                                                        "height": 2048,
                                                                        "width": 922,
                                                                        "focus_rects": [
                                                                            {
                                                                                "x": 0,
                                                                                "y": 202,
                                                                                "w": 922,
                                                                                "h": 516,
                                                                            },
                                                                            {
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 922,
                                                                                "h": 922,
                                                                            },
                                                                            {
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 922,
                                                                                "h": 1051,
                                                                            },
                                                                            {
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 922,
                                                                                "h": 1844,
                                                                            },
                                                                            {
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 922,
                                                                                "h": 2048,
                                                                            },
                                                                        ],
                                                                    },
                                                                    "media_results": {
                                                                        "result": {
                                                                            "media_key": "3_1836929928563941377"
                                                                        }
                                                                    },
                                                                }
                                                            ]
                                                        },
                                                        "favorite_count": 266,
                                                        "favorited": False,
                                                        "full_text": 'The best thing about @__tinygrad__ website is that they straight up reveal how much each box costs.\n\nNo goofy "contact sales" garbage.\n\nAlso, @realGeorgeHotz your HTML skills are 🔥🔥.\n\nHmmm. Hoping to be able to afford this someday. https://t.co/o1zAAXed3P',
                                                        "is_quote_status": False,
                                                        "lang": "en",
                                                        "possibly_sensitive": False,
                                                        "possibly_sensitive_editable": True,
                                                        "quote_count": 4,
                                                        "reply_count": 8,
                                                        "retweet_count": 7,
                                                        "retweeted": False,
                                                        "user_id_str": "2391320852",
                                                        "id_str": "1836929941654417861",
                                                    },
                                                }
                                            },
                                            "legacy": {
                                                "bookmark_count": 186,
                                                "bookmarked": False,
                                                "created_at": "Wed Sep 25 04:05:12 +0000 2024",
                                                "conversation_id_str": "1838791842361430148",
                                                "display_text_range": [0, 272],
                                                "entities": {
                                                    "hashtags": [],
                                                    "symbols": [],
                                                    "timestamps": [],
                                                    "urls": [],
                                                    "user_mentions": [],
                                                },
                                                "favorite_count": 1455,
                                                "favorited": False,
                                                "full_text": "Whenever you see \"contact sales\" there's likely a better option elsewhere.\n\nCompanies put that when they either want to price discriminate (which should be illegal) or when they believe they need a person to get you to convert.\n\nDon't do business with losers, just say no.",
                                                "is_quote_status": True,
                                                "lang": "en",
                                                "quote_count": 9,
                                                "quoted_status_id_str": "1836929941654417861",
                                                "quoted_status_permalink": {
                                                    "url": "https://t.co/pr4VufZl6S",
                                                    "expanded": "https://twitter.com/BhaskerSriHarsh/status/1836929941654417861",
                                                    "display": "x.com/BhaskerSriHars…",
                                                },
                                                "reply_count": 64,
                                                "retweet_count": 69,
                                                "retweeted": False,
                                                "user_id_str": "771970414155182081",
                                                "id_str": "1838791842361430148",
                                            },
                                            "quick_promote_eligibility": {
                                                "eligibility": "IneligibleNotProfessional"
                                            },
                                        }
                                    },
                                    "tweetDisplayType": "Tweet",
                                    "hasModeratedReplies": False,
                                },
                            },
                        },
                        {
                            "entryId": "conversationthread-1838800733292105957",
                            "sortIndex": "7384580194493345649",
                            "content": {
                                "entryType": "TimelineTimelineModule",
                                "__typename": "TimelineTimelineModule",
                                "items": [
                                    {
                                        "entryId": "conversationthread-1838800733292105957-tweet-1838800733292105957",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838800733292105957",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjoyNzg2MjQ5NTE=",
                                                                    "rest_id": "278624951",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": True,
                                                                        "created_at": "Thu Apr 07 16:54:38 +0000 2011",
                                                                        "default_profile": True,
                                                                        "default_profile_image": False,
                                                                        "description": "Formerly built the fastest filesystem in the world at AWS, now building the fastest spreadsheet at https://t.co/hLkbCuJG7H",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": [
                                                                                    {
                                                                                        "display_url": "rowzero.com",
                                                                                        "expanded_url": "http://rowzero.com",
                                                                                        "url": "https://t.co/hLkbCuJG7H",
                                                                                        "indices": [
                                                                                            99,
                                                                                            122,
                                                                                        ],
                                                                                    }
                                                                                ]
                                                                            },
                                                                            "url": {
                                                                                "urls": [
                                                                                    {
                                                                                        "display_url": "grantslatton.com",
                                                                                        "expanded_url": "https://grantslatton.com",
                                                                                        "url": "https://t.co/LjlRrCZTYZ",
                                                                                        "indices": [
                                                                                            0,
                                                                                            23,
                                                                                        ],
                                                                                    }
                                                                                ]
                                                                            },
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 16118,
                                                                        "followers_count": 8887,
                                                                        "friends_count": 701,
                                                                        "has_custom_timelines": True,
                                                                        "is_translator": False,
                                                                        "listed_count": 129,
                                                                        "location": "Seattle, WA",
                                                                        "media_count": 462,
                                                                        "name": "Grant Slatton",
                                                                        "normal_followers_count": 8887,
                                                                        "pinned_tweet_ids_str": [],
                                                                        "possibly_sensitive": False,
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1809298505330262016/fSGwXuzT_normal.jpg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "GrantSlatton",
                                                                        "statuses_count": 5950,
                                                                        "translator_type": "none",
                                                                        "url": "https://t.co/LjlRrCZTYZ",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838800733292105957"
                                                            ],
                                                            "editable_until_msecs": "1727242832000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "2143",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
                                                        "legacy": {
                                                            "bookmark_count": 8,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 04:40:32 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                16,
                                                                75,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "media": [
                                                                    {
                                                                        "display_url": "pic.x.com/sdx6p73slm",
                                                                        "expanded_url": "https://twitter.com/GrantSlatton/status/1838800733292105957/photo/1",
                                                                        "id_str": "1838800730570002434",
                                                                        "indices": [
                                                                            76,
                                                                            99,
                                                                        ],
                                                                        "media_key": "3_1838800730570002434",
                                                                        "media_url_https": "https://pbs.twimg.com/media/GYS7haZakAIYUfj.jpg",
                                                                        "type": "photo",
                                                                        "url": "https://t.co/Sdx6P73SlM",
                                                                        "ext_media_availability": {
                                                                            "status": "Available"
                                                                        },
                                                                        "features": {
                                                                            "large": {
                                                                                "faces": []
                                                                            },
                                                                            "medium": {
                                                                                "faces": []
                                                                            },
                                                                            "small": {
                                                                                "faces": []
                                                                            },
                                                                            "orig": {
                                                                                "faces": []
                                                                            },
                                                                        },
                                                                        "sizes": {
                                                                            "large": {
                                                                                "h": 928,
                                                                                "w": 1142,
                                                                                "resize": "fit",
                                                                            },
                                                                            "medium": {
                                                                                "h": 928,
                                                                                "w": 1142,
                                                                                "resize": "fit",
                                                                            },
                                                                            "small": {
                                                                                "h": 553,
                                                                                "w": 680,
                                                                                "resize": "fit",
                                                                            },
                                                                            "thumb": {
                                                                                "h": 150,
                                                                                "w": 150,
                                                                                "resize": "crop",
                                                                            },
                                                                        },
                                                                        "original_info": {
                                                                            "height": 928,
                                                                            "width": 1142,
                                                                            "focus_rects": [
                                                                                {
                                                                                    "x": 0,
                                                                                    "y": 0,
                                                                                    "w": 1142,
                                                                                    "h": 640,
                                                                                },
                                                                                {
                                                                                    "x": 0,
                                                                                    "y": 0,
                                                                                    "w": 928,
                                                                                    "h": 928,
                                                                                },
                                                                                {
                                                                                    "x": 21,
                                                                                    "y": 0,
                                                                                    "w": 814,
                                                                                    "h": 928,
                                                                                },
                                                                                {
                                                                                    "x": 196,
                                                                                    "y": 0,
                                                                                    "w": 464,
                                                                                    "h": 928,
                                                                                },
                                                                                {
                                                                                    "x": 0,
                                                                                    "y": 0,
                                                                                    "w": 1142,
                                                                                    "h": 928,
                                                                                },
                                                                            ],
                                                                        },
                                                                        "media_results": {
                                                                            "result": {
                                                                                "media_key": "3_1838800730570002434"
                                                                            }
                                                                        },
                                                                    }
                                                                ],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "771970414155182081",
                                                                        "name": "George Hotz 🌑",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "indices": [
                                                                            0,
                                                                            15,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "extended_entities": {
                                                                "media": [
                                                                    {
                                                                        "display_url": "pic.x.com/sdx6p73slm",
                                                                        "expanded_url": "https://twitter.com/GrantSlatton/status/1838800733292105957/photo/1",
                                                                        "id_str": "1838800730570002434",
                                                                        "indices": [
                                                                            76,
                                                                            99,
                                                                        ],
                                                                        "media_key": "3_1838800730570002434",
                                                                        "media_url_https": "https://pbs.twimg.com/media/GYS7haZakAIYUfj.jpg",
                                                                        "type": "photo",
                                                                        "url": "https://t.co/Sdx6P73SlM",
                                                                        "ext_media_availability": {
                                                                            "status": "Available"
                                                                        },
                                                                        "features": {
                                                                            "large": {
                                                                                "faces": []
                                                                            },
                                                                            "medium": {
                                                                                "faces": []
                                                                            },
                                                                            "small": {
                                                                                "faces": []
                                                                            },
                                                                            "orig": {
                                                                                "faces": []
                                                                            },
                                                                        },
                                                                        "sizes": {
                                                                            "large": {
                                                                                "h": 928,
                                                                                "w": 1142,
                                                                                "resize": "fit",
                                                                            },
                                                                            "medium": {
                                                                                "h": 928,
                                                                                "w": 1142,
                                                                                "resize": "fit",
                                                                            },
                                                                            "small": {
                                                                                "h": 553,
                                                                                "w": 680,
                                                                                "resize": "fit",
                                                                            },
                                                                            "thumb": {
                                                                                "h": 150,
                                                                                "w": 150,
                                                                                "resize": "crop",
                                                                            },
                                                                        },
                                                                        "original_info": {
                                                                            "height": 928,
                                                                            "width": 1142,
                                                                            "focus_rects": [
                                                                                {
                                                                                    "x": 0,
                                                                                    "y": 0,
                                                                                    "w": 1142,
                                                                                    "h": 640,
                                                                                },
                                                                                {
                                                                                    "x": 0,
                                                                                    "y": 0,
                                                                                    "w": 928,
                                                                                    "h": 928,
                                                                                },
                                                                                {
                                                                                    "x": 21,
                                                                                    "y": 0,
                                                                                    "w": 814,
                                                                                    "h": 928,
                                                                                },
                                                                                {
                                                                                    "x": 196,
                                                                                    "y": 0,
                                                                                    "w": 464,
                                                                                    "h": 928,
                                                                                },
                                                                                {
                                                                                    "x": 0,
                                                                                    "y": 0,
                                                                                    "w": 1142,
                                                                                    "h": 928,
                                                                                },
                                                                            ],
                                                                        },
                                                                        "media_results": {
                                                                            "result": {
                                                                                "media_key": "3_1838800730570002434"
                                                                            }
                                                                        },
                                                                    }
                                                                ]
                                                            },
                                                            "favorite_count": 74,
                                                            "favorited": False,
                                                            "full_text": "@realGeorgeHotz If SpaceX can price rocket launches online, so can B2B SaaS https://t.co/Sdx6P73SlM",
                                                            "in_reply_to_screen_name": "realGeorgeHotz",
                                                            "in_reply_to_status_id_str": "1838791842361430148",
                                                            "in_reply_to_user_id_str": "771970414155182081",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "possibly_sensitive": False,
                                                            "possibly_sensitive_editable": True,
                                                            "quote_count": 0,
                                                            "reply_count": 2,
                                                            "retweet_count": 4,
                                                            "retweeted": False,
                                                            "user_id_str": "278624951",
                                                            "id_str": "1838800733292105957",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFUAKCGBngBUKAAIAAAAAFgDACAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    },
                                    {
                                        "entryId": "conversationthread-1838800733292105957-tweet-1838845290163638432",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838845290163638432",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjo3NzE5NzA0MTQxNTUxODIwODE=",
                                                                    "rest_id": "771970414155182081",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": True,
                                                                        "created_at": "Sat Sep 03 07:17:44 +0000 2016",
                                                                        "default_profile": True,
                                                                        "default_profile_image": False,
                                                                        "description": "President @comma_ai. Founder @__tinygrad__",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            },
                                                                            "url": {
                                                                                "urls": [
                                                                                    {
                                                                                        "display_url": "1m2019.com",
                                                                                        "expanded_url": "http://1m2019.com/",
                                                                                        "url": "https://t.co/jjCk5yFUcy",
                                                                                        "indices": [
                                                                                            0,
                                                                                            23,
                                                                                        ],
                                                                                    }
                                                                                ]
                                                                            },
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 25,
                                                                        "followers_count": 268843,
                                                                        "friends_count": 189,
                                                                        "has_custom_timelines": True,
                                                                        "is_translator": False,
                                                                        "listed_count": 1804,
                                                                        "location": "San Diego, CA",
                                                                        "media_count": 18,
                                                                        "name": "George Hotz 🌑",
                                                                        "normal_followers_count": 268843,
                                                                        "pinned_tweet_ids_str": [],
                                                                        "possibly_sensitive": False,
                                                                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/771970414155182081/1472975904",
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/772342671721455616/FE79-7Ev_normal.jpg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "statuses_count": 159,
                                                                        "translator_type": "none",
                                                                        "url": "https://t.co/jjCk5yFUcy",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "professional": {
                                                                        "rest_id": "1593098633032843264",
                                                                        "professional_type": "Creator",
                                                                        "category": [],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838845290163638432"
                                                            ],
                                                            "editable_until_msecs": "1727253455000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "1531",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
                                                        "legacy": {
                                                            "bookmark_count": 1,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 07:37:35 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                14,
                                                                228,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "278624951",
                                                                        "name": "Grant Slatton",
                                                                        "screen_name": "GrantSlatton",
                                                                        "indices": [
                                                                            0,
                                                                            13,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 46,
                                                            "favorited": False,
                                                            "full_text": "@GrantSlatton I've kind of wanted to put something in orbit just because of this, even though I don't have a need.\n\nThis demonstrates that they are the best deal around, haven't looked but I'm gonna guess Lockheed is contact us.",
                                                            "in_reply_to_screen_name": "GrantSlatton",
                                                            "in_reply_to_status_id_str": "1838800733292105957",
                                                            "in_reply_to_user_id_str": "278624951",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 0,
                                                            "reply_count": 2,
                                                            "retweet_count": 0,
                                                            "retweeted": False,
                                                            "user_id_str": "771970414155182081",
                                                            "id_str": "1838845290163638432",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFUAKEKIDgZEKAAIAAAAAFACCCAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    },
                                    {
                                        "entryId": "conversationthread-1838800733292105957-cursor-showmore-3540853043304513919",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTimelineCursor",
                                                "__typename": "TimelineTimelineCursor",
                                                "value": "PAAAAPAtPBwcFsDC1NGPg_KEMxUCAAAYJmNvbnZlcnNhdGlvbnRocmVhZC0xODM4ODAwNzMzMjkyMTA1OTU3IgAA",
                                                "cursorType": "ShowMore",
                                                "displayTreatment": {
                                                    "actionText": "Show replies"
                                                },
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    }
                                                }
                                            },
                                        },
                                    },
                                ],
                                "displayType": "VerticalConversation",
                                "clientEventInfo": {
                                    "details": {
                                        "conversationDetails": {
                                            "conversationSection": "HighQuality"
                                        }
                                    }
                                },
                            },
                        },
                        {
                            "entryId": "conversationthread-1838795245456163155",
                            "sortIndex": "7384580194493345639",
                            "content": {
                                "entryType": "TimelineTimelineModule",
                                "__typename": "TimelineTimelineModule",
                                "items": [
                                    {
                                        "entryId": "conversationthread-1838795245456163155-tweet-1838795245456163155",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838795245456163155",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjo1NTM1ODY3MjM=",
                                                                    "rest_id": "553586723",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": False,
                                                                        "created_at": "Sat Apr 14 14:46:02 +0000 2012",
                                                                        "default_profile": False,
                                                                        "default_profile_image": False,
                                                                        "description": "dad, swe, automator, robot wrangler",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            },
                                                                            "url": {
                                                                                "urls": [
                                                                                    {
                                                                                        "display_url": "vimbtw.com",
                                                                                        "expanded_url": "http://vimbtw.com",
                                                                                        "url": "https://t.co/YhtpXWYbTu",
                                                                                        "indices": [
                                                                                            0,
                                                                                            23,
                                                                                        ],
                                                                                    }
                                                                                ]
                                                                            },
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 26000,
                                                                        "followers_count": 608,
                                                                        "friends_count": 553,
                                                                        "has_custom_timelines": True,
                                                                        "is_translator": False,
                                                                        "listed_count": 2,
                                                                        "location": "🇺🇸",
                                                                        "media_count": 360,
                                                                        "name": "nlev",
                                                                        "normal_followers_count": 608,
                                                                        "pinned_tweet_ids_str": [
                                                                            "1815919215699742887"
                                                                        ],
                                                                        "possibly_sensitive": False,
                                                                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/553586723/1726685609",
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1828867206492344320/2mDl3s0Q_normal.jpg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "nlevnaut",
                                                                        "statuses_count": 2961,
                                                                        "translator_type": "none",
                                                                        "url": "https://t.co/YhtpXWYbTu",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "professional": {
                                                                        "rest_id": "1781081232794681545",
                                                                        "professional_type": "Creator",
                                                                        "category": [],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838795245456163155"
                                                            ],
                                                            "editable_until_msecs": "1727241524000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "2021",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
                                                        "legacy": {
                                                            "bookmark_count": 1,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 04:18:44 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                16,
                                                                81,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "771970414155182081",
                                                                        "name": "George Hotz 🌑",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "indices": [
                                                                            0,
                                                                            15,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 51,
                                                            "favorited": False,
                                                            "full_text": '@realGeorgeHotz "hi I\'d like to buy an X"\n\n"oh sweet, how much money do you have"',
                                                            "in_reply_to_screen_name": "realGeorgeHotz",
                                                            "in_reply_to_status_id_str": "1838791842361430148",
                                                            "in_reply_to_user_id_str": "771970414155182081",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 0,
                                                            "reply_count": 1,
                                                            "retweet_count": 1,
                                                            "retweeted": False,
                                                            "user_id_str": "553586723",
                                                            "id_str": "1838795245456163155",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFQQKCSQDgBUKAAIAAAAAFADACAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    },
                                    {
                                        "entryId": "conversationthread-1838795245456163155-tweet-1838796390463606977",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838796390463606977",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjo3NzE5NzA0MTQxNTUxODIwODE=",
                                                                    "rest_id": "771970414155182081",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": True,
                                                                        "created_at": "Sat Sep 03 07:17:44 +0000 2016",
                                                                        "default_profile": True,
                                                                        "default_profile_image": False,
                                                                        "description": "President @comma_ai. Founder @__tinygrad__",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            },
                                                                            "url": {
                                                                                "urls": [
                                                                                    {
                                                                                        "display_url": "1m2019.com",
                                                                                        "expanded_url": "http://1m2019.com/",
                                                                                        "url": "https://t.co/jjCk5yFUcy",
                                                                                        "indices": [
                                                                                            0,
                                                                                            23,
                                                                                        ],
                                                                                    }
                                                                                ]
                                                                            },
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 25,
                                                                        "followers_count": 268843,
                                                                        "friends_count": 189,
                                                                        "has_custom_timelines": True,
                                                                        "is_translator": False,
                                                                        "listed_count": 1804,
                                                                        "location": "San Diego, CA",
                                                                        "media_count": 18,
                                                                        "name": "George Hotz 🌑",
                                                                        "normal_followers_count": 268843,
                                                                        "pinned_tweet_ids_str": [],
                                                                        "possibly_sensitive": False,
                                                                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/771970414155182081/1472975904",
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/772342671721455616/FE79-7Ev_normal.jpg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "statuses_count": 159,
                                                                        "translator_type": "none",
                                                                        "url": "https://t.co/jjCk5yFUcy",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "professional": {
                                                                        "rest_id": "1593098633032843264",
                                                                        "professional_type": "Creator",
                                                                        "category": [],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838796390463606977"
                                                            ],
                                                            "editable_until_msecs": "1727241797000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "3513",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
                                                        "legacy": {
                                                            "bookmark_count": 9,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 04:23:17 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                10,
                                                                280,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "553586723",
                                                                        "name": "nlev",
                                                                        "screen_name": "nlevnaut",
                                                                        "indices": [
                                                                            0,
                                                                            9,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 113,
                                                            "favorited": False,
                                                            "full_text": "@nlevnaut This is a deep cultural problem in American business, and one of the reasons we prefer to work with Chinese suppliers. Everyone is losing out because of this.\n\nCompanies should determine the profit they are okay with and post that price. This rot needs to be ripped out.",
                                                            "in_reply_to_screen_name": "nlevnaut",
                                                            "in_reply_to_status_id_str": "1838795245456163155",
                                                            "in_reply_to_user_id_str": "553586723",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 1,
                                                            "reply_count": 2,
                                                            "retweet_count": 2,
                                                            "retweeted": False,
                                                            "user_id_str": "771970414155182081",
                                                            "id_str": "1838796390463606977",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFUR6EigDgZEKAAIAAAAAFACCCAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    },
                                    {
                                        "entryId": "conversationthread-1838795245456163155-cursor-showmore-7824698620531760084",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTimelineCursor",
                                                "__typename": "TimelineTimelineCursor",
                                                "value": "PAAAAPAtPBwcFoLD1L3k5NuEMxUCAAAYJmNvbnZlcnNhdGlvbnRocmVhZC0xODM4Nzk1MjQ1NDU2MTYzMTU1IgAA",
                                                "cursorType": "ShowMore",
                                                "displayTreatment": {
                                                    "actionText": "Show replies"
                                                },
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    }
                                                }
                                            },
                                        },
                                    },
                                ],
                                "displayType": "VerticalConversation",
                                "clientEventInfo": {
                                    "details": {
                                        "conversationDetails": {
                                            "conversationSection": "HighQuality"
                                        }
                                    }
                                },
                            },
                        },
                        {
                            "entryId": "conversationthread-1838808985241034818",
                            "sortIndex": "7384580194493345629",
                            "content": {
                                "entryType": "TimelineTimelineModule",
                                "__typename": "TimelineTimelineModule",
                                "items": [
                                    {
                                        "entryId": "conversationthread-1838808985241034818-tweet-1838808985241034818",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838808985241034818",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjoxMjM5Njk3OTY3NTg3NzY2Mjc2",
                                                                    "rest_id": "1239697967587766276",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": False,
                                                                        "can_media_tag": True,
                                                                        "created_at": "Mon Mar 16 23:40:17 +0000 2020",
                                                                        "default_profile": True,
                                                                        "default_profile_image": False,
                                                                        "description": "Humble blockhead shares unsolicited opinions about technology, management, and the current thing. Endorsements ≠ endorsements.",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            }
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 35391,
                                                                        "followers_count": 1311,
                                                                        "friends_count": 862,
                                                                        "has_custom_timelines": False,
                                                                        "is_translator": False,
                                                                        "listed_count": 13,
                                                                        "location": "Michigan",
                                                                        "media_count": 1274,
                                                                        "name": "Stonewright",
                                                                        "normal_followers_count": 1311,
                                                                        "pinned_tweet_ids_str": [],
                                                                        "possibly_sensitive": False,
                                                                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1239697967587766276/1724460652",
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1827146074768678912/7g0hwtwc_normal.jpg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "StonewrightAI",
                                                                        "statuses_count": 8920,
                                                                        "translator_type": "none",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "professional": {
                                                                        "rest_id": "1461143556928720903",
                                                                        "professional_type": "Business",
                                                                        "category": [
                                                                            {
                                                                                "id": 713,
                                                                                "name": "Science & Technology",
                                                                                "icon_name": "IconBriefcaseStroke",
                                                                            }
                                                                        ],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838808985241034818"
                                                            ],
                                                            "editable_until_msecs": "1727244800000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "814",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
                                                        "legacy": {
                                                            "bookmark_count": 1,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 05:13:20 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                16,
                                                                267,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "771970414155182081",
                                                                        "name": "George Hotz 🌑",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "indices": [
                                                                            0,
                                                                            15,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 6,
                                                            "favorited": False,
                                                            "full_text": "@realGeorgeHotz Dear Diary, I tell all my vendors to act like low cost Chinese commodity brokers. That would be nice for me, a buyer. But many of them still don't do it!\n\nI can't understand. I told them nicely, diary. Ugh. Maybe I will tell them less nicely tomorrow.",
                                                            "in_reply_to_screen_name": "realGeorgeHotz",
                                                            "in_reply_to_status_id_str": "1838791842361430148",
                                                            "in_reply_to_user_id_str": "771970414155182081",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 1,
                                                            "reply_count": 1,
                                                            "retweet_count": 0,
                                                            "retweeted": False,
                                                            "user_id_str": "1239697967587766276",
                                                            "id_str": "1838808985241034818",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFQAKDDADgBUKAAIAAAAAFADACAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    }
                                ],
                                "displayType": "VerticalConversation",
                                "clientEventInfo": {
                                    "details": {
                                        "conversationDetails": {
                                            "conversationSection": "HighQuality"
                                        }
                                    }
                                },
                            },
                        },
                        {
                            "entryId": "conversationthread-1838988944517513493",
                            "sortIndex": "7384580194493345619",
                            "content": {
                                "entryType": "TimelineTimelineModule",
                                "__typename": "TimelineTimelineModule",
                                "items": [
                                    {
                                        "entryId": "conversationthread-1838988944517513493-tweet-1838988944517513493",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838988944517513493",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjoxNTk5MDI4ODA1MTI5MDc2NzM3",
                                                                    "rest_id": "1599028805129076737",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": False,
                                                                        "created_at": "Sat Dec 03 13:15:04 +0000 2022",
                                                                        "default_profile": True,
                                                                        "default_profile_image": True,
                                                                        "description": "Software, Technology and Systems. Love things that work. Here to listen and learn.",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            }
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 18672,
                                                                        "followers_count": 523,
                                                                        "friends_count": 1054,
                                                                        "has_custom_timelines": False,
                                                                        "is_translator": False,
                                                                        "listed_count": 0,
                                                                        "location": "Germany",
                                                                        "media_count": 1,
                                                                        "name": "Martin Heyer",
                                                                        "normal_followers_count": 523,
                                                                        "pinned_tweet_ids_str": [],
                                                                        "possibly_sensitive": False,
                                                                        "profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "MartinHeyer85",
                                                                        "statuses_count": 279,
                                                                        "translator_type": "none",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838988944517513493"
                                                            ],
                                                            "editable_until_msecs": "1727287705000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "40",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
                                                        "legacy": {
                                                            "bookmark_count": 0,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 17:08:25 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                16,
                                                                136,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "771970414155182081",
                                                                        "name": "George Hotz 🌑",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "indices": [
                                                                            0,
                                                                            15,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 0,
                                                            "favorited": False,
                                                            "full_text": "@realGeorgeHotz tbf, there may be a high level of individualization or scale effects in some products, which warrant a negotiated price.",
                                                            "in_reply_to_screen_name": "realGeorgeHotz",
                                                            "in_reply_to_status_id_str": "1838791842361430148",
                                                            "in_reply_to_user_id_str": "771970414155182081",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 0,
                                                            "reply_count": 0,
                                                            "retweet_count": 0,
                                                            "retweeted": False,
                                                            "user_id_str": "1599028805129076737",
                                                            "id_str": "1838988944517513493",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFQAKiCADgAUKAAIAAAAAFACgCAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    }
                                ],
                                "displayType": "VerticalConversation",
                                "clientEventInfo": {
                                    "details": {
                                        "conversationDetails": {
                                            "conversationSection": "HighQuality"
                                        }
                                    }
                                },
                            },
                        },
                        {
                            "entryId": "conversationthread-1839042164111847795",
                            "sortIndex": "7384580194493345609",
                            "content": {
                                "entryType": "TimelineTimelineModule",
                                "__typename": "TimelineTimelineModule",
                                "items": [
                                    {
                                        "entryId": "conversationthread-1839042164111847795-tweet-1839042164111847795",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1839042164111847795",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjo3OTAyMDY1NjI5MjkzNDg2MDk=",
                                                                    "rest_id": "790206562929348609",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": False,
                                                                        "created_at": "Sun Oct 23 15:01:40 +0000 2016",
                                                                        "default_profile": False,
                                                                        "default_profile_image": False,
                                                                        "description": "Mainly epistemology and bad jokes.\nPSA: I'm currently translating the Taking Children Seriously website to French. Help is welcome!",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            },
                                                                            "url": {
                                                                                "urls": [
                                                                                    {
                                                                                        "display_url": "adrienchauvet.com",
                                                                                        "expanded_url": "https://www.adrienchauvet.com",
                                                                                        "url": "https://t.co/yDGJ0yI4k5",
                                                                                        "indices": [
                                                                                            0,
                                                                                            23,
                                                                                        ],
                                                                                    }
                                                                                ]
                                                                            },
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 15507,
                                                                        "followers_count": 153,
                                                                        "friends_count": 0,
                                                                        "has_custom_timelines": True,
                                                                        "is_translator": False,
                                                                        "listed_count": 0,
                                                                        "location": "Bourges, France",
                                                                        "media_count": 64,
                                                                        "name": "Adrien Chauvet",
                                                                        "normal_followers_count": 153,
                                                                        "pinned_tweet_ids_str": [
                                                                            "1838201656225284218"
                                                                        ],
                                                                        "possibly_sensitive": False,
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1836003583596048384/PPO1wIJL_normal.jpg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "adrien_chauvet",
                                                                        "statuses_count": 1272,
                                                                        "translator_type": "none",
                                                                        "url": "https://t.co/yDGJ0yI4k5",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "tipjar_settings": {
                                                                        "is_enabled": False
                                                                    },
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1839042164111847795"
                                                            ],
                                                            "editable_until_msecs": "1727300394000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "21",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
                                                        "legacy": {
                                                            "bookmark_count": 0,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 20:39:54 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                16,
                                                                152,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "771970414155182081",
                                                                        "name": "George Hotz 🌑",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "indices": [
                                                                            0,
                                                                            15,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 0,
                                                            "favorited": False,
                                                            "full_text": "@realGeorgeHotz I also run away from websites that ask for payment card numbers and various personal details before revealing the cost of their service.",
                                                            "in_reply_to_screen_name": "realGeorgeHotz",
                                                            "in_reply_to_status_id_str": "1838791842361430148",
                                                            "in_reply_to_user_id_str": "771970414155182081",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 0,
                                                            "reply_count": 0,
                                                            "retweet_count": 0,
                                                            "retweeted": False,
                                                            "user_id_str": "790206562929348609",
                                                            "id_str": "1839042164111847795",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFQAKiCADgAUKAAIAAAAAFADACAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    }
                                ],
                                "displayType": "VerticalConversation",
                                "clientEventInfo": {
                                    "details": {
                                        "conversationDetails": {
                                            "conversationSection": "HighQuality"
                                        }
                                    }
                                },
                            },
                        },
                        {
                            "entryId": "conversationthread-1838797384564031728",
                            "sortIndex": "7384580194493345599",
                            "content": {
                                "entryType": "TimelineTimelineModule",
                                "__typename": "TimelineTimelineModule",
                                "items": [
                                    {
                                        "entryId": "conversationthread-1838797384564031728-tweet-1838797384564031728",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838797384564031728",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjo4MDA4NTQwOTYyMTk0NzE4NzI=",
                                                                    "rest_id": "800854096219471872",
                                                                    "affiliates_highlighted_label": {
                                                                        "label": {
                                                                            "url": {
                                                                                "url": "https://twitter.com/hyperbolic_labs",
                                                                                "urlType": "DeepLink",
                                                                            },
                                                                            "badge": {
                                                                                "url": "https://pbs.twimg.com/profile_images/1775708849707819008/1RRWsmmg_bigger.jpg"
                                                                            },
                                                                            "description": "Hyperbolic",
                                                                            "userLabelType": "BusinessLabel",
                                                                            "userLabelDisplayType": "Badge",
                                                                        }
                                                                    },
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": True,
                                                                        "created_at": "Tue Nov 22 00:11:10 +0000 2016",
                                                                        "default_profile": True,
                                                                        "default_profile_image": False,
                                                                        "description": "Co-founder & CTO @hyperbolic_labs 🧑\u200d🍳 fun AI systems. Previously @octoaicloud building @ApacheTVM, PhD @uwcse 🤖",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            },
                                                                            "url": {
                                                                                "urls": [
                                                                                    {
                                                                                        "display_url": "yuchenjin.github.io",
                                                                                        "expanded_url": "https://yuchenjin.github.io/",
                                                                                        "url": "https://t.co/i4moxD2Mss",
                                                                                        "indices": [
                                                                                            0,
                                                                                            23,
                                                                                        ],
                                                                                    }
                                                                                ]
                                                                            },
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 12229,
                                                                        "followers_count": 10889,
                                                                        "friends_count": 325,
                                                                        "has_custom_timelines": True,
                                                                        "is_translator": False,
                                                                        "listed_count": 99,
                                                                        "location": "another Galaxy",
                                                                        "media_count": 472,
                                                                        "name": "Yuchen Jin",
                                                                        "normal_followers_count": 10889,
                                                                        "pinned_tweet_ids_str": [
                                                                            "1796963544883409044"
                                                                        ],
                                                                        "possibly_sensitive": False,
                                                                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/800854096219471872/1714238368",
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1319081238439751681/kCcqnwoF_normal.jpg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "Yuchenj_UW",
                                                                        "statuses_count": 3281,
                                                                        "translator_type": "none",
                                                                        "url": "https://t.co/i4moxD2Mss",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838797384564031728"
                                                            ],
                                                            "editable_until_msecs": "1727242034000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "854",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
                                                        "legacy": {
                                                            "bookmark_count": 0,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 04:27:14 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                16,
                                                                211,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "771970414155182081",
                                                                        "name": "George Hotz 🌑",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "indices": [
                                                                            0,
                                                                            15,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 4,
                                                            "favorited": False,
                                                            "full_text": "@realGeorgeHotz True, I talked to AWS sales for almost 2 months before to get a 8xA100 (40GB) ec2 quota, and their price is (still) SO HIGH! ☹️\n\nThen I was like, darn it, I will build a GPU Airbnb to disrupt it.",
                                                            "in_reply_to_screen_name": "realGeorgeHotz",
                                                            "in_reply_to_status_id_str": "1838791842361430148",
                                                            "in_reply_to_user_id_str": "771970414155182081",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 0,
                                                            "reply_count": 0,
                                                            "retweet_count": 0,
                                                            "retweeted": False,
                                                            "user_id_str": "800854096219471872",
                                                            "id_str": "1838797384564031728",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABDQAKiCADgAUKAAIAAAAAFACgCAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    }
                                ],
                                "displayType": "VerticalConversation",
                                "clientEventInfo": {
                                    "details": {
                                        "conversationDetails": {
                                            "conversationSection": "HighQuality"
                                        }
                                    }
                                },
                            },
                        },
                        {
                            "entryId": "conversationthread-1838849842086338690",
                            "sortIndex": "7384580194493345589",
                            "content": {
                                "entryType": "TimelineTimelineModule",
                                "__typename": "TimelineTimelineModule",
                                "items": [
                                    {
                                        "entryId": "conversationthread-1838849842086338690-tweet-1838849842086338690",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838849842086338690",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjo0NjEzMDgwNg==",
                                                                    "rest_id": "46130806",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": True,
                                                                        "created_at": "Wed Jun 10 14:59:17 +0000 2009",
                                                                        "default_profile": False,
                                                                        "default_profile_image": False,
                                                                        "description": "Dad of two boys / AI Tech Person / Ex @freshbooks / Ex-CTO of @fastbillnews",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            }
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 9651,
                                                                        "followers_count": 1070,
                                                                        "friends_count": 539,
                                                                        "has_custom_timelines": True,
                                                                        "is_translator": False,
                                                                        "listed_count": 50,
                                                                        "location": "Frankfurt / Germany",
                                                                        "media_count": 711,
                                                                        "name": "Mario Hachemer",
                                                                        "normal_followers_count": 1070,
                                                                        "pinned_tweet_ids_str": [],
                                                                        "possibly_sensitive": False,
                                                                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/46130806/1656209927",
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/378800000386480481/fd3542345ded59c8e000d96e66fdb9c6_normal.jpeg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "MarioHachemer",
                                                                        "statuses_count": 9536,
                                                                        "translator_type": "regular",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "professional": {
                                                                        "rest_id": "1688910435163025657",
                                                                        "professional_type": "Creator",
                                                                        "category": [
                                                                            {
                                                                                "id": 958,
                                                                                "name": "Entrepreneur",
                                                                                "icon_name": "IconBriefcaseStroke",
                                                                            }
                                                                        ],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838849842086338690"
                                                            ],
                                                            "editable_until_msecs": "1727254541000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "539",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
                                                        "legacy": {
                                                            "bookmark_count": 0,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 07:55:41 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                16,
                                                                222,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "771970414155182081",
                                                                        "name": "George Hotz 🌑",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "indices": [
                                                                            0,
                                                                            15,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 0,
                                                            "favorited": False,
                                                            "full_text": "@realGeorgeHotz I've had a few very good experiences with contact sales from companies that just had middleware that relied on trusting their customers to meter their usage for them so they don't have to include telemetry.",
                                                            "in_reply_to_screen_name": "realGeorgeHotz",
                                                            "in_reply_to_status_id_str": "1838791842361430148",
                                                            "in_reply_to_user_id_str": "771970414155182081",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 0,
                                                            "reply_count": 0,
                                                            "retweet_count": 0,
                                                            "retweeted": False,
                                                            "user_id_str": "46130806",
                                                            "id_str": "1838849842086338690",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFQAKiCADgAUKAAIAAAAAFADACAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    }
                                ],
                                "displayType": "VerticalConversation",
                                "clientEventInfo": {
                                    "details": {
                                        "conversationDetails": {
                                            "conversationSection": "HighQuality"
                                        }
                                    }
                                },
                            },
                        },
                        {
                            "entryId": "conversationthread-1838796569354887534",
                            "sortIndex": "7384580194493345579",
                            "content": {
                                "entryType": "TimelineTimelineModule",
                                "__typename": "TimelineTimelineModule",
                                "items": [
                                    {
                                        "entryId": "conversationthread-1838796569354887534-tweet-1838796569354887534",
                                        "item": {
                                            "itemContent": {
                                                "itemType": "TimelineTweet",
                                                "__typename": "TimelineTweet",
                                                "tweet_results": {
                                                    "result": {
                                                        "__typename": "Tweet",
                                                        "rest_id": "1838796569354887534",
                                                        "has_birdwatch_notes": False,
                                                        "core": {
                                                            "user_results": {
                                                                "result": {
                                                                    "__typename": "User",
                                                                    "id": "VXNlcjoxMzcyNzUxNTQ3MzI3NjcyMzIy",
                                                                    "rest_id": "1372751547327672322",
                                                                    "affiliates_highlighted_label": {},
                                                                    "has_graduated_access": True,
                                                                    "is_blue_verified": True,
                                                                    "profile_image_shape": "Circle",
                                                                    "legacy": {
                                                                        "following": False,
                                                                        "can_dm": True,
                                                                        "can_media_tag": True,
                                                                        "created_at": "Fri Mar 19 03:27:35 +0000 2021",
                                                                        "default_profile": True,
                                                                        "default_profile_image": False,
                                                                        "description": "New Tesla FSD Beta tester with the 100 score expansion. #RatingFSDBeta\nI love learning about AI.",
                                                                        "entities": {
                                                                            "description": {
                                                                                "urls": []
                                                                            }
                                                                        },
                                                                        "fast_followers_count": 0,
                                                                        "favourites_count": 38558,
                                                                        "followers_count": 580,
                                                                        "friends_count": 126,
                                                                        "has_custom_timelines": True,
                                                                        "is_translator": False,
                                                                        "listed_count": 5,
                                                                        "location": "Utah, USA",
                                                                        "media_count": 481,
                                                                        "name": "Mike Stirner",
                                                                        "normal_followers_count": 580,
                                                                        "pinned_tweet_ids_str": [
                                                                            "1832296082296168576"
                                                                        ],
                                                                        "possibly_sensitive": False,
                                                                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1372751547327672322/1645488416",
                                                                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1372751886135128075/pC8lzUF3_normal.jpg",
                                                                        "profile_interstitial_type": "",
                                                                        "screen_name": "MikeStirner",
                                                                        "statuses_count": 11400,
                                                                        "translator_type": "none",
                                                                        "verified": False,
                                                                        "want_retweets": False,
                                                                        "withheld_in_countries": [],
                                                                    },
                                                                    "tipjar_settings": {},
                                                                    "verified_phone_status": False,
                                                                }
                                                            }
                                                        },
                                                        "unmention_data": {},
                                                        "edit_control": {
                                                            "edit_tweet_ids": [
                                                                "1838796569354887534"
                                                            ],
                                                            "editable_until_msecs": "1727241839000",
                                                            "is_edit_eligible": False,
                                                            "edits_remaining": "5",
                                                        },
                                                        "is_translatable": False,
                                                        "views": {
                                                            "count": "581",
                                                            "state": "EnabledWithCount",
                                                        },
                                                        "source": '<a href="https://mobile.twitter.com" rel="nofollow">Twitter Web App</a>',
                                                        "legacy": {
                                                            "bookmark_count": 0,
                                                            "bookmarked": False,
                                                            "created_at": "Wed Sep 25 04:23:59 +0000 2024",
                                                            "conversation_id_str": "1838791842361430148",
                                                            "display_text_range": [
                                                                16,
                                                                120,
                                                            ],
                                                            "entities": {
                                                                "hashtags": [],
                                                                "symbols": [],
                                                                "timestamps": [],
                                                                "urls": [],
                                                                "user_mentions": [
                                                                    {
                                                                        "id_str": "771970414155182081",
                                                                        "name": "George Hotz 🌑",
                                                                        "screen_name": "realGeorgeHotz",
                                                                        "indices": [
                                                                            0,
                                                                            15,
                                                                        ],
                                                                    }
                                                                ],
                                                            },
                                                            "favorite_count": 2,
                                                            "favorited": False,
                                                            "full_text": "@realGeorgeHotz I was literally just talking about how annoying this is today!\n\nYeah I also feel like it wastes my time.",
                                                            "in_reply_to_screen_name": "realGeorgeHotz",
                                                            "in_reply_to_status_id_str": "1838791842361430148",
                                                            "in_reply_to_user_id_str": "771970414155182081",
                                                            "is_quote_status": False,
                                                            "lang": "en",
                                                            "quote_count": 0,
                                                            "reply_count": 0,
                                                            "retweet_count": 0,
                                                            "retweeted": False,
                                                            "user_id_str": "1372751547327672322",
                                                            "id_str": "1838796569354887534",
                                                        },
                                                        "quick_promote_eligibility": {
                                                            "eligibility": "IneligibleNotProfessional"
                                                        },
                                                    }
                                                },
                                                "tweetDisplayType": "Tweet",
                                            },
                                            "clientEventInfo": {
                                                "details": {
                                                    "conversationDetails": {
                                                        "conversationSection": "HighQuality"
                                                    },
                                                    "timelinesDetails": {
                                                        "controllerData": "DAACDAAEDAABCgABFQQKiCADgAUKAAIAAAAAFADACAAAAAA="
                                                    },
                                                }
                                            },
                                        },
                                    }
                                ],
                                "displayType": "VerticalConversation",
                                "clientEventInfo": {
                                    "details": {
                                        "conversationDetails": {
                                            "conversationSection": "HighQuality"
                                        }
                                    }
                                },
                            },
                        },
                        {
                            "entryId": "cursor-bottom-4937057000279906246",
                            "sortIndex": "7384580194493345578",
                            "content": {
                                "entryType": "TimelineTimelineItem",
                                "__typename": "TimelineTimelineItem",
                                "itemContent": {
                                    "itemType": "TimelineTimelineCursor",
                                    "__typename": "TimelineTimelineCursor",
                                    "value": "UgAAAPBDHBmGhIG18fLB4YQz3IXXqZnv24QzysPUicnh3YQz4IPajdOe3IQzqoSy_fOss4UzhIK3jYqM9IQzpoW8wZGi24Qz5sXR7djGy4UzJQISFQQAAA",
                                    "cursorType": "Bottom",
                                },
                            },
                        },
                    ],
                },
                {"type": "TimelineTerminateTimeline", "direction": "Top"},
            ]
        }
    }
}


pprint.pprint(response, indent=1)
