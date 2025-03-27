from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ApplicationServicePrincipal(BaseModel):
	application: Optional[Application] = Field(alias="application", default=None,)
	servicePrincipal: Optional[ServicePrincipal] = Field(alias="servicePrincipal", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .application import Application
from .service_principal import ServicePrincipal

