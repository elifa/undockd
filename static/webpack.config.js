module.exports = {
  "debug": true,
  "devtool": "source-map",
  "entry": "application",
  "output": {
    "filename": "undockd.js"
  },
  "resolve": {
    "modulesDirectories": ["node_modules", "."],
    "extensions": ["", ".webpack.js", ".ts", ".js"]
  },
  "module": {
    "preLoaders": [{
      "test": /\.ts(x?)$/,
      "loader": "ts-loader",
      "query": {
        "configFileName": "typescript.config.json"
      }
    }],
    "loaders": [{
      "test": /\.(j|t)s(x?)$/,
      "loader": "babel-loader",
      "query": {
        "presets": [
          "es2015",
          "stage-2"
        ]
      }
    }]
  }
};
