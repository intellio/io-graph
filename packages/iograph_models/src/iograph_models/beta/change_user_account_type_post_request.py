from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Change_user_account_typePostRequest(BaseModel):
	userAccountType: Optional[CloudPcUserAccountType | str] = Field(alias="userAccountType", default=None,)

from .cloud_pc_user_account_type import CloudPcUserAccountType
