## Playing with pola.rs to count tokens

This is a quick experiment to test pola.rs on a text dataset.

Starting from the transcriptions of The Simpson episodes, it calculates the sequence of tokens most "characteristic" for each character.

This is decided based on a tf-idf approach, using laplacian smoothing.

Data from:
https://www.kaggle.com/datasets/prashant111/the-simpsons-dataset

## Install

pola.rs is the only direct dependency, you can use PDM and the included pyproject.toml

## Result

The results are not super accurate, but still make sense to me.

For better results could be possible to:

* use nicer normalization and tokenization on text
* preprocess the ngrams of different sizes to isolate common ones before the polarization count
* use a greedy approach, expanding ngrams under some frequency threshold to detect the catchphrases at different length


<details>
  <summary>Click to expand</summary>

```json
{"name":"Homer Simpson","ngram":"why you little","polarity":0.8273921200750469}
{"name":"Marge Simpson","ngram":"lisa needs braces","polarity":0.5420560747663551}
{"name":"Homer Simpson","ngram":"shut up boy","polarity":0.5242718446601942}
{"name":"Homer Simpson","ngram":"wait a minute","polarity":0.5241157556270096}
{"name":"Bart Simpson","ngram":"ow quit it","polarity":0.5148514851485149}
{"name":"Homer Simpson","ngram":"oh no you dont","polarity":0.5116279069767442}
{"name":"Homer Simpson","ngram":"so long suckers","polarity":0.5086206896551724}
{"name":"Marge Simpson","ngram":"homer what are you doing","polarity":0.46808510638297873}
{"name":"Homer Simpson","ngram":"gimme another one","polarity":0.4673913043478261}
{"name":"Homer Simpson","ngram":"who are you","polarity":0.45871559633027525}
{"name":"Homer Simpson","ngram":"shut up flanders","polarity":0.4444444444444444}
{"name":"Waylon Smithers","ngram":"homer simpson sir","polarity":0.44}
{"name":"Homer Simpson","ngram":"why you little --","polarity":0.4367816091954023}
{"name":"Bart Simpson","ngram":"eat my shorts","polarity":0.43157894736842106}
{"name":"Marge Simpson","ngram":"homie whats wrong","polarity":0.43023255813953487}
{"name":"C. Montgomery Burns","ngram":"release the hounds","polarity":0.4117647058823529}
{"name":"Homer Simpson","ngram":"yeah youre right","polarity":0.40625}
{"name":"Bart Simpson","ngram":"i didnt do it","polarity":0.39855072463768115}
{"name":"Marge Simpson","ngram":"homer stop that","polarity":0.3950617283950617}
{"name":"Homer Simpson","ngram":"thats my girl","polarity":0.39285714285714285}
{"name":"Homer Simpson","ngram":"honey im home","polarity":0.38271604938271603}
{"name":"Marge Simpson","ngram":"oh my goodness","polarity":0.3805970149253731}
{"name":"Lisa Simpson","ngram":"bart quit it","polarity":0.379746835443038}
{"name":"Kent Brockman","ngram":"this is kent brockman","polarity":0.379746835443038}
{"name":"Kent Brockman","ngram":"this is kent","polarity":0.379746835443038}
{"name":"Homer Simpson","ngram":"go to hell","polarity":0.37209302325581395}
{"name":"Homer Simpson","ngram":"what the hell","polarity":0.3719512195121951}
{"name":"Marge Simpson","ngram":"whats wrong homie","polarity":0.3717948717948718}
{"name":"Bart Simpson","ngram":"is that her","polarity":0.3717948717948718}
{"name":"Bart Simpson","ngram":"wheres my elephant","polarity":0.3717948717948718}
{"name":"Homer Simpson","ngram":"why you little--","polarity":0.3717948717948718}
{"name":"Homer Simpson","ngram":"what about now","polarity":0.3717948717948718}
{"name":"Lisa Simpson","ngram":"peace on earth","polarity":0.37037037037037035}
{"name":"Homer Simpson","ngram":"what the hell is that","polarity":0.35051546391752575}
{"name":"Lisa Simpson","ngram":"dad are you okay","polarity":0.3466666666666667}
{"name":"Homer Simpson","ngram":"i didnt say stop","polarity":0.3466666666666667}
{"name":"Homer Simpson","ngram":"dont mind if i do","polarity":0.34210526315789475}
{"name":"Homer Simpson","ngram":"who told you","polarity":0.34210526315789475}
{"name":"Homer Simpson","ngram":"come on boy","polarity":0.34177215189873417}
{"name":"Homer Simpson","ngram":"all right then","polarity":0.32967032967032966}
{"name":"Marge Simpson","ngram":"oh thats wonderful","polarity":0.3287671232876712}
{"name":"Marge Simpson","ngram":"thank you homie","polarity":0.3287671232876712}
{"name":"Announcer","ngram":"we now return","polarity":0.3287671232876712}
{"name":"Seymour Skinner","ngram":"off the list","polarity":0.3246753246753247}
{"name":"Marge Simpson","ngram":"oh my lord","polarity":0.32}
{"name":"Announcer","ngram":"we now return to","polarity":0.3194444444444444}
{"name":"Apu Nahasapeemapetilon","ngram":"hopin for a dream","polarity":0.3194444444444444}
{"name":"Bart Simpson","ngram":"way to go dad","polarity":0.3146067415730337}
{"name":"Homer Simpson","ngram":"ill kill you","polarity":0.3108108108108108}
{"name":"Bart Simpson","ngram":"i love you dad","polarity":0.31}
{"name":"Marge Simpson","ngram":"good night homer","polarity":0.30985915492957744}
{"name":"Marge Simpson","ngram":"hello listen lady","polarity":0.30985915492957744}
{"name":"Bart Simpson","ngram":"kool moe dee","polarity":0.30985915492957744}
{"name":"Lisa Simpson","ngram":"i stand corrected","polarity":0.30985915492957744}
{"name":"Waylon Smithers","ngram":"allow me sir","polarity":0.30985915492957744}
{"name":"Rev. Timothy Lovejoy","ngram":"let us pray","polarity":0.30985915492957744}
```
</details>
