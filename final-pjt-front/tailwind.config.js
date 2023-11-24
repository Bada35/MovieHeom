/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        "Heum-Primary": "#DDDBE6",
        "Heum-Secondary": "#004E71",
        "Heum-Third": "#163661",
        "Heum-Fourth": "#0D2039"
      },
      fontFamily: {
        'Eczar': ['Eczar', 'serif'],
        'Gowun': ['Gowun Dodum', 'sans-serif'],
        'PermanentMarker': ['Permanent Marker', 'cursive'],
        'Rowdies': ['Rowdies', 'sans-serif'],
        'Caveat': ['Caveat', 'cursive'],
        'Satisfy': ['Satisfy', 'cursive'],
      },
      container: {
        padding: "2rem",
        center: true,
      },
    },
  },
  plugins: [require("tw-elements/dist/plugin.cjs")],
}
