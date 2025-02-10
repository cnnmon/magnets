
<img width="914" alt="Screenshot 2025-02-10 at 1 14 51 PM" src="https://github.com/user-attachments/assets/e6c25ceb-af98-432c-8ae1-f08525b52ca7" />

next.js + python + flask (api) + faiss vector search

i've been journaling nearly every day since i turned 22 (also made a [quick app to do that more often](https://github.com/cnnmon/milktea/tree/main)) and i thought, how do my thoughts about (blank) evolve? or do they just stay the same?

memory is fickle, use semantic search instead

## how to use

install packages via `pip install`

dump your journal textfiles into dataset_template.txt and rename it to dataset.txt

NOTE: cache/ will be generated if it does not exist and will make it fast to search through entries. however, if you change dataset.txt in any way, you must delete cache/ so indexing is not weird.

`npm run dev`

profit
