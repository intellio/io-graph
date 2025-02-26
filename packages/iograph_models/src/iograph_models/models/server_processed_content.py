from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServerProcessedContent(BaseModel):
	htmlStrings: list[MetaDataKeyStringPair] = Field(alias="htmlStrings",)
	imageSources: list[MetaDataKeyStringPair] = Field(alias="imageSources",)
	links: list[MetaDataKeyStringPair] = Field(alias="links",)
	searchablePlainTexts: list[MetaDataKeyStringPair] = Field(alias="searchablePlainTexts",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair
from .meta_data_key_string_pair import MetaDataKeyStringPair

