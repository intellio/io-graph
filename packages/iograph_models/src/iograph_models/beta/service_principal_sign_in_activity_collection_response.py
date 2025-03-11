from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalSignInActivityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ServicePrincipalSignInActivity]] = Field(alias="value",default=None,)

from .service_principal_sign_in_activity import ServicePrincipalSignInActivity

