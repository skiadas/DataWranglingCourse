TEMPLATE = template.html
TEXTEMPLATE = template.tex
MDFILES := $(shell find . -name \*.md)
HTMLFILES := $(MDFILES:./%.md=site/%.html)
# ASSIGNMENTS := $(filter ./assignments/%.md,$(MDFILES))
PDFS := $(MDFILES:./%.md=site/%.pdf)
# TEXS := $(ASSIGNMENTS:./%.md=site/%.tex)

$(HTMLFILES): site/%.html: %.md $(TEMPLATE)
	pandoc -o $@ --template=$(TEMPLATE) --mathjax --filter ./makeHtml.hs $<

$(PDFS): site/%.pdf: %.md $(TEXTEMPLATE)
	pandoc -o $@ --template=$(TEXTEMPLATE) -t latex --listings --filter ./makeTex.hs $<

site: $(HTMLFILES) $(PDFS)

email:
	open "mailto:`cat students.txt`"

all: site
