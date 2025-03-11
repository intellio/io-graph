from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AwsSecurityToolAdministrationFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AwsSecurityToolAdministrationFinding]]] = Field(alias="value",default=None,)

from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding

