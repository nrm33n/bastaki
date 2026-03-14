-- ============================================================
-- Bastaki Dictionary — initial schema
-- Run this in: Supabase Dashboard → SQL Editor
-- ============================================================

-- Approved dictionary entries
create table if not exists entries (
  id                      uuid primary key default gen_random_uuid(),
  english                 text not null,
  bastaki_transliteration text not null,
  part_of_speech          text,
  additional_classifier   text,
  example                 text,
  audio_url               text,   -- Supabase Storage public URL
  approved                boolean not null default true,
  created_at              timestamptz not null default now()
);

-- Full-text search index (English + Bastaki)
create index if not exists entries_fts_idx
  on entries using gin (
    to_tsvector('simple', english || ' ' || bastaki_transliteration)
  );

-- Community submissions (pending review)
create table if not exists submissions (
  id                      uuid primary key default gen_random_uuid(),
  english                 text not null,
  bastaki_transliteration text not null,
  part_of_speech          text,
  additional_classifier   text,
  example                 text,
  audio_url               text,
  submitter_email         text,
  submitter_id            uuid references auth.users (id) on delete set null,
  status                  text not null default 'pending'
                            check (status in ('pending', 'approved', 'rejected')),
  notes                   text,   -- reviewer notes
  created_at              timestamptz not null default now(),
  reviewed_at             timestamptz
);

-- ============================================================
-- Row-Level Security
-- ============================================================

alter table entries enable row level security;
alter table submissions enable row level security;

-- Anyone can read approved entries
create policy "public read entries"
  on entries for select
  using (approved = true);

-- Anyone can insert a submission
create policy "public insert submissions"
  on submissions for insert
  with check (true);

-- Only authenticated users can read their own submissions
create policy "submitter read own"
  on submissions for select
  using (auth.uid() = submitter_id);

-- ============================================================
-- Storage bucket for audio files
-- ============================================================
-- Create manually in Dashboard → Storage → New bucket
-- Name: "audio"
-- Public: true (so audio_url links work without auth)
-- ============================================================
