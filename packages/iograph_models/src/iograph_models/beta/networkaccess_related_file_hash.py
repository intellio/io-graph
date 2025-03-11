from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedFileHash(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	algorithm: Optional[NetworkaccessAlgorithm | str] = Field(alias="algorithm",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)

from .networkaccess_algorithm import NetworkaccessAlgorithm

