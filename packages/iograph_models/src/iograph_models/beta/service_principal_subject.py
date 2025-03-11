from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalSubject(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	servicePrincipalId: Optional[str] = Field(alias="servicePrincipalId",default=None,)


