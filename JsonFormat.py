

data = {
    "sitename": {

        "menus": ["menu1", "menu2", "menu3"],

        "menu1": {

            "url": "https://..",
            "haschild": "True",
            "child": {

                "menus": ["child1", "child2"],
                "child1": {
                        "url": "https://..",
                        "haschild": "False",
                        "child": {},
                },

                "child2": {

                    "url": 'https: // ...",
                    "haschild": "True",
                    "child": {

                        "menus": ["grandchild1"],
                        "grandchild"{
                                "url": 'https: // ..."
                                "haschild": "False"
                                "child": {}
                        }

                    }
                }
            },

            "menu2": {
                "url": "https://..",
                "haschild": "False",
                "child": {}
            },

            "menu3": {
                "url": "https://..",
                "haschild": "True",
                "child": {
                    "menus": ["child1"],
                    "child1": {
                            "url": 'https: // ..."
                            "haschild": "False"
                            "child": {}
                    },

                },
            },
        }
    }
}
