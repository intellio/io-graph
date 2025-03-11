from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServerProcessedContent(BaseModel):
	componentDependencies: Optional[list[MetaDataKeyStringPair]] = Field(alias="componentDependencies",default=None,)
	customMetadata: Optional[list[MetaDataKeyValuePair]] = Field(alias="customMetadata",default=None,)
	htmlStrings: Optional[list[MetaDataKeyStringPair]] = Field(alias="htmlStrings",default=None,)
	imageSources: Optional[list[MetaDataKeyStringPair]] = Field(alias="imageSources",default=None,)
	links: Optional[list[MetaDataKeyStringPair]] = Field(alias="links",default=None,)
	searchablePlainTexts: Optional[list[MetaDataKeyStringPair]] = Field(alias="searchablePlainTexts",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_value_pair import MetaDataKeyValuePair
from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair

