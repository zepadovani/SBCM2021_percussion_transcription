\version "2.22.1"

smallFlageolet =
#(let ((m (make-articulation "flageolet")))
   (set! (ly:music-property m 'tweaks)
         (acons 'font-size -3
                (ly:music-property m 'tweaks)))
   m)




\score{
\new StaffGroup <<

	\set Score.proportionalNotationDuration = #(ly:make-moment 1/30)
	\new Staff = cym_cow \with {
							instrumentName = \markup{\column{ "Cymbals and" "Cowbell" } }
							\override StaffSymbol.line-count = #3
							\override StaffSymbol.line-positions = #'(-4 0 4)
							\override Staff.InstrumentName.self-alignment-X = #RIGHT }
	{
	\time 3/4
		\clef percussion

		f4^\markup{ \box "Cowbell"}
		\override NoteHead.style = #'cross
		c'^\markup{ \box "Small Cymbal" }
		g'^\markup{ \box "Large Cymbal" } g'^\markup{\bold " ,"}

		\bar ".|"
	}

	\new Staff = conga_bongo\with {
							instrumentName = \markup{ \column { "Conga and" "Bongo" } }
						 	\override StaffSymbol.line-count = #2
							\override StaffSymbol.line-positions = #'(-3 3)
							\override Staff.InstrumentName.self-alignment-X = #RIGHT }
	{
	\time 3/4
		\clef percussion

		\tuplet 2/3 {
		g4^\markup{ \column{ \box "Conga" \fontsize #-2 "Slap = Sl." \fontsize #-2 "Muff = Mf." } }
		f'^\markup{ \column{ \box "Bongo" \fontsize #-2 "Slap = Sl." \fontsize #-2 "Muff = Mf." } }
		}
	}

	\new Staff = tom_snare \with {
							instrumentName = \markup{ \column { "Snare and" "Tom" } }
							\override StaffSymbol.line-count = #2
							\override StaffSymbol.line-positions = #'(-3 3)
							\override Staff.InstrumentName.self-alignment-X = #RIGHT }
	{
	\clef percussion
	\time 3/4
		g4^\markup{ \box "Large Tom" }
		f'^+^\markup{ \column{  \box "Snare" \fontsize #-2 "Dampen" } }
		f'^\flageolet^\markup{ \fontsize #-2 "Open" } f'^\markup{{\musicglyph "scripts.open" }}

	}

	\new Staff = shakers \with {
							instrumentName = "Shakers"
							\override StaffSymbol.line-count = #2
							\override StaffSymbol.line-positions = #'(-3 3)
							\override Staff.InstrumentName.self-alignment-X = #RIGHT } {
	\clef percussion
	\time 3/4
		\tuplet 2/3 {
		\override NoteHead.style = #'xcircle
		g4^\markup{ \box "Metal shaker" }
		f'^\markup{ \box "Cabassa" }
		}
	}

>>

\layout{
	\context{
	\StaffGroup
	\override StaffGrouper.staff-staff-spacing.basic-distance = #15
	\omit TimeSignature
	\omit TupletBracket
	\omit TupletNumber
	}

	\context{
	\Score
	\omit Stem
	}

}
}

\paper {
	indent = #20
	print-all-headers = ##f
	top-margin = 15
	right-margin = 10
	bottom-margin = 10
	left-margin = 20
	tagline = ##f
}
