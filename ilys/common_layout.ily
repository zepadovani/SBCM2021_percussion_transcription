\version "2.22.1"

#(set-global-staff-size 14)

#(ly:set-option 'relative-includes #t)

%{ \include "lily_scheme_snippets.ily"
\include "zepadovani_snippets_strings.ily"
\include "general_use_snippets.ily" %}

\pointAndClickOff   % disable point and click


%{ \paper {
    evenFooterMarkup = ##f
    evenHeaderMarkup = ##f
    indent = #0
    left-margin = 1\in
    oddFooterMarkup = ##f
    oddHeaderMarkup = ##f
    print-first-page-number = ##f
    print-page-number = ##f
    ragged-right = ##t
} %}


\paper {
  #(set-paper-size "a4" 'landscape) %'landscape

  % no tagline
  tagline = ##f

  % margins and spacings
  left-margin = 1.6 \cm
  right-margin = 1.4 \cm
  top-margin = 0.9 \cm
  bottom-margin = 1 \cm
  before-title-spacing = 0\cm
  top-title-spacing = 0\cm

  after-title-space = 1\cm
  between-title-spacing = 1\cm

  ragged-bottom=##f
  ragged-last-bottom=##f
  % ragged-right = ##t
  indent= 2 \cm
  short-indent= 1.2\cm

  score-system-spacing =
  #'((basic-distance . 4)
  (minimum-distance . 4)
  (padding . 0.2)
  (stretchability . 2))

  last-bottom-spacing =
  #'((basic-distance . 4)
  (minimum-distance . 4)
  (padding . 5))

  top-markup-spacing =
  #'((basic-distance . 1)
  (padding . 1))



  #'((basic-distance . 0)
  (padding . 0))

  markup-system-spacing =
  #'((basic-distance . 3)
  (minimum-distance . 3)
  (padding . 2)
  (stretchability . 3))


  system-system-spacing =
  #'((basic-distance . 8)
  (minimum-distance . 8)
  (padding . 8)
  (stretchability . 8))

  oddHeaderMarkup =  \markup \fill-line {\sans \huge \bold ""}% \fontsize #-2 { \sans "rev.03" }}
  evenHeaderMarkup = \markup \fill-line {\sans \huge \bold ""}% \fontsize #-2 {\sans "rev.03" }}
  oddFooterMarkup = \markup { \fill-line {\column{" "{\sans \fontsize #3 \on-the-fly #print-page-number-check-first \fromproperty #'page:page-number-string }}}}
  evenFooterMarkup = \markup { \fill-line {\column{" "{\sans {\fontsize #3 \on-the-fly #print-page-number-check-first \fromproperty #'page:page-number-string }}}}}
  print-page-number = ##t
  print-first-page-number = ##t
%	annotate-spacing = ##t
}

\layout {


  \context {
    \Score
    %{ \remove Bar_number_engraver %}

    \override Flag.stencil = #modern-straight-flag
    \override BarNumber.break-visibility = ##(#t #t #t)
    \override BarNumber.self-alignment-X = #CENTER
    \override BarNumber.outside-staff-priority = ##f
    \override BarNumber.font-family = #'sans
    \override BarNumber.color = #(x11-color 'grey50)
    \override BarNumber.Y-offset = 4
    \override Beam.beam-thickness = 0.75
    \override Beam.breakable = ##t
    \override Beam.length-fraction = 1.5

    \override Glissando.breakable = ##t
    \override Glissando.thickness = 2

    \override NoteCollision.merge-differently-dotted = ##t
    \override NoteCollision.merge-differently-headed = ##t

    \override NoteColumn.ignore-collision = ##t

    \override SpacingSpanner.uniform-stretching = ##t

    \override Rest.color = #(x11-color 'grey75)
    \override StaffSymbol.color = #(x11-color 'grey50)
    \override StaffSymbol.layer = -1

    \override TextScript.outside-staff-padding = 1

    \override TimeSignature.style = #'numbered
    \override TupletNumber #'font-family = #'sans

    \override TupletBracket.bracket-visibility = ##t
    \override TupletBracket.breakable = ##t
    \override TupletBracket.minimum-length = 3
    \override TupletBracket.outside-staff-padding = 1.5
    \override TupletBracket.padding = 1.25
    \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods

    \override TupletNumber.text = #tuplet-number::calc-fraction-text

    \override VerticalAxisGroup.staff-staff-spacing = #'(
        (basic-distance . 8)
        (minimum-distance . 14)
        (padding . 4)
        (stretchability . 0)
        )

    proportionalNotationDuration = #(ly:make-moment 1 8)
    tupletFullLength = ##t

  }

  \context {
    \Staff
    \override InstrumentName.self-alignment-X = #'RIGHT
    \override InstrumentName.self-alignment-X = #'RIGHT
    \override BarLine.bar-extent = #'(2 . 3)
    \override BarLine.color = #(x11-color 'grey50)
    \remove "Time_signature_engraver"
  }

  \context {
    \Score
    \override SpanBar.transparent = ##t
  }




}


\header {
  %{ nomepeca = \txtitulo %}
  %{

  nomepecab = \txnomepecab
  contextoa = \txcontextoa
  contextob = \txcontextob
  contextob = \txcontextoc
  compositor = \txcompositor %}
}
