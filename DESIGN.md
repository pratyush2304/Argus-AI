# Design guide

## Token palette

| Role | Token | Value | Tailwind |
| --- | --- | --- | --- |
| Background | `--bg` | `#09090b` | `bg-zinc-950` |
| Card surface | `--surface` | `rgba(255,255,255,.03)` | `bg-white/[0.03]` |
| Card hover | `--surface-hover` | `rgba(255,255,255,.06)` | `hover:bg-white/[0.06]` |
| User card | `--surface-user` | `rgba(99,102,241,.09)` | `bg-indigo-500/[0.09]` |
| Border | `--border` | `rgba(255,255,255,.10)` | `border-white/10` |
| Subtle border | `--border-subtle` | `rgba(255,255,255,.06)` | `border-white/[0.06]` |
| Text | `--text` / `--text-2` | `#fafafa` / `#d4d4d8` | `text-zinc-50` / `text-zinc-300` |
| Muted text (metadata) | `--text-muted` | `#a1a1aa` (≈7:1 on bg, AA) | `text-zinc-400` |
| Accent | `--accent` / `--accent-strong` | `#818cf8` / `#6366f1` | `indigo-400` / `indigo-500` |
| Danger / success | | `#f87171` / `#4ade80` | `red-400` / `green-400` |

Spacing is an 8px grid (4/8/12/16/24/32). Radii: 8px controls, 12px cards, 16px input and panels.
Type: Inter, sentence case, 15px body at 1.65 line height, 12px muted metadata.
Icons: Lucide, stroke-width 1.75.

## Tailwind equivalents (if you port to React/Next)

```text
Container   min-h-screen bg-zinc-950 text-zinc-50 font-sans
Sidebar     bg-zinc-900/60 backdrop-blur-md border-r border-white/10 shadow-xl shadow-black/40
Assistant   rounded-xl border border-white/[0.06] bg-white/[0.03] p-4 shadow-lg shadow-black/30 hover:border-white/10
User        rounded-xl border border-indigo-400/20 bg-indigo-500/[0.09] p-4
Meta        text-xs text-zinc-400
Input bar   rounded-2xl border border-white/10 bg-zinc-900/70 backdrop-blur-md shadow-2xl shadow-black/50
            focus-within:border-indigo-400/60 focus-within:ring-4 focus-within:ring-indigo-500/20
Button      h-10 rounded-lg border border-white/10 bg-white/5 px-4 text-sm font-medium text-zinc-300
            hover:-translate-y-px hover:bg-white/10 active:scale-[.98]
            focus-visible:outline-2 focus-visible:outline-indigo-400 disabled:opacity-40 disabled:cursor-not-allowed
```

## Motion

Easing `cubic-bezier(.2,.8,.2,1)`. Timings: press 150ms, hover/focus 200ms, message entrance 280ms.
Only transform and opacity animate. `prefers-reduced-motion` is respected.

Framer Motion equivalents for a React port:

```tsx
// message entrance
<motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.28, ease: [0.2, 0.8, 0.2, 1] }} />

// button
<motion.button whileHover={{ y: -1 }} whileTap={{ scale: 0.98 }} />

// streaming caret: blink with CSS `animation: blink 1s steps(2) infinite`
```

## Streamlit limits

- Action pills cannot live inside `st.chat_input`; the model chip sits in the header and sidebar instead.
- Chat avatars accept emoji, images or Material icons, not inline Lucide SVG; Lucide is used everywhere else.
- Selectors target Streamlit `data-testid` attributes, which can shift between versions (tested on 1.42+).
