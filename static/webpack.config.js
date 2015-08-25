module.exports = {
    "entry": "./application.js",
    "output": {
        "path": __dirname,
        "filename": "undockd.js"
    },
    "module": {
        "loaders": [
            {
                "test": /\.css$/,
                "loader": "style!css"
            }, {
                "test": /\.scss$/,
                "loader": "style!css!sass"
            }
        ]
    }
};