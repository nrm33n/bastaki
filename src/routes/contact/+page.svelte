<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from './$types';

	let { form }: { form: ActionData } = $props();
</script>

<svelte:head>
	<title>Contact — Bastaki</title>
</svelte:head>

<h1 class="text-3xl font-display font-semibold text-deep-olive mb-2">Contact</h1>
<p class="text-gray-600 mb-8">Questions, corrections, or contributions — reach out below.</p>

{#if form?.success}
	<div class="bg-green-50 border border-green-200 text-green-800 rounded px-5 py-4 mb-6">
		Message sent — thank you!
	</div>
{/if}

{#if form?.error}
	<div class="bg-red-50 border border-red-200 text-red-700 rounded px-5 py-4 mb-6">
		{form.error}
	</div>
{/if}

<!--
  data-netlify="true" tells Netlify to intercept this form in production.
  The hidden input is required for Netlify to identify the form.
-->
<form
	method="POST"
	use:enhance
	data-netlify="true"
	name="contact"
	class="max-w-lg flex flex-col gap-4"
>
	<input type="hidden" name="form-name" value="contact" />

	<div>
		<label for="email" class="block text-sm font-medium text-gray-700 mb-1">Your email</label>
		<input
			id="email"
			name="email"
			type="email"
			required
			value={form?.email ?? ''}
			class="input"
			placeholder="you@example.com"
		/>
	</div>

	<div>
		<label for="subject" class="block text-sm font-medium text-gray-700 mb-1">Subject</label>
		<input
			id="subject"
			name="subject"
			type="text"
			required
			value={form?.subject ?? ''}
			class="input"
			placeholder="e.g. correction for entry 'water'"
		/>
	</div>

	<div>
		<label for="message" class="block text-sm font-medium text-gray-700 mb-1">Message</label>
		<textarea
			id="message"
			name="message"
			rows="5"
			required
			class="input resize-none"
			placeholder="Your message…"
		>{form?.message ?? ''}</textarea>
	</div>

	<button type="submit" class="btn-primary self-start">Send message</button>
</form>
