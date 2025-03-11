from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OidcClientSecretAuthentication(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	clientSecret: Optional[str] = Field(alias="clientSecret",default=None,)


