import os
from py2neo import Graph
queries = {}

queries["textOfPapersAndPatents"] = 'CALL db.index.fulltext.createNodeIndex("textOfPapersAndPatents",["Fragment", "Abstract", "Paper", "Patent", "PatentTitle", "PatentClaim","PatentAbstract"],["title", "text"])'
queries["GeneSymbolFullTextIndex"] = 'CALL db.index.fulltext.createNodeIndex("GeneSymbolFullTextIndex",["GeneSymbol"],["sid"])'
queries["AuthorFullTextIndex"] = 'CALL db.index.fulltext.createNodeIndex("AuthorFullTextIndex",["Author"],["first", "middle","last"])'
queries["EntityFullTextIndex"] = 'CALL db.index.fulltext.createNodeIndex("EntityFullTextIndex",["Entity"],["name"])'
g = Graph(host=os.getenv("GC_NEO4J_URL", None), user=os.getenv(
    "GC_NEO4J_USER", None), password=os.getenv("GC_NEO4J_PASSWORD", None))

for name, query in queries.items():
    print("Create fulltext index '{}'".format(name))
    g.run(query)
