from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnenforcedMfaAwsUserFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[UnenforcedMfaAwsUserFinding]] = Field(alias="value",default=None,)

from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding

