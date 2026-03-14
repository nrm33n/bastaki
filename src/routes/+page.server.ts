import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	const [{ count }, { data: featured }] = await Promise.all([
		locals.supabase.from('entries').select('*', { count: 'exact', head: true }).eq('approved', true),
		locals.supabase
			.from('entries')
			.select('*')
			.eq('approved', true)
			.order('english')
			.limit(10)
	]);

	return {
		entryCount: count ?? 0,
		featured: featured ?? []
	};
};
