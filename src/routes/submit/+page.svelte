<script lang="ts">
	import { enhance } from '$app/forms';
	import { PARTS_OF_SPEECH } from '$lib/types';
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();
</script>

<svelte:head>
	<title>Submit a Word — Bastaki</title>
</svelte:head>

<h1 class="text-3xl font-display font-semibold text-deep-olive mb-2">Submit a Word</h1>
<p class="text-gray-600 mb-8 max-w-xl">
	Know a word, phrase, or correction we're missing? Submissions are reviewed before being added
	to the dictionary. Thank you for helping preserve this language.
</p>

{#if form?.success}
	<div class="bg-green-50 border border-green-200 text-green-800 rounded px-5 py-4 mb-6">
		Thank you — your submission is under review!
	</div>
{/if}

{#if form?.error}
	<div class="bg-red-50 border border-red-200 text-red-700 rounded px-5 py-4 mb-6">
		{form.error}
	</div>
{/if}

<form method="POST" use:enhance class="max-w-lg flex flex-col gap-5">
	<div class="grid sm:grid-cols-2 gap-4">
		<div>
			<label for="english" class="block text-sm font-medium text-gray-700 mb-1">
				English <span class="text-red-500">*</span>
			</label>
			<input
				id="english"
				name="english"
				type="text"
				required
				value={form?.english ?? ''}
				class="input"
				placeholder="e.g. water"
			/>
		</div>
		<div>
			<label for="bastaki_transliteration" class="block text-sm font-medium text-gray-700 mb-1">
				Bastaki transliteration <span class="text-red-500">*</span>
			</label>
			<input
				id="bastaki_transliteration"
				name="bastaki_transliteration"
				type="text"
				required
				value={form?.bastaki_transliteration ?? ''}
				class="input"
				placeholder="e.g. ov"
			/>
		</div>
	</div>

	<div class="grid sm:grid-cols-2 gap-4">
		<div>
			<label for="part_of_speech" class="block text-sm font-medium text-gray-700 mb-1">
				Part of speech
			</label>
			<select id="part_of_speech" name="part_of_speech" class="input">
				<option value="">— select —</option>
				{#each PARTS_OF_SPEECH as { value, label }}
					<option {value} selected={form?.part_of_speech === value}>{label}</option>
				{/each}
			</select>
		</div>
		<div>
			<label for="additional_classifier" class="block text-sm font-medium text-gray-700 mb-1">
				Additional classifier
			</label>
			<input
				id="additional_classifier"
				name="additional_classifier"
				type="text"
				class="input"
				placeholder="e.g. body part, animal…"
			/>
		</div>
	</div>

	<div>
		<label for="example" class="block text-sm font-medium text-gray-700 mb-1">
			Example sentence
		</label>
		<input
			id="example"
			name="example"
			type="text"
			value={form?.example ?? ''}
			class="input"
			placeholder="Optional usage example"
		/>
	</div>

	<div>
		<label for="email" class="block text-sm font-medium text-gray-700 mb-1">
			Your email <span class="text-gray-400 font-normal">(optional, for follow-up)</span>
		</label>
		<input
			id="email"
			name="email"
			type="email"
			value={form?.submitter_email ?? ''}
			class="input"
			placeholder="you@example.com"
		/>
	</div>

	<!-- Audio upload placeholder — wire to Supabase Storage when ready -->
	<div>
		<label class="block text-sm font-medium text-gray-700 mb-1">
			Audio recording <span class="text-gray-400 font-normal">(coming soon)</span>
		</label>
		<div class="border border-dashed border-gray-300 rounded px-4 py-6 text-center text-sm text-gray-400">
			Audio upload will be available here
		</div>
	</div>

	<button type="submit" class="btn-primary self-start">Submit word</button>
</form>
