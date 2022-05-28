module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        'lisa-pink': '#e9008d',
        'lisa-orange': '#f6841b',
        'lisa-yellow': '#fcea08',
        'lisa-green': '	#6eb63f',
        'lisa-blue': '#05aded',
      },
      lineClamp: {
        7: '7',
        8: '8',
        9: '9',
        10: '10',
      }
    },
  },
  plugins: [
    require("daisyui"),
    require('@tailwindcss/line-clamp')
  ]
};