var path = require('path');

module.exports = {
  context: path.join(__dirname, 'src'),
  devtool: 'inline-source-map',
  mode: 'development',
  entry: './index.js',
  module: {
    rules: [{
      test: /\.js?$/,
      exclude: /node_modules/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['env', 'react'],
        },
      },
    }]
  },
  devServer: {
    contentBase: path.resolve(__dirname,　"dst"),
    port: 8080,
  },
  output: {
    path: path.join(__dirname, "dst"),
    filename: 'bundle.js',
  },
}