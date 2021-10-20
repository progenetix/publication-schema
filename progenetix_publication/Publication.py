# Auto generated from Publication.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-10-15 15:36
# Schema: hello-world
#
# id: https://progenetix.org/services/schemas/Publication
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PGXPUB = CurieNamespace('pgxpub', 'https://github.com/progenetix/')
SCHEMA = CurieNamespace('schema', 'http://example.org/UNKNOWN/schema/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = PGXPUB


# Types

# Class references
class PublicationId(extended_str):
    pass


class SampleTypeCountId(extended_str):
    pass


@dataclass
class Publication(YAMLRoot):
    """
    A Publication represents basic information about a scientific article used in the Progenetix resource to indicate
    and annotate sources for genomic screening experiments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PGXPUB.Publication
    class_class_curie: ClassVar[str] = "pgxpub:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = PGXPUB.Publication

    id: Union[str, PublicationId] = None
    label: Optional[str] = None
    _id: Optional[str] = None
    pubmedid: Optional[str] = None
    pmcid: Optional[str] = None
    title: Optional[str] = None
    authors: Optional[str] = None
    journal: Optional[str] = None
    pubYear: Optional[str] = None
    abstract: Optional[str] = None
    contact: Optional[Union[dict, "Contact"]] = None
    status: Optional[str] = None
    counts: Optional[Union[dict, "TechnologyCounts"]] = None
    sample_types: Optional[Union[Dict[Union[str, SampleTypeCountId], Union[dict, "SampleTypeCount"]], List[Union[dict, "SampleTypeCount"]]]] = empty_dict()
    note: Optional[str] = None
    provenance: Optional[str] = None
    info: Optional[str] = None
    updated: Optional[str] = None
    progenetix_curator: Optional[str] = None
    progenetix_use: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self._id is not None and not isinstance(self._id, str):
            self._id = str(self._id)

        if self.pubmedid is not None and not isinstance(self.pubmedid, str):
            self.pubmedid = str(self.pubmedid)

        if self.pmcid is not None and not isinstance(self.pmcid, str):
            self.pmcid = str(self.pmcid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        if self.journal is not None and not isinstance(self.journal, str):
            self.journal = str(self.journal)

        if self.pubYear is not None and not isinstance(self.pubYear, str):
            self.pubYear = str(self.pubYear)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.contact is not None and not isinstance(self.contact, Contact):
            self.contact = Contact(**as_dict(self.contact))

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.counts is not None and not isinstance(self.counts, TechnologyCounts):
            self.counts = TechnologyCounts(**as_dict(self.counts))

        self._normalize_inlined_as_list(slot_name="sample_types", slot_type=SampleTypeCount, key_name="id", keyed=True)

        if self.note is not None and not isinstance(self.note, str):
            self.note = str(self.note)

        if self.provenance is not None and not isinstance(self.provenance, str):
            self.provenance = str(self.provenance)

        if self.info is not None and not isinstance(self.info, str):
            self.info = str(self.info)

        if self.updated is not None and not isinstance(self.updated, str):
            self.updated = str(self.updated)

        if self.progenetix_curator is not None and not isinstance(self.progenetix_curator, str):
            self.progenetix_curator = str(self.progenetix_curator)

        if self.progenetix_use is not None and not isinstance(self.progenetix_use, str):
            self.progenetix_use = str(self.progenetix_use)

        super().__post_init__(**kwargs)


@dataclass
class Contact(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PGXPUB.Contact
    class_class_curie: ClassVar[str] = "pgxpub:Contact"
    class_name: ClassVar[str] = "Contact"
    class_model_uri: ClassVar[URIRef] = PGXPUB.Contact

    name: Optional[str] = None
    email: Optional[str] = None
    affiliation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.affiliation is not None and not isinstance(self.affiliation, str):
            self.affiliation = str(self.affiliation)

        super().__post_init__(**kwargs)


@dataclass
class SampleTypeCount(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PGXPUB.SampleTypeCount
    class_class_curie: ClassVar[str] = "pgxpub:SampleTypeCount"
    class_name: ClassVar[str] = "SampleTypeCount"
    class_model_uri: ClassVar[URIRef] = PGXPUB.SampleTypeCount

    id: Union[str, SampleTypeCountId] = None
    label: Optional[str] = None
    count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleTypeCountId):
            self.id = SampleTypeCountId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        super().__post_init__(**kwargs)


@dataclass
class Provenance(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PGXPUB.Provenance
    class_class_curie: ClassVar[str] = "pgxpub:Provenance"
    class_name: ClassVar[str] = "Provenance"
    class_model_uri: ClassVar[URIRef] = PGXPUB.Provenance

    geo_location: Optional[Union[dict, "GeoLocation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.geo_location is not None and not isinstance(self.geo_location, GeoLocation):
            self.geo_location = GeoLocation(**as_dict(self.geo_location))

        super().__post_init__(**kwargs)


@dataclass
class GeoLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PGXPUB.GeoLocation
    class_class_curie: ClassVar[str] = "pgxpub:GeoLocation"
    class_name: ClassVar[str] = "GeoLocation"
    class_model_uri: ClassVar[URIRef] = PGXPUB.GeoLocation

    type: Optional[str] = None
    geometry: Optional[Union[dict, "GeoJSONgeometry"]] = None
    properties: Optional[Union[dict, "GeoJSONproperties"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.geometry is not None and not isinstance(self.geometry, GeoJSONgeometry):
            self.geometry = GeoJSONgeometry(**as_dict(self.geometry))

        if self.properties is not None and not isinstance(self.properties, GeoJSONproperties):
            self.properties = GeoJSONproperties(**as_dict(self.properties))

        super().__post_init__(**kwargs)


@dataclass
class GeoJSONgeometry(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PGXPUB.GeoJSONgeometry
    class_class_curie: ClassVar[str] = "pgxpub:GeoJSONgeometry"
    class_name: ClassVar[str] = "GeoJSONgeometry"
    class_model_uri: ClassVar[URIRef] = PGXPUB.GeoJSONgeometry

    type: Optional[str] = None
    coordinates: Optional[Union[float, List[float]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.coordinates, list):
            self.coordinates = [self.coordinates] if self.coordinates is not None else []
        self.coordinates = [v if isinstance(v, float) else float(v) for v in self.coordinates]

        super().__post_init__(**kwargs)


@dataclass
class GeoJSONproperties(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PGXPUB.GeoJSONproperties
    class_class_curie: ClassVar[str] = "pgxpub:GeoJSONproperties"
    class_name: ClassVar[str] = "GeoJSONproperties"
    class_model_uri: ClassVar[URIRef] = PGXPUB.GeoJSONproperties

    label: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    continent: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    ISO3166alpha3: Optional[str] = None
    precision: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.continent is not None and not isinstance(self.continent, str):
            self.continent = str(self.continent)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.ISO3166alpha3 is not None and not isinstance(self.ISO3166alpha3, str):
            self.ISO3166alpha3 = str(self.ISO3166alpha3)

        if self.precision is not None and not isinstance(self.precision, str):
            self.precision = str(self.precision)

        super().__post_init__(**kwargs)


@dataclass
class TechnologyCounts(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PGXPUB.TechnologyCounts
    class_class_curie: ClassVar[str] = "pgxpub:TechnologyCounts"
    class_name: ClassVar[str] = "TechnologyCounts"
    class_model_uri: ClassVar[URIRef] = PGXPUB.TechnologyCounts

    ccgh: Optional[int] = None
    acgh: Optional[int] = None
    wes: Optional[int] = None
    wgs: Optional[int] = None
    ngs: Optional[int] = None
    genomes: Optional[int] = None
    progenetix: Optional[int] = None
    arraymap: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ccgh is not None and not isinstance(self.ccgh, int):
            self.ccgh = int(self.ccgh)

        if self.acgh is not None and not isinstance(self.acgh, int):
            self.acgh = int(self.acgh)

        if self.wes is not None and not isinstance(self.wes, int):
            self.wes = int(self.wes)

        if self.wgs is not None and not isinstance(self.wgs, int):
            self.wgs = int(self.wgs)

        if self.ngs is not None and not isinstance(self.ngs, int):
            self.ngs = int(self.ngs)

        if self.genomes is not None and not isinstance(self.genomes, int):
            self.genomes = int(self.genomes)

        if self.progenetix is not None and not isinstance(self.progenetix, int):
            self.progenetix = int(self.progenetix)

        if self.arraymap is not None and not isinstance(self.arraymap, int):
            self.arraymap = int(self.arraymap)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

