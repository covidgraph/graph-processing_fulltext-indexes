queries = {}

queries[
    "textOfPapersAndPatents"
] = 'CALL db.index.fulltext.createNodeIndex("textOfPapersAndPatents",["Fragment", "Abstract", "Paper", "Patent", "PatentTitle", "PatentClaim","PatentAbstract"],["title", "text"])'
queries[
    "GeneSymbolFullTextIndex"
] = 'CALL db.index.fulltext.createNodeIndex("GeneSymbolFullTextIndex",["GeneSymbol"],["sid"])'
queries[
    "AuthorFullTextIndex"
] = 'CALL db.index.fulltext.createNodeIndex("AuthorFullTextIndex",["Author"],["first", "middle","last"])'
queries[
    "EntityFullTextIndex"
] = 'CALL db.index.fulltext.createNodeIndex("EntityFullTextIndex",["Entity"],["name"])'
g = Graph()

log = None

for name, query in queries.items():
    log.info("Create fulltext index '{}'".format(name))
    try:
        g.run(query)
    except:
        pass
