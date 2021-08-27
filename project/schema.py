import graphene
import catalog.schema

# we created project.schema to represent the root query for all applications 
class Query(catalog.schema.Query, graphene.ObjectType):
    pass

class Mutation(catalog.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


# this is the default to enable the graphical interface 
schema.execute