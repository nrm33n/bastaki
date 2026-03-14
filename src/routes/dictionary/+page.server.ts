import type { PageServerLoad } from './$types';
import type { Entry } from '$lib/types';
import { json } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ locals, url }) => {
	const q = url.searchParams.get('q')?.trim() ?? '';
	const pos = url.searchParams.get('pos') ?? '';
	const isJson = url.searchParams.get('json') === '1';

	let query = locals.supabase
		.from('entries')
		.select('*')
		.eq('approved', true)
		.order('english');

	if (q) {
		query = query.or(
			`english.ilike.%${q}%,bastaki_transliteration.ilike.%${q}%`
		);
	}

	if (pos && pos !== 'all') {
		query = query.eq('part_of_speech', pos);
	}

	const { data: entries } = await query;
	const result = (entries ?? []) as Entry[];

	// Allow the home page quick-search to fetch JSON directly
	if (isJson) {
		return json(result) as unknown as { entries: Entry[]; q: string; pos: string };
	}

	return { entries: result, q, pos };
};
