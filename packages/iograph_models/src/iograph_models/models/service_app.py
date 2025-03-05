from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceApp(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	application: SerializeAsAny[Optional[Identity]] = Field(alias="application",default=None,)
	effectiveDateTime: Optional[datetime] = Field(alias="effectiveDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	registrationDateTime: Optional[datetime] = Field(alias="registrationDateTime",default=None,)
	status: Optional[str | ServiceAppStatus] = Field(alias="status",default=None,)

from .identity import Identity
from .identity_set import IdentitySet
from .service_app_status import ServiceAppStatus

