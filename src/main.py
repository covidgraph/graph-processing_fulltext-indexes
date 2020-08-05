import os
from py2neo import Graph
from py2neo.database import ClientError
queries = {}

queries["textOfPapersAndPatents"] = 'CALL db.index.fulltext.createNodeIndex("textOfPapersAndPatents",["Fragment", "Abstract", "Paper", "Patent", "PatentTitle", "PatentClaim","PatentAbstract"],["title", "text"])'
queries["GeneSymbolFullTextIndex"] = 'CALL db.index.fulltext.createNodeIndex("GeneSymbolFullTextIndex",["GeneSymbol"],["sid"])'
queries["AuthorFullTextIndex"] = 'CALL db.index.fulltext.createNodeIndex("AuthorFullTextIndex",["Author"],["first", "middle","last"])'
queries["EntityFullTextIndex"] = 'CALL db.index.fulltext.createNodeIndex("EntityFullTextIndex",["Entity"],["name"])'
neo4j_host = os.getenv("GC_NEO4J_URL", None)
neo4j_pw = os.getenv("GC_NEO4J_PASSWORD", None)
neo4j_user = os.getenv("GC_NEO4J_USER", None)
print("Connect to '{}'@'{}'".format(neo4j_user, neo4j_host))
g = Graph(neo4j_host, user=neo4j_user, password=neo4j_pw)

for name, query in queries.items():
    print("Create fulltext index '{}'".format(name))
    try:
        g.run(query)
    except ClientError as e:
        print("Index '{}' allready exists. Skip.".format(name))
