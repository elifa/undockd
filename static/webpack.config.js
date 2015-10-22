module.exports = {
  "entry": "./application.ts",
  "devtool": "source-map",
  "output": {
    "path": __dirname,
    "filename": "undockd.js"
  },
  "resolve": {
    "extensions": ["", ".webpack.js", ".ts", ".js"]
  },
  "module": {
    "loaders": [
      {
        "test": /\.ts$/,
        "exclude": /node_modules/,
        "loader": "ts"
      }
    ]
  },
  "ts": {
    "configFileName": "ts.config.json"
  }
};
