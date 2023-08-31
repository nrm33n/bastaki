/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily:{
        'poppins': ['Poppins'],
        'bitter' : ['Bitter'],
      },
      colors: {
        'light-olive': '#f8f8f8',
        'ml-olive' : '#DCE1D7',
        'med-olive': '#c7d1b6',
        'deep-olive': '#7A8967',
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

