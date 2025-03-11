from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_all_cloud_certification_authorityPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CloudCertificationAuthority]] = Field(alias="value",default=None,)

from .cloud_certification_authority import CloudCertificationAuthority

