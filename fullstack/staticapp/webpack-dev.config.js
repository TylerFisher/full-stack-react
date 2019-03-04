const path = require('path');
const glob = require('glob');
const _ = require('lodash');
const portfinder = require('portfinder');

portfinder.basePort = 3000;

const config = (env, argv, port) => ({
  mode: 'development',
  devtool: 'cheap-eval-source-map',
  entry: _.zipObject(
    glob.sync('./src/js/main-*.js*').map(f => path.basename(f, path.extname(f))),
    glob.sync('./src/js/main-*.js*').map(f => [
      '@babel/polyfill',
      'whatwg-fetch',
      f,
    ])
  ),
  output: {
    path: path.resolve(__dirname, '/static/fullstack'),
    filename: 'js/[name].js',
  },
  devServer: {
    compress: true,
    port,
    open: true,
    contentBase: false,
    proxy: {
      '/': {
        target: 'http://localhost:8000',
      },
      '/ws': {
        target: 'ws://localhost:8000/',
        ws: true,
      },
    },
    publicPath: '/static/fullstack/',
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              ['@babel/env', {
                'targets': {
                  'browsers': 'last 2 versions',
                },
              }],
              '@babel/react',
            ],
            plugins: [
              '@babel/proposal-class-properties',
            ],
          },
        },
      }, {
        test: /theme.*\.scss$/,
        use: [{
          loader: 'style-loader',
        }, {
          loader: 'css-loader',
          options: {
            sourceMap: true,
          },
        }, {
          loader: 'sass-loader',
          options: {
            sourceMap: true,
          },
        }],
      }, {
        test: /\.scss$/,
        exclude: /theme.*\.scss$/,
        use: [{
          loader: 'style-loader',
        }, {
          loader: 'css-loader',
          options: {
            modules: true,
            sourceMap: true,
          },
        }, {
          loader: 'sass-loader',
          options: {
            sourceMap: true,
          },
        }],
      }, {
        test: /\.css$/,
        use: [{
          loader:  'style-loader',
        }, {
          loader: 'css-loader',
          options: {
            sourceMap: true,
          },
        }],
      }
    ],
  },
});

module.exports = (env, argv) =>
  portfinder.getPortPromise()
    .then(port => config(env, argv, port));
