export type PartOfSpeech =
	| 'pronoun'
	| 'noun'
	| 'verb'
	| 'adjective'
	| 'preposition'
	| 'adverb'
	| 'misc';

export interface Entry {
	id: string;
	english: string;
	bastaki_transliteration: string;
	part_of_speech: PartOfSpeech | null;
	additional_classifier: string | null;
	example: string | null;
	audio_url: string | null;
	approved: boolean;
	created_at: string;
}

export interface Submission {
	id: string;
	english: string;
	bastaki_transliteration: string;
	part_of_speech: PartOfSpeech | null;
	additional_classifier: string | null;
	example: string | null;
	audio_url: string | null;
	submitter_email: string | null;
	submitter_id: string | null;
	status: 'pending' | 'approved' | 'rejected';
	notes: string | null;
	created_at: string;
	reviewed_at: string | null;
}

export const PARTS_OF_SPEECH: { value: PartOfSpeech; label: string }[] = [
	{ value: 'pronoun', label: 'Pronoun' },
	{ value: 'noun', label: 'Noun' },
	{ value: 'verb', label: 'Verb' },
	{ value: 'adjective', label: 'Adjective' },
	{ value: 'preposition', label: 'Preposition' },
	{ value: 'adverb', label: 'Adverb' },
	{ value: 'misc', label: 'Miscellaneous' }
];
