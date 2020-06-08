from ..utils.commands import run_linguakit_cmd

class RelationExtraction:
    TASK = 'rel'
    
    @staticmethod
    def extract_triplets(text):
        output = run_linguakit_cmd(text, RelationExtraction.TASK)
        meanings = output.split('\n')
        resp = []
        for meaning in meanings:
            if len(meaning.split('\t')) > 1:
                m, subject, predicate, object = meaning.split('\t')
                resp.append((subject, predicate, object))
        return resp
