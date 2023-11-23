/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        "Heum-Primary": "#00668A",
        "Heum-Secondary": "#004E71",
      },
    },
      fontFamily: {
        'Eczar': ['Eczar', 'serif'],
        'Gowun': ['Gowun Dodum', 'sans-serif'],
        'PermanentMarker': ['Permanent Marker', 'cursive'],
        'Rowdies': ['Rowdies', 'sans-serif'],
      },
      container: {
        padding: "2rem",
        center: true,
      },
  },
  plugins: [],
}
