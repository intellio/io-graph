from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedFileHash(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedFileHash"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedFileHash")
	algorithm: Optional[NetworkaccessAlgorithm | str] = Field(alias="algorithm", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)

from .networkaccess_algorithm import NetworkaccessAlgorithm

