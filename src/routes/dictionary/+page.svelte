<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { PARTS_OF_SPEECH } from '$lib/types';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	let q = $state(data.q ?? '');
	let pos = $state(data.pos ?? '');

	function applyFilters() {
		const params = new URLSearchParams();
		if (q) params.set('q', q);
		if (pos) params.set('pos', pos);
		goto(`/dictionary?${params.toString()}`, { replaceState: true });
	}

	function clearFilters() {
		q = '';
		pos = '';
		goto('/dictionary', { replaceState: true });
	}
</script>

<svelte:head>
	<title>Dictionary — Bastaki</title>
</svelte:head>

<h1 class="text-3xl font-display font-semibold text-deep-olive mb-6">Dictionary</h1>

<!-- Filters -->
<form
	class="flex flex-wrap gap-3 mb-6"
	onsubmit={(e) => { e.preventDefault(); applyFilters(); }}
>
	<input
		type="search"
		bind:value={q}
		placeholder="Search English or Bastaki…"
		class="input max-w-xs"
	/>
	<select bind:value={pos} class="input max-w-[180px]">
		<option value="">All parts of speech</option>
		{#each PARTS_OF_SPEECH as { value, label }}
			<option {value}>{label}</option>
		{/each}
	</select>
	<button type="submit" class="btn-primary">Filter</button>
	{#if q || pos}
		<button type="button" onclick={clearFilters} class="btn-secondary">Clear</button>
	{/if}
</form>

<!-- Results count -->
<p class="text-sm text-gray-500 mb-3">
	{data.entries.length} {data.entries.length === 1 ? 'entry' : 'entries'}
	{#if q || pos}— filtered{/if}
</p>

{#if data.entries.length > 0}
	<div class="overflow-x-auto rounded border border-med-olive">
		<table class="w-full text-sm">
			<thead class="bg-med-olive text-left">
				<tr>
					<th class="px-4 py-2 font-semibold">English</th>
					<th class="px-4 py-2 font-semibold">Bastaki</th>
					<th class="px-4 py-2 font-semibold hidden sm:table-cell">Part of speech</th>
					<th class="px-4 py-2 font-semibold hidden md:table-cell">Classifier</th>
					<th class="px-4 py-2 font-semibold hidden lg:table-cell">Example</th>
					<th class="px-4 py-2 font-semibold">Audio</th>
				</tr>
			</thead>
			<tbody>
				{#each data.entries as entry}
					<tr class="table-row-alt hover:bg-med-olive/50 transition">
						<td class="px-4 py-2 font-medium">{entry.english}</td>
						<td class="px-4 py-2">{entry.bastaki_transliteration}</td>
						<td class="px-4 py-2 hidden sm:table-cell capitalize text-gray-500">
							{entry.part_of_speech ?? '—'}
						</td>
						<td class="px-4 py-2 hidden md:table-cell text-gray-500">
							{entry.additional_classifier ?? '—'}
						</td>
						<td class="px-4 py-2 hidden lg:table-cell text-gray-500 italic">
							{entry.example ?? ''}
						</td>
						<td class="px-4 py-2">
							{#if entry.audio_url}
								<audio controls src={entry.audio_url} class="h-7 w-28" preload="none"></audio>
							{:else}
								<span class="text-gray-300 text-xs">—</span>
							{/if}
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
{:else}
	<div class="text-center py-16 text-gray-400">
		<p class="text-lg">No entries found.</p>
		{#if q || pos}
			<button onclick={clearFilters} class="mt-3 text-deep-olive underline text-sm">
				Clear filters
			</button>
		{/if}
	</div>
{/if}

<p class="mt-6 text-sm text-gray-500">
	Know a word we're missing?
	<a href="/submit" class="text-deep-olive underline underline-offset-2 hover:opacity-80">
		Submit it here.
	</a>
</p>
