from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionStageSetting(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	stage: Optional[str | AccessPackageCustomExtensionStage] = Field(alias="stage",default=None,)
	customExtension: SerializeAsAny[Optional[CustomCalloutExtension]] = Field(alias="customExtension",default=None,)

from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
from .custom_callout_extension import CustomCalloutExtension

