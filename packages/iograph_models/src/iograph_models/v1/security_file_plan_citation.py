from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityFilePlanCitation(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Literal["#microsoft.graph.security.filePlanCitation"] = Field(alias="@odata.type",)
	citationJurisdiction: Optional[str] = Field(alias="citationJurisdiction", default=None,)
	citationUrl: Optional[str] = Field(alias="citationUrl", default=None,)

