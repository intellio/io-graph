from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ApplicationServicePrincipal(BaseModel):
	application: Optional[Application] = Field(default=None,alias="application",)
	servicePrincipal: Optional[ServicePrincipal] = Field(default=None,alias="servicePrincipal",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .application import Application
from .service_principal import ServicePrincipal

