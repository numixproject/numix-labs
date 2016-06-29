This is idiot proof HOW-TO for people like me (Gjorgi) who forget the basic stuff and need idiot proof document to remind them of how stupid they are. :>


ΑΠΟΦΙΣ - Αποφις!


SYMBOL SHADOWS

"translate(0,-1)" in template.meta controls the shadow displacement for icon themes that don't use blur shadow.

"opacity="0.1" in template meta controls the shadow opaque level for icon themes that don't use blur shadow.

"opacity="0.5" ->" in template meta controls the blur opaque level for icon themses that use blur shadow.

"<feGaussianBlur stdDeviation="1"/>" in blur.svg controls the blur strength for icons themes that have blur shadows. The number must be between 0 and 1.


TEMPLATES:

background.svg is the ... well the background. Gee, imagine that!

clip.svg is a copy of the background. I kid you not.

shadow.svg is ... hold on tight (you know she's a little bit dangerous) ... the shadow around / below / above / everything outside the background. Also used for frame around the icons like in "suqircle" case. Shocking, isn't it?

undrlay.svg is eeverything tha goes about the background, but below the symbol. We use it for gardient control with semi transparent dark gradients. 

overlay.svg is sverything that goes above ALL the things. We use it for inset shadows.

blur.svg and meta template are described in the symbol shadows bits.


GENERATING:
./numix-kit - t <template-name>
like you know:
./numix-kit - t baba-jaga (yaga with silly English spelling)


CAUTION:

After you've done the preset grab svgclean from the numix-git repo (git clone https://github.com/numixproject/numix-tools.git) and run it for the /input/template/baba-jaga, it is mucho importante.


CHEERS!
