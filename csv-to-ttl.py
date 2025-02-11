import pandas as pd
from rdflib import Graph, Literal, URIRef, Namespace
from rdflib.namespace import XSD, OWL, RDF, RDFS, DCTERMS

dir = r"C:\Users\ezgi\Desktop\cato\example_data.csv"
df = pd.read_csv(dir).fillna("")
g = Graph()
cato = Namespace("http://www.semanticweb.org/CatO/")
persp = Namespace("http://www.ontologydesignpatterns.org/ont/persp/perspectivisation.owl#")
arco = Namespace("https://w3id.org/arco/ontology/arco/")
arco_core = Namespace("https://w3id.org/arco/ontology/core/")
arco_cont_desc = Namespace("https://w3id.org/arco/ontology/context-description/")
arco_den_desc = Namespace("https://w3id.org/arco/ontology/denotative-description/")
schema = Namespace("https://schema.org/")
wd = Namespace("https://www.wikidata.org/wiki/")
getty = Namespace("https://www.getty.edu/")
cidoccrm = Namespace("http://www.cidoc-crm.org/cidoc-crm/")
g.bind("cato",cato)
g.bind("persp",persp)
g.bind("arco", arco)
g.bind("arco_core", arco_core)
g.bind("arco_cont_desc", arco_cont_desc)
g.bind("arco_den_desc", arco_den_desc)
g.bind("schema",schema)
g.bind("wd",wd)
g.bind("getty",getty)
g.bind("cidoccrm",cidoccrm)


g.add((persp.Eventuality, RDF.type, OWL.Class))
g.add((arco.ArchaeologicalProperty, RDF.type, OWL.Class))
g.add((arco.ArchaeologicalProperty, RDFS.subClassOf, persp.Eventuality))
g.add((schema.SizeSpecification, RDF.type, OWL.Class))
g.add((wd.myth, RDF.type, OWL.Class))
g.add((arco_den_desc.FunctionalPurpose, RDF.type, OWL.Class))
g.add((getty.PhysicalDescription, RDF.type, OWL.Class))
g.add((arco.CulturalPropertyComponent, RDF.type, OWL.Class))
g.add((arco.ScientificOrTechnologicalHeritage, RDF.type, OWL.Class))

g.add((persp.BackgroundKnowledge, RDF.type, OWL.Class))
g.add((DCTERMS.PeriodOfTime, RDF.type, OWL.Class))
g.add((DCTERMS.PeriodOfTime, RDFS.subClassOf, persp.BackgroundKnowledge))
g.add((arco_core.Agent,RDF.type,OWL.Class))
g.add((arco_core.Agent, RDFS.subClassOf, persp.BackgroundKnowledge))
g.add((arco_core.Location,RDF.type,OWL.Class))
g.add((arco_core.Location, RDFS.subClassOf, persp.BackgroundKnowledge))
g.add((arco_cont_desc.Documentation,RDF.type,OWL.Class))
g.add((arco_cont_desc.Documentation, RDFS.subClassOf, persp.BackgroundKnowledge))

g.add((persp.Cut, RDF.type, OWL.Class))
g.add((cato.Interpretation, RDF.type, OWL.Class))
g.add((cato.Interpretation, RDFS.subClassOf, persp.Cut))
g.add((cato.LackOfDocumentation, RDF.type, OWL.Class))
g.add((cato.SizeAsImprobableToBuildByHumans, RDF.type, OWL.Class))
g.add((cato.SizeAsProbableToBuildByHumans, RDF.type, OWL.Class))
g.add((cato.BasedOnMyth, RDF.type, OWL.Class))
g.add((cato.RelevantFunctionalPurpose, RDF.type, OWL.Class))
g.add((cato.PhysicalDescriptionAsImprobableToBuildByHumans, RDF.type, OWL.Class))
g.add((cato.PhysicalDescriptionAsProbableToBuildByHumans, RDF.type, OWL.Class))
g.add((cato.TechnologyAsProbableCreatedByHumans, RDF.type, OWL.Class))
g.add((cato.TechnologyAsImprobableCreatedByHumans, RDF.type, OWL.Class))
g.add((cato.RelevantCulturalPropertyComponent, RDF.type, OWL.Class))
g.add((cato.RelevantFindingsResultingFromMethod, RDF.type, OWL.Class))

g.add((persp.Lens, RDF.type, OWL.Class))
g.add((cato.Theory, RDF.type, OWL.Class))
g.add((arco_core.Method, RDF.type, OWL.Class))
g.add((cato.Proponent, RDF.type, OWL.Class))
g.add((cidoccrm.E73_Information_Object, RDF.type, OWL.Class))
g.add((cato.PseudoarchaeologicalTheory, RDF.type, OWL.Class))
g.add((cato.PseudoarchaeologicalTheory, RDFS.subClassOf, persp.Lens))
g.add((cato.ArchaeologicalTheory, RDF.type, OWL.Class))
g.add((cato.ArchaeologicalTheory, RDFS.subClassOf, persp.Lens))

g.add((persp.Attitude, RDF.type, OWL.Class))
g.add((cato.Supportive, RDF.type, OWL.Class))
g.add((cato.Supportive, RDFS.subClassOf, persp.Attitude))
g.add((cato.Skeptical, RDF.type, OWL.Class))
g.add((cato.Skeptical, RDFS.subClassOf, persp.Attitude))
g.add((cato.Mixed, RDF.type, OWL.Class))
g.add((cato.Mixed, RDFS.subClassOf, persp.Attitude))

g.add((persp.Conceptualizer, RDF.type, OWL.Class))



g.add((DCTERMS.coverage, RDF.type, OWL.ObjectProperty))
g.add((DCTERMS.creator, RDF.type, OWL.ObjectProperty))
g.add((schema.location, RDF.type, OWL.ObjectProperty))
g.add((schema.mentiones, RDF.type, OWL.ObjectProperty))
g.add((cato.hasSizeSpecification, RDF.type, OWL.ObjectProperty))
g.add((cato.hasMyth, RDF.type, OWL.ObjectProperty))
g.add((cato.hasFunctionalPurpose, RDF.type, OWL.ObjectProperty))
g.add((cato.hasPhysicalDescription, RDF.type, OWL.ObjectProperty))
g.add((cato.involves, RDF.type, OWL.ObjectProperty))
g.add((cato.builtWith, RDF.type, OWL.ObjectProperty))
g.add((arco.hasCulturalPropertyComponent, RDF.type, OWL.ObjectProperty))
g.add((cidoccrm.P165i_is_incorporated_in, RDF.type, OWL.ObjectProperty))
g.add((cato.proposedBy, RDF.type, OWL.ObjectProperty))
g.add((arco_core.hasMethod, RDF.type, OWL.ObjectProperty))
g.add((cato.theoryType, RDF.type, OWL.ObjectProperty))
g.add((schema.about, RDF.type, OWL.ObjectProperty))
g.add((cato.hasAttitudeTowards, RDF.type, OWL.ObjectProperty))
g.add((cato.inFavourOf, RDF.type, OWL.ObjectProperty))
g.add((cato.PartOf, RDF.type, OWL.ObjectProperty))
g.add((persp.hasAttitude, RDF.type, OWL.ObjectProperty))



g.add((cato.hasContent, RDF.type, OWL.DatatypeProperty))


archeological_property = []

attribute_elems_dict = {"Location":{}, "Documentation":{}, "Agent":{}, "PeriodOfTime" : {}, "PhysicalDescription": {}, "SizeSpecification": {}, 
                  "Myth": {}, "FunctionalPurpose": {}, "Technology": {}, "CulturalPropertyComponent": {}, "E73InformationObject" : {}, 
                  "Proponent":{}, "Method":{}}

attributes_dict = {"Location":[arco_core.Location, schema.location], 
                  "Documentation": [arco_cont_desc.Documentation, schema.mentions,["LackOfDocumentation"]], 
                  "Agent":[arco_core.Agent, DCTERMS.creator], "PeriodOfTime" : [DCTERMS.PeriodOfTime, DCTERMS.coverage], 
                  "PhysicalDescription": [getty.PhysicalDescription, cato.hasPhysicalDescription,["PhysicalDescriptionAsImprobableToBuildByHumans","PhysicalDescriptionAsProbableToBuildByHumans"]], 
                  "SizeSpecification": [schema.SizeSpecification, cato.hasSizeSpecification,["SizeAsImprobableToBuildByHumans","SizeAsProbableToBuildByHumans"]], 
                  "Myth": [wd.Myth, cato.hasMyth,["BasedOnMyth"]], 
                  "FunctionalPurpose": [arco_den_desc.FunctionalPurpose, cato.hasFunctionalPurpose,["RelevantFunctionalPurpose"]], 
                  "Technology": [arco.ScientificOrTechnologicalHeritage, cato.builtWith,["TechnologyAsProbableCreatedByHumans","TechnologyAsImprobableCreatedByHumans"]], 
                  "CulturalPropertyComponent": [arco.CulturalPropertyComponent, arco.hasCulturalPropertyComponent,["RelevantCulturalPropertyComponent"]]}

theory_attributes_dict = {"E73InformationObject" : [cidoccrm.E73_Information_Object, cidoccrm.P165i_is_incorporated_in],
                   "Proponent": [cato.Proponent, cato.proposedBy],
                   "Method": [arco_core.Method, arco_core.hasMethod,["RelevantFindingsResultingFromMethod"]]}

attitudes_dict = {"Mixed":cato.Mixed, "Skeptical":cato.Skeptical, "Supportive":cato.Supportive} 


for idx, row in df.iterrows():
    ap = URIRef(cato+(row["ArcheologicalProperty"].replace(" ","_")))
    if ap not in archeological_property:
        archeological_property.append(ap)
        g.add((ap, RDF.type, arco.ArchaeologicalProperty))

    theory = row["Theory content"]
    theory_name = URIRef(cato + "theory_" + str(idx))
    g.add((theory_name, RDF.type, cato.Theory))
    g.add((theory_name, cato.hasContent, Literal(theory)))
    g.add((theory_name, schema.about, ap))
    if row["Theory type"]=="Scientific archeological":
        g.add((theory_name, cato.theoryType, cato.ArcheologicalTheory))
    elif row["Theory type"]=="Pseudoarcheological":
        g.add((theory_name, cato.theoryType, cato.PseudoarchaeologicalTheory))

    interpretations = row["Interpretation"].split("; ")
    interpretation_name = URIRef(cato + "interpretation_" + str(idx))
    g.add((interpretation_name, RDF.type, cato.Interpretation))
    g.add((interpretation_name, cato.inFavourOf, theory_name))
    archeologists = URIRef(cato + "Archeologists_" + str(idx))
    pseudoarcheologists = URIRef(cato + "Pseudoarcheologists_" + str(idx))
    g.add((archeologists, RDF.type, persp.Conceptualizer))
    g.add((pseudoarcheologists, RDF.type, persp.Conceptualizer))
    g.add((archeologists, persp.hasAttitude, attitudes_dict[row["Attitude of Archeologists"]]))
    g.add((archeologists,cato.hasAttitudeTowards,interpretation_name))
    g.add((pseudoarcheologists, persp.hasAttitude, attitudes_dict[row["Attitude of Pseudoarcheologists"]]))
    g.add((pseudoarcheologists,cato.hasAttitudeTowards,interpretation_name))

    for key in theory_attributes_dict:
        if row[key] != "":
            theory_attribute = row[key].lower().split("; ")
            theory_attribute_elem = theory_attributes_dict[key]
            for att in theory_attribute:
                if att not in attribute_elems_dict[key].keys():
                    attribute_elems_dict[key][att] = key + "_" + str(len(attribute_elems_dict[key]))
                    att_name = URIRef(cato + attribute_elems_dict[key][att])
                    g.add((att_name, RDF.type, theory_attribute_elem[0]))
                    g.add((att_name, cato.hasContent, Literal(att)))
                    g.add((theory_name, theory_attribute_elem[1], att_name))
                else:
                    att_name = URIRef(cato + attribute_elems_dict[key][att])
                    g.add((theory_name, theory_attribute_elem[1], att_name))
                if len(theory_attribute_elem) > 2:
                    for interpretation_type in interpretations:
                        if interpretation_type in theory_attribute_elem[2]:
                           intpt = URIRef(cato + interpretation_type)
                           g.add((intpt, cato.partOf, interpretation_name))
                           g.add((att_name, cato.involves, intpt))

    for key in attributes_dict:
        if row[key] != "":
            attribute = row[key].lower().split("; ")
            attribute_elem = attributes_dict[key]
            for att in attribute:
                if att not in attribute_elems_dict[key].keys():
                    attribute_elems_dict[key][att] = key + "_" + str(len(attribute_elems_dict[key]))
                    att_name = URIRef(cato + attribute_elems_dict[key][att])
                    g.add((att_name, RDF.type, attribute_elem[0]))
                    g.add((att_name, cato.hasContent, Literal(att)))
                    if key == "Documentation":
                        g.add((att_name, attribute_elem[0], ap))
                    else:
                        g.add((ap, attribute_elem[0], att_name))
                else:
                    att_name = URIRef(cato + attribute_elems_dict[key][att])
                    if key == "Documentation":
                        g.add((att_name, attribute_elem[1], ap))
                    else:
                        g.add((ap, attribute_elem[1], att_name))
                if len(attribute_elem) > 2:
                    for interpretation_type in interpretations:
                        if interpretation_type in attribute_elem[2]:
                           intpt = URIRef(cato + interpretation_type)
                           g.add((intpt, cato.partOf, interpretation_name))
                           g.add((att_name, cato.involves, intpt))
    

turtle_str = g.serialize(format="turtle", base=cato, encoding="utf-8")
with open("output.ttl", "wb") as f:
    f.write(turtle_str)