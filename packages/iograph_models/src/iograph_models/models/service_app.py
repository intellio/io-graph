from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceApp(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	application: Optional[Identity] = Field(default=None,alias="application",)
	effectiveDateTime: Optional[datetime] = Field(default=None,alias="effectiveDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	registrationDateTime: Optional[datetime] = Field(default=None,alias="registrationDateTime",)
	status: Optional[ServiceAppStatus] = Field(default=None,alias="status",)

from .identity import Identity
from .identity_set import IdentitySet
from .service_app_status import ServiceAppStatus

