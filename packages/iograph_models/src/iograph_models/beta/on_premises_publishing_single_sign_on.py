from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesPublishingSingleSignOn(BaseModel):
	kerberosSignOnSettings: Optional[KerberosSignOnSettings] = Field(alias="kerberosSignOnSettings", default=None,)
	singleSignOnMode: Optional[SingleSignOnMode | str] = Field(alias="singleSignOnMode", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .kerberos_sign_on_settings import KerberosSignOnSettings
from .single_sign_on_mode import SingleSignOnMode
