from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_targeted_users_and_devicesPostRequest(BaseModel):
	deviceConfigurationIds: Optional[list[str]] = Field(alias="deviceConfigurationIds", default=None,)

