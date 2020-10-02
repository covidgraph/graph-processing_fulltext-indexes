import os
from py2neo import Graph
from py2neo.database import ClientError

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
] = 'CALL db.index.fulltext.createNodeIndex("EntityFullTextIndex",["Entity"],["name","dummycol"])'
queries[
    "GeneFunctionsFullTextIndex"
] = 'CALL db.index.fulltext.createNodeIndex("GeneFunctionsFullTextIndex",["GOTerm"],["name"])'

NEO4J_CONFIG_STRING = os.getenv("NEO4J")
NEO4J_CONFIG_DICT = json.loads(NEO4J_CONFIG_STRING)
graph = Graph(**NEO4J_CONFIG_DICT)

for name, query in queries.items():
    print("Create fulltext index '{}'".format(name))
    try:
        g.run(query)
    except ClientError as e:
        if "index already exists" in e.message:
            print("Index '{}' allready exists. Skip.".format(name))
        else:
            raise e
