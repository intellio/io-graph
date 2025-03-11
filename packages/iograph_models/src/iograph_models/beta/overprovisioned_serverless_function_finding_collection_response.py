from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OverprovisionedServerlessFunctionFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[OverprovisionedServerlessFunctionFinding]] = Field(alias="value",default=None,)

from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding

