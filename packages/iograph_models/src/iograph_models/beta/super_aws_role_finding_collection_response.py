from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SuperAwsRoleFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SuperAwsRoleFinding]] = Field(alias="value", default=None,)

from .super_aws_role_finding import SuperAwsRoleFinding
