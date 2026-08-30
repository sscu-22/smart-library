/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // 🌟 Dark Mode လုပ်ဖို့ ဒီအချက်က အရေးကြီးဆုံးပါ
  content: [
    './templates/**/*.html', // သင်၏ templates ဖိုင်များရှိရာ နေရာ
    './**/templates/**/*.html',
    './**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}