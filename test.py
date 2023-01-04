from translator_easynmt import translate
import time

t = time.time()
sentence = translate('Today is the anniversary of the publication of Robert Frost’s iconic poem “Stopping by Woods on a Snowy Evening,” a fact that spurred the Literary Hub office into a long conversation about their favorite poems, the most iconic poems written in English, and which poems we should all have already read (or at least be reading next).', 'en', 'pl')
print(sentence)
elapsed = time.time() - t
print(elapsed)