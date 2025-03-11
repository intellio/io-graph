from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_ad_domain_passwordPostRequest(BaseModel):
	adDomainPassword: Optional[str] = Field(alias="adDomainPassword",default=None,)


