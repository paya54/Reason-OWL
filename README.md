# Reasoning with Web Ontology Language and Description Logic

# Description
This project shows how Web Ontology Language (OWL) can be used as knowledge representation to capture the concepts and relationships for the cutting tool issue analysis and how HermiT can be used to reason about the potential root causes for tool breakage incidents.

Knowledge Representation and Reasoning (KRR) needs to distinguish knowledge and facts. This project follows this guidance and consists of two files:
- cutting_tool.owl: Knowledge representation based on OWL, which consists of all the classes, object properties, data properties and individuals in the domain of cutting tool analysis
- tool_break_reason.py: This Python file contains two tool breakage facts and leverages Owlready2 to reason about potential root causes

# Dependencies
The code depends on [owlready2](https://pythonhosted.org/Owlready2) package, which includes HermiT as the inference engine.

The cutting_tool.owl is created using [Protege](https://protege.standford.edu)