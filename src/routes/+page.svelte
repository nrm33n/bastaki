<script lang="ts">
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	let query = $state('');
	let results = $derived.by(() => data.featured ?? []);
	let liveResults = $state<typeof data.featured>([]);
	let searched = $state(false);

	async function search() {
		if (!query.trim()) {
			searched = false;
			liveResults = [];
			return;
		}
		const res = await fetch(`/dictionary?q=${encodeURIComponent(query)}&json=1`);
		if (res.ok) {
			liveResults = await res.json();
			searched = true;
		}
	}
</script>

<svelte:head>
	<title>Bastaki — Endangered Dialect Dictionary</title>
</svelte:head>

<!-- Hero -->
<section class="mb-12">
	<h1 class="text-4xl font-display font-semibold text-deep-olive mb-4">Bastaki Dictionary</h1>
	<p class="text-lg text-gray-700 max-w-2xl leading-relaxed">
		A living digital dictionary for <strong>Bastaki</strong>, an endangered dialect of Ajami
		(Achomi/Larestani) spoken in southern Iran and across the Gulf diaspora.
		Classified by UNESCO as <em>definitely endangered</em>.
	</p>
	<p class="mt-3 text-sm text-gray-500">
		{data.entryCount ?? '—'} entries &mdash;
		<a href="/submit" class="text-deep-olive underline underline-offset-2 hover:opacity-80">
			contribute a word
		</a>
	</p>
</section>

<!-- Quick search -->
<section class="mb-10">
	<label for="search" class="block text-sm font-medium text-gray-700 mb-1">Quick search</label>
	<div class="flex gap-2 max-w-md">
		<input
			id="search"
			type="search"
			bind:value={query}
			oninput={search}
			placeholder="Search English or Bastaki…"
			class="input"
		/>
		<a href="/dictionary" class="btn-secondary whitespace-nowrap">Browse all</a>
	</div>
</section>

<!-- Results / featured -->
{#snippet entryTable(rows: typeof data.featured)}
	<div class="overflow-x-auto rounded border border-med-olive">
		<table class="w-full text-sm">
			<thead class="bg-med-olive text-left">
				<tr>
					<th class="px-4 py-2 font-semibold">English</th>
					<th class="px-4 py-2 font-semibold">Bastaki</th>
					<th class="px-4 py-2 font-semibold hidden sm:table-cell">Part of speech</th>
					<th class="px-4 py-2 font-semibold hidden md:table-cell">Example</th>
					<th class="px-4 py-2"></th>
				</tr>
			</thead>
			<tbody>
				{#each rows as entry}
					<tr class="table-row-alt hover:bg-med-olive/50 transition">
						<td class="px-4 py-2 font-medium">{entry.english}</td>
						<td class="px-4 py-2">{entry.bastaki_transliteration}</td>
						<td class="px-4 py-2 hidden sm:table-cell capitalize text-gray-500">{entry.part_of_speech ?? '—'}</td>
						<td class="px-4 py-2 hidden md:table-cell text-gray-500 italic">{entry.example ?? ''}</td>
						<td class="px-4 py-2">
							{#if entry.audio_url}
								<audio controls src={entry.audio_url} class="h-7 w-28" preload="none"></audio>
							{/if}
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
{/snippet}

{#if searched}
	{#if liveResults.length > 0}
		{@render entryTable(liveResults)}
	{:else}
		<p class="text-gray-500 text-sm">No results for <em>"{query}"</em>.</p>
	{/if}
{:else if results.length > 0}
	{@render entryTable(results)}
{/if}
