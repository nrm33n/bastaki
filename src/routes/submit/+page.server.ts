import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions: Actions = {
	default: async ({ request, locals }) => {
		const data = await request.formData();

		const english = data.get('english')?.toString().trim();
		const bastaki_transliteration = data.get('bastaki_transliteration')?.toString().trim();
		const part_of_speech = data.get('part_of_speech')?.toString().trim() || null;
		const additional_classifier = data.get('additional_classifier')?.toString().trim() || null;
		const example = data.get('example')?.toString().trim() || null;
		const submitter_email = data.get('email')?.toString().trim() || null;

		if (!english || !bastaki_transliteration) {
			return fail(400, {
				error: 'English and Bastaki transliteration are required.',
				english,
				bastaki_transliteration,
				part_of_speech,
				example,
				submitter_email
			});
		}

		const { data: sessionData } = await locals.supabase.auth.getUser();

		const { error } = await locals.supabase.from('submissions').insert({
			english,
			bastaki_transliteration,
			part_of_speech,
			additional_classifier,
			example,
			submitter_email,
			submitter_id: sessionData.user?.id ?? null,
			status: 'pending'
		});

		if (error) {
			console.error(error);
			return fail(500, { error: 'Submission failed. Please try again.' });
		}

		return { success: true };
	}
};
