from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class FileStorageContainerCustomPropertyDictionary(BaseModel):
	odata_type: Literal["#microsoft.graph.fileStorageContainerCustomPropertyDictionary"] = Field(alias="@odata.type", default="#microsoft.graph.fileStorageContainerCustomPropertyDictionary")

