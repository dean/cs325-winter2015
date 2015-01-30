LATEX	= latex -shell-escape
DVIPS	= dvips
DVIPDF  = dvipdft
PS2PDF	= ps2pdf
XDVI	= xdvi -gamma 4
GH		= gv

SRC	:= $(shell egrep -l '^[^%]*\\begin\{document\}' *.tex)
TRG	= $(SRC:%.tex=%.dvi)
PSF	= $(SRC:%.tex=%.ps)
PDF	= $(SRC:%.tex=%.pdf)

pdf: $(PDF)

ps: $(PSF)

$(TRG): %.dvi: %.tex 
	$(LATEX) $<
	$(LATEX) $<

$(PSF):%.ps: %.dvi
	$(DVIPS) $< -o $@

# $(PDF): %.pdf: %.dvi
# 	$(DVIPDF) -o $@ $<

$(PDF): $(PSF)
	$(PS2PDF) $< $@

show: $(TRG)
	@for i in $(TRG) ; do $(XDVI) $$i & done

showps: $(PSF)
	@for i in $(PSF) ; do $(GH) $$i & done

all: pdf

clean:
	rm -f *.pdf *.ps *.dvi *.out *.log *.aux *.bbl *.blg *.pyg

.PHONY: all show clean ps pdf showps

