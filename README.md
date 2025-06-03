
<img width="914" alt="Screenshot 2025-02-10 at 1 14 51 PM" src="https://github.com/user-attachments/assets/e6c25ceb-af98-432c-8ae1-f08525b52ca7" />

next.js + python + flask (api) + faiss vector search

i've been journaling nearly every day since i turned 22 (also made a [quick app to do that more often](https://github.com/cnnmon/milktea/tree/main)) and i thought, how do my thoughts about (blank) evolve? or do they just stay the same?

memory is fickle, use semantic search instead

## how to use

install packages via `pip install`

dump your journal textfiles into dataset_template.txt and rename it to dataset.txt

NOTE: currently `clean.py` will delete any lines that start with [ because that's usually how i format my todo lists. if you want to change this, modify clean.py!

`npm run dev`, which will also clean the cache every time & regenerate embeddings from the dataset

profit
