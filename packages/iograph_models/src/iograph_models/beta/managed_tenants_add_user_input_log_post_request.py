from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Managed_tenants_add_user_input_logPostRequest(BaseModel):
	logInformation: Optional[str] = Field(alias="logInformation", default=None,)

