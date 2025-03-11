from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Retrieve_cloud_pki_leaf_certificate_summary_reportPostRequest(BaseModel):
	certificationAuthorityId: Optional[str] = Field(alias="certificationAuthorityId",default=None,)
	select: Optional[list[str]] = Field(alias="select",default=None,)


