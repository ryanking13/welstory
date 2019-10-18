module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: '웰스토리 식단 뷰어',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Welstory menu viewer ' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: 'favicon.ico' }
    ]
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend(config, { isDev, isClient }) {
      if (isDev && isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },
  generate: {
    dir: '../docs',
  },
  router: {
    base: '/welstory/'
  },
  plugins: [
    { src: '~plugins/ga.js', ssr: false }
  ],
  modules: [
    '@nuxtjs/vuetify',
  ]
}

