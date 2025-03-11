from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Retrieve_cloud_pki_leaf_certificate_reportPostRequest(BaseModel):
	certificationAuthorityId: Optional[str] = Field(alias="certificationAuthorityId",default=None,)
	top: Optional[int] = Field(alias="top",default=None,)
	skip: Optional[int] = Field(alias="skip",default=None,)
	select: Optional[list[str]] = Field(alias="select",default=None,)
	filter: Optional[str] = Field(alias="filter",default=None,)
	search: Optional[str] = Field(alias="search",default=None,)
	orderBy: Optional[list[str]] = Field(alias="orderBy",default=None,)


