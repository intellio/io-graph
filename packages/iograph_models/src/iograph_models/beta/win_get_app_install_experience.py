from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WinGetAppInstallExperience(BaseModel):
	runAsAccount: Optional[RunAsAccountType | str] = Field(alias="runAsAccount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .run_as_account_type import RunAsAccountType

