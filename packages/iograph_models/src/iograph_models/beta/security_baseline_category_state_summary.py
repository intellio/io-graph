from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBaselineCategoryStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.securityBaselineCategoryStateSummary"] = Field(alias="@odata.type", default="#microsoft.graph.securityBaselineCategoryStateSummary")
	conflictCount: Optional[int] = Field(alias="conflictCount", default=None,)
	errorCount: Optional[int] = Field(alias="errorCount", default=None,)
	notApplicableCount: Optional[int] = Field(alias="notApplicableCount", default=None,)
	notSecureCount: Optional[int] = Field(alias="notSecureCount", default=None,)
	secureCount: Optional[int] = Field(alias="secureCount", default=None,)
	unknownCount: Optional[int] = Field(alias="unknownCount", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)


