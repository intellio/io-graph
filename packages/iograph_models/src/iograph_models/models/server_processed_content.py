from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServerProcessedContent(BaseModel):
	htmlStrings: Optional[list[MetaDataKeyStringPair]] = Field(default=None,alias="htmlStrings",)
	imageSources: Optional[list[MetaDataKeyStringPair]] = Field(default=None,alias="imageSources",)
	links: Optional[list[MetaDataKeyStringPair]] = Field(default=None,alias="links",)
	searchablePlainTexts: Optional[list[MetaDataKeyStringPair]] = Field(default=None,alias="searchablePlainTexts",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair

