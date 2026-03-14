import type { Config } from 'tailwindcss';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				'deep-olive': '#7A8967',
				'med-olive': '#c7d1b6',
				'light-olive': '#f8f8f8'
			},
			fontFamily: {
				sans: ['Poppins', 'sans-serif'],
				display: ['Bitter', 'serif']
			}
		}
	},
	plugins: []
} satisfies Config;
