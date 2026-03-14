import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions: Actions = {
	default: async ({ request }) => {
		const data = await request.formData();
		const email = data.get('email')?.toString().trim();
		const subject = data.get('subject')?.toString().trim();
		const message = data.get('message')?.toString().trim();

		if (!email || !subject || !message) {
			return fail(400, { error: 'All fields are required.', email, subject, message });
		}

		// Netlify Forms handles delivery — no backend email service needed.
		// In local dev this action is a no-op; in production Netlify intercepts
		// submissions to forms with data-netlify="true".
		return { success: true };
	}
};
