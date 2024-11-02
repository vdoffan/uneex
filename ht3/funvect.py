def superposition(funmod, funseq):
    return [lambda x, f = f: funmod(f(x)) for f in funseq]
