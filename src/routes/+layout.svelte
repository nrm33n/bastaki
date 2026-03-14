<script lang="ts">
	import '../app.css';
	import { invalidate } from '$app/navigation';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	let { data, children } = $props();

	onMount(() => {
		const { data: authData } = data.supabase.auth.onAuthStateChange((_, session) => {
			if (session?.expires_at !== data.session?.expires_at) {
				invalidate('supabase:auth');
			}
		});
		return () => authData.subscription.unsubscribe();
	});

	let mobileOpen = $state(false);

	const navLinks = [
		{ href: '/', label: 'Home' },
		{ href: '/dictionary', label: 'Dictionary' },
		{ href: '/info', label: 'Information' },
		{ href: '/submit', label: 'Submit a Word' },
		{ href: '/contact', label: 'Contact' }
	];
</script>

<nav class="bg-white border-b border-med-olive sticky top-0 z-50">
	<div class="max-w-5xl mx-auto px-4 flex items-center justify-between h-16">
		<a href="/" class="font-display text-xl font-semibold text-deep-olive tracking-wide">
			Bastaki
		</a>

		<!-- Desktop nav -->
		<ul class="hidden md:flex gap-6 text-sm font-medium">
			{#each navLinks as link}
				<li>
					<a
						href={link.href}
						class="transition hover:text-deep-olive {$page.url.pathname === link.href
							? 'text-deep-olive border-b-2 border-deep-olive pb-0.5'
							: 'text-gray-600'}"
					>
						{link.label}
					</a>
				</li>
			{/each}
		</ul>

		<!-- Mobile toggle -->
		<button
			class="md:hidden p-2 text-gray-600 hover:text-deep-olive"
			onclick={() => (mobileOpen = !mobileOpen)}
			aria-label="Toggle menu"
		>
			<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
				{#if mobileOpen}
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
				{:else}
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
				{/if}
			</svg>
		</button>
	</div>

	<!-- Mobile menu -->
	{#if mobileOpen}
		<ul class="md:hidden border-t border-med-olive bg-white px-4 py-3 flex flex-col gap-3 text-sm font-medium">
			{#each navLinks as link}
				<li>
					<a
						href={link.href}
						onclick={() => (mobileOpen = false)}
						class="block py-1 {$page.url.pathname === link.href
							? 'text-deep-olive font-semibold'
							: 'text-gray-700'}"
					>
						{link.label}
					</a>
				</li>
			{/each}
		</ul>
	{/if}
</nav>

<main class="max-w-5xl mx-auto px-4 py-10">
	{@render children()}
</main>

<footer class="border-t border-med-olive mt-16 py-8 text-center text-sm text-gray-500">
	<p>Bastaki Language Dictionary &mdash; preserving an endangered dialect.</p>
</footer>
