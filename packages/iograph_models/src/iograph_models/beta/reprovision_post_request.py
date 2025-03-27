from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ReprovisionPostRequest(BaseModel):
	userAccountType: Optional[CloudPcUserAccountType | str] = Field(alias="userAccountType", default=None,)
	osVersion: Optional[CloudPcOperatingSystem | str] = Field(alias="osVersion", default=None,)

from .cloud_pc_user_account_type import CloudPcUserAccountType
from .cloud_pc_operating_system import CloudPcOperatingSystem

