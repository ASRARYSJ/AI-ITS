from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Initialize graph
g = Graph()

# Load the existing ontology
g.parse("ontology.owl")

# Define the namespaces for the ontology
namespace = URIRef("http://example.org/")

# Create the individuals
student = URIRef(namespace + "Jane_Doe")
instructor = URIRef(namespace + "Jane_Instructor")
course = URIRef(namespace + "Math_101")

# Add classes
g.add((URIRef(namespace + "Student"), RDF.type, URIRef("http://www.w3.org/2002/07/owl#Class")))
g.add((URIRef(namespace + "Instructor"), RDF.type, URIRef("http://www.w3.org/2002/07/owl#Class")))
g.add((URIRef(namespace + "Course"), RDF.type, URIRef("http://www.w3.org/2002/07/owl#Class")))

# Add individuals with their types and properties
g.add((student, RDF.type, URIRef(namespace + "Student")))
g.add((instructor, RDF.type, URIRef(namespace + "Instructor")))
g.add((course, RDF.type, URIRef(namespace + "Course")))

# Add properties (e.g., age)
g.add((student, URIRef(namespace + "age"), Literal(22)))
g.add((instructor, URIRef(namespace + "age"), Literal(22)))

# Add labels (names)
g.add((student, RDFS.label, Literal("Jane_Doe")))
g.add((instructor, RDFS.label, Literal("Jane_Instructor")))
g.add((course, RDFS.label, Literal("Math_101")))

# Save the updated ontology
g.serialize("updated_ontology.owl", format="xml")

# Output success message
print("=== Intelligent Tutoring System Ontology ===")
print("\nClasses in the ontology:")
print("- Student")
print("- Course")
print("- Instructor")

print("\nCreated Student: Jane_Doe, Age: 22")
print("Created Instructor: Jane_Instructor, Age: 22")
print("Course created: Math_101")

print("\nOntology updated and saved as 'updated_ontology.owl'.")
