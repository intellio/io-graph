from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Target_appsPostRequest(BaseModel):
	apps: Optional[list[ManagedMobileApp]] = Field(alias="apps", default=None,)

from .managed_mobile_app import ManagedMobileApp
